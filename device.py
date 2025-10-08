

'''
سلام استاد روز بخیر ان کد هاست بخش اول برای سوال اول و در ادامه به سوال دوم و سوم پرداختم 
در بخشی که باید سوال سوم رو انجام میدادم سعی کرد متن های درست انگلیسی رو برای پرینت بگذارم ولی خب انگلیسیم ضعیفه و شرمنده ام اگر جایی رو اشتباه نوشتم 
 ممنون که دارید چک میکنید و وقت میگذارید اگر هم جایی اشکال داشت ممنون میشم بگید درستش کنم 
استاد بخش آخر هنوز کامل نشده براتون آماده شد بخش آخر اضافه میکنم


سلام عرض شد خیلی عالی موردی نداره باز من هر بخشی نیاز بود رو براتون تغییر میدم همچنین سعی کن یک فایل به نام دیوایس فقط دیوایس و 
camera
توش باشه و یک فایل به نام کنترل پنل بساز که دیوایس و کنترل پنل داخلش باشه چون دوتا قسمت حساب میشه پروژه 
اگه سختت بود بگو من خودم اینجا برات تغییرات رو بدم دوتا فایلش کنم برای راحتی
موفق باشی



استاد جسارته میدونم ولی بنده بلد نیستم دوتا فایلش کنم اگر زحمت ننمیشه خودتون انجام من هنوز روی بخش آخر قسمت سوم پروژ] گیر کردم ممنون میشم خودتون این دوفایلی کردن رو انجام بدید و من به اون برسم بازم ببخشید که زحمت میدم


استاد سلام بخش آخر سوال سوم رو ارسال کردم و به آخر این پروژه اضافه کردم ولی یه مشکلی که داره اینه که درست اجرا نمیشه میشه لطفا چک کنید هرچه کردم درست نشد یعنی به نظر کد درسته البته فکر کنم ولی درست اجرا نمیشه


'''








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

    # روشن کردن همه دستگاه‌های یک گروه
   
    def turn_on_in_group(self, group_name):
        if group_name in self.groups:
            print(f" روشن کردن همه دستگاه‌های گروه '{group_name}' ...")
            for device in self.groups[group_name]:
                device.turn_on()
            print(f" همه دستگاه‌های '{group_name}' روشن شدند.")
        else:
            print(f" گروه '{group_name}' یافت نشد!")

  
    # خاموش کردن همه دستگاه‌های یک گروه
   
    def turn_off_in_group(self, group_name):
        if group_name in self.groups:
            print(f" خاموش کردن همه دستگاه‌های گروه '{group_name}' ...")
            for device in self.groups[group_name]:
                device.turn_off()
            print(f" همه دستگاه‌های '{group_name}' خاموش شدند.")
        else:
            print(f" گروه '{group_name}' یافت نشد!")

    # روشن کردن تمام دستگاه‌ها در همه گروه‌ها
 
    def turn_on_all(self):
        print(" روشن کردن تمام دستگاه‌های خانه ...")
        for group_name, devices in self.groups.items():
            for device in devices:
                device.turn_on()
        print(" همه دستگاه‌های خانه روشن شدند!")
    # خاموش کردن تمام دستگاه‌ها در همه گروه‌ها

    def turn_off_all(self):
        print(" خاموش کردن تمام دستگاه‌های خانه ...")
        for group_name, devices in self.groups.items():
            for device in devices:
                device.turn_off()
        print(" همه دستگاه‌های خانه خاموش شدند!")


 
    def get_status_in_group(self, group_name):
        if group_name in self.groups:
            print(f" وضعیت دستگاه‌های گروه '{group_name}':")
            for device in self.groups[group_name]:
                status = "روشن " if device.get_status() else "خاموش "
                print(f"  • {device.device_name} --> {status}")
        else:
            print(f" گروه '{group_name}' وجود ندارد!")
   
    def get_status_in_device_type(self, device_type):
        print(f" بررسی وضعیت تمام دستگاه‌های نوع '{device_type}':")
        found = False
        for group_name, devices in self.groups.items():
            for device in devices:
                if device.device_type == device_type:
                    found = True
                    status = "روشن " if device.get_status() else "خاموش "
                    print(f"  • {device.device_name} ({group_name}) --> {status}")
        if not found:
            print(f" هیچ دستگاهی از نوع '{device_type}' یافت نشد.")

