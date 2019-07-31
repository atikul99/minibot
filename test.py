from miniLib import ArcadeDrive, Servo, Joystick
servo = Servo()
leftServo = servo.newServo(0)
rightServo = servo.newServo(1)

jstick = Joystick()
jstick.info()
jstick.newJoystick(0)

drive = ArcadeDrive(leftServo, rightServo)
while True:
    try:
        forwardAxis = round(jstick.getAxis(0), 2)
        steerAxis = round(jstick.getAxis(3), 2)
        drive.drive(forwardAxis, steerAxis)
    except:
        drive.drive(0, 0)

