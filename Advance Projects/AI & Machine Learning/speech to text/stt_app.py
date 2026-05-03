import whisper
import sounddevice as sd
import numpy as np
import tempfile
import wave
import os

#load Model
print("Loading wispher model .......")
model=whisper.load_model("base") #base or #large

def record_and_transcribe(time=5,sampling_rate=16000):
    print(f"\n Listening for {time} seconds...")
    #caputur audio
    recording=sd.rec(int(time*sampling_rate),samplerate=sampling_rate,channels=1,dtype='float32')
    sd.wait()
    print("Processing")

    #data extraction

    with tempfile.NamedTemporaryFile(suffix=".wav",delete=False)as tmpfile:
        temp_path= tmpfile.name

    #write as WAV
    with wave.open(temp_path,"wb")as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sampling_rate)
        #convert float32 to int64 for wav
        wf.writeframes((recording*32767).astype(np.int16).tobytes())

    result= model.transcribe(temp_path,fp16=False)

    os.remove(temp_path)
    return result["text"]

if __name__ == "__main__":
    while True:
        text= record_and_transcribe()
        print(f"AI recognised:{text}")

        if "q" in text.lower() or "stop" in text.lower():
            print("Shutting down")
            break