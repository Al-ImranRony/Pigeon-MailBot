import smtplib
import speech_recognition as sRec
import pyttsx3
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from email.message import EmailMessage


class Pigeon(App):
    def build(self):
        return ContentGrid()

class ContentGrid(GridLayout):
    def __init__(self, **kwargs):
        super(ContentGrid, self).__init__(**kwargs)
        self.cols = 1                               # Columns in main grid layout         

        self.add_widget(Label(text="Pigeon - Your personal Email Bot is listenning"))
        self.header = TextInput(multiline=False)
        # self.add_widget(self.header)

        # New grid layout
        self.inside = GridLayout()                 # Creating multiple grid layout
        self.inside.cols = 2                        # Columns in new grid layout

        self.inside.add_widget(Label(text="Receipient: "))
        self.adrs = TextInput(multiline=False)
        self.inside.add_widget(self.adrs)

        self.inside.add_widget(Label(text="Subject: "))
        self.sub = TextInput(multiline=True)
        self.inside.add_widget(self.sub)

        self.inside.add_widget(Label(text="Message: "))
        self.msg = TextInput(multiline=True)
        self.inside.add_widget(self.msg)

        self.add_widget(self.inside)

        self.add_widget(Label(text="Connfirmation..."))
        self.confMsg = TextInput(multiline=True)

# listener = sRec.Recognizer()
# engine = pyttsx3.init()

# def talking(text):
#     engine.say(text)
#     engine.runAndWait()

# def get_info():
#     try:
#         with sRec.Microphone() as source:
#             print('Listening...')
#             voice = listener.listen(source)
#             info = listener.recognize_google(voice)
#             print(info)
#             return info.capitalize()
#     except:
#         pass

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
#     talking('Your message is sent you lazy dumb !')
#     talking('Do you want to sent more email ?')
#     send_more = get_info()
#     if 'Yes' in send_more:
#         get_email_info()

# get_email_info()

if __name__ == "__main__":
    Pigeon().run()