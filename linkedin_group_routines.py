from linkedin import linkedin
import urllib

#########################
#Import secrets
from secrets import secret

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
    authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, 													 CONSUMER_SECRET,
                                                          USER_TOKEN, USER_SECRET,
                                                          RETURN_URL, linkedin.PERMISSIONS.enums.values())
    # Pass it in to the app...
    application = linkedin.LinkedInApplication(authentication)
    
    # Use the app....
    #app_data=application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations','interests','honors-awards','num-recommenders'])
    
    #names = [app_data['firstName'],app_data['lastName']]
    #print names

    # Use the app to get group info
    response_json = application.get_group(GROUP_ID)
    print response_json
