from gpiozero import MCP3008
import paho.mqtt.client as paho
import time
import json

pot= MCP3008(0)

broker="broker.hivemq.com"
port=8000

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    global connected
    connected = True

def on_subscribe(client, userdata, mid, granted_qos):   #create function for callback
   print("subscribed with qos",granted_qos, "\n")
   pass
def on_message(client, userdata, message):
    print("message received  "  ,str(message.payload.decode("utf-8")))
def on_publish(client,userdata,mid):   #create function for callback
   print("data published mid=",mid, "\n")
   pass
def on_disconnect(client, userdata, rc):
   print("client disconnected ok")
   
client= paho.Client("tempclient",transport='websockets')       #create client object
client.on_subscribe = on_subscribe       #assign function to callback
client.on_publish = on_publish        #assign function to callback
client.on_message = on_message        #assign function to callback
client.on_disconnect = on_disconnect
client.on_connect = on_connect
print("connecting to broker ",broker,"on port ",port)
connected = False
client.connect(broker,port)
client.loop_start()
while connected != True:    #Wait for connection
    time.sleep(0.1)
while (True):
    time.sleep(1)
    client.publish("nextlab_potentiometer", json.dumps({ "potentiometer":pot.value}))
    client.loop()