from instagrapi import Client
cl = Client()
cl.login('osam_canary','admin0408')
user_id = cl.user_id_from_username("adw0rd")
medias = cl.user_medias(user_id, 20)

