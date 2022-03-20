/***************************************************************************
  This is an awesome project
 
 ***************************************************************************/
#include <soc/sens_reg.h>
#include <base64.h>

#define uS_TO_S_FACTOR 1000000 //Conversion factor for micro seconds to seconds
#define TIME_TO_SLEEP 5 * 60   //Time ESP32 will go to sleep (in seconds)

// To save registry for the first time
uint64_t reg_a;
uint64_t reg_b;
uint64_t reg_c;

int err;
int duration = 30 * 1000; // 30 s to millis

// Relay
int relay12V = 15;

RTC_DATA_ATTR int bootCount = 0;
unsigned long delayTime;

void setup()
{
  delay(1000);
  Serial.begin(115200);

  pinMode(relay12V, OUTPUT);
  digitalWrite(relay12V, HIGH);

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
