import pytube

link = ("https://www.youtube.com/watch?v=4jcZdo2ak5E")

yt=pytube.YouTube(link)
yt.streams.get_highest_resolution().download()
print("downloaded")
