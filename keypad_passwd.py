import RPi.GPIO as GPIO
import time

#GPIO Setup
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)

#set gpio for key pad

COL = [7,11,13,15]
ROW = [12,16,18,22]

for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)
for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

# set gpio for servo   
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11,50)
pwm.start(5)

#Function to check keypad input!
def check_keypad(length):

    COL = [4,17,22,21]
    ROW = [18,23,24,25]

    MATRIX = [["1","2","3","A"],
              ["4","5","6","B"],
              ["7","8","9","C"],
              ["0","F","E","D"]]
    result = ""
    while(True):
        for j in range(4):
            GPIO.output(COL[j], 0)

            for i in range(4):
                if GPIO.input(ROW[i]) == 0:
                    time.sleep(0.02)
                    result = result + MATRIX[i][j]
                    while(GPIO.input(ROW[i]) == 0):
                          time.sleep(0.02)

            GPIO.output(COL[j], 1)
            if len(result) >= length:
                return result


# password
password = "A1234"
length = len(password)

#Password From KeyPad
print("Please Enter User Password: ")
result = check_keypad(length)


#Password Check
if result == password:
    print("Unlock ")
    pwm.ChangeDutyCycle(10)

else:
    print("Stay locked")   
