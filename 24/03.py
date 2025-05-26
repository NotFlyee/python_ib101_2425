import wave
import struct

def chip_and_dale(number: int):
    audio = wave.open('wave.wav', mode='rb')
    new_audio = wave.open('wave2.wav', mode='wb')

    new_audio.setparams(audio.getparams())
    frames_count = audio.getnframes()

    data = struct.unpack('<' + str(frames_count) + 'h', audio.readframes(frames_count))

    new_data = data[::number]

    new_frames = struct.pack('<' + str(len(new_data)) + 'h', *new_data)

    new_audio.writeframes(new_frames)
    audio.close()
    new_audio.close()
