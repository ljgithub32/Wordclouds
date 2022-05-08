# api key AIzaSyAc4E5M_HlhKMqOxFZRc7-3QWAs_uPwhm0
# guardian oxIxWIrPL-E
#sky ZVxaAiqDHKs

from googleapiclient.discovery import build
import pandas as pd

api_key ="AIzaSyAVyDpYPdVsR-kSn5Sc4HG_5CUoia75eRw"
video_id = "oxIxWIrPL-E"

resource = build('youtube', 'v3', developerKey=api_key)

request = resource. commentThreads().list(
                            part="snippet",
                            videoId=video_id,
                            maxResults=20,   # number of comments
                            order="orderUnspecified")

response = request.execute()



items = response["items"][:10]
for item in items:
    item_info = item["snippet"]
    topLevelComment = item_info["topLevelComment"]
    comment_info = topLevelComment["snippet"]
    comment_text = comment_info["textDisplay"]
    comment_author = comment_info["authorDisplayName"]
    comment_likes = comment_info["likeCount"]
    print(comment_text)




