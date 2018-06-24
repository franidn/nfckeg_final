#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <EEPROM.h>
#include <Arduino.h>

//Definim red wifi on ens conectem
#define wifi_ssid "MOVISTAR_BD52"
#define wifi_password "4fkJNmcCE4MdQGX6HTka"

//#define wifi_ssid "pic2"
//#define wifi_password "pic2essuperguay"
//IP de la wifi on esta el servidor

//#define mqtt_server "192.168.43.110"

#define mqtt_server "192.168.1.38"

//#define mqtt_user "your_username"
//#define mqtt_password "your_password"

//TOPICS
#define humidity_topic "sensor/nfc"
#define flux_topic "sensor/flux"

//Pins i variables pel flowmeter
const int buttonPin = D2; // variable for D2 pin
char push_data[200];
int addr = 0;
byte sensorInterrupt = 0; // 0 = digital pin 2

//VALOR DE CALIBRACIO SHA DE CAMBIAR
float calibrationFactor = 4.5;

volatile byte pulseCount;

float flowRate;
unsigned int flowMilliLitres;
unsigned long totalMilliLitres;
unsigned long oldTime;



#define DHTTYPE DHT22
#define DHTPIN  14

WiFiClient espClient;
PubSubClient client(espClient);
//DHT dht(DHTPIN, DHTTYPE, 11); // 11 works fine for ESP8266

void setup() {
  Serial.begin(115200);
  pinMode(buttonPin, INPUT);
  //Inicialitzacio variables flowmeter
  pulseCount = 0;
  flowRate = 0.0;
  flowMilliLitres = 0;
  totalMilliLitres = 0;
  oldTime = 0;
  digitalWrite(buttonPin, HIGH);
  attachInterrupt(digitalPinToInterrupt(buttonPin), pulseCounter, RISING);

  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(wifi_ssid);

  WiFi.begin(wifi_ssid, wifi_password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    // If you want to use a username and password, change next line to
    if (client.connect("ESP8266Client")) {
    //if (client.connect("ESP8266Client", mqtt_user, mqtt_password)) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

bool checkBound(float newValue, float prevValue, float maxDiff) {
  return !isnan(newValue) &&
         (newValue < prevValue - maxDiff || newValue > prevValue + maxDiff);
}

long lastMsg = 0;
float temp = 0.0;
float hum = 0.0;
float diff = 1.0;

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  delay(2000);


        ///////////////////////////////CALCULS FLUXOMETRE
        detachInterrupt(sensorInterrupt);

        flowRate = ((1000.0 / (millis() - oldTime)) * pulseCount) / calibrationFactor;

        oldTime = millis();

        flowMilliLitres = (flowRate / 60) * 1000;
        totalMilliLitres += flowMilliLitres;
        
        unsigned int frac;
////////////////FI CALCULS FLUXOMETRE/////////////////////////////////////////////////////////

/////////////////imprimim i enviem per MQTT al topic sensor/flux/////////////////////////////
        
      Serial.print("Flow rate:");
      Serial.println(String(flowRate).c_str());
      client.publish(flux_topic, String(flowRate).c_str(), true);
      
/////////////////////////////////////////////////////////////////////////////////////////////


      


}


void pulseCounter() {
    // Increment the pulse counter
    pulseCount++;
}


