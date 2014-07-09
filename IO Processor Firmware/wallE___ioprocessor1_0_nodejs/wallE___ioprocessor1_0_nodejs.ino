#include <Wire.h>
#include <Servo.h> 

#define SLAVE_ADDRESS 0x04

Servo myservo; 
int pos = 80;    // variable to store the servo position 

int number = 0;

int state = 0;
int upflag=0,downflag=0;
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
    
    myservo.attach(9);  // attaches the servo on pin 9 to the servo object 
    myservo.write(pos);
    delay(15);
}
 
void loop() {
   // delay(100);
   
     if(upflag == 1)
         {
          if(pos<=180 && pos>=0)
         { pos=pos+10;
           myservo.write(pos);              // tell servo to go to position in variable 'pos' 
            delay(15);
         }
         upflag=0;
         }
       if(downflag == 1)
         { 
              if(pos<=180 && pos>=0)
              {pos=pos-10;
             myservo.write(pos);              // tell servo to go to position in variable 'pos' 
              delay(15);
          }
          downflag=0;
         }
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
           //delay(1000);
           //halt();
         }
       else if(number == 2)
         { //Serial.println("Left");
           left();
          // delay(1000);
         //  halt();
         }
      else if(number == 3)
         {// Serial.println("Right");
           right();
          // delay(1000);
         //  halt();
         }
      else if(number == 4)
         { //Serial.println("Stop");
         halt();
         }
         else if(number == 5)
         { //Serial.println("Stop");
         backward();
       //  delay(1000);
        //   halt();
         }
           else if(number == 6)
         {
         upflag=1;
         }
           else if(number == 7)
         { 
              downflag=1;
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
  digitalWrite(leftmotorp,HIGH);
  digitalWrite(leftmotorp,LOW); ///
}

void left(){
  digitalWrite(rightmotorp,LOW);
  digitalWrite(rightmotorn,HIGH);
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
