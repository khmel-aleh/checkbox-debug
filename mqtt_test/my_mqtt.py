import paho.mqtt.client as mqtt
import os
from urllib.parse import urlparse

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://vvyidaml:iEqc_6pBU8XO@m15.cloudmqtt.com:10509')
print(url_str)
url = urlparse(url_str)
topic = 'test'
# topic = url.path[1:] or 'test'

# mqtt://user:password@server:port
# mqtt://vvyidaml:iEqc_6pBU8XO@m15.cloudmqtt.com:10509

# Connect
print('Connecting with {}:{} to {} {}'.format(url.username, url.password, url.hostname, url.port))
mqttc.username_pw_set(url.username, url.password)
mqttc.connect(url.hostname, url.port)

# Start subscribe, with QoS level 0
print('Subscribe to ' + topic)
mqttc.subscribe(topic, 0)

# Publish a message
mqttc.publish(topic, "my message1")

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))
