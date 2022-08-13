from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry("900x600")
root.title("Classes")
root.configure(bg = "turquoise")

class CreateElements:
    
    def __init__(self):
        print("This Is CreateElements Class")
        
    def createNewElement(self):
        label = Label(root, text = "A New Label Is Been Created Using Class", fg = "red", bg = "yellow")
        label.pack()
        btn = Button(root, text = "Button", command = self.message, bg = "medium purple1")
        btn.pack(padx = 20, pady = 10)
        
    def message(self):
        messagebox.showinfo("showinfo", "You Clicked The The Button Created Using Class")
        
obj_of_CreateElements = CreateElements()

btn = Button(root, text = "Click To Create Label And Element Button", command = obj_of_CreateElements.createNewElement, bg = "light pink")
btn.pack(padx = 20, pady = 10)

root.mainloop()
        