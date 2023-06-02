from tkinter import *
from program2 import *
from subprocess import call

class Generate_otp(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x580+200+80")
        self.configure(bg = "#FFFFFF")
        self.resizable(False, False)

        self.f = ("Times bold", 14)

    
        
       # def nextPage(self):
         #import program2
         #program1 = self.destroy()
            
    def Labels(self):
        
        self.upper_frame = Frame(self , bg = "#3d3d5c" , width = 1500 , height = 130 )
        self.upper_frame.place ( x = 0 , y = 0 )
        self.lower_frame = Frame(self , bg = "#3d3d5c" , width = 1500 , height = 200 )
        self.lower_frame.place ( x = 0 , y = 270 )
        self.picture = PhotoImage (file = "c1.png")
        
        self.k = Label ( self.upper_frame , image = self.picture , bg = "#3d3d5c").place(x=220,y=35)
        

        self.j = Label(self.upper_frame, text="Biometric Fingerprint ", font = "TimesNewRoman 38 bold",bg= "#3d3d5c", fg="white").place(x= 230, y= 35)
        #Create an instance of tkinter frame

    
    def Buttons(self):
        self.GenerateOTP=PhotoImage(file = "finger.png")
        self.generatebutton = Button(self , image=self.GenerateOTP, command = self.Open, border = 0 )
        self.generatebutton.place(x = 370 ,y = 250)
        
    
    def Open(self):
        program1 = self.destroy()
        call(["python", "atm.py"])  
        #self.a = Label(self,
         #           text="This is First page",
          #          padx=20,
           #         pady=20,
            #        bg='#5d8a82',
             #       font=self.f
              #  ).pack(expand=True, fill=BOTH)
 

if __name__ == "__main__":
    window = Generate_otp()
    
    window.Labels()
    window.Buttons()
    window.mainloop()
    
