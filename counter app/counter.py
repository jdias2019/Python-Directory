import customtkinter 


customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("green")  

gui = customtkinter.CTk()  
gui.title("Counter App")  
gui.geometry("1000x600")



count = 0
counter_label = customtkinter.CTkLabel(gui, text=str(count), font=customtkinter.CTkFont(size=90))
counter_label.pack(pady=50)

def plus():
    global count
    count = count + 1
    counter_label.configure(text=str(count))

plus_button = customtkinter.CTkButton(gui, text="+", command=plus)
plus_button.pack(pady=50)

def minus():
    global count
    count = count - 1
    counter_label.configure(text=str(count))

minus_button = customtkinter.CTkButton(gui, text="-", command=minus)
minus_button.pack(pady=50)

def reset():
    global count
    count = 0
    counter_label.configure(text=str(count))

reset_button = customtkinter.CTkButton(gui, text="Reset", command=reset)
reset_button.pack(pady=50)

gui.mainloop()