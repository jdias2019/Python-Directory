import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

gui = customtkinter.CTk()
gui.title("Counter App")
gui.geometry("1000x600")



count = 0
counter_label = customtkinter.CTkLabel(gui, text=str(count), font=customtkinter.CTkFont(size=90))
counter_label.pack(pady=80)

def plus():
    global count
    count = count + 1
    counter_label.configure(text=str(count))

def minus():
    global count
    count = count - 1
    counter_label.configure(text=str(count))

def reset():
    global count
    count = 0
    counter_label.configure(text=str(count))


frame_butons = customtkinter.CTkFrame(gui, fg_color="transparent")
frame_butons.pack(pady=50)

plus_button  = customtkinter.CTkButton(frame_butons, text="+",     command=plus,  width=150, height=50, font=customtkinter.CTkFont(size=24))
minus_button = customtkinter.CTkButton(frame_butons, text="-",     command=minus, width=150, height=50, font=customtkinter.CTkFont(size=24))
reset_button = customtkinter.CTkButton(frame_butons, text="Reset", command=reset, width=150, height=50)

plus_button.pack(side="left",  padx=40)
minus_button.pack(side="left", padx=40)
reset_button.pack(side="left", padx=40)


gui.mainloop()
