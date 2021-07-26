# Python-Opencv-Arduino-ServoControl  
With pyFirmata, opencv and cvzone  
pip install pyFirmata  
pip install cvzone  
pip install opencv-python  

<img src="https://github.com/heimdilon/Python-Opencv-Arduino-ServoControl/blob/main/pics/demo.gif" width="500" height="400" />  

#Setting up Arduino  

->Open Arduino IDE  
->Open Tools/Manage Libraries  
<img src="https://github.com/heimdilon/Python-Opencv-Arduino-ServoControl/blob/main/pics/1.png" width="500" height="400" />  
->Search firmata and install  
<img src="https://github.com/heimdilon/Python-Opencv-Arduino-ServoControl/blob/main/pics/2.png" width="500" height="400" />  
->Open File/Examples/Firmata/StandartFirmata  
<img src="https://github.com/heimdilon/Python-Opencv-Arduino-ServoControl/blob/main/pics/3.png" width="500" height="400" />  
->Open Tools and choose your board and serial port  
<img src="https://github.com/heimdilon/Python-Opencv-Arduino-ServoControl/blob/main/pics/4.png" width="500" height="400" />  
->Upload  

#Other things  

->If you want to calulate different fingers distance you can change codefrom line 36  
<img src="https://github.com/heimdilon/Python-Opencv-Arduino-ServoControl/blob/main/pics/5.png" width="1000" height="100" />  
->Here is hand landmarks  
<img src="https://github.com/heimdilon/Python-Opencv-Arduino-ServoControl/blob/main/pics/hand_landmarks.png" width="600" height="400" />  
->If you want to control arduino with HC-05 bluetooth. You nedd to chance baudrate in arduino code uploaded. Change Firmata.begin(57600); to Firmata.begin(9600);  
<img src="https://github.com/heimdilon/Python-Opencv-Arduino-ServoControl/blob/main/pics/6.png" width="500" height="400" />  
->Here is Bluetoot module connection
<img src="https://github.com/heimdilon/Python-Opencv-Arduino-ServoControl/blob/main/pics/7.png" width="600" height="400" />  
