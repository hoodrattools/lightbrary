import machine
import neopixel
import time

class Light:
    def __init__(self, n, p): 
        self.n = n
        self.p = p
        self.np = neopixel.NeoPixel(machine.Pin(self.p), self.n)

    def c1(self):
        for x in range (0,180,4):
            self.np[x] = (150, 75, 150)
            #self.np.write()
        for a in range (1,180,4):
            self.np[a] = (150,0,50)
            #self.np.write()
        for b in range (2,180,4):
            self.np[b] = (250,0,250)
            #self.np.write()
        for c in range (3,180,4):
            self.np[c] = (75,0,5)
            #self.np.write()
        #self.np.write()
            
    def c2(self):
        for x in range (0,180,4):
            self.np[x] = (100, 175, 20)
            #self.np.write()
        for a in range (1,180,4):
            self.np[a] = (150,30,150)
            #self.np.write()
        for b in range (2,180,4):
            self.np[b] = (150,50,200)
            #self.np.write()
        for c in range (3,180,4):
            self.np[c] = (75,100,5)
            #self.np.write()
        #self.np.write()
            
    def c3(self):
        for x in range (0,180,4):
            self.np[x] = (100, 175, 20)
            #self.np.write()
        for a in range (1,180,4):
            self.np[a] = (150,30,150)
            #self.np.write()
        for b in range (2,180,4):
            self.np[b] = (150,50,200)
            #self.np.write()
        for c in range (3,180,4):
            self.np[c] = (75,100,5)
            #self.np.write()
        #self.np.write()

    def c4(self):
        for x in range (0,180,4):
            self.np[x] = (50, 15, 220)
            #self.np.write()
        for a in range (1,180,4):
            self.np[a] = (50,230,180)
            #self.np.write()
        for b in range (2,180,4):
            self.np[b] = (50,250,10)
            #self.np.write()
        for c in range (3,180,4):
            self.np[c] = (15,100,225)
            #self.np.write()
        #self.np.write()
        
    def blink(self, x, timer):
        while True:
            x()
            self.np.write()
            time.sleep_ms(timer)
            for i in range (0,180):
                self.np[i]=(0,0,0)
            self.np.write()    
            time.sleep_ms(timer)
            
    def prog_chase(self, z):
        while True:
            for i in range (0,180):
                minus=(i-1)
                for x in range (0,minus):
                    z()
                    x=int(x)
                    self.np[x]=(0,0,0)
                    self.np.write()

                  
    def chase(self, z):
        while True:
            for i in range (0,180):
                z()
                plus=(i+1)
                minus=(i-1)
                for x in range(180):
                    if x != i:
                        self.np[x]=(0,0,0)
                self.np.write()
                
                
    def two_chase(self, z):
        while True:
            for i in range (0,180):
                z()
                for x in range(180):
                    interval = (i-10)
                    if x != i and x != interval:
                        self.np[x]=(0,0,0)
                self.np.write()
                
    def three_chase(self, z):
        while True:
            for i in range (0,180):
                z()
                for x in range(180):
                    interval = (i-45)
                    intervall = (i-90)
                    if x != i and x != interval and x != intervall:
                        self.np[x]=(0,0,0)
                self.np.write()
                
                
    def neg_chase(self, z):
        while True:
            for i in range (0,180):
                for x in range(180):
                    z()
                    if x != i:
                        self.np[x]=(0,0,0)
                    self.np.write()
                
    def pulse(self, x,y,z):
        while True:
            self.x = x
            self.y = y
            self.z = z
            xx=0
            yy=0
            zz=0
            while xx < x or yy < y or zz < z:
                xx = (xx+1)
                yy = (yy+1)
                zz = (zz+1)
                for i in range (180):
                    self.np[i]=(xx,yy,zz)
                self.np.write()
            while xx >= x or yy >=y or zz>=z or xx !=5 or yy!= 5 or zz!= 5:
                xx = (xx-1)
                yy = (yy-1)
                zz = (zz-1)
                for i in range (180):
                    self.np[i]=(xx,yy,zz)
                self.np.write()
                
    def s_pulse(self, x,y,z):
        #while True:
        self.x = x
        self.y = y
        self.z = z
        xx=0
        yy=0
        zz=0
        while xx < x or yy < y or zz < z:
            if xx < x:
                xx = (xx+1)
            if yy < y:    
                yy = (yy+1)
            if zz < z:    
                zz = (zz+1)
            for i in range (180):
                self.np[i]=(xx,yy,zz)
            #print('3')    
            self.np.write()
        while xx == x and yy ==y and zz==z:
            while xx !=0 or yy!= 0 or zz != 0:
                if xx > 0:
                    xx = (xx-1)
                if yy > 0:
                    yy = (yy-1)
                if zz > 0:
                    zz = (zz-1)
                for i in range (180):
                    self.np[i]=(xx,yy,zz)
                #print('1')
                self.np.write()
                
    
    def s_blink(self, x, timer):
        x()
        self.np.write()
        time.sleep_ms(timer)
        for i in range (0,180):
            self.np[i]=(0,0,0)
        self.np.write()    
        time.sleep_ms(timer)
            
    def s_prog_chase(self, z):
        for i in range (0,180):
            minus=(i-1)
            for x in range (0,minus):
                z()
                x=int(x)
                self.np[x]=(0,0,0)
                self.np.write()

                  
    def s_chase(self, z):
        for i in range (0,180):
            z()
            plus=(i+1)
            minus=(i-1)
            for x in range(180):
                if x != i:
                    self.np[x]=(0,0,0)
            self.np.write()
                
                
    def s_two_chase(self, z):
        for i in range (0,180):
            z()
            for x in range(180):
                interval = (i-10)
                if x != i and x != interval:
                    self.np[x]=(0,0,0)
            self.np.write()
                
    def s_three_chase(self, z):
        for i in range (0,180):
            z()
            for x in range(180):
                interval = (i-45)
                intervall = (i-90)
                if x != i and x != interval and x != intervall:
                    self.np[x]=(0,0,0)
            self.np.write()
                
                
    def s_neg_chase(self, z):
        for i in range (0,180):
            #for x in range(180):
            z()
                #if x != i:
            self.np[i]=(0,0,0)
            self.np.write()
                
l = Light(180,12)
l.s_neg_chase(l.c1)
