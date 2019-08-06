from gpiozero import Motor
import time
import math

#	Motors	P+	N-
#	FL		4	17
#	FR		27	22
#	BL		23	24
#	BR		26	19

motorFL = Motor( 4, 17, pwm=True)
motorFR = Motor(27, 22, pwm=True)
motorBL = Motor(23, 24, pwm=True)
motorBR = Motor(26, 19, pwm=True)

while True:
	spd = math.sin(time.time())
	motorFL.value = spd
	motorFR.value = spd
	motorBL.value = spd
	motorBR.value = spd
	print(spd)
