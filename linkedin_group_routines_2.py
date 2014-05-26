# use the py code from https://developer.linkedin.com/documents/quick-start-guide

import oauth2 as oauth
import httplib2
import time, os, simplejson

#########################
#Import secrets
from secrets import secret

#######################
#Load auth keys
CONSUMER_KEY = secret['API_KEY']
CONSUMER_SECRET = secret['Secret_Key']
USER_TOKEN = secret['OAUT']
USER_SECRET = secret['OAUS']
RETURN_URL = 'http://localhost:8000'
GROUP_ID = secret['Group_ID']

def linkedin_group_read():
    # Use your API key and secret to instantiate consumer object
    consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
 
    # Use the consumer object to initialize the client object
    client = oauth.Client(consumer)
     
    # Use your developer token and secret to instantiate access token object
    access_token = oauth.Token(
                key=USER_TOKEN,
                secret=USER_SECRET)
     
    client = oauth.Client(consumer, access_token)
     
    # Make call to LinkedIn to retrieve your own profile in json
    resp,content = client.request("http://api.linkedin.com/v1/people/~?format=json", "GET", "")
    
    # print "resp"
    # print resp
    
    print "content"
    print content

