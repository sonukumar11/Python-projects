from pytube import YouTube

Weblink = "https://www.youtube.com/watch?v=1U3Uwct45IY"

#if we want to download at a particular location use location with double back slash...
location = 'C:\\Users\\Sonu Kumar\\Desktop\\coursera\\My_courses'

#creation of a yt object
yt = YouTube(Weblink)

print("The title of the Video is : ",yt.title)

print("The Strams availible for this video are : ",yt.streams)

# progressive streams have the video and audio in a single file, but typically do not provide the highest quality media
#  yt.streams.filter(progressive=True)

#adaptive streams split the video and audio tracks but can provide much higher quality.
yt.streams.filter(adaptive=True)

#getting the mp4 Stream..
#yt.streams.filter(file_extension='mp4')

stream = yt.streams.get_by_itag(22)
stream.download('C:\\Users\\Sonu Kumar\\Desktop\\coursera\\My_courses')
print("Mission Accomplished...")    





