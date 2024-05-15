import pyautogui
import math
import time

# Set the center of the circle and its radius
center_x = 500  # Adjust these coordinates as needed
center_y = 500
radius = 100

# Set the speed of the cursor movement
speed = 0.01  # Adjust this value to control the speed (in seconds)

try:
    angle = 0
    while True:
        # Calculate the coordinates of the point on the circle's circumference
        x = center_x + int(radius * math.cos(math.radians(angle)))
        y = center_y + int(radius * math.sin(math.radians(angle)))
        
        # Move the mouse cursor to the calculated coordinates
        pyautogui.moveTo(x, y)
        
        # Increment the angle for the next point on the circle
        angle += 1  # Adjust the increment to control the speed of the movement
        
        # Wrap the angle around to keep it within the range [0, 360)
        angle %= 360
        
        # Pause for a short duration to control the speed of the movement
        time.sleep(speed)

except KeyboardInterrupt:
    # Stop the loop if Ctrl+C is pressed
    pass
