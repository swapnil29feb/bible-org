import requests

API_KEY = 'eb4181141bb4d9eb938fafc09bc51aeb'  # Replace with your actual API key
BASE_URL = 'https://api.scripture.api.bible/v1/bibles'
BIBLE_ID = '8c49129a458d4059-01'  # Hindi Bible ID (Indian Revised Version)
PSALMS_BOOK_ID = 'PSA'  # Book ID for Psalms (you may need to confirm this ID from the API documentation)

def get_chapters(bible_id, book_id):
    url = f'{BASE_URL}/{bible_id}/books/{book_id}/chapters'
    headers = {
        'api-key': API_KEY
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        chapters = response.json()
        return chapters['data']
    else:
        print(f"Error fetching chapters: {response.status_code}")
        return None

def get_chapter_content(bible_id, chapter_id):
    url = f'{BASE_URL}/{bible_id}/chapters/{chapter_id}'
    headers = {
        'api-key': API_KEY
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        chapter = response.json()
        return chapter['data']
    else:
        print(f"Error fetching chapter content: {response.status_code}")
        return None

chapters = get_chapters(BIBLE_ID, PSALMS_BOOK_ID)

if chapters:
    psalms_content = []
    for chapter in chapters:
        chapter_id = chapter['id']
        chapter_content = get_chapter_content(BIBLE_ID, chapter_id)
        if chapter_content:
            psalms_content.append(chapter_content['content'])

    # Join all chapters' content into a single string
    all_psalms = '\n'.join(psalms_content)
    print("All Psalms content:")
    print(all_psalms)
else:
    print("No chapters found or there was an error.")
