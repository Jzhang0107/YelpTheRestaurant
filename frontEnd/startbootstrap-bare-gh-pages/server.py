from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('helloWorld.html')


@app.route('/initialResults', methods=['POST'])
def restaurantCall():
    experience = request.form['experience']
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    # api-endpoint
    url = 'https://api.yelp.com/v3/businesses/search'

    # authorization using access token
    headers = {'Authorization': 'Bearer os.environ["yelp_token"]'}

    # parameters I'm passing in to the api request
    params = {'term': experience,
              'latitude': latitude,
              'longitude': longitude,
              'open_now': True,
              'limit': 5
              }
    # api-call
    r = requests.get(url=url, params=params, headers=headers, mapBox_token=os.environ['mapbox_token'])

    # information passed back from api
    apiDict = r.json()

    # list of dictionaries, each index is an individual business
    businessList = apiDict['businesses']

    # information I want
    nameList = []
    addressList = []
    latitudeList = []
    longitudeList = []
    urlList = []
    imageUrlList = []

    for business in businessList:
        nameList.append(business['name'])
        addressList.append(business['location']['display_address'])
        latitudeList.append(business['coordinates']['latitude'])
        longitudeList.append(business['coordinates']['longitude'])
        urlList.append(business['url'])
        imageUrlList.append(business['image_url'])

    return render_template(experience + '.html', imageUrl= imageUrlList, url=urlList, name=nameList, address=addressList, latitude=latitudeList, longitude=longitudeList)


@app.route('/results', methods=['POST'])
def yelpCall():
    # information passed in from the form
    type = request.form['type']
    city = request.form['city']
    price = request.form['price']

    # api-endpoint
    url = 'https://api.yelp.com/v3/businesses/search'

    # authorization using access token
    headers = {'Authorization': 'Bearer os.environ["yelp_token"]'}

    # parameters I'm passing in to the api request
    params = {'term': type,
              'location': city,
              'price': price,
              'limit': 5
              }

    # api-call
    r = requests.get(url=url, params=params, headers=headers)

    # information passed back from api
    apiDict = r.json()

    # list of dictionaries, each index is an individual business
    businessList = apiDict['businesses']

    # information I want
    nameList = []
    addressList = []
    latitudeList = []
    longitudeList = []
    urlList = []
    imageUrlList = []

    for business in businessList:
        nameList.append(business['name'])
        addressList.append(business['location']['display_address'])
        latitudeList.append(business['coordinates']['latitude'])
        longitudeList.append(business['coordinates']['longitude'])
        urlList.append(business['url'])
        imageUrlList.append(business['image_url'])

    return render_template('result.html', mapBox_token=os.environ['mapbox_token'], url=urlList, imageUrl=imageUrlList, name=nameList, address=addressList, latitude=latitudeList, longitude=longitudeList)


if __name__ == '__main__':
    app.run(debug=True)
