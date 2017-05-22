#
# Note: Replace < > with the appropriate variable

from umqtt.simple import MQTTClient

client = MQTTClient ("ESP8266-<YOUR_NAME_HERE>", "192.168.50.10")
client.connect()

client.publish("<neo/rgb/lcd>", "<message>")


client.publish('neo', '{"command":"loop"}')
client.publish('neo', '{"command":"one", "pixelNum": 11, "color":"(100,255,255)"}')

client.publish('lcd', '{"command","date"}')
client.publish('lcd', '{"command","time"}')
client.publish('lcd', '{"command","text","text","beepBoopMEEP"}')

client.publish('rgb', '{"color": "255,255,255")}')('rgb')
