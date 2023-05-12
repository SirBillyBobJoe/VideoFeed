import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import threading
import time

class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.vid = cv2.VideoCapture(video_source)
        self.showing_image = False  # Initialize showing_image here

        self.canvas = tk.Canvas(window, width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        self.btn_snapshot=tk.Button(window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

        self.btn_load_img=tk.Button(window, text="Load Image", width=50, command=self.load_img)
        self.btn_load_img.pack(anchor=tk.CENTER, expand=True)

        self.btn_return_vid=tk.Button(window, text="Return to Video", width=50, command=self.return_vid)
        self.btn_return_vid.pack(anchor=tk.CENTER, expand=True)

        self.delay = 15
        self.update()  # Now it's safe to call update
        self.window.mainloop()

    def snapshot(self):
        ret, frame = self.vid.read()
        if ret:
            cv2.imwrite("C:/Users/tongh/Downloads/App Snap/frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            self.showing_image = False

    def load_img(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.showing_image = True
            img = Image.open(file_path)
            self.img_tk = ImageTk.PhotoImage(img)
            self.canvas.create_image(0,0, image=self.img_tk, anchor='nw')

    def return_vid(self):
        self.showing_image = False

    def update(self):
        if not self.showing_image:
            ret, frame = self.vid.read()
            if ret:
                self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
                self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
        self.window.after(self.delay, self.update)

App(tk.Tk(), "Tkinter and OpenCV")
