import time
import board
import digitalio

LED_PINS = [board.GP0, board.GP1,board.GP2,board.GP3,
board.GP4,board.GP5,board.GP6,board.GP7,
board.GP16,board.GP17,board.GP26,board.GP27,
board.GP28]

LEDS = []
for pin in LED_PINS:
    # Set pins as digital output
    digout = digitalio.DigitalInOut(pin)
    digout.direction = digitalio.Direction.OUTPUT
    LEDS.append(digout)

# for loop
for i in range(len(LEDS)):
    LEDS[i].value = True    
    time.sleep(0.5) # sleep for 0.5 seconds