
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime, timedelta
filename ='calendar_id.txt'


##
timezone='America/New_York'
##credentials =pickle.load(open('credentials1.pkl', 'rb'))
##service = build('calendar', 'v3', credentials=credentials)
##
calendar = {
    'summary': 'Sample Calendar',
    'timeZone': timezone
}

scopes=['https://www.googleapis.com/auth/calendar']
credentials =pickle.load(open('credentials1.pkl', 'rb'))
service = build('calendar', 'v3', credentials=credentials)
class Event():#class to represent an event
    def __init__(self, idnum,start, evid=None,name='MyEvent',duration=60, address='', description ='',tz='America/New_York',):
                                                                        #constructs an event. default values prevent errors
        self.start= start
        self.end=self.start+timedelta(minutes=duration)
        self.name =name
        self.address=address
        self.description= description
        self.timezone=tz
        self.cal_id=idnum
        self.event_id=evid
        self.setup()
    def setup(self):#the self.event variable is in the format necessary to pass into a google calendar object
        self.event = {
          'summary': self.name,
          'location': self.address,
          'description': self.description,
          'start': {
            'dateTime': self.start.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': self.timezone,
          },
          'end': {
            'dateTime': self.end.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': self.timezone,
          },
          'reminders': {
            'useDefault': True
          }
        }
    def __str__(self):#creates a string representation of an event
        rtn=''
        startstr=datetime.strftime(self.start, '%m/%d/%Y %H:%M:%S')
        endstr=datetime.strftime(self.end, '%m/%d/%Y %H:%M:%S')

        rtn+=self.name.title()+"\n\t\t\tStart: "+startstr+"\t"+"End: "+endstr+"\n"
        if self.address:
            rtn+="\t\t\t"+str(self.address)+"\n"
        if self.description:
            rtn+="\t\t\t"+str(self.description)+"\n"
        return rtn
    #-------------------Accessor Methods----------------------#
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def get_id(self):
        return self.event_id
    def __lt__(self, other):#comparison of events is based on start time. end time breaks ties.
        if self.start<other.get_start():
            return True
        elif self.start== other.get_start() and self.end<other.get_end():
            return True
        else:
            return False
    def __gt__(self, other):
        if self.start>other.get_start():
            return True
        elif self.start== other.get_start() and self.end>other.get_end():
            return True
        else:
            return False
    def __eq__(self, other):
        if self.start==other.get_start() and self.end==other.get_end():
            return True
        else:
            return False
class New_Event(Event):#creates an event and adds it to the google calendar
    def __init__(self, idnum,start, name='MyEvent',duration=60, address='', description ='',tz='America/New_York'):
        super().__init__(idnum= idnum,start=start, name=name,duration=duration, address=address, description =description,tz=tz)
        e=service.events().insert(calendarId=self.cal_id, body=self.event).execute()
        self.event_id=e['id']

class Shared_Event(Event):#creates and event with attendees
    def __init__(self, idnum,start, evid=None, name='',duration=60, address='', attendees=[],description ='',tz='America/New_York'):
        self.attendees =attendees
        super().__init__(idnum=idnum, name =name,evid=evid,start=start, duration=duration, address=address,description=description,tz=tz)
    def setup(self):
        super().setup()
        self.event['attendees']= self.attendees
        self.event['reminders']={
            'useDefault': False,
            'overrides': [
              {'method': 'email', 'minutes': 2*24 * 60},
              {'method': 'popup', 'minutes': 10},
            ],
        }
    def __str__(self):#creates a string representation of a shared event
        rtn=super().__str__()
        rtn+='\t\t\tAttendees:\n'
        for a in self.attendees:
            rtn+='\t\t\t'
            rtn+=a['email']
            rtn+='\n'
        return rtn
class New_Shared_Event(Shared_Event):#creates a shared event and adds it to the google calendar
    def __init__(self, idnum,start, name='MyEvent',duration=60, address='', attendees=[],description ='',tz='America/New_York'):
        super().__init__(idnum= idnum,start=start, name=name,duration=duration, address=address, attendees=attendees,description =description,tz=tz)
        e=service.events().insert(calendarId=self.cal_id, body=self.event).execute()
        self.event_id=e['id']
    
