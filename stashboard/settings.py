import os

DEBUG = False

SITE_NAME = "Guardian Status Dashboard"
SITE_AUTHOR = "Web Systems"
SITE_URL = "http://guardian-dashbooard.appspot.com"
REPORT_URL = "mailto:faults.gu@guardian.co.uk"

# OAuth Consumer Credentials
CONSUMER_KEY = 'anonymous'
CONSUMER_SECRET = 'anonymous'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
    )
