from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/results', methods=['POST'])
def yelpCall():
    # information passed in from the form
    type = request.form['type']
    city = request.form['city']
    price = request.form['price']

    # api-endpoint
    url = 'https://api.yelp.com/v3/businesses/search'

    # authorization using access token
    headers = {'Authorization': 'Bearer '}

    # parameters I'm passing in to the api request
    params = {'term': type,
              'location': city,
              'price': price,
              'limit': 3
              }
    # api-call
    r = requests.get(url=url, params=params, headers=headers)

    # information passed back from api
    apiDict = r.json()

    # list of dictionaries, each index is an individual business
    businessList = apiDict['businesses']

    # information I want
    nameList = []
    displayAddresses = []
    latitudeList = []
    longitudeList = []

    for business in businessList:
        nameList.append(business['name'])
        displayAddresses.append(business['location']['display_address'])
        latitudeList.append(business['coordinates']['latitude'])
        longitudeList.append(business['coordinates']['longitude'])

    # return str(latitudeList)
    # return str(str(nameList[0]) + "\n" + str(displayAddresses[0]) + "\n" + str(latitudeList[0]) + "\n" + str(longitudeList[0]))

    return render_template('result.html', restaurantName=nameList[0], address=displayAddresses[0], latitude=latitudeList[0], longitude=longitudeList[0])

@app.route('/')
def main():
    return render_template('mainpage.html')

if __name__ == '__main__':
    app.run(debug=True)
