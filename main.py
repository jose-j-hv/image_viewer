import sys
import os
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from func import PhotoViewer

if len(sys.argv) > 1:
    real_path = os.path.realpath(sys.argv[1])
    user_file = 'file:///' + real_path

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.load('./UI/main.qml')
engine.quit.connect(app.quit)

photo_viewer = PhotoViewer(user_file)
engine.rootObjects()[0].setProperty('viewer',photo_viewer)
engine.rootObjects()[0].setProperty('actual_image',user_file)

sys.exit(app.exec())