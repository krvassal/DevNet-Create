import machine
import network
import ubinascii
import time

SSID = "devnetcreate"
PASSWORD = "devnetcreate"

def ConnectWifi(ssid, password):
    ap = network.WLAN(network.AP_IF)
    if (ap.active()):
        ap.active(False)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(1)
    wlan.connect(ssid, password)
    return (wlan.ifconfig(),wlan.active())

ConnectWifi(SSID,PASSWORD)

mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
mac

time.sleep(5)
import webrepl_setup
