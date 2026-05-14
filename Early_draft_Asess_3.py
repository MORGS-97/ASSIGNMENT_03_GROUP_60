import tkinter as tk
import cv2
from tkinter import filedialog
import numpy as np
from PIL import Image, ImageTk

#Creates Window
root = tk.Tk()
root.title("Spot The Difference") 
root.geometry("900x900") 
root.resizable(False, False) 

#Upload Function
def im_upload():
    picture = filedialog.askopenfilename( 
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
        )
    if picture:
        img = cv2.imread(picture) #reads
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #converts colour
        img = cv2.resize(img, (600, 300)) #resizes
        original_img = img.copy()
        altered_img = img.copy()
        original_img_pl = Image.fromarray(original_img) #Converts from numpy to PIL
        original_img_tk = ImageTk.PhotoImage(original_img_pl) #Converts from PIL to tkinter
        altered_img_pl = Image.fromarray(altered_img) #Converts from numpy to PIL
        altered_img_tk = ImageTk.PhotoImage(altered_img_pl) #Converts from PIL to tkinter
        im_original_label.config(image = original_img_tk) #Label displays image
        im_original_label.image = (original_img_tk) #Stores image in variable
        im_altered_label.config(image = altered_img_tk) #Label displays image
        im_altered_label.image = (altered_img_tk) #Stores image in variable



#Labels for Image Storage
im_original_label = tk.Label(root)
im_original_label.pack()
im_altered_label = tk.Label(root)
im_altered_label.pack()

#Button for Importing Impage
import_but = tk.Button(root, 
                       text='Import Image', 
                       command = im_upload
                       )
import_but.pack()



#Creation of Image Processor class
class Image_processor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.original_img = None
        self.altered_img = None

    def load_image(self):
        self.original_img = cv2.imread(self.image_path)
        self.original_img = cv2.cvtColor(self.original_img, cv2.COLOR_BGR2RGB)
        self.original_img = cv2.resize(self.original_img, (300, 600))
        self.altered_img = self.original_img.copy()

    def alter_image(self):
        cv2.circle(self.altered_img, (150, 300), 40, (255, 0, 0), -1)

    def get_images(self):
        return self.original_img, self.altered_img


root.mainloop()