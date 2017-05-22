import kris
from umqtt.simple import MQTTClient

SSID = "devnetcreate"
PASSWORD = "devnetcreate"
CLIENT = MQTTClient("ESP-OLED", "192.168.50.10")
TOPIC = b"lcd"
#TOPIC = b"lcd"

#c = MQTTClient(client_id = "umqtt_client", server = "test.mosquitto.org", port = 8883, ssl = True, ssl_params={"cert_reqs":ssl.CERT_REQUIRED, "ca_certs":"/flash/cert/ca.pem"})
#c.connect()



kris.ConnectWifi(SSID,PASSWORD)
kris.ConnectSubscribe(TOPIC,CLIENT)
kris.print_topic_to_oled(CLIENT)


