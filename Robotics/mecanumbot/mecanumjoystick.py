import time
import math

from gpiozero import Motor

#	Motors	P+	N-
#	FL		4	17
#	FR		23	24
#	BL		27	22
#	BR		26	19

motorFL = Motor( 4, 17, pwm=True)
motorFR = Motor(23, 24, pwm=True)
motorBL = Motor(27, 22, pwm=True)
motorBR = Motor(26, 19, pwm=True)

from pygame import display, joystick, event
from pygame import QUIT, JOYAXISMOTION, JOYBALLMOTION, JOYHATMOTION, JOYBUTTONUP, JOYBUTTONDOWN
display.init()
joystick.init()
joyaxisstate = [0,0,0,0,0,0,0,0,0,0] # LX, LY, LT, RX, RY, RT, ...

for i in range(joystick.get_count()):
	joystick.Joystick(i).init()

e = event.wait()
while e.type != QUIT:
	if e.type == JOYAXISMOTION:	joyaxisstate[e.axis] = round(e.value, 2)
	#elif e.type == JOYBALLMOTION: 	print('js', e.joy, 'ball', e.ball, round(e.rel, P))
	#elif e.type == JOYHATMOTION:  	print('js', e.joy, 'hat', e.hat, h[e.value])
	#elif e.type == JOYBUTTONUP:   	print('js', e.joy, 'button', e.button, 'up')
	#elif e.type == JOYBUTTONDOWN: 	print('js', e.joy, 'button', e.button, 'down')
	print(joyaxisstate)
	motorFL.value = min(max(joyaxisstate[3] - joyaxisstate[1] + joyaxisstate[0],-1.0),1.0)
	motorFR.value = min(max(joyaxisstate[3] + joyaxisstate[1] + joyaxisstate[0],-1.0),1.0)
	motorBL.value = min(max(joyaxisstate[3] - joyaxisstate[1] - joyaxisstate[0],-1.0),1.0)
	motorBR.value = min(max(joyaxisstate[3] + joyaxisstate[1] - joyaxisstate[0],-1.0),1.0)
	e = event.wait()
