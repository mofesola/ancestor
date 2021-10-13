import struct
import pyaudio
import wave
from datetime import datetime
from common import Common
import pvporcupine
from playback import Playback

porcupine = None
pa = None
audio_stream = None

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second
seconds = Common.recording_duration()

class Recorder:
    def listen():
        try:
            #porcupine = pvporcupine.create(keyword_paths=['config/ancestor.ppn'])
            porcupine = pvporcupine.create(keywords=["computer"])
            pa = pyaudio.PyAudio()
            print("Listening for Hotword")
            audio_stream = pa.open(
                            rate=porcupine.sample_rate,
                            channels=1,
                            format=pyaudio.paInt16,
                            input=True,
                            frames_per_buffer=porcupine.frame_length)

            while True:
                pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
                pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

                keyword_index = porcupine.process(pcm)

                if keyword_index >= 0:
                    print("Hotword Detected")
                    # Stop and close the stream 
                    audio_stream.stop_stream()
                    #audio_stream.close()
                    Playback.talk_to_me()
                    Recorder.record()
                    Playback.playsound()
            
        except Exception as e:
                Recorder.listen()

        finally:
            if porcupine is not None:
                porcupine.delete()

            if audio_stream is not None:
                audio_stream.close()

            if pa is not None:
                pa.terminate()


    
    def record():
        p = pyaudio.PyAudio()  # Create an interface to PortAudio
        print('Recording')

        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)

        frames = []  # Initialize array to store frames

        # Store data in chunks for 3 seconds
        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk, exception_on_overflow=False)
            frames.append(data)

        # Stop and close the stream 
        stream.stop_stream()
        stream.close()
        # Terminate the PortAudio interface
        p.terminate()

        print('Finished recording')

        # Save the recorded data as a WAV file
        wf = wave.open("recordings/"+datetime.now().strftime("%m-%d-%Y-%H-%M-%S")+".wav", 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()


if __name__ == "__main__":
    Recorder.listen()
