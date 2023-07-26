#include <ESP8266WiFi.h>
 
#define GND D0
#define V5 D1
#define SPEAKER D2
 
const char* ssid = "Hackatton4";
const char* password = "230726h4";
 
WiFiServer server(80);
 
void setup() {
  pinMode(SPEAKER, OUTPUT);
  pinMode(GND, OUTPUT);
  pinMode(V5, OUTPUT);
  
  digitalWrite(GND, LOW);
  digitalWrite(V5, LOW);
  
  Serial.begin(115200);
  
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connecting to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  
  server.begin();
  Serial.println("Server started");
}
 
void loop() {
  digitalWrite(GND, LOW);
  digitalWrite(V5, HIGH);
  WiFiClient client = server.available();
  if(!client) return;
  
  Serial.println("새로운 클라이언트");
  client.setTimeout(5000);
  
  String request = client.readStringUntil('\r');
  Serial.println("request: ");
  Serial.println(request);
 
  if(request.indexOf("/AI/1") != -1) {
    tone(SPEAKER, 349);
    delay(1000);
  }else if(request.indexOf("/AI/2") != -1) {
    tone(SPEAKER, 349);
    delay(500);
  }else if(request.indexOf("/AI/3") != -1) {
    tone(SPEAKER, 349);
    delay(250);
  }else if(request.indexOf("/AI/4") != -1) {
    tone(SPEAKER, 349);
    delay(125);
  }else {
    Serial.println("invalid request");
  }
 
  while(client.available()) {
    client.read();
  }
 
  client.print("HTTP/1.1 200 OK");
  client.print("Content-Type: text/html\r\n\r\n");
  client.print("<!DOCTYPE HTML>");
  client.print("<html>");
  client.print("<head>"); 
  client.print("<meta&nbsp;charset=\"UTF-8\">");
  client.print("<title>AI</title>");
  client.print("</head>");
  client.print("<body>");
  client.print("");
  client.print("</body>");
  client.print("</html>");
 
  Serial.println("클라이언트 연결 해제");
}
