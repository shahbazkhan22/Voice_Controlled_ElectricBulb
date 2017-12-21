
int incomingByte = 0;   // for incoming serial data

void setup() {
        // opens serial port, sets data rate to 9600 bps
        Serial.begin(9600);
        //Setting relay pin for OUTPUT mode
        pinMode(7,OUTPUT);
}

void loop() {

        // command relay only when data is available at serial port
        if (Serial.available() > 0) {
                // read the incoming byte:
                incomingByte = Serial.read();
                //check if input received is HIGH
                if(incomingByte==49)
                digitalWrite(7,HIGH);
                else
                digitalWrite(7,LOW);
                //displaying on serial monitor
                Serial.println((incomingByte));
        }
}
 
