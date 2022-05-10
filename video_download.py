from pytube import YouTube

# where to save
SAVE_PATH = "C:/Users/valeriya.nikiforova/Documents/UCA\Senior/FYP/remote_library_static_server/videos"  # to_do

# link of the video to be downloaded
link = "https://www.youtube.com/watch?v=ij774Lur3GA"

try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error")  # to handle exception

# filters out all the files with "mp4" extension
# mp4files = yt.filter('mp4')
# mp4files = yt.streams.filter(file_extension='mp4', )
mp4files360 = yt.streams.filter(resolution='360p', file_extension='mp4', progressive='True')[-1]
print(mp4files360)
try:
    mp4files360.download(SAVE_PATH)
    print("The video is saved")
except:
    print("Video can not be downloaded!")


# get the video with the extension and
# resolution passed in the get() function
# d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
# try:
#     # downloading the video
#     d_video.download(SAVE_PATH)
# except:
#     print("Some Error!")
# print('Task Completed!')