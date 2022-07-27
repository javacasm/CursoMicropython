import machine

v=0.5

STOP = 0
A = 10
MIN = MIN_SPEED = 3
MAX = MAX_SPEED = A
MED = MED_SPEED = (MIN_SPEED + MAX_SPEED)//2
LOW = LOW_SPEED = (MIN_SPEED + MED_SPEED)//2


class motor():
    def __init__(self):
        pass

    def forward(self):
        pass

    def back(self):
        pass

    def stop(self):
        pass

class motorL298(motor):
    def __init__(self,pin_in1,pin_in2,pin_en):
        self.in1 = machine.Pin(pin_in1,machine.Pin.OUT)
        self.in2 = machine.Pin(pin_in2,machine.Pin.OUT)
        self.en = machine.PWM(machine.Pin(pin_en),machine.Pin.OUT)
        self.en.freq(1000)    
        self.stop()
        
    def forward(self,speed = MED_SPEED):
        self.in1.on()
        self.in2.off()
        self.en.duty(speed)
      
    def back(self,speed = MED_SPEED):
        self.in1.off()
        self.in2.on()
        self.en.duty(speed)  
      
    def go(self,speed):
        if speed>0:
            self.forward(speed)
        elif speed <0:
            self.back(-speed)
        else:
            self.stop()
            
    def stop(self):
        self.en.duty(STOP)