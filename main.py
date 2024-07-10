import customtkinter as ctk
import CTkMenuBar as ctkmb

app = ctk.CTk()
app.geometry("700x500") # widthxheight
ctk.set_appearance_mode("light") # light - dark - system
ctk.set_default_color_theme("green") # blue - green - dark-blue
app.title("app")
# app.iconbitmap("icon.ico")


menubar = ctkmb.CTkMenuBar(app)
menubar.add_cascade(text="file")
menubar.configure()






container = ctk.CTkFrame(app)
inputContainer = ctk.CTkFrame(container, width = 700)
TextEntry = ctk.CTkEntry(inputContainer, placeholder_text="Enter your task here.", width = 400, height = 35)
addButton = ctk.CTkButton(inputContainer, text = "Add", width = 80, height = 35)
textLabel = ctk.CTkLabel(container, text =" This is a text label.", height = 35)

container.pack(padx = 10, pady = 10, fill = "both", expand = True)
inputContainer.pack(anchor = "n", ipadx = 10, ipady = 10, expand = True)
TextEntry.pack(side = "left", anchor = "w", expand = True)
addButton.pack(side = "left", expand = True)
textLabel.pack()

app.mainloop() # run the program in loop

