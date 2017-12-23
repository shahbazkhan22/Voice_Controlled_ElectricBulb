# Voice_Controlled_ElectricBulb
A software to control an electric bulb or any other household electrical appliance with human voices. It has been designed using arduino microcontroller and UART serial adapter.

# Header files to be included in Python code
* serial
* speech_recognition

# Driver required
* CP210x USB to UART Bridge VCP Driver

# About code
First the voice is converted in text using speech_recognition module then it is sent to arduino using serial (UART) communication. Using arduino, text is received from serial and then it is processed to control electrical devices.

# Commands 
* Say 'switch on' to turn the bulb on.
* Say 'switch off' to turn the bulb off.
* Say 'break' to completely shut down the device.
