import speech as sr

# Create a recognizer instance
r = sr.speech()

# Use the microphone as source
with sr.Microphone() as source:
    # Adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    # Prompt user to speak
    print("Please say something...")
    # Record audio input
    audio = sr.listen(source)

try:
    # Use the Google Speech Recognition API to recognize audio input
    text = r.speech_google(audio)
    # Print the recognized text
    print("You said: " + text)
except sr.UnknownValueError:
    print("Sorry, could not recognize what you said.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

