from instagrapi import Client
from instagrapi.types import Location, StoryMention, StoryLocation, StoryLink, StoryHashtag

cl = Client()
cl.login('osam_canary','admin0408')

media_path = cl.video_download(
    cl.media_pk_from_url('https://www.instagram.com/p/CGgDsi7JQdS/')
)

adw0rd = cl.user_info_by_username('adw0rd')
loc = cl.location_complete(Location(name='Test', lat=42.0, lng=42.0))
ht = cl.hashtag_info('dhbastards')

cl.video_upload_to_story(
    media_path,
    "Credits @adw0rd",
    mentions=[StoryMention(user=adw0rd, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)],
    locations=[StoryLocation(location=loc, x=0.33, y=0.22, width=0.4, height=0.7)],
    links=[StoryLink(webUri='https://github.com/adw0rd/instagrapi')],
    hashtags=[StoryHashtag(hashtag=ht, x=0.23, y=0.32, width=0.5, height=0.22)],
)