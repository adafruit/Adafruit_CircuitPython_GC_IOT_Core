# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
from os import getenv

import adafruit_connection_manager
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import board
import busio
import neopixel
from adafruit_esp32spi import adafruit_esp32spi, adafruit_esp32spi_wifimanager
from digitalio import DigitalInOut

from adafruit_gc_iot_core import MQTT_API, Cloud_Core

# Get WiFi details and Google Cloud keys, ensure these are setup in settings.toml
ssid = getenv("CIRCUITPY_WIFI_SSID")
password = getenv("CIRCUITPY_WIFI_PASSWORD")
cloud_region = getenv("cloud_region")
device_id = getenv("device_id")
private_key = getenv("private_key")
project_id = getenv("project_id")
registry_id = getenv("registry_id")
jwt = getenv("jwt")

### WiFi ###

# If you are using a board with pre-defined ESP32 Pins:
esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)

# If you have an externally connected ESP32:
# esp32_cs = DigitalInOut(board.D9)
# esp32_ready = DigitalInOut(board.D10)
# esp32_reset = DigitalInOut(board.D5)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)
"""Use below for Most Boards"""
status_pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)  # Uncomment for Most Boards
"""Uncomment below for ItsyBitsy M4"""
# status_pixel = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)
# Uncomment below for an externally defined RGB LED
# import adafruit_rgbled
# from adafruit_esp32spi import PWMOut
# RED_LED = PWMOut.PWMOut(esp, 26)
# GREEN_LED = PWMOut.PWMOut(esp, 27)
# BLUE_LED = PWMOut.PWMOut(esp, 25)
# status_pixel = adafruit_rgbled.RGBLED(RED_LED, BLUE_LED, GREEN_LED)
wifi = adafruit_esp32spi_wifimanager.WiFiManager(esp, ssid, password, status_pixel=status_pixel)

### Code ###


# Define callback methods which are called when events occur
def connect(client, userdata, flags, rc):
    # This function will be called when the client is connected
    # successfully to the broker.
    print("Connected to MQTT Broker!")
    print(f"Flags: {flags}\n RC: {rc}")
    # Subscribes to commands/# topic
    google_mqtt.subscribe_to_all_commands()

    # Publish to the default "events" topic
    google_mqtt.publish("testing", "events", qos=1)


def disconnect(client, userdata, rc):
    # This method is called when the client disconnects
    # from the broker.
    print("Disconnected from MQTT Broker!")


def subscribe(client, userdata, topic, granted_qos):
    # This method is called when the client subscribes to a new topic.
    print(f"Subscribed to {topic} with QOS level {granted_qos}")


def unsubscribe(client, userdata, topic, pid):
    # This method is called when the client unsubscribes from a topic.
    print(f"Unsubscribed from {topic} with PID {pid}")


def publish(client, userdata, topic, pid):
    # This method is called when the client publishes data to a topic.
    print(f"Published to {topic} with PID {pid}")


def message(client, topic, msg):
    # This method is called when the client receives data from a topic.
    print(f"Message from {topic}: {msg}")


# Connect to WiFi
print("Connecting to WiFi...")
wifi.connect()
print("Connected!")

pool = adafruit_connection_manager.get_radio_socketpool(esp)
ssl_context = adafruit_connection_manager.get_radio_ssl_context(esp)

# Initialize Google Cloud IoT Core interface
settings = {
    cloud_region: cloud_region,
    device_id: device_id,
    private_key: private_key,
    project_id: project_id,
    registry_id: registry_id,
}
google_iot = Cloud_Core(esp, settings)

# Optional JSON-Web-Token (JWT) Generation
# print("Generating JWT...")
# jwt = google_iot.generate_jwt()
# print("Your JWT is: ", jwt)

# Set up a new MiniMQTT Client
client = MQTT.MQTT(
    broker=google_iot.broker,
    username=google_iot.username,
    password=jwt,
    client_id=google_iot.cid,
    socket_pool=pool,
    ssl_context=ssl_context,
)

# Initialize Google MQTT API Client
google_mqtt = MQTT_API(client)

# Connect callback handlers to Google MQTT Client
google_mqtt.on_connect = connect
google_mqtt.on_disconnect = disconnect
google_mqtt.on_subscribe = subscribe
google_mqtt.on_unsubscribe = unsubscribe
google_mqtt.on_publish = publish
google_mqtt.on_message = message


print(f"Attempting to connect to {client.broker}")
google_mqtt.connect()

# Pump the message loop forever, all events are
# handled in their callback handlers
# while True:
#    google_mqtt.loop()

# Start a blocking message loop...
# NOTE: NO code below this loop will execute
# NOTE: Network reconnection is handled within this loop
while True:
    try:
        google_mqtt.loop()
    except (ValueError, RuntimeError) as e:
        print("Failed to get data, retrying\n", e)
        wifi.reset()
        google_mqtt.reconnect()
        continue
    time.sleep(1)
