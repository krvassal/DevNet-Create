import machine
from machine import I2C, Pin
import neopixel
import network
from umqtt.simple import MQTTClient
import time
from ssd1306 import SSD1306_I2C

c = MQTTClient(client_id = "umqtt_client", server = "test.mosquitto.org", port = 8883, ssl = True, ssl_params={"cert_reqs":ssl.CERT_REQUIRED, "ca_certs":"/flash/cert/ca.pem"})
c.connect()






# Uncomment below for OLED screen.
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c)
oled.invert(True)

# Uncomment below for NeoPixel
# np = neopixel.NeoPixel(machine.Pin(5), 12)

def ConnectWifi(ssid, password):
    ap = network.WLAN(network.AP_IF)
    if (ap.active()):
        ap.active(False)
    wlan = network.WLAN(network.STA_IF)
    wlan.connect(ssid, password)
    return (wlan.ifconfig(),wlan.active())

def ConnectSubscribe(topic,client):
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic)

def PixelShow(np, choice):
    n = np.n
    print(choice)

    if choice == "cycle":
        # cycle
        for i in range(4 * n):
            for j in range(n):
                np[j] = (0, 0, 0)
            np[i % n] = (255, 255, 255)
            np.write()
            time.sleep_ms(25)

    elif choice == "bounce":
        # bounce
        for i in range(4 * n):
            for j in range(n):
                np[j] = (0, 0, 128)
            if (i // n) % 2 == 0:
                np[i % n] = (0, 0, 0)
            else:
                np[n - 1 - (i % n)] = (0, 0, 0)
            np.write()
            time.sleep_ms(60)

    elif choice == "fade":
        # fade in/out
        for i in range(0, 4 * 256, 8):
            for j in range(n):
                if (i // 256) % 2 == 0:
                    val = i & 0xff
                else:
                    val = 255 - (i & 0xff)
                np[j] = (val, 0, 0)
            np.write()

    elif choice == "clear":
        # clear
        for i in range(n):
            np[i] = (0, 0, 0)
            np.write()


# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic,msg):
    print((topic,msg))
    result = msg.decode("utf-8")
    formattedTopic = 'Topic: ' + topic.decode("utf-8")
    oled.fill(0)
    oled.text(formattedTopic,1,4)
    oled.text(result,1,17)
    oled.show()

def print_topic_to_oled(client):
    while True:
        if True:
            client.wait_msg()
        else:
            client.check_msg()
            time.sleep(1)


# for i in range (0,128):
#     oled.text ('Hello',x ,4)
#     oled.fill(0)
#     oled.show()
#     time.sleep_ms(100)
