import requests
import os

api_key = 'your_osu_api_key'
user_id = 'your_user_id'
osu_songs_folder = 'your_file_path'
osu_email = 'your_osu_email'
osu_password = 'your_osu_password'

def get_recently_played_beatmaps(session):
    url = f'https://osu.ppy.sh/api/get_user_recent?k={api_key}&u={user_id}&limit=150'
    response = session.get(url)
    return response.json()

def get_top_performance_beatmaps(session):
    url = f'https://osu.ppy.sh/api/get_user_best?k={api_key}&u={user_id}&limit=150'
    response = session.get(url)
    return response.json()

def download_beatmap(session, beatmapset_id):
    url = f'https://osu.ppy.sh/beatmapsets/{beatmapset_id}/download'
    response = session.get(url)
    with open(os.path.join(osu_songs_folder, f'{beatmapset_id}.osz'), 'wb') as f:
        f.write(response.content)

def login_to_osu(session, email, password):
    url = 'https://osu.ppy.sh/session'
    payload = {
        "username": email,
        "password": password,
    }
    response = session.post(url, data=payload)

with requests.Session() as session:
    login_to_osu(session, osu_email, osu_password)
    recent_beatmaps = get_recently_played_beatmaps(session)
    top_beatmaps = get_top_performance_beatmaps(session)

    for beatmap in recent_beatmaps:
        download_beatmap(session, beatmap['beatmap_id'])

    for beatmap in top_beatmaps:
        download_beatmap(session, beatmap['beatmap_id'])
