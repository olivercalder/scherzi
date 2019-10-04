import os

files = os.listdir(".")
for file in files:
    if file[-4:] == '.wav':
        name = "'"+file.rstrip('.wav')
        print(name)
        print(type(name))
        os.system("ffmpeg -i {0}.wav' {0}.flac'".format(name))
