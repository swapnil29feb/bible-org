import requests

API_KEY = 'eb4181141bb4d9eb938fafc09bc51aeb'
BASE_URL = 'https://api.scripture.api.bible/v1/bibles'
Bible_id = '8c49129a458d4059-01'
Pslams_book = 'PSA'
CHAPTER_ID = 'PSA.63'  # Assuming 'PSA.63' is the correct chapter ID for Psalms 63


def get_chapter(CHAPTER_ID, Bible_id):
    url = f'{BASE_URL}/{Bible_id}/chapters/{CHAPTER_ID}'

    headers = {
        'api-key': API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
            chapter = response.json()
            return chapter
    else:
        print(f"Error fetching chapters: {response.status_code}")
        return None


pslams = get_chapter(CHAPTER_ID, Bible_id)
print(pslams['data']['content'])