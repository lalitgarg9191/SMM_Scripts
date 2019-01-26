import schedule
import time
import os
from datetime import datetime

def job(t):
    x = datetime.today()
    print(x)
    dir_path = r'C:\Users\Nishant\Music\Playlists\\' + str(x.day) + '\\'
    print(dir_path)
    list_of_songs = [x for x in os.listdir(dir_path) if x.endswith(".mp3")]
    print(list_of_songs)
    cmd = ""
    for i in range(len(list_of_songs)):
        cmd =cmd + '"' + dir_path + list_of_songs[i] + "\"/fullscreen "
    print(cmd)
    cmd1 = r"start wmplayer "+ cmd
    os.system(cmd1)
    

schedule.every().day.at("13:38").do(job,'It is 13:08')

while True:
    schedule.run_pending()
