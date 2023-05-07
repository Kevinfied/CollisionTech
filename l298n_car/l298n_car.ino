// Motor A connections
int enA = 9;
int in1 = 2;
int in2 = 3;
// Motor B connections
int enB = 6;
int in3 = 4;
int in4 = 5;
int chl2 = 21;//channel 2 pin, right hand vertical on the controller
int chl4 = 19;//channel 4 pin, left hand horizontal on the controller
int va2;
int va4;
int va2b;
int va4b;
int stickH = 1940;
int stickL = 1060;
int mapLow = 50;
int va2up = 1515, va2low = 1485;  //pwm upper and lower bounds for rounding off close-to-zero values
void setup() {
  // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(chl2, INPUT);
  pinMode(chl4, INPUT);
  // Turn off motors - Initial state
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  Serial.begin(9600);
}

void loop() {
  va2 = pulseIn(chl2, HIGH, 25000);
  va4 = pulseIn(chl4, HIGH, 25000);//reading pwm ranging from 1000 to 2000 from flysky receiver
  
  //desensitize joystick and map pwm range to: -255 to 255
  if (va2 == 0 || (va2low < va2 && va2 < va2up)) va2b = 0;
  else {
    if (va2 >= va2up) {
      va2b = map(va2, va2up, stickH, mapLow, 255);
    } else va2b = map(va2, stickL, va2low, -255, -mapLow);  // round off close to zero joystick values
  }

  if (va4 == 0 || (va2low < va4 && va4 < va2up)) va4b = 0;
  else {
    if (va4 >= va2up) {
      va4b = map(va4, va2up, stickH, mapLow, 255);
    } else va4b = map(va4, stickL, va2low, -255, -mapLow);
  }

  // Serial.print(va4);
  // Serial.print(" va4, va4b");
  // Serial.print(va4b);
  // Serial.print("      ");
  // Serial.print(va2);
  // Serial.print(" va2, va2b");
  // Serial.println(va2b);

  arcadeDrive();
}

// This function lets you control spinning direction of motors
void directionControl() {
  // Set motors to maximum speed
  // For PWM maximum possible values are 0 to 255
  analogWrite(enA, 255);
  analogWrite(enB, 255);

  // Turn on motor A & B
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  delay(2000);

  // Now change motor directions
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  delay(2000);

  // Turn off motors
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  delay(2000);
}

// Arcade drive with variable control(not on/off)
void arcadeDrive() {
  int fwd = va2b;
  int turn = va4b;
  Serial.print(fwd);
  Serial.print("    ");
  Serial.print(turn);
  Serial.print("        ");
  Serial.print(fwd - turn);
  Serial.print("     ");
  Serial.println(fwd + turn);
  if (fwd - turn > 0) {
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    analogWrite(enA, fwd - turn);
    
  } else {
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    analogWrite(enA, -(fwd - turn));
  }

  if (fwd + turn > 0) {
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
    analogWrite(enB, fwd + turn);
  } else {
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
    analogWrite(enB, -(fwd + turn));
  }

  // Accelerate from zero to maximum speed
  // for (int i = 0; i < 256; i++) {
  // 	analogWrite(enA, i);
  // 	analogWrite(enB, i);
  // 	delay(20);
  // }

  // // Decelerate from maximum speed to zero
  // for (int i = 255; i >= 0; --i) {
  // 	analogWrite(enA, i);
  // 	analogWrite(enB, i);
  // 	delay(20);
  // }

  // Now turn off motors
  // digitalWrite(in1, LOW);
  // digitalWrite(in2, LOW);
  // digitalWrite(in3, LOW);
  // digitalWrite(in4, LOW);
}

void tankDrive(){
  int fwd = va2b;
  int turn = va4b;
  int leftPow;
  int rightPow;
  if (fwd < 0){//fwd stick forward
     if (turn >= 0) {
    leftPow = fwd - turn;
    rightPow = fwd;
    }
    else{
      leftPow = fwd;
      rightPow =  fwd + turn;
    }
  }else if (fwd > 0){
    if (turn < 0) {
    leftPow = fwd;
    rightPow = fwd - turn;
    }
    else{
      leftPow = fwd + turn;
      rightPow =  fwd;
    }
  }else{
    if (turn < 0) {
    leftPow =  fwd;
    rightPow = turn;
    }
    else{
      leftPow = -turn;
      rightPow =  fwd;
    }
  }
 
  Serial.print(fwd);
  Serial.print("    ");
  Serial.print(turn);
  Serial.print("    ");
  Serial.print(leftPow);
  Serial.print("    ");
  Serial.println(rightPow);

  if (leftPow > 0) {
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    analogWrite(enA, leftPow);
    
  } else {
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    analogWrite(enA, -(leftPow));
  }

  if (rightPow > 0) {
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
    analogWrite(enB, rightPow);
  } else {
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
    analogWrite(enB, -(rightPow));
  }
}
