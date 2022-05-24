import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2 import service_account
from pytube import YouTube

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def search_download_video(query, save_path, id_material):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "store/still-gravity-346208-3d3a7396cf01.json"

    # Get credentials and create an API client
    flow = service_account.Credentials.from_service_account_file(
        client_secrets_file, scopes=scopes)
    # credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=flow)
    try:
        request = youtube.search().list(
            part="snippet",
            maxResults=3,
            q=query
        )
        response = request.execute()
        info = []
        for video in response["items"]:
            id = video["id"]["videoId"]
            name = video["snippet"]["title"]
            author = video["snippet"]["channelTitle"]
            description = video["snippet"]["description"]
            source = "YouTube"
            url = "https://www.youtube.com/watch?v="+str(video["id"]["videoId"])
            filename = "video" + str(id)+str(id_material)+".mp4"
            path = "http://10.129.0.217:4000/videos/" + filename
            publish_date = int(video["snippet"]["publishedAt"].split('-')[0])
            video_category = 4
            info_object = {"name": name, "author": author, "description": description,
                           "source": source, "url": url, "path": path,
                           "publish_date": publish_date, "video_category": video_category
                            }
            try:
                yt = YouTube(url)
            except:
                print("Connection Error")  # to handle exception
            mp4files360 = yt.streams.filter(resolution='360p', file_extension='mp4', progressive='True')[-1]
            print(mp4files360)
            try:
                mp4files360.download(save_path, filename=filename)
                print("The video is saved")
                info.append(info_object)
            except:
                print("Video can not be downloaded!")

        return info
    except:
        return False
