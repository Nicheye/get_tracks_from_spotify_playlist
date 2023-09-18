from dotenv import load_dotenv
import os
from requests import post,get
import base64
import json
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" +client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type":"client_credentials"}
    result = post(url,headers=headers,data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_songs_by_artist(token,artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers= get_auth_header(token)
    result = get(url,headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result
def get_songs_from_playlist(token,playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?&offset=99"
    headers= get_auth_header(token)
    result = get(url,headers=headers)
    json_result = json.loads(result.content)['items']
    return json_result

def search_for_track(token,song_name):
    url = "https://api.spotify.com/v1/search"
    headers =get_auth_header(token)
    query = f"?q={song_name}&type=track&limit=1"
    query_url = url+query
    result  =get(query_url,headers=headers)
    json_result = json.loads(result.content)['tracks']['items']
   
    if len(json_result)==0:
        print("no tracks")
        return None
    return json_result[0]['name'],json_result[0]['artists']

token = get_token()
# songs = get_songs_by_artist(token,"50co4Is1HCEo8bhOyUWKpn")
# for idx,song in enumerate(songs):
#     print(f"{idx+1}. {song['name']}")

playlist = get_songs_from_playlist(token,"0Zm6U4JJLAzkX9afHzhkVn")

# print(search_for_track(token,"Memo young thug"))



