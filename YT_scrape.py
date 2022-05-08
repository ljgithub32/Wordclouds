from youtube_comment_scraper_python import *

import pandas as pd

URL = input("Video URL: ")

CSV_name = input("Name of csv file: ")

times = int(input("number of times to scroll (20 comments per scroll): "))

combined_data = []

youtube.open(URL)
for i in range(0, times):

    response = youtube.video_comments()

    data = response['body']

    combined_data.extend(data)

df = pd.DataFrame(data)

df.to_csv(CSV_name)

