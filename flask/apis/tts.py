from gtts import gTTS
message = "ethan is a boy"
tts = gTTS(message)
tts.save("audio.mp3")