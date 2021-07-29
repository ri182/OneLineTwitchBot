import os
while 0==0:: os.system("streamlink https://www.twitch.tv/destiny worst -O | ffmpeg -re -i pipe:0 -bsf:a aac_adtstoasc -vcodec copy -c copy -crf 50 /dev/null")
