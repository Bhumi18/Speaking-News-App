from pyttsx3 import engine
import pyttsx3
import speech_recognition as sr
import pyaudio
from GoogleNews import GoogleNews

today_news = GoogleNews()
a = pyttsx3.init()
speaking_voice = a.getProperty('voices')
a.setProperty('voice', speaking_voice[1].id)
recognizer = sr.Recognizer()

def speak_news():
    with sr.Microphone() as source:        
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        print("Tell me the topic for which you want the news")
        listen_voice = recognizer.listen(source, timeout=5)
        print("Your voice has been recorded")
    try:
        news_txt = recognizer.recognize_google(listen_voice, language='en_US')
        news_txt = news_txt.lower()
        print("Your message which you sent is :", format(news_txt))
    except Exception as e:
        print(e)
    if 'headlines' in news_txt:
        a.say("Wait getting headlines of today for you")
        a.runAndWait()
        today_news.get_news('Todays news')
        today_news.result()
        b = today_news.gettext()
        print(*b[1:5], sep=',')
    
    if 'sports' in news_txt:
        a.say("Wait getting sports news for you of today")
        a.runAndWait()
        today_news.get_news('Sports')
        today_news.result()
        b = today_news.gettext()
        print(*b[1:5], sep=',')

    if 'tech' in news_txt:
        a.say("Wait getting technology news for you of today")
        a.runAndWait()
        today_news.get_news('Tech')
        today_news.result()
        b = today_news.gettext()
        print(*b[1:5], sep=',')    

speak_news()