# ---- Device Class ----
class Device:
    def init(self, location, group, device_type, device_name):
        self.location = location
        self.group = group
        self.device_type = device_type
        self.device_name = device_name
        self.status = 'off'

    def turn_on(self):
        self.status = 'on'
        print(f" {self.device_name} در گروه '{self.group}' روشن شد ")

    def turn_off(self):
        self.status = 'off'
        print(f" {self.device_name} در گروه '{self.group}' خاموش شد ")

    def get_status(self):
        return self.status == 'on'


# ---- Sensor Class ----
import random

class Sensor:
    def init(self, location, group, sensor_type, sensor_name):
        self.location = location
        self.group = group
        self.sensor_type = sensor_type
        self.sensor_name = sensor_name

    def read_data(self):


# ---- Control Panel ----
class ControlPanel:
    def init(self):
        self.groups = {}
        print(" سیستم کنترل هوشمند خانه راه‌اندازی شد ")

 
    def create_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f" گروه '{group_name}' با موفقیت ایجاد شد ")
        else:
            print(f" گروه '{group_name}' از قبل وجود دارد!")

  
    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            print(f" دستگاه '{device.device_name}' به گروه '{group_name}' افزوده شد ")
        else:
            print(f" گروه '{group_name}' پیدا نشد!")

  
    def create_device(self, group_name, device_type, device_name):
        if group_name in self.groups:
            location = 'home'
            new_device = Device(location, group_name, device_type, device_name)
            self.groups[group_name].append(new_device)
            print(f" دستگاه '{device_name}' از نوع '{device_type}' ساخته شد ")
        else:
            print(f" گروه '{group_name}' یافت نشد، ابتدا آن را ایجاد کنید!")

  
    def create_multiple_device(self, group_name, device_type, device_number):
        if group_name in self.groups:
            for i in range(1, device_number + 1):
                device_name = f"{device_type}_{i}"
                self.create_device(group_name, device_type, device_name)
            print(f" {device_number} دستگاه از نوع '{device_type}' به گروه '{group_name}' اضافه شد.")
        else:
            print(f" گروه '{group_name}' وجود ندارد!")

  
    def get_devices(self, group_name):
        if group_name in self.groups:
            return self.groups[group_name]
        else:
            print(f" گروه '{group_name}' وجود ندارد!")
            return [] ;

      
          def create_sensor(self, group_name, sensor_type, sensor_name):
        '''
        yeki sensor besaze va ezafe kone be group
        '''
        if group_name in self.groups:
            location = 'home'
            new_sensor = Sensor(location, group_name, sensor_type, sensor_name)
            self.groups[group_name].append(new_sensor)
            print(f" Sensor '{sensor_name}' created in '{group_name}' ")
        else:
            print(f" Group '{group_name}' not found!")


    def create_multiple_sensor(self, group_name, sensor_type, sensor_number):
        '''
        chand ta sensor besaz
        '''
        if group_name in self.groups:
            print(f" Creating {sensor_number} sensors in '{group_name}' ...")
            for i in range(1, sensor_number + 1):
                sensor_name = f"{sensor_type}_{i}"
                self.create_sensor(group_name, sensor_type, sensor_name)
            print(f" {sensor_number} sensors created successfully in '{group_name}'.")
        else:
            print(f" Group '{group_name}' not found!")

      def turn_off_in_group(self, group_name):
        '''
        biad dakhele oon group_name doone doone ro
        khamoosh kone 
        '''
        if group_name in self.groups:
            devices = self.groups[group_name]
            if not devices:
                print(f" Group '{group_name}' is empty, no devices to turn off.")
                return

            print(f" Turning OFF all devices in group '{group_name}' ...")
            for device in devices:
                if hasattr(device, 'turn_off'):
                    device.turn_off()
                    print(f" → device '{device.device_name}' khamoosh shod ")
            print(f" All devices in '{group_name}' are now OFF.")
        else:
            print(f" Group '{group_name}' does not exist!")


    def turn_on_all(self):
        '''
        tamame device haro roshan kone
        too living_room, kitchen, parking ya harjaa hastan
        hamaro roshan kone
        '''
        if not self.groups:
            print(" No groups found! please create a group first.")
            return

        print(" Turning ON all devices in ALL groups ...")
        for group_name, devices in self.groups.items():
            if not devices:
                print(f" (Group '{group_name}' is empty.)")
                continue
            print(f" Group '{group_name}':")
            for device in devices:
                if hasattr(device, 'turn_on'):
                    device.turn_on()
                    print(f" device '{device.device_name}' roshan shod ")
        print(" All devices in all groups are now ON!")


    def turn_off_all(self):
        '''
        hamaro khamoosh kone
        '''
        if not self.groups:
            print(" No groups found to turn off.")
            return

        print(" Turning OFF ALL devices in ALL groups ...")
        for group_name, devices in self.groups.items():
            if not devices:
                print(f"   (Group '{group_name}' is empty.)")
                continue
            print(f" Group '{group_name}':")
            for device in devices:
                if hasattr(device, 'turn_off'):
                    device.turn_off()
                    print(f" device '{device.device_name}' khamoosh shod ")
        print(" All devices are OFF now.")


    def get_status_in_group(self, group_name):
        '''
        be ezaye device haye tooye masalan felan group
        living_room --> bebine roshanan ya khamoshan
        print kone
        '''
        if group_name not in self.groups:
            print(f" Group '{group_name}' does not exist.")
            return

        devices = self.groups[group_name]
        if not devices:
            print(f" No devices in '{group_name}' yet.")
            return

        print(f" Device status in group '{group_name}':")
        for device in devices:
            if hasattr(device, 'get_status'):
                status = "ON " if device.get_status() else "OFF "
                print(f" {device.device_name} is {status}")
        print(" Status report finished.")


    def get_status_in_device_type(self, device_type):
        '''
        varaye kole device haee k hastan
        bere device_type shono check kone
        fght lamparo ya doora check kone
        '''
        found = False
        print(f" Searching for all devices with type '{device_type}' ...")

        for group_name, devices in self.groups.items():
            for device in devices:
                if hasattr(device, 'device_type') and device.device_type == device_type:
                    found = True
                    status = "ON " if device.get_status() else "OFF "
                    print(f"  {device.device_name} (in '{group_name}') is {status}")

        if not found:
            print(f" No devices of type '{device_type}' found in any group.")
        else:
            print(" Status check completed.")

def create_sensor(self, group_name, sensor_type, sensor_name):
        '''
        yeki sensor besaze va ezafe kone be group
        '''
        if group_name in self.groups:
            location = 'home'
            new_sensor = Sensor(location, group_name, sensor_type, sensor_name)
            self.groups[group_name].append(new_sensor)
            print(f" Sensor '{sensor_name}' created in '{group_name}' ")
        else:
            print(f"Group '{group_name}' not found!")

# بخش آخر و افزوده شده 

def create_multiple_sensor(self, group_name, sensor_type, sensor_number):
        '''
     chand ta sensor besaz
        '''
        if group_name in self.groups:
          print(f" Creating {sensor_number} sensors in '{group_name}' ...")
         
            for i in range(1, sensor_number + 1):
                sensor_name = f"{sensor_type}_{i}"
                self.create_sensor(group_name, sensor_type, sensor_name)
            print(f" {sensor_number} sensors created successfully in '{group_name}'.")
         
        else:
            print(f" Group '{group_name}' not found!")


