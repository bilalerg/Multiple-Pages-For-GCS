from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1291, 708)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45,45,45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        # Üst kısım
        self.Top_bar = QFrame(self.centralwidget)
        self.Top_bar.setObjectName(u"Top_bar")
        self.Top_bar.setMaximumSize(QSize(16777215, 40))
        self.Top_bar.setStyleSheet(u"background-color: rgb(35,35,35);")
        self.Top_bar.setFrameShape(QFrame.NoFrame)
        self.Top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.frame_toggle = QFrame(self.Top_bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(80, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(153, 193, 241);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.incele = QPushButton(self.frame_toggle)
        self.incele.setObjectName(u"incele")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.incele.sizePolicy().hasHeightForWidth())
        self.incele.setSizePolicy(sizePolicy)
        self.incele.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.incele.setFont(font)
        self.incele.setStyleSheet(u"color: rgb(255,255,255);\n" "border: 0px solid;")
        self.verticalLayout_4.addWidget(self.incele)
        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_bar)

        # Orta kısım
        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        # Sol Menü
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(0, 0))
        self.frame_left_menu.setMaximumSize(QSize(85, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35,35,35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.Kamera = QPushButton(self.frame_top_menus)
        self.Kamera.setObjectName(u"Kamera")
        self.Kamera.setMinimumSize(QSize(0, 50))
        self.Kamera.setMaximumSize(QSize(16777215, 50))
        self.Kamera.setFont(font)
        self.Kamera.setStyleSheet(u"QPushButton {\n"
                                  "color: rgb(255,255,255);\n"
                                  "background-color: rgb(35,35,35);\n"
                                  "border : 0px solid;\n"
                                  "}\n"
                                  "QPushButton:hover {\n"
                                  "background-color: rgb(85,170,255);\n"
                                  "}")
        self.verticalLayout_3.addWidget(self.Kamera)

        self.Harita = QPushButton(self.frame_top_menus)
        self.Harita.setObjectName(u"Harita")
        self.Harita.setMinimumSize(QSize(0, 50))
        self.Harita.setFont(font)
        self.Harita.setStyleSheet(u"QPushButton {\n"
                                  "color: rgb(255,255,255);\n"
                                  "background-color: rgb(35,35,35);\n"
                                  "border : 0px solid;\n"
                                  "}\n"
                                  "QPushButton:hover {\n"
                                  "background-color: rgb(85,170,255);\n"
                                  "}")
        self.verticalLayout_3.addWidget(self.Harita)

        self.Gyroscope = QPushButton(self.frame_top_menus)
        self.Gyroscope.setObjectName(u"Gyroscope")
        self.Gyroscope.setMinimumSize(QSize(0, 50))
        self.Gyroscope.setFont(font)
        self.Gyroscope.setStyleSheet(u"QPushButton {\n"
                                     "color: rgb(255,255,255);\n"
                                     "background-color: rgb(35,35,35);\n"
                                     "border : 0px solid;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "background-color: rgb(85,170,255);\n"
                                     "}")
        self.verticalLayout_3.addWidget(self.Gyroscope)
        self.verticalLayout_2.addWidget(self.frame_top_menus, 0, Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        # Sayfa içerikleri
        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 1191, 651))

        # Sayfa ve Butonlar
        self.Kamera_sayfa = QWidget()
        self.Kamera_sayfa.setObjectName(u"Kamera_sayfa")
        self.kamera_label = QLabel(self.Kamera_sayfa)
        self.kamera_label.setObjectName(u"kamera_label")
        self.kamera_label.setGeometry(QRect(0, 0, 1100, 30))
        font1 = QFont()
        font1.setPointSize(20)
        self.kamera_label.setFont(font1)
        self.kamera_label.setStyleSheet(u"color: #FFF;")
        self.kamera_label.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.Kamera_sayfa)

        self.Harita_sayfa = QWidget()
        self.Harita_sayfa.setObjectName(u"Harita_sayfa")
        self.harita_label = QLabel(self.Harita_sayfa)
        self.harita_label.setObjectName(u"harita_label")
        self.harita_label.setGeometry(QRect(0, 0, 1100, 30))
        self.harita_label.setFont(font1)
        self.harita_label.setStyleSheet(u"color: #FFF;")
        self.harita_label.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.Harita_sayfa)

        self.Gyroscope_sayfa = QWidget()
        self.Gyroscope_sayfa.setObjectName(u"Gyroscope_sayfa")
        self.gyro_label = QLabel(self.Gyroscope_sayfa)
        self.gyro_label.setObjectName(u"gyro_label")
        self.gyro_label.setGeometry(QRect(0, 0, 1100, 30))
        self.gyro_label.setFont(font1)
        self.gyro_label.setStyleSheet(u"color: #FFF;")
        self.gyro_label.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.Gyroscope_sayfa)

        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)

        # Alt kısım ve butonlar
        self.frame_buttons = QFrame(self.centralwidget)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setMinimumSize(QSize(0, 150))
        self.frame_buttons.setMaximumSize(QSize(16777215, 150))
        self.frame_buttons.setStyleSheet(u"background-color: rgb(35,35,35);")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)

        self.gridLayout = QGridLayout(self.frame_buttons)
        self.gridLayout.setObjectName(u"gridLayout")

        # 12 adet buton oluşturuluyor
        self.buttons = []
        for i in range(12):
            button = QPushButton(f"Button {i + 1}", self.frame_buttons)
            button.setFont(font)
            button.setMinimumSize(QSize(0, 50))
            button.setStyleSheet(u"QPushButton {\n"
                                 "color: rgb(255,255,255);\n"
                                 "background-color: rgb(35,35,35);\n"
                                 "border : 0px solid;\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "background-color: rgb(85,170,255);\n"
                                 "}")
            self.gridLayout.addWidget(button, i // 4, i % 4)
            self.buttons.append(button)

        self.verticalLayout.addWidget(self.frame_buttons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)

        self.connectSignals()

        QMetaObject.connectSlotsByName(MainWindow)

    def connectSignals(self):
        # Connecting the top menu buttons
        self.Kamera.clicked.connect(self.showCameraPage)
        self.Harita.clicked.connect(self.showHaritaPage)
        self.Gyroscope.clicked.connect(self.showGyroscopePage)

        # Connecting the bottom buttons
        for i, button in enumerate(self.buttons):
            button.clicked.connect(lambda checked, idx=i: self.handleButtonClick(idx))

    def handleButtonClick(self, index):
        print(f"Button {index + 1} clicked")

    def showCameraPage(self):
        self.stackedWidget.setCurrentWidget(self.Kamera_sayfa)

    def showHaritaPage(self):
        self.stackedWidget.setCurrentWidget(self.Harita_sayfa)

    def showGyroscopePage(self):
        self.stackedWidget.setCurrentWidget(self.Gyroscope_sayfa)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.incele.setText(QCoreApplication.translate("MainWindow", u"İncele", None))
        self.Kamera.setText(QCoreApplication.translate("MainWindow", u"Kamera", None))
        self.Harita.setText(QCoreApplication.translate("MainWindow", u"Harita", None))
        self.Gyroscope.setText(QCoreApplication.translate("MainWindow", u"Gyroscope", None))
        self.kamera_label.setText(QCoreApplication.translate("MainWindow", u"Kamera Sayfası", None))
        self.harita_label.setText(QCoreApplication.translate("MainWindow", u"Harita Sayfası", None))
        self.gyro_label.setText(QCoreApplication.translate("MainWindow", u"Gyroscope Sayfası", None))
