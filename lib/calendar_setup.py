
import os

from dotenv import load_dotenv
from nylas import Client

load_dotenv()

CALENDAR_KEY = os.getenv('NYLAS_API_KEY')
CALENDAR_URI = os.getenv('NYLAS_API_URI')



nylas = Client(
    api_key=CALENDAR_KEY,
    api_uri=CALENDAR_URI
)


application = nylas.applications.info()
application_id = application[1]
print("Application ID:", application_id) 