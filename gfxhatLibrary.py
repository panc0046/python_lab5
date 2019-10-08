from gfxhat import lcd
from gfxhat import backlight
import time
import random

# Show vertical line
def verticalLine(x):
    y = 0;
    lcd.clear()
    lcd.show()
    backlight.set_all(0,0,255)
    backlight.show()
    if x < 127:
        for y in range(0,63):
            lcd.set_pixel(x,y,1)
            y = y+1
            lcd.show()

# Show horizontal line
def horizontalLine(y):
    x = 0;
    lcd.clear()
    lcd.show()
    backlight.set_all(0,0,255)
    backlight.show()
    if y < 63:
        for x in range(0,127):
            lcd.set_pixel(x,y,1)
            x = x+1
            lcd.show()
        
        
# Show staircase
def staircase(x,y,w,h):
    temp_w = x + w
    temp_h = y + h
    lcd.clear()
    lcd.show()
    backlight.set_all(0,0,255)
    backlight.show()
    while(x < 127 and y < 63):
        for x in range(x,temp_w):
            if x < 127 and y < 63:
                lcd.set_pixel(x,y,1)
                x=x+1
                lcd.show()
        for y in range(y,temp_h):
            if y < 63 and x < 127:
                lcd.set_pixel(x,y,1)
                y=y+1
                lcd.show()
        temp_w = temp_w+w
        temp_h = temp_h+h

#Show random pixels
def randomPixel(t):
    lcd.clear()
    lcd.show()
    backlight.set_all(0,0,255)
    backlight.show()
    end_time = time.time() + t
    while(time.time()<end_time):
       x = random.randrange(128)
       y = random.randrange(64)
       lcd.set_pixel(x,y,1)
       lcd.show()
       time.sleep(0.5)
    
#Clear backlight
def clearBacklight():
    time.sleep(2)
    backlight.set_all(0,0,0)
    backlight.show()