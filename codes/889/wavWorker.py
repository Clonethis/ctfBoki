import wave
# Open WAV file in read-only mode.
with wave.open("you_know_what_to_do.wav", "rb") as wav_file:
    # Get basic information.
    # Number of channels. (1=Mono, 2=Stereo).
    n_channels = wav_file.getnchannels()
    sample_width = wav_file.getsampwidth()    # Sample width in bytes.
    framerate = wav_file.getframerate()       # Frame rate.
    n_frames = wav_file.getnframes()          # Number of frames.
    # Compression type (only supports "NONE").
    comp_type = wav_file.getcomptype()
    comp_name = wav_file.getcompname()        # Compression name.

    # Read audio data.
    frames = wav_file.readframes(n_frames)    # Read n_frames new frames.
    assert len(frames) == sample_width * n_frames

# Duplicate to a new WAV file.
# Open WAV file in write-only mode.
with wave.open("path_to_new_wav_file.wav", "wb") as wav_file:
    # Write audio data.
    params = (n_channels, sample_width, framerate,
              n_frames, comp_type, comp_name)
    wav_file.setparams(params)
    wav_file.writeframes(frames)
