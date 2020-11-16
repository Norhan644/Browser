from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from SpeechRecognition import *
import webbrowser

class EnterName(QDialog):
    def __init__(self):
        super(EnterName, self).__init__()
        loadUi(r'Browser\forms\name.ui', self)
        self.namebtn.clicked.connect(self.GoToNext)

    def store_name(self):
        name = self.name.text()


    def GoToNext(self):
        mainpage = MainBage()
        widget.addWidget(mainpage)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(570)
        widget.setFixedHeight(493)



class MainBage(QDialog):
    def __init__(self):
        super(MainBage, self).__init__()
        loadUi(r'Browser\forms\main.ui', self)
        self.voicebtn.clicked.connect(self.voice)
        self.discover_another_btn.clicked.connect(self.more_options)
    

    def voice(self):
        time.sleep(1)
        alexis_speak('How can I help you')
        while 1:
            voice_data = record_audio()
            respond(voice_data)

    def more_options(self):
        more_op = MoreOptions()
        widget.addWidget(more_op)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(599)
        widget.setFixedHeight(599)



class MoreOptions(QDialog):
    def __init__(self):
        super(MoreOptions, self).__init__()
        loadUi(r'Browser\forms\moreoptions.ui', self)
        self.googlebtn.clicked.connect(self.google_fun)
        self.youtubebtn.clicked.connect(self.youtube_fun)
        self.whatsappbtn.clicked.connect(self.whatsapp_fun)
        self.soundcloudbtn.clicked.connect(self.soundcloud_fun)
        self.stackoverflowbtn.clicked.connect(self.stack_overflow_fun)
        self.gitbtn.clicked.connect(self.git_fun)

    def google_fun(self):
        url = 'https://google.com/search?q='
        webbrowser.get().open(url)

    def youtube_fun(self):
        url = 'https://youtube.com/search?q='
        webbrowser.get().open(url)

    def whatsapp_fun(self):
        url = 'https://whatsapp.com/search?q='
        webbrowser.get().open(url)

    def soundcloud_fun(self):
        url = 'https://soundcloud.com/search?q='
        webbrowser.get().open(url)

    def stack_overflow_fun(self):
        url = 'https://stackoverflow.com/search?q='
        webbrowser.get().open(url)
    
    def git_fun(self):
        url = 'https://github.com/search?q='
        webbrowser.get().open(url)
    

app = QApplication([])  
dialog_name = EnterName()
widget=QtWidgets.QStackedWidget()
widget.setFixedWidth(474)
widget.setFixedHeight(153)

widget.addWidget(dialog_name)
widget.show()
app.exec_()



