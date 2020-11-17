#include <Servo.h>             //Servo library
Servo servo_test;      
int angle = 0;

int ACWATERPUMP = 13; //You can remove this line, it has no use in the program.
int sensor = 8; //You can remove this line, it has no use in the program.
int val; //This variable stores the value received from Soil moisture sensor.
void setup() {
  pinMode(13,OUTPUT); //Set pin 13 as OUTPUT pin, to send signal to relay
  pinMode(8,INPUT); //Set pin 8 as input pin, to receive data from Soil moisture sensor.
  servo_test.attach(9); 
 
}

void loop() {  
  String stop  = "%, stop fill the water ";
  String run = "%, fill the water now ";
  Serial.begin(9600);
  { 
  for(angle = 0; angle < 180; angle += 2)    // command to move from 0 degrees to 180 degrees 
  {                                  
    servo_test.write(angle);                 //command to rotate the servo to the specified angle
    delay(15);                       
  } 
 
  delay(1000);
  
  for(angle = 180; angle>=1; angle-=2)     // command to move from 180 degrees to 0 degrees 
  {                                
    servo_test.write(angle);              //command to rotate the servo to the specified angle
    delay(5);                       
  } 
    delay(1000);
}
  int val = digitalRead(8);
  int sensorValue = analogRead(8);//Read data from soil moisture sensor  
  if(val == HIGH ) 
  {
  digitalWrite(13,LOW); //if soil moisture sensor provides LOW value send LOW value to relay
  Serial.print(sensorValue);
  Serial.print(run);
  Serial.println("Spray Activated!");
  delay(1000);
  }
  else
  {
  digitalWrite(13,HIGH);
  Serial.print(sensorValue);
  Serial.print(stop);//if soil moisture sensor provides HIGH value send HIGH value to relay
  Serial.println("Spray Activated!");
  delay(1000);
  }
  delay(400); //Wait for few second and then continue the loop.
}
