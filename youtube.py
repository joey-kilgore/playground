# download youtube video
vid_url = 'https://www.youtube.com/watch?v=dj8wKg2OOUo'

# import library
from pytube import YouTube

# get the video
youtube = YouTube(vid_url)

# get the info
print('Title: %s' % (youtube.title))
print('ID   : %s' % (youtube.video_id))
print('AGE RESTRICTED: %s' % (youtube.age_restricted))

# download
vid = youtube.streams.first()
vid.download('/mnt/c/Users/Joey/Desktop')

# get captions
caption = youtube.captions.get_by_language_code('en')
f = open('/mnt/c/Users/Joey/Desktop/caption.txt', 'w')
f.write(caption.generate_srt_captions())
f.close()
