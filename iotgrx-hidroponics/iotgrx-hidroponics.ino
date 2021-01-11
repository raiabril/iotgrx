/***************************************************************************
  This is an awesome project
 
 ***************************************************************************/
#include <WiFiMulti.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <soc/sens_reg.h>
#include <base64.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

// #define SEALEVELPRESSURE_HPA (1013.25)
#define SEALEVELPRESSURE_HPA (942.19) // Madrid
#define I2C_SDA 21
#define I2C_SCL 22
#define uS_TO_S_FACTOR 1000000  //Conversion factor for micro seconds to seconds
#define TIME_TO_SLEEP 30*60    //Time ESP32 will go to sleep (in seconds)
#define SENSOR_TEST 20 //Times the sensor will be read
#define SENSOR_WITHRAW 5
#define TEST_DELAY 200

// To save registry for the first time
uint64_t reg_a;
uint64_t reg_b;
uint64_t reg_c;

// Auth
String device_name = "hidroponics";
String token = "3c4751b9-b4b9-4b98-b343-d31226e7458b";
String Url = "https://iotgrx.pythonanywhere.com/api/v1";

// Wifi credentials
// const char* ssid = "MIWIFI_xua4";
// const char* password =  "RybpDPX4jHXd";
// const char* ssid = "MOVISTAR_DE60";
// const char* password =  "Jo4Ye3o3H4jUmdWpjqjj";
const char* ssid = "MIWIFI_5778";
const char* password =  "6KDXENH8";

String GPIO_names[12] = {
  "hTEMP",
  "hHUMI",
  "hPRES",
  "hALTI",
  "hMOIS1",
  "hMOIS2",
  "hLIGHT",
  "hCURRENT",
  "hVOLT",
  "hPOWE",
  "hBATT",
  "hBATT12V"
  };

float GPIO_values[12] = {
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0
  };

float bmeTemp = 0.0;
float bmeHumi = 0.0;
float bmePres = 0.0;
float bmeAlti = 0.0;
float moisture1 = 0.0;
float moisture2 = 0.0;
float light = 0.0;
float current = 0.0;
float voltage = 0.0;
float power = 0.0;
float battery = 0.0;
float battery_12v = 0.0;

float bmeTempAverage = 0.0;
float bmeHumiAverage = 0.0;
float bmePresAverage = 0.0;
float bmeAltiAverage = 0.0;
float moisture1Average = 0.0;
float moisture2Average = 0.0;
float currentAverage = 0.0;
float voltageAverage = 0.0;
float lightAverage = 0.0;
float powerAverage = 0.0;
float batteryAverage = 0.0;
float batteryAverage_12v = 0.0;

int err;
int sensorCount = 0;
int duration;

// Relay
int relay12V = 15;
int relay5V = 14;

// pins
int moisture1Pin = 25;
int moisture2Pin = 26;
int lightPin = 33;
int currentPin = 27;
int voltagePin = 32;
int batteryPin = 35;
int battery12Pin = 34;

RTC_DATA_ATTR int bootCount = 0;
unsigned long delayTime;
RTC_DATA_ATTR bool protection5v = 0;
RTC_DATA_ATTR bool protection12v = 0;
int batteryMin = 540;

// Create object BME280
Adafruit_BME280 bme; // I2C
TwoWire I2CBME = TwoWire(0);

// Create object Wifi
WiFiMulti wifiMulti;

