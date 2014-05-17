#Append path and import
import sys
sys.path.append('../python3-linkedin/')
from linkedin import linkedin

import urllib

#Import secrets
from secrets import secret


CONSUMER_KEY = secret['API_KEY']
CONSUMER_SECRET = secret['Secret_Key']
USER_TOKEN = secret['OAUT']
USER_SECRET = secret['OAUS']
RETURN_URL = 'http://localhost:8000'


authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,
                                                          USER_TOKEN, USER_SECRET,
                                                          RETURN_URL, linkedin.PERMISSIONS.enums.values())
# Pass it in to the app...
application = linkedin.LinkedInApplication(authentication)

# Use the app....
g = application.get_profile()
u1 = g['siteStandardProfileRequest']['url']
d1 = urllib.request.urlopen(u1)