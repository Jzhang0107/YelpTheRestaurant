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
    headers = {'Authorization': 'Bearer'}

    # parameters I'm passing in to the api request
    params = {'term': type,
              'location': city,
              'price': price,
              'limit': 2
              }
    # api-call
    r = requests.get(url=url, params=params, headers=headers)

    # information passed back from api
    apiDict = r.json()

    # list of dictionaries, each index is an individual business
    businessList = apiDict['businesses']

    # information I want
    nameList = []
    photoURLS = []
    displayAddresses = []
    for business in businessList:
        nameList.append(business['name'])

        # display addresses holds a list of lists, the first index tells you the restaurant and the second index is
        # the address split by commas
        displayAddresses.append(business['location']['display_address'])
        # for image in business['photos']:
            # photoURLS.append(image)
    # return str(businessList)
    # return str(str(nameList) + '\n' + str(displayAddresses))
    return render_template('results.html', name=nameList[0], address=displayAddresses[0])

@app.route('/')
def main():
    return render_template('mainpage.html')


if __name__ == '__main__':
    app.run(debug=True)
