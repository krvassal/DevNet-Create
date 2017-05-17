import kris
from umqtt.simple import MQTTClient

SSID = "devnetcreate"
PASSWORD = "devnetcreate"
CLIENT = MQTTClient("ESP-OLED", "192.168.50.12")
TOPIC = b"oled"

kris.ConnectWifi(SSID,PASSWORD)
kris.ConnectSubscribe(TOPIC,CLIENT)
kris.print_topic_to_oled(CLIENT)


