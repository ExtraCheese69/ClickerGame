import customtkinter
import threading
import time as t
from PIL import Image

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("ClickerGame")
        self.geometry("500x350")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.clicks = 0
        self.cps = 0

        self.pricemodifierSC=customtkinter.IntVar()
        self.pricemodifierSC.set(1)
        self.pricemodifierAC=customtkinter.IntVar()
        self.pricemodifierAC.set(1)
        self.pricemodifierFAC=customtkinter.IntVar()
        self.pricemodifierFAC.set(1)

        self.clickstrength = 1
        self.automatedclicker = None
        self.clickrate=1

        img_path = r"C:/Users/Mario/OneDrive - HTL Anichstrasse/Desktop/Fsst collectione/FSST/4.Klasse/TK.png"
        self.tk_image = customtkinter.CTkImage(light_image=Image.open(img_path), size=(100, 100))

        self.button = customtkinter.CTkButton(self, image=self.tk_image,text="", width=100, height=100, fg_color="transparent", hover_color="lightgray", command=self.button_click)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="", columnspan=8)

        self.clickcount = customtkinter.CTkLabel(self, text="Clicks:0", fg_color="transparent")
        self.clickcount.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=8)

        self.cpscount = customtkinter.CTkLabel(self, text=f"CPS:{self.cps}", fg_color="transparent")
        self.cpscount.grid(row=2, column=0, padx=20, pady=40, sticky="ew", columnspan=8)

        self.optionmenu_var = customtkinter.StringVar(value="Upgrades")
        self.optionmenu = customtkinter.CTkOptionMenu(self,
                                                        values=[f"Automated Clicking | {100 * self.pricemodifierAC.get()}",
                                                                f"Stronger Clicks | {100 * self.pricemodifierSC.get()}"],
                                                        command=self.optionmenu_callback,
                                                        variable=self.optionmenu_var)
        self.optionmenu.grid(row=1, column=2, padx=20, pady=40, sticky="ew", columnspan=8)

    def upgradeupdate(self):
        self.upgrades = [f"Automated Clicking | {100 * self.pricemodifierAC.get()}",
                         f"Stronger Clicks | {100 * self.pricemodifierSC.get()}",
                         f"FasterAutomatedClicking | {50 * self.pricemodifierFAC.get()}"]
        self.optionmenu.configure(self, values=self.upgrades)

    def button_click(self):
        self.clicks += self.clickstrength
        self.clickcount.configure(text=(f"Clicks:{self.clicks}"))

    def optionmenu_callback(self, choice):
        if choice == f"Automated Clicking | {100 * self.pricemodifierAC.get()}":
            if self.clicks >= 100*self.pricemodifierAC.get():
                self.clicks -= 100*self.pricemodifierAC.get()
                self.clickcount.configure(text=(f"Clicks:{self.clicks}"))
                self.pricemodifierAC.set(self.pricemodifierAC.get()+1)
                self.cps += 1
                self.cpscount.configure(self, text=f"CPS:{self.cps}")
                self.upgradeupdate()
                
                try:
                    if self.automatedclicker.is_alive() == True:
                        pass
                    pass
                except:
                    self.automatedclicker = threading.Thread(target=self.AutomatedClicking, daemon=True)
                    self.automatedclicker.start()
            else:
                print("Insufficient Funds!")

        elif choice == f"Stronger Clicks | {100 * self.pricemodifierSC.get()}":
            if self.clicks >= 100 * self.pricemodifierSC.get():
                self.clicks -= 100 * self.pricemodifierSC.get()
                self.clickcount.configure(text=(f"Clicks:{self.clicks}"))
                self.pricemodifierSC.set(self.pricemodifierSC.get()+1)
                self.clickstrength +=1

                self.upgradeupdate()
            else:
                print("Insufficient Funds!")
        
        elif choice == f"FasterAutomatedClicking | {50 * self.pricemodifierFAC.get()}":
            if self.clicks >= 50 * self.pricemodifierFAC.get():
                self.clicks -= 50 * self.pricemodifierFAC.get()
                self.clickcount.configure(text=(f"Clicks:{self.clicks}"))
                self.pricemodifierFAC.set(self.pricemodifierFAC.get()+1)
                self.clickrate=self.clickrate*0.8

                self.upgradeupdate()
            else:
                print("Insufficient Funds!")

    def AutomatedClicking(self):
        while True:
            self.clicks += self.cps
            t.sleep(self.clickrate)
            print(self.cps)
            self.clickcount.configure(text=(f"Clicks:{self.clicks}"))


app = App()    
app.mainloop()