from googletrans import Translator
import speech_recognition as sr
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listen, speak everything...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        print("STOP")
    try:
        text = r.recognize_google(audio).lower()
        print("You said: " + text)
    except sr.UnknownValueError:
        print("not recognized")
        text = command()
    except sr.TimeoutError:
        print("The attempt to establish a connection was unsuccessful.")
    return text
def makeSomething(command):
    tarjimon = Translator()
    tarjima = tarjimon.translate(str(command), dest='ru')
    print(f"Translate: {tarjima.text}")
 
while True:
    makeSomething(command())
