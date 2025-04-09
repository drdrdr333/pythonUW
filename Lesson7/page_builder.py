import text,image
import tkinter as tk
from PIL import ImageTk, Image


def add_text_for_widget(input_text, output_text, initial_text):
    input = input_text.get("1.0", "end-1c")
    output_text.delete("1.0", "end")
    output_text.insert("end", initial_text.add_text(input))




class Page(text.Text, image.Image):
    def display():

        """
        Very brittle... displays a tkinter window with an image where the path is specified.
        """
        
        the_image = image.Image()
        root = tk.Tk()
        root.title("Simple app")
        root.configure(width=500, height=500)
        txt = tk.Text(root, height=8)
        txt.pack()
        my_text = text.Text("Hello!!!")
        txt.insert(1.0, my_text.get_text_as_string())
        img = ImageTk.PhotoImage(Image.open(the_image.path))
        panel = tk.Label(root, image=img)
        panel.pack(fill="both")
        root.mainloop()

    
    def get_input_text():
        """
        Also very brittle... allows you to input text to screen and add to already existing text
        """
        
        root = tk.Tk()
        root.title("Simple app")
        root.configure(width=500, height=500)
        initial = text.Text("hello")
        label = tk.Label(text=initial.get_text_as_string())
        inputtext = tk.Text(root, height=10, width=15)
        output = tk.Text(root, height=10, width=15)
        output.insert("end", initial.get_text_as_string())

        btn = tk.Button(root, height=3, width=10, text="Add Text", command= lambda:add_text_for_widget(inputtext, output, initial))

        label.pack()
        inputtext.pack()
        output.pack()
        btn.pack()
        
        root.mainloop()