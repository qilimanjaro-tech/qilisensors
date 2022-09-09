import paho.mqtt.client as mqttClient
import time
import os
  
def on_connect(client, userdata, flags, rc):
  
    if rc == 0:
  
        print("Connected to broker")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
  
    else:
  
        print("Connection failed")
  
def on_message(client, userdata, message):
    print("Message received: %d" % int(message.payload))
  

if __name__ == "__main__":
    
    Connected = False   #global variable for the state of the connection
    
    broker_address= os.getenv("MQTT_HOST")   #Broker address
    port = 1881                              #Broker port
    #user = "yourUser"                       #Connection username
    #password = "yourPassword"               #Connection password
    
    client = mqttClient.Client("Python")               #create new instance
    #client.username_pw_set(user, password=password)   #set username and password
    client.on_connect= on_connect                      #attach function to callback
    client.on_message= on_message                      #attach function to callback
    
    client.connect(broker_address, port=port)          #connect to broker
    
    client.loop_start()        #start the loop
    
    while Connected != True:    #Wait for connection
        time.sleep(0.1)
    
    client.subscribe("shellies/shellyem-BCFF4DFD0908/emeter/0/energy")

    try:
        while True:
            time.sleep(100)
  
    except KeyboardInterrupt:
        print("exiting")
        client.disconnect()
        client.loop_stop()