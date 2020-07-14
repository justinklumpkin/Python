from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime, timedelta
scopes=['https://www.googleapis.com/auth/calendar']
'''
flow=InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes=scopes)
credentials =flow.run_console()


pickle.dump(credentials,open('credentials1.pkl', 'wb'))'''
'''
filename ='F:/Pythonprojects/Internal Assessment/credfile.txt'
f= open(filename, 'w+')
f.write(credentials)
'''
'''service = build('calendar', 'v3', credentials=credentials)
service.
'''

timezone='America/New_York'
credentials =pickle.load(open('credentials1.pkl', 'rb'))
service = build('calendar', 'v3', credentials=credentials)

calendar = {
    'summary': 'Sample Calendar',
    'timeZone': timezone
}

new_cal = service.calendars().insert(body=calendar).execute()

#print(calendars['items'][0])
calid=new_cal
events = service.events().list(calendarId=calid, timeMin='2020-01-20T01:00:00-05:00', timeMax='2020-02-20T01:00:00-05:00').execute()
#print(events['items'][0])#create my own toString for this

start=datetime(2020, 1,22,7,25,0)
end=start+timedelta(hours=1,minutes=26)

event = {
  'summary': 'CompSci Class',
  'location': '128 Clarendon Crescent',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': start.strftime('%Y-%m-%dT%H:%M:%S'),
    'timeZone': 'America/New_York',
  },
  'end': {
    'dateTime': end.strftime('%Y-%m-%dT%H:%M:%S'),
    'timeZone': 'America/New_York',
  },
  ''''recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],'''
  'attendees': [],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 2*24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}
#create an event
events = service.events().insert(calendarId=calid, body=event).execute()
print(events['end']['dateTime'])
