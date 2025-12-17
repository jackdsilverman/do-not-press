from machine import Pin
from utime import sleep
import urequests  # Import the urequests library for HTTP requests
import network  # Import the network module for Wi-Fi connectivity
from my_secrets import secrets  # Import Wi-Fi credentials and API key

# Wi-Fi credentials
WIFI_SSID = secrets['WIFI_SSID']  # Replace with your Wi-Fi SSID
WIFI_PASSWORD = secrets['WIFI_PASSWORD']  # Replace with your Wi-Fi password

# REST API endpoint
API_URL = "https://odzzi38fjk.execute-api.us-east-2.amazonaws.com/dev/button"
headers = {
    "x-api-key": secrets['API_KEY'],  # Replace with your actual API key
}

# Configure LED on GPIO 14 as output
led = Pin(16, Pin.OUT)
# Configure button on GPIO 13 as input with pull-up resistor
button = Pin(0, Pin.IN)
pi_led = Pin('LED', Pin.OUT)

# Function to connect to Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)  # Create a station interface
    wlan.active(True)  # Activate the interface
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)  # Connect to the Wi-Fi network

    print("Connecting to Wi-Fi...")
    while not wlan.isconnected():  # Wait until connected
        sleep(1)
        print("Still connecting...")

    print("Connected to Wi-Fi!")
    print("IP Address:", wlan.ifconfig()[0])  # Print the IP address
    pi_led.on()  # Turn on the built-in LED to indicate Wi-Fi connection
# Connect to Wi-Fi
connect_to_wifi()

print("Press the button to turn on the LED...")

while True:
    try:
        if button.value() == 1:  # Button pressed (active low)
            print(button.value())
            led.on()
            
            # Call the REST API
            try:
                response = urequests.post(API_URL, json={}, headers=headers)
                print("API Response:", response.text)
                response.close()
            except Exception as e:
                print("Failed to call REST API:", e)
            led.off()
        else:
            led.off()
    except KeyboardInterrupt:
        break