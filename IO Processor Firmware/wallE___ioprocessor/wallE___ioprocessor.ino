#include <Wire.h>

#define SLAVE_ADDRESS 0x04

int number = 0;

int state = 0;

int rightmotorp = 13;
int rightmotorn = 14;
int leftmotorp = 15;
int leftmotorn = 20;
 
void setup() {
  for(int i=13;i<16;i++)
  {
    pinMode(i,OUTPUT);
  }
  pinMode(20,OUTPUT);
  
    //Serial.begin(9600);         // start serial for output

    // initialize i2c as slave

    Wire.begin(SLAVE_ADDRESS);

 

    // define callbacks for i2c communication

    Wire.onReceive(receiveData);

    //Wire.onRequest(sendData);

 
    //Serial.println("Ready!");
}
 
void loop() {
    delay(100);
}

// callback for received data
void receiveData(int byteCount){
 
    while(Wire.available()) {
        number = Wire.read();
        //Serial.print("data received: ");
       // Serial.println(number);
       if(number == 1)
         { //Serial.println("Forward");
           forward();  
         }
       else if(number == 2)
         { //Serial.println("Left");
           left();
         }
      else if(number == 3)
         {// Serial.println("Right");
           right();
         }
      else if(number == 4)
         { //Serial.println("Stop");
         halt();
         }
         else if(number == 5)
         { //Serial.println("Stop");
         backward();
         }
     }

}

 void forward(){
  digitalWrite(rightmotorp,HIGH);
  digitalWrite(rightmotorn,LOW);
  digitalWrite(leftmotorp,HIGH);
  digitalWrite(leftmotorn,LOW);
}
void backward(){
digitalWrite(rightmotorp,LOW);
digitalWrite(rightmotorn,HIGH);
digitalWrite(leftmotorp,LOW);
digitalWrite(leftmotorn,HIGH);
}

void right()
{
  digitalWrite(rightmotorp,HIGH);
  digitalWrite(rightmotorn,LOW);
  digitalWrite(leftmotorp,LOW);
  digitalWrite(leftmotorp,LOW);
}

void left(){
  digitalWrite(rightmotorp,LOW);
  digitalWrite(rightmotorn,LOW);
  digitalWrite(leftmotorp,HIGH);
  digitalWrite(leftmotorn,LOW);
}



void halt(){
digitalWrite(rightmotorp,LOW);
digitalWrite(rightmotorn,LOW);
digitalWrite(leftmotorp,LOW);
digitalWrite(leftmotorn,LOW);
}

// callback for sending data

//void sendData(){

//    Wire.write(number);

//}
