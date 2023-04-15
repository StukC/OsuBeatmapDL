import requests
import json

# Replace YOUR_API_KEY with your actual osu! API key
API_KEY = "YOUR_API_KEY"
USER_ID = "6522897"

def get_user_best(user_id, api_key):
    url = f"https://osu.ppy.sh/api/get_user_best?k={api_key}&u={user_id}&limit=100"
    response = requests.get(url)
    return json.loads(response.text)

def download_beatmap(beatmap_id, folder="beatmaps"):
    url = f"https://osu.ppy.sh/beatmapsets/{beatmap_id}/download"
    response = requests.get(url)
    with open(f"{folder}/{beatmap_id}.osz", "wb") as file:
        file.write(response.content)

def main():
    user_best = get_user_best(USER_ID, API_KEY)
    for score in user_best:
        beatmap_id = score["beatmap_id"]
        print(f"Downloading beatmap {beatmap_id}")
        download_beatmap(beatmap_id)

if __name__ == "__main__":
    main()
