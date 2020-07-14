import Calendar_Event
from tkinter import* 


from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime, timedelta
scopes=['https://www.googleapis.com/auth/calendar']

c=None
ans=2

def build_new_event():
    start=date.get("1.0",'end-1c')+' '+time.get("1.0",'end-1c')
    emails=[]
    if unit.get()=='hours':
        dur=int(duration.get("1.0",'end-1c'))*60
    elif unit.get()=='days':
        dur=int(duration.get("1.0",'end-1c'))*60*24
    else:
        dur=int(duration.get("1.0",'end-1c'))
    if len(attendee.get("1.0",'end-1c'))>0:
        emails = list(attendee.get("1.0",'end-1c').split(';'))
    c.create_event(start=start, name=name.get("1.0",'end-1c'), duration=dur, address=loc.get("1.0",'end-1c'), description =description.get("1.0",'end-1c'), attendee_emails=emails)
    print("Event created.")
def del_event():
    t1=time1.get("1.0",'end-1c')
    if t1=='':
        t1='01/01/0001 01:00:00'
    t2=time2.get("1.0",'end-1c')
    if t2=='':
        t2=None
    c.delete_event(tmin=t1,tmax=t2)
    print("Event deleted.")
while ans!=5:
    ans=int(input("\n1)Setup Calendar\n2)Display Events\n3)New Event\n4)Remove Events\n5)Exit\n"))
    
    if ans==1:
        flow=InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes=scopes)
        credentials=flow.run_console()
        #pickle.dump(credentials,open('credentials2.pkl', 'wb'))
        service = build('calendar', 'v3', credentials=credentials)
        name=input("Enter the calendar name: ")
        new=input('Is this a new calendar? (y/n) ')
        c=Calendar_Event.Calendar(name=name, new=(new!='n'))
        print("Setup complete.")
    elif c==None and ans!=5:
        print('Error. You must set up a calendar first.')
    elif ans==2:
        print(c)
    elif ans==3:
        master = Tk()
        name_lab=Label(master, text="Event Name")
        name_lab.pack()
        name=Text(master, height = 2, width = 20)
        name.pack()

        date_lab=Label(master, text="Start Date (mm/dd/yyyy)")
        date_lab.pack()
        date=Text(master, height = 2, width = 10)
        date.pack()

        time_lab=Label(master, text="Start Time on a 24hr Clock(hh:mm:ss)")
        time_lab.pack()
        time=Text(master, height = 2, width = 10)
        time.pack()

        
        duration_lab=Label(master, text="Duration")
        duration_lab.pack()
        duration=Text(master, height = 2, width = 10)
        duration.pack()
        unit = StringVar(master)
        unit.set("minutes") # default value
        dur_unit = OptionMenu(master, unit, "days","hours", "minutes")
        dur_unit.pack()

        loc_lab=Label(master, text="Address/Location (Optional)")
        loc_lab.pack()
        loc=Text(master, height = 4, width = 30)
        loc.pack()

        description_lab=Label(master, text="Description (Optional)")
        description_lab.pack()
        description=Text(master, height = 6, width = 30)
        description.pack()

        attendee_lab=Label(master, text="Attendee Emails (Optional, separate with ';')")
        attendee_lab.pack()
        attendee=Text(master, height = 6, width = 30)
        attendee.pack()

        Button(master, text='Create Event', command=build_new_event).pack()
        master.mainloop() 
    elif ans==4:
        master = Tk()
        time1_lab=Label(master, text="From (24hr Clock, mm/dd/yyyy hh:mm:ss)")
        time1_lab.pack()
        time1=Text(master, height = 2, width = 20)
        time1.pack()

        time2_lab=Label(master, text="To (24hr Clock, mm/dd/yyyy hh:mm:ss)")
        time2_lab.pack()
        time2=Text(master, height = 2, width = 20)
        time2.pack()

        Button(master, text='Remove Events', command=del_event).pack()
        master.mainloop() 
