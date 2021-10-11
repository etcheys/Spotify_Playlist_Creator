import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

#SET SPOTIPY_CLIENT_ID='42b91e976c9e47f18c7099264000e651'
#SET SPOTIPY_CLIENT_SECRET='72aa1fe959b948ccb909c6290bcc51c5'


REDIRECT_URI='http://localhost'
CLIENT_ID = "42b91e976c9e47f18c7099264000e651"
CLIENT_SECRET = "72aa1fe959b948ccb909c6290bcc51c5"

scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id = CLIENT_ID, client_secret = CLIENT_SECRET, redirect_uri = REDIRECT_URI))
user_id = sp.me()['id']


Freshman = sp.user_playlist_create(user_id, "Freshman Year")
Sophomore = sp.user_playlist_create(user_id, "Sophomore Year")
Junior = sp.user_playlist_create(user_id, "Junior Year")
Senior = sp.user_playlist_create(user_id, "Senior Year")


scope = 'playlist-read-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
playlists = sp.current_user_playlists()

for playlist in playlists['items']:
    if playlist['owner']['id'] == user_id:
        results = sp.playlist(playlist['id'], fields="tracks,next")
        tracks = results['tracks']
        show_tracks(tracks)



#Good_Music = sp.user_playlist_tracks("username", "4bikROunQl3WN89vHyuc2")