#formating dataset vivos and fpt together
import shutil, os
import pandas as pd
from os.path import join, dirname, splitext, basename
from pydub import AudioSegment

# shutil.copytree will raise excection when destination folder exists
from distutils.dir_util import copy_tree


# # convert mp3 to wav
# directory = "/home/500/anh_lbt/NLP/Tacotron-2/fpt_dataset/FPTOpenSpeechData_Set001_V0.1/mp3"
audio_file = '/home/500/anh_lbt/NLP/Tacotron-2/fpt_dataset/FPTOpenSpeechData_Set002_V0.1/FPTOpenSpeechData_Set002_Part2_V0.1/mp3/FPTOpenSpeechData_Set002_V0.1_000537.mp3'

try:
    filename_w_ext = basename(audio_file)
    filename, file_extension = splitext(filename_w_ext)
    dst = join(os.getcwd(), filename + '.wav')
    sound = AudioSegment.from_file(audio_file,format='mp3')
    sound.export(dst,bitrate="256k", format="wav", parameters=["-b:a", "256k"], codec="avlib")
except Exception as ex:
    print(ex)
