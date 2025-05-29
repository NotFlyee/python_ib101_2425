import wave
import struct

def break_the_silence():
    sound = wave.open('wave.wav', 'rb')
    new_sound = wave.open('out.wav', 'wb')

    new_sound.setparams(sound.getparams())

    frames_count = sound.getnframes()

    data = struct.unpack('<' + str(frames_count) + 'h', sound.readframes(frames_count))
    new_data = list(filter(lambda x: not(-5 <= x <= 5), data))

    new_frames = struct.pack('<' + str(len(new_data)) + 'h', *new_data)

    new_sound.writeframes(new_frames)

    sound.close()
    new_sound.close()
