#Desktop Assistant
from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

#speaks audio passed as argument
def talkToMe(audio):
    print(audio)
    tts = gTTS(text-audio, lang='en')
    os.system('mpg123 audio.mp3')

#listen for commands
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am ready for your next command!')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
    try:
        command = r.recognize_google(audio)
        print('you said:' + command + '\n')

#loop back to continue to listen for commands if unrecognize
    except sr.UnknownValueError:
        assistant(myCommand())
    return command

#if statements for executing commands
def assistant(command):
    if 'open Reddit python' in command:
        chrome_path = '/usr/bin/google.chrome'
        url = 'https://www.reddit.com/r/python/'
        webbrowser.get(chrome_path).open(url)

    if 'what\'s up' in command:
        talkToMe('Just doing my thing')

    if 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'Talat' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

        #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)
 
        #identify to server
        mail.ehlo()

        #encrypt session
        mail.starttls()

        #login
        mail.login('username', 'password')

        #send message
        mail.sendmail('PERSON NAME', 'emailaddress@gmail.com', content)
        mail.close()
        talkToMe('Email sent')
talkToMe('I am ready for your command')
while True:
    assistant(myCommand())

