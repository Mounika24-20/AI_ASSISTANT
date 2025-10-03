import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests
import pywhatkit


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  
def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
    except Exception:
        print("❌ Sorry, say that again...")
        return "None"
    return query.lower()


def get_weather(city):
    api_key = "your_api_key_here"   
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url).json()

    if response["cod"] != "404":
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {desc}"
    else:
        return "City not found."


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("mounikaboyapati2005@gmail.com", "Mounika32")   
    server.sendmail("mounikaboyapati2005@mail@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    speak("Hello Mounika, I am your AI assistant. How can I help you?")

    while True:
        query = take_command()

       
        if "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        
        elif "date" in query:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today is {date}")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

      
        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")
        elif "open google" in query:
            webbrowser.open("https://google.com")
        elif "open linkedin" in query:
            webbrowser.open("https://linkedin.com")

      
        elif "play music" in query:
            music_dir = "D:\\AI_Music"

            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

     
        elif "weather" in query:
            speak("Tell me the city name")
            city = take_command()
            weather_report = get_weather(city)
            speak(weather_report)

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "receiver_email@gmail.com"   
                send_email(to, content)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry babe, I couldn't send the email.")

        elif "send message" in query:
            speak("What should I send?")
            message = take_command()
            pywhatkit.sendwhatmsg("+9100751604", message, 19, 30) 
            speak("Message scheduled successfully!")

   
        elif "open code" in query:
            codePath = "C:\\Users\\Mounika\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

  
        elif "exit" in query or "quit" in query:
            speak("Goodbye babe! Have a nice day.")
            break

