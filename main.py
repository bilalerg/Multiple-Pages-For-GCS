import sys
import math
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QCoreApplication, QTimer
from PySide2.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, \
    QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
from PySide2.QtWidgets import QMainWindow, QApplication
from dronekit import connect, VehicleMode

# GUI FILE
from ui_untitled import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

vehicle = None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.incele.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.Kamera.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Kamera_sayfa))

        # PAGE 2
        self.ui.Harita.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Harita_sayfa))

        # PAGE 3
        self.ui.Gyroscope.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Gyroscope_sayfa))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

        # Connect to vehicle
        self.connect_vehicle()

    def connect_vehicle(self):
        try:
            self.vehicle = connect('127.0.0.1:14550', wait_ready=True)
            print("Bağlanıyor...")
            print("Bağlandı")

            self.timer = QTimer()

            self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

        except Exception as e:
            print(f"Bağlantı hatası: {e}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