class Calendar():
    def __init__(self,tz='America/New_York', events=[], name='MyCalendar', new=False):
        self.timezone = tz
        self.events =events
        self.name = name
        self.cal_id=None
        if new:
            self.create_calendar()
        else:
            self.use_default()
    def create_calendar(self):#creates new calendar and returns its id
        calendar = {
            'summary': self.name,
            'timeZone': self.timezone
        }
        new_cal = service.calendars().insert(body=calendar).execute()
        self.cal_id=new_cal['id']

        f= open(filename, 'w+')
        f.write(self.cal_id)
    def use_default(self):
        f= open(filename, 'r+')
        self.cal_id =f.read()
        
        page_token = None
        while True:
            events = service.events().list(calendarId=self.cal_id, pageToken=page_token).execute()
            for event in events['items']:
                #print(event.keys())
                start=event['start']['dateTime']
                start_time= datetime.strptime(start[:-6], '%Y-%m-%dT%H:%M:%S')
                end =event['end']['dateTime']
                end_time= datetime.strptime(end[:-6], '%Y-%m-%dT%H:%M:%S')
                td =end_time-start_time
                duration=td.seconds/60
                if 'location' in event:
                    address=event['location']
                else:
                    address=''
                if 'description' in event:
                    description=event['description']
                else:
                    description=''
                tz=start_time.tzinfo
                e=None
                if 'attendees' in event:
                    e= Shared_Event(idnum=self.cal_id, start=start_time, name=event['summary'], duration=duration,description=description, address=address,attendees =event['attendees'], tz=tz, evid=event['id'])
                else:
                    e = Event(idnum=self.cal_id, start=start_time, name=event['summary'],duration=duration, address=address, description=description, tz=tz, evid=event['id'])
                self.events.append(e)
            page_token = events.get('nextPageToken')
            if not page_token:
                break
        self.events.sort()
    def create_event(self, start, name='',duration=60, address='', attendee_emails=[], description =''):
        start_time= datetime.strptime(start, '%m/%d/%Y %H:%M:%S')

        
        if attendee_emails  !=[]:
            attendees =[]
            for email in attendee_emails:
                attendees.append({'email':email})
            e = New_Shared_Event(self.cal_id, start_time, name,duration=duration, address=address, attendees=attendees, description=description)
        else:
            e = New_Event(self.cal_id, start_time, name,duration=duration, address=address, description=description)

        self.events.append(e)
        self.events.sort()
        
    '''def clear_events(self, mintime, maxtime):
        for e in self.events:
            if e.get_start()>#continue here'''
    def delete_event(self, tmin, tmax=None):
        time1=datetime.strptime(tmin, '%m/%d/%Y %H:%M:%S')
        if tmax==None:
            time2=time1
        else:
            time2=datetime.strptime(tmax, '%m/%d/%Y %H:%M:%S')
        for i in range(len(self.events)-1,-1,-1):
            if (self.events[i].get_start()>time1 and self.events[i].get_start()<time2) or self.events[i].get_start()==time1 or self.events[i].get_start()==time2:
                service.events().delete(calendarId=self.cal_id, eventId=self.events[i].get_id()).execute()
                self.events.pop(i)
    def __str__(self):
        rtn=''
        rtn+=self.name.title()+":\n\tEvents:\n"
        if self.events !=[]:
            for e in self.events:
                rtn+='\t\t'+str(e)+'\n'
        else:
            rtn+="\t\tNo Events"
        return rtn


#events = service.events().list(calendarId=calid, timeMin='2020-01-20T01:00:00-05:00', timeMax='2020-02-20T01:00:00-05:00').execute()
#print(events['items'][0])#create my own toString for this



'''

c=Calendar(name ='MyCalendar')
for event in c.events:
    print(event)
c.delete_event('01/30/2020 06:05:00', '01/30/2020 07:15:00')
print('---------------------------------')
for event in c.events:
    print(event)
c.create_event('01/28/2020 07:25:00', 'CompSci', attendee_emails = ['justinklumpkin@gmail.com'])
c.create_event('01/30/2020 06:25:00', 'Band', attendee_emails = ['justinklumpkin@gmail.com'])
c.create_event('02/02/2020 08:25:00', 'Math')
c.create_event('01/30/2020 07:14:00', 'History', attendee_emails = ['justinklumpkin@gmail.com'])
'''


