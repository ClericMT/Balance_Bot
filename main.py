import time
from adafruit_crickit import crickit
from adafruit_circuitplayground import cp

# Create one continuous servo on crickit servo port #1
left_wheel = crickit.continuous_servo_1
# Create one continuous servo on crickit servo port #2
right_wheel = crickit.continuous_servo_3

const = 250
#servos top speed
max_speed = 1.0
#gyro position for vertical balance
bal_point = 30

def throttle(speed):
    if bal_point < angle < (bal_point + 45):
        left_wheel.throttle = -speed
        right_wheel.throttle = speed
    elif (bal_point - 45) < angle < bal_point:
        left_wheel.throttle = speed
        right_wheel.throttle = -speed

def balance():
        if -45 < angle < 45:
            throttle(speed)
        else:
            throttle(max_speed)

while True:
    if cp.button_a:
        bal_point += 5
        time.sleep(0.1)
    if cp.button_b:
        bal_point -= 5
        time.sleep(0.1)
    angle = cp.acceleration[1]*9
    speed = int(angle-bal_point)**2/2500
    balance()
    x, y, z = cp.acceleration
    print((x,y,z))
    time.sleep(0.05)
