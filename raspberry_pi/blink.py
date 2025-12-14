from machine import Pin
from utime import sleep

# Configure LED on GPIO 14 as output
led = Pin(16, Pin.OUT)
pin = Pin("LED", Pin.OUT)


# Configure button on GPIO 13 as input with pull-up resistor
button = Pin(15, Pin.IN)

print("Press the button to turn on the LED...")

while True:
    try:
       if button.value() == 1:  # Button pressed (active low)
          led.on()
          sleep(1)  # Keep the LED on for 3 seconds
          led.off()       
       else:
          led.off()
    except KeyboardInterrupt:
          break

print("Finished.")