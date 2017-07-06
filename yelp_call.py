from rauth import OAuth1Session

def get_search_params(lat, long, open_now):
    params = {}
    params['ll'] = '{},{}'.format(str(lat), str(long))
    params['open'] = open_now == True
    params['limit'] = '1'

    return params

def get_results(params):
    consumer_key = ''
    consumer_secret=''
    token = ''
    token_secret=''

    session = rauth.OAuth1Session(
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = token,
        access_token_secret = token_secret
    )

    request = session.get('http://api.yelp.com')

    #Transforms the JSON API response into a dict

    data = request.json()
    session.close

    return data

def main():
    locations=[#pull from yelp as user location]
    api_calls = []
    time.sleep(1.0)