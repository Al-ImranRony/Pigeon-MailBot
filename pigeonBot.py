import smtplib
import speech_recognition as sRec
import pyttsx3
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from email.message import EmailMessage



class Pigeon(Screen):
    listener = sRec.Recognizer()
    engine = pyttsx3.init()

    def talking(text):
        engine.say(text)
        engine.runAndWait()

    sender = ObjectProperty(None)
    receiver = ObjectProperty(None)
    subject = ObjectProperty(None)
    message = ObjectProperty(None)

    def get_info():
        try:
            with sRec.Microphone() as source:
                print('Listening...')
                voice = listener.listen(source)
                info = listener.recognize_google(voice)
                print(info)
                return info.capitalize()
        except:
            pass
    
    

class ContentGrid(Widget):
    
    sender = ObjectProperty(None)
    receiver = ObjectProperty(None)

    def btn(self):
        print("Sender is", self.sender.text, "Receiver", self.receiver.text)
        self.sender.text = ""
        self.receiver.text = ""

        





# def send_email(receiver, subject, message):    
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login('imranrony871@gmail.com', 'rr.M1neGA2')
#     email = EmailMessage()
#     email['From'] = 'imranrony687@gmail.com'
#     email['To'] = receiver
#     email['Subject'] = subject
#     email.set_content(message)
#     server.send_message(email)


# email_list = {
#     'Imran': 'imranrony537@outlook.com',
#     'Boka': 'abrhsn1998@gmail.com',
#     'Galib': 'asadullahpranto@gmail.com',
#     'Bondhu': 'imranrony537@gmail.com',
#     'Nahid': 'mdrabbaninahid96@gmail.com',
#     'Sakib': 'sakibzaman19@gmail.com',
#     'Hridoy': 'aashrafulhridoy@gmail.com',
#     'Aman': 'mdamanulla@gmail.com',
#     'Shariful': 'sisagor98@gmail.com',
#     'Jhankar': 'khan4019@gmail.com'
# }


# def get_email_info():
#     talking('Sending email to: ')
#     name = get_info()
#     receiver = email_list[name]
#     print(receiver)
#     talking('What will be the subject of your email ?')
#     subject = get_info()
#     talking('Now, Tell me the text message of your email')
#     message = get_info()

#     send_email(receiver, subject, message)
#     talking('Your message is sent you lazy freak !')
#     talking('Do you want to sent more email ?')
#     send_more = get_info()
#     if 'Yes' in send_more:
#         get_email_info()

# get_email_info()

if __name__ == "__main__":
    Pigeon().run()
    