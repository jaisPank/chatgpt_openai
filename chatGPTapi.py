from PyQt6.QtWidgets import QApplication,QMainWindow,QTextEdit,QPushButton,QLineEdit
import sys
from backend import Chatbot
import threading

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot()
        self.setWindowTitle("ChatGPT OPENAI")
        #self.setStyleSheet("background-color: rgb(38, 59, 74);\n"
        #                         "background-color: rgb(255, 255, 255);")
        self.setMinimumSize(700,500)
        self.chat_area=QTextEdit(self)
        self.chat_area.setGeometry(10,10,480,320)
        self.chat_area.setReadOnly(True)

        self.input_feild=QLineEdit(self)
        self.input_feild.setGeometry(10,340,480,40)
        self.input_feild.setPlaceholderText("Type here...")
        self.input_feild.returnPressed.connect(self.send_message)

        self.button =QPushButton("send",self)
        self.button.setGeometry(500,340,100,40)
        self.button.clicked.connect(self.send_message)

        self.show()
    def send_message(self):
        input1=self.input_feild.text().strip()
        self.chat_area.append(f"Myself: {input1}")
        self.input_feild.clear()
        thread=threading.Thread(target=self.get_response, args=(input1,))
        thread.start()


    def get_response(self,input1):
        response = self.chatbot.get_response(input1)
        self.chat_area.append(f"ChapGPT: {response}")


app=QApplication(sys.argv)
window=ChatbotWindow()
sys.exit(app.exec())