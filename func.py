import os
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from collections import deque
from time import sleep
import threading

class PhotoViewer(QObject):
    def __init__(self, currfile=""):
        super().__init__()
        self.curr_file = currfile
        self.curr_index = 0
        self.folder = ""
        self.supported_formats = ['.jpeg' , '.jpg' , '.png' , '.gif']
        self.image_list = deque([])
        self.find_others_images()

    changeImage = pyqtSignal(str, arguments=['change_image'])
    
    def find_others_images(self)->None:
        find_thread = threading.Thread(target=self._find_others_images)
        find_thread.daemon = True
        find_thread.start()

    def _find_others_images(self):
        self.folder = os.path.dirname(self.curr_file)
        mainfile = os.path.split(self.curr_file)[-1]

        conts = os.listdir(self.folder)

        self.image_list = deque([
            x for x in conts
                if os.path.splitext(x)[-1] in self.supported_formats])
        
        ###sleep(2)

        ind = -1
        for img in self.image_list:
            ind +=1
            if mainfile == img:
                self.curr_index = ind

    @pyqtSlot(str)
    def get_next_image(self, direccion):
        f_thread = threading.Thread(target=self._get_next_image, args=[direccion])
        f_thread = True
        f_thread.start()

    def _get_next_image(self, direccion):
        if direccion == 'letf':
            self.curr_index -= 1
        else:
            self.curr_index += 1
        curr_img = self.image_list[self.curr_index]
        curr_img_path = f'file:///{os.path.join(self.folder, curr_img)}'
        self.changeImage.emit(curr_img_path)