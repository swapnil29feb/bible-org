from flask import Flask, render_template, url_for, redirect, request
import requests
import json
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route("/home")
def index():
    return render_template("home.html")

@app.route("/<int:id>", methods= ['POST', 'GET'])
def home(id):
    API_KEY = 'eb4181141bb4d9eb938fafc09bc51aeb'
    BASE_URL = 'https://api.scripture.api.bible/v1/bibles'
    Bible_id = '8c49129a458d4059-01'
    Pslams_book = 'PSA'
    CHAPTER_ID = 'PSA.64'  # Assuming 'PSA.63' is the correct chapter ID for Psalms 63
    # chapter_number = 64

    if request.method == 'POST':
        chapter_number = request.form['psalm']
        print("User Enter: ", chapter_number, id)

        def Psalms_chapter(CHAPTER_ID,Bible_id):
            url = f"{BASE_URL}/{Bible_id}/chapters/{CHAPTER_ID}"

            headers = {
                'api-key' : API_KEY
            }

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                print("Good")
                chapter = response.json()
                return chapter
            else:
                print("not good", response.status_code)

        Get_pslams =  Psalms_chapter(CHAPTER_ID,Bible_id)
        # print(Get_pslams['data'])

        Pslams = Get_pslams['data']['content']
        # print(Pslams)

        soup = BeautifulSoup(Pslams, "html.parser")
        # print(soup)
        title = soup.find('p', {'class':'s'}).getText()
        print("\n\n\nTITLE: ",title)

        heading = soup.find('p', {'class':'d'}).getText()
        print("\n\n\nHeading: ", heading)

        formated_verse = []
        all_verses = soup.select('p.q')

        for verse in all_verses:
            span_tag = verse.find('span', class_='v')
            if span_tag:
                verse_number = span_tag.text
                verse_text = verse.text.split(' ', 1)[1]
                data_vid_p = soup.find('p', attrs={'data-vid': f'PSA {chapter_number}:{verse_number}'})
                
                if data_vid_p:
                    verse_text2 = data_vid_p.get_text()
                    # Combine the number and text
                    combi = f'{verse_number} : {verse_text} {verse_text2}'
                    # Append the result to the formatted_verse list
                    formated_verse.append(combi)
                else:
                    print(f"No match found for data-vid: PSA {chapter_number}:{verse_number}")
            else:
                print(f"No <span> tag found for verse: {verse.text}")
        return render_template('index.html', data = formated_verse, title=title, heading=heading, chapter_number=chapter_number)
    else:
        return render_template("home.html")



@app.route('/previous')
def previous():
    return redirect(url_for('home'))

@app.route('/refresh')
def refresh():
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)