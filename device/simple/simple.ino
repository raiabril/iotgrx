/***************************************************************************
  This is an awesome project
 
 ***************************************************************************/
#include <WiFiMulti.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <soc/sens_reg.h>
#include <base64.h>

// #define SEALEVELPRESSURE_HPA (1013.25)
#define SEALEVELPRESSURE_HPA (942.19) // Madrid

#define uS_TO_S_FACTOR 1000000 //Conversion factor for micro seconds to seconds
#define TIME_TO_SLEEP 5 * 60   //Time ESP32 will go to sleep (in seconds)

// To save registry for the first time
uint64_t reg_a;
uint64_t reg_b;
uint64_t reg_c;

// Auth
String device_name = "simple";
String token = "3c4751b9-b4b9-4b98-b343-d31226e74585";
String Url = "https://iotgrx.pythonanywhere.com/api/v1";

// Wifi credentials
// const char* ssid = "MIWIFI_xua4";
// const char* password =  "RybpDPX4jHXd";
// const char* ssid = "MOVISTAR_DE60";
// const char* password =  "Jo4Ye3o3H4jUmdWpjqjj";
const char *ssid = "MIWIFI_5778";
const char *password = "6KDXENH8";

int err;
int duration = 30 * 1000;

// Relay
int relay12V = 15;

RTC_DATA_ATTR int bootCount = 0;
unsigned long delayTime;

// Create object Wifi
WiFiMulti wifiMulti;

void setup()
{
  delay(1000);
  Serial.begin(115200);

  pinMode(relay12V, OUTPUT);
  digitalWrite(relay12V, HIGH);

  Serial.println("");
  Serial.println("");
  Serial.println("### Simple Naos 8 ###");
  Serial.println("Device = " + device_name);
  Serial.println("Token = " + token);
  Serial.println("");
  Serial.println("## Test ##");
  Serial.println("Boot number = " + String(bootCount + 1));

  if (bootCount == 0)
  {
    Serial.println("... First boot. Saving registry ...");
    reg_a = READ_PERI_REG(SENS_SAR_START_FORCE_REG);
    reg_b = READ_PERI_REG(SENS_SAR_READ_CTRL2_REG);
    reg_c = READ_PERI_REG(SENS_SAR_MEAS_START2_REG);
  }
  else
  {
    Serial.println("... Fixing registry ...");
    WRITE_PERI_REG(SENS_SAR_START_FORCE_REG, reg_a); // fix ADC registers
    WRITE_PERI_REG(SENS_SAR_READ_CTRL2_REG, reg_b);
    WRITE_PERI_REG(SENS_SAR_MEAS_START2_REG, reg_c);
  }
  delay(1000);

  //Increment boot number and print it every reboot
  ++bootCount;

  Serial.println("");
  Serial.println("Watering for: " + String(duration) + " ms");
  digitalWrite(relay12V, LOW);
  delay(duration);
  digitalWrite(relay12V, HIGH);
  Serial.println("Done");

  wifiMulti.addAP(ssid, password);
  delay(1000);

  Serial.println("");
  Serial.println("### Connecting Wifi... ###");

  if (wifiMulti.run() == WL_CONNECTED)
  {
    Serial.print("Connected: ");
    Serial.println(WiFi.localIP());
    delay(1000);
  }

  if (WiFi.status() == WL_CONNECTED && duration > 0)
  {
    HTTPClient httpLog;
    httpLog.addHeader("Content-Type", "application/json"); //Specify content-type header
    httpLog.addHeader("Authorization", token);
    httpLog.begin(Url + "/water/log"); //Specify destination for HTTP request

    char buffer[1024];
    StaticJsonDocument<128> logEvent;
    logEvent["device_code"] = device_name;
    logEvent["duration"] = duration;
    serializeJson(logEvent, buffer);
    Serial.println("Sending log");
    Serial.println(buffer);

    Serial.println("");
    Serial.println("Launching POST to log watering event ...");
    int httpResponseCode = httpLog.POST(buffer); //Send the actual POST request

    if (httpResponseCode == 201)
    {
      String response = httpLog.getString(); //Get the response to the request
      Serial.println("201 Created");
      Serial.println(response);
    }
    else
    {
      Serial.print("Error on sending GET: ");
      String response = httpLog.getString();
      Serial.println(httpResponseCode);
      //Serial.println(response);
    }

    httpLog.end(); //Free resources for log
  }
  else
  {
    Serial.println("Water log not sent");
  }

  //Set timer to x seconds
  esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);
  delay(1000);
  Serial.println("### Sleeping for " + String(TIME_TO_SLEEP) + " secs ###");

  //Go to sleep now
  esp_deep_sleep_start();
}

void loop()
{
}
