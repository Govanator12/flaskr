from app import app
from flask import render_template, url_for, jsonify, request
from config import Config
from app.forms import SearchForm
import requests


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    photos = []
    API_KEY = app.config['FLICKR_API_KEY']

    def getImageURL(id):

        url = f'http://api.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key={API_KEY}&photo_id={id}&format=json&nojsoncallback=1'

        response = requests.get(url).json()


        for i in range(len( response['sizes']['size'])):
            ans = ''
            if response['sizes']['size'][i]['label'] == 'Original':
                ans = response['sizes']['size'][i]['source']
        ans.replace("\\", "")
        return ans

    if form.validate_on_submit():
        text = form.search.data

        url = f'http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={API_KEY}&text={text}&sort=interestingness-desc&privacy_filter=1&format=json&nojsoncallback=1'

        response = requests.get(url).json()
        print(response['photos']['photo'])

        for i in range(len(response['photos']['photo'])):
            id = response['photos']['photo'][i]['id']


            if len(photos) <= 9:
                response['photos']['photo'][i].update({
                    'url': getImageURL(id)
                })

                photos.append(response['photos']['photo'][i])
            else:
                break

        return render_template('index.html', form=form, response=response, photos=photos, title='Home')

    return render_template('index.html', form=form)
