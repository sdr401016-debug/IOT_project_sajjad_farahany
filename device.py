
class Device:
    
    def init(self,location,group,device_type,device_name,pin):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name 
        self.status='off'
        
        self.mqtt_broker='jasdhash'
        self.port=37362  
         
        self.mqtt_client=pin
        
        # self.connect_mqtt() 
        # self.setup_gpio()
        
    def connect_mqtt(self):
        mqtt.connect(self.mqtt_broker,self.port)
        
        
    def setup_gpio(self):
        
        if self.device_type=='lights':
            GPIO.setup(17,GPIO.OUT)
            
        elif self.device_type=='doors':
            GPIO.setup(27,GPIO.OUT)
            
        elif self.device_type=='camera':
        # دوربین
            GPIO.setup(38,GPIO.OUT) 

    def turn_on(self):
        self.status='on'
        mqtt.publish(self.mqtt_client,self.device_name,'TURN ON')
        
    def turn_off(self):
        self.status='off'
        mqtt.publish(self.mqtt_client,self.device_name,'TURN OFF')

    

