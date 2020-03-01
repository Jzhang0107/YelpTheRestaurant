from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def yelpCall():
    zipCode = request.form['city']
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer'}
    params = {'location': 'San Bruno',
          'term': 'Japanese Restaurant',
          'pricing_filter': '1, 2',
          'sort_by': 'rating'
         }

    r = requests.get(url=url, params=params, headers=headers)
    apiDict = r.json()
    businesses = apiDict['businesses']
    return str(businesses)
    # return render_template('results.html')

@app.route('/')
def main():
    return render_template('mainpage.html')

if __name__ == '__main__':
    app.run(debug=True)
