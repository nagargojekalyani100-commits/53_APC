# Base class
class Media:
    def play(self):
        print("Playing media")


# Audio class
class Audio(Media):
    def play(self):
        print("Playing Audio")


# Video class
class Video(Media):
    def play(self):
        print("Playing Video")


# Podcast class
class Podcast(Media):
    def play(self):
        print("Playing Podcast")


# Create objects
audio = Audio()
video = Video()
podcast = Podcast()

# Store objects in a list
media_list = [audio, video, podcast]

# Runtime polymorphism
for media in media_list:
    media.play()