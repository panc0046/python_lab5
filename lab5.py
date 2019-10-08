from gfxhatLibrary import *

print("Enter 1. Draw vertical line")
print("Enter 2. Draw horizontal line")
print("Enter 3. Draw stair case")
print("Enter 4. Draw random pixels")
choice = int(input("Make your choice"))

# Show vertical line
if(choice == 1):
    x = int(input("Enter value of x"))
    verticalLine(x)

# Show horizontal line
elif(choice == 2):
    y = int(input("Enter value of y"))
    horizontalLine(y)

# Show Staircase
elif(choice == 3):
    x = int(input("Enter value of x"))
    y = int(input("Enter value of y"))
    w = int(input("Enter value of w"))
    h = int(input("Enter value of h"))
    staircase(x,y,w,h)

#Show random pixel
elif(choice == 4):
    time = int(input("Enter time in seconds"))
    randomPixel(time)

clearBacklight()