void setup() {
  delay(1000);
  Serial.begin(115200);

  //Set timer to x seconds
  esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);
  delay(1000);

  battery_12v = analogRead(battery12Pin);
  battery = analogRead(batteryPin);
  
  if (battery_12v < batteryMin){
    protection12v = 1;
  }
  else {
    protection12v = 0;
  }

  if (battery < batteryMin){
    Serial.println("Protection mode active. Forced sleeping");
    protection5v = 1;
    esp_deep_sleep_start();
  }
  else {
    protection5v = 0;
  }
  
  
  pinMode(relay5V, OUTPUT);
  pinMode(relay12V, OUTPUT);
  digitalWrite(relay5V, HIGH);
  digitalWrite(relay12V, HIGH);
  
  Serial.println("");
  Serial.println("");
  Serial.println("");
  Serial.println("### Naos 8 ###");
  Serial.println("Device = " + device_name);
  Serial.println("Token = " + token);
  Serial.println("");
  Serial.println("## Test ##");
  Serial.println("Boot number = " + String(bootCount+1));
  
  
  if(bootCount==0){
    Serial.println("... First boot. Saving registry ...");
    reg_a = READ_PERI_REG(SENS_SAR_START_FORCE_REG);
    reg_b = READ_PERI_REG(SENS_SAR_READ_CTRL2_REG);
    reg_c = READ_PERI_REG(SENS_SAR_MEAS_START2_REG);
  }
  else {
    Serial.println("... Fixing registry ...");
    WRITE_PERI_REG(SENS_SAR_START_FORCE_REG, reg_a);  // fix ADC registers
    WRITE_PERI_REG(SENS_SAR_READ_CTRL2_REG, reg_b);
    WRITE_PERI_REG(SENS_SAR_MEAS_START2_REG, reg_c);
    }
  delay(1000);
  
  //Increment boot number and print it every reboot
  ++bootCount;

  Serial.println("");
  Serial.println("### Read Analog sensors ###");

  if (!protection12v) {
    digitalWrite(relay5V, LOW);
    delay(2000);
  }
  else {
    Serial.println("Protecting power battery");
  }
  
  sensorCount = 0;
  for(int i=0; i< SENSOR_TEST; i++){
    moisture1 = analogRead(moisture1Pin);
    moisture2 = analogRead(moisture2Pin);
    current = analogRead(currentPin);
    voltage = analogRead(voltagePin);
    light = analogRead(lightPin);
    battery = analogRead(batteryPin);
    battery_12v = analogRead(battery12Pin);
    
    Serial.print("Analog - OK -  " + String(i) + "  ");
    Serial.print(String(moisture1) + " ()  ");
    Serial.print(String(moisture2) + " ()  ");
    Serial.print(String(current) + " ()  ");
    Serial.print(String(voltage) + " ()  ");
    Serial.print(String(light) + " ()  ");
    Serial.print(String(battery) + "() ");
    Serial.println(String(battery_12v) + "()");
    
    moisture1Average = moisture1Average + moisture1;
    moisture2Average = moisture2Average + moisture2;
    currentAverage = currentAverage + current;
    voltageAverage = voltageAverage + voltage;
    lightAverage = lightAverage + light;
    batteryAverage = batteryAverage + battery;
    batteryAverage_12v = batteryAverage_12v + battery_12v;

    sensorCount++;
    delay(TEST_DELAY);
  }

  // Stop power in sensors
  digitalWrite(relay5V, HIGH);
  delay(200);
  
  moisture1Average = moisture1Average/sensorCount;
  moisture2Average = moisture2Average/sensorCount;
  currentAverage = currentAverage/sensorCount;
  voltageAverage = voltageAverage/sensorCount;
  lightAverage = lightAverage/sensorCount;
  batteryAverage = batteryAverage/sensorCount;
  batteryAverage_12v = batteryAverage_12v/sensorCount;

  Serial.print("Analog - FINAL  ");
  Serial.print(String(moisture1Average) + " ()  ");
  Serial.print(String(moisture2Average) + " ()  ");
  Serial.print(String(currentAverage) + " ()  ");
  Serial.print(String(voltageAverage) + " ()  ");
  Serial.print(String(lightAverage) + " ()  ");
  Serial.print(String(batteryAverage) + "() ");
  Serial.println(String(batteryAverage_12v) + "()");

  GPIO_values[4]= moisture1Average;
  GPIO_values[5]= moisture2Average;
  GPIO_values[6] = lightAverage;
  GPIO_values[7]= currentAverage;
  GPIO_values[8]= voltageAverage;
  GPIO_values[9] = voltageAverage*currentAverage;
  GPIO_values[10] = batteryAverage;
  GPIO_values[11] = batteryAverage_12v;

  if (batteryAverage_12v < batteryMin){
    protection12v = 1;
    Serial.println("Protection 12v enabled");
    GPIO_values[4]= 0;
    GPIO_values[5]= 0;
    GPIO_values[6] = 0;
    GPIO_values[7]= 0;
    GPIO_values[8]= voltageAverage;
    GPIO_values[9] = 0;
    GPIO_values[10] = batteryAverage;
    GPIO_values[11] = batteryAverage_12v;
   }
   else {
    protection12v = 0;
    Serial.println("Protection 12v disabled");
   }

  // I2C for bme
  Serial.println("");
  Serial.println("### Testing BME ###");
  I2CBME.begin(I2C_SDA, I2C_SCL, 100000);
 
  bool status;
  status = bme.begin(0x76, &I2CBME);
   
  if (!status) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }
  Serial.println("Connected to BME280");

  sensorCount = 0;
  for(int i=0; i< SENSOR_TEST; i++){
    
    bmeTemp = bme.readTemperature();
    bmeHumi = bme.readHumidity();
    bmePres = bme.readPressure() / 100.0F;
    bmeAlti = bme.readAltitude(SEALEVELPRESSURE_HPA);
    delay(TEST_DELAY);
    
    if (bmeTemp > 0.1 && (i>SENSOR_WITHRAW-1)){
      bmeTempAverage = bmeTempAverage+bmeTemp;
      bmeHumiAverage = bmeHumiAverage+bmeHumi;
      bmePresAverage = bmePresAverage+bmePres;
      bmeAltiAverage = bmeAltiAverage+bmeAlti;
      sensorCount++;
      
      Serial.print("BME280 - OK  " + String(i) + "  ");
      Serial.print(String(bmeTemp) + " *C  ");
      Serial.print(String(bmeHumi)+" %  ");
      Serial.print(String(bmePres) + " hPa  ");
      Serial.println(String(bmeAlti) + " m");
    }
    else {
      Serial.print("BME280 - KO  " + String(i) + "  ");
      Serial.print(String(bmeTemp) + " *C  ");
      Serial.print(String(bmeHumi)+" %  ");
      Serial.print(String(bmePres) + " hPa  ");
      Serial.println(String(bmeAlti) + " m");
      }
   }
   
   if (sensorCount > 0){
    bmeTemp = bmeTempAverage/sensorCount;
    bmeHumi = bmeHumiAverage/sensorCount;
    bmePres = bmePresAverage/sensorCount;
    bmeAlti = bmeAltiAverage/sensorCount;
   }
  else {
    bmeTemp = 0;
    bmeHumi = 0;
    bmePres = 0;
    bmeAlti = 0;
   }
  
  Serial.print("BME280 - FINAL ");
  Serial.print(String(bmeTemp) + " *C  ");
  Serial.print(String(bmeHumi)+" %  ");
  Serial.print(String(bmePres) + " hPa  ");
  Serial.println(String(bmeAlti) + " m");
    
  GPIO_values[0]=bmeTemp;
  GPIO_values[1]=bmeHumi;
  GPIO_values[2]=bmePres;
  GPIO_values[3]=bmeAlti;
 
  delay(1000);
  
  StaticJsonDocument<1024> event;
  StaticJsonDocument<128> sensor;

  event["device"]["id"] = device_name;
  event["device"]["boot"] = bootCount;

  JsonArray datos = event.createNestedArray("data");
 
  for(int i=0; i< 12; i++){
    sensor["id"] = GPIO_names[i];
    sensor["value"] = GPIO_values[i];
    datos.add(sensor);
   
   }
   
  char buffer[1024];
  serializeJson(event, buffer);
  Serial.println("");
  Serial.println("### Results ###");
  Serial.println(buffer);
  delay(1000);

  
  wifiMulti.addAP(ssid, password);
  delay(1000);
  
  Serial.println("");
  Serial.println("### Connecting Wifi... ###");
 
  if(wifiMulti.run() == WL_CONNECTED) {
    Serial.print("Connected: ");
    Serial.println(WiFi.localIP());
    delay(1000);
    }
 
  // Sending results of the tests
  if(WiFi.status()== WL_CONNECTED){
   
   HTTPClient http;
   http.addHeader("Content-Type", "application/json");             //Specify content-type header
   http.addHeader("Authorization", token);
   http.begin(Url+"/events");  //Specify destination for HTTP request
   Serial.println("Launching POST data from sensors...");
   int httpResponseCode = http.POST(buffer);   //Send the actual POST request
   
   if(httpResponseCode==201){
    String response = http.getString();                       //Get the response to the request
    Serial.println("OK - Data sent");
    }
   
   else{
    Serial.print("Error on sending POST: ");
    String response = http.getString();
    Serial.println(httpResponseCode);
    //Serial.println(response);
    }
   
   http.end();  //Free resources
   
  }
  else{
    Serial.println("Not possible to send results, no wifi");
    }

  if (!protection12v) {
    // Require watering
    if(WiFi.status()== WL_CONNECTED){
      HTTPClient httpWater;
      httpWater.addHeader("Content-Type", "application/json");             //Specify content-type header
      httpWater.addHeader("Authorization", token);
      httpWater.begin(Url + "/water/" + device_name);  //Specify destination for HTTP request
      Serial.println("Launching GET to water ...");
      int httpResponseCode = httpWater.GET();   //Send the actual GET request
      
      if(httpResponseCode==200){
        
        String response = httpWater.getString();                       //Get the response to the request
        Serial.println("200 OK");
        Serial.println(response);
        duration = response.toInt();
      }
     
      else{
        Serial.print("Error on sending watering GET: ");
        String response = httpWater.getString();
        Serial.println(httpResponseCode);
        if(httpResponseCode==404){
          duration=0;
          }
        //Serial.println(response);
      }
  
      httpWater.end();  //Free resources for water
    }
    else{
      Serial.println("Using standard watering, no wifi");
      duration = 9000;
    }
    
    Serial.println("Watering for: " + String(duration) + " ms");
    digitalWrite(relay12V, LOW);
    delay(duration);
    digitalWrite(relay12V, HIGH);
  
    if(WiFi.status()== WL_CONNECTED && duration > 0){
      HTTPClient httpLog;
      httpLog.addHeader("Content-Type", "application/json");             //Specify content-type header
      httpLog.addHeader("Authorization", token);
      httpLog.begin(Url + "/water/log");  //Specify destination for HTTP request
        
      StaticJsonDocument<128> logEvent;
      logEvent["device_code"] = device_name;
      logEvent["duration"] = duration;
      serializeJson(logEvent, buffer);
      Serial.println("Sending log");
      Serial.println(buffer);
        
      Serial.println("");
      Serial.println("Launching POST to log watering event ...");
      int httpResponseCode = httpLog.POST(buffer);   //Send the actual POST request
        
      if(httpResponseCode==201){
        String response = httpLog.getString();                       //Get the response to the request
        Serial.println("201 Created");
        Serial.println(response);
      }
      else{
        Serial.print("Error on sending GET: ");
        String response = httpLog.getString();
        Serial.println(httpResponseCode);
        //Serial.println(response);
      }
     
      httpLog.end();  //Free resources for log
     
    }
    else{
      Serial.println("Water log not sent");
    }
    }
  
  Serial.println("");
  Serial.println("### Sleeping for " + String(TIME_TO_SLEEP) + " secs ###");

  //Go to sleep now
  esp_deep_sleep_start();
}

void loop() {
}
