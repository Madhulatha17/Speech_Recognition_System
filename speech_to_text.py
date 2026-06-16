

import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile("sample.wav") as source:
    audio = recognizer.record(source)

text = recognizer.recognize_google(audio)

print("Recognized Text:")
print(text)

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("\nText saved to output.txt")
