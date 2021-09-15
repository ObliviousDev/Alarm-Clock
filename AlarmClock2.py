import PySimpleGUI as sg
import datetime
import os
import time

#default_values = ['12','11','10','9','8','7','6','5','4','3','2','1']
#default_values = ['59','58','57','56','55','54','53','52','51','50','49','48','47','46','45','44','43','42','41','40','39','38','37','36','35','34','33','32','31','30','29','28','27','26','25','24','23','22','21','20','19','18','17','16','15','14','13','12','11','10','09','08','07','06','05','04','03','02','01','00']
#default_values = ['AM'],

hour = datetime.datetime.now().hour - 12
minute = str(datetime.datetime.now().minute)
second = str(datetime.datetime.now().second)
isSet = False
stop = True

Hours = []
Minutes = []
AmPms = []
IsFinished = []

if datetime.datetime.now().minute < 10:
    minute = str(0) + minute
if datetime.datetime.now().second < 10:
    minute = str(0) + second

sg.theme('DarkAmber')

layout = [
    [sg.Text(str(hour)+':'+str(minute)+':'+str(second), font = ('Courier 60'), key=('time'))],
    [sg.Text('ALARMS', font=('Courier 30'))],
    [sg.Listbox(values = ('12','11','10','9','8','7','6','5','4','3','2','1'), font = 'Courier 20', key = ('Hour'))],
    [sg.Listbox(values = ('59','58','57','56','55','54','53','52','51','50','49','48','47','46','45','44','43','42','41','40','39','38','37','36','35','34','33','32','31','30','29','28','27','26','25','24','23','22','21','20','19','18','17','16','15','14','13','12','11','10','09','08','07','06','05','04','03','02','01','00'), font = 'Courier 20', key = ('Minute'))],
    [sg.Listbox(values = ('PM','AM'), font = 'Courier 20', key = ('AMPM'))],
    [sg.Button('SET')]
    ]

window = sg.Window("Alarm Clock", layout)

while True:
    event, values = window.read(timeout = 10)
    if event == 'SET':
        
        Minute = values['Minute']
        Hour = values['Hour']
        AmPm = values['AMPM']
        
        isSet = True
        print(Minute[0])
        Minute = int(Minute[0])
        Hour = int(Hour[0])
        AmPm = AmPm[0]

        Hours.append(Hour)
        Minutes.append(str(Minute))
        AmPms.append(AmPm)
        IsFinished.append(False)
    if event == sg.WIN_CLOSED:
        break
    
    hour = datetime.datetime.now().hour - 12
    minute = str(datetime.datetime.now().minute)
    second = datetime.datetime.now().second

    if datetime.datetime.now().minute < 10:
        minute = str(0) + str(minute)
    if datetime.datetime.now().second < 10:
        second = str(0) + str(second)

    if isSet == True:
        for i in range(len(Hours)):
            if Hours[i] == hour:
                if Minutes[i] == minute:
                    if not IsFinished[i]:
                        print("RINGA DINGA DING!")
                        os.system("[PUT AUDIO FILE HERE]") #Add your audio file place here
                        IsFinished[i] = True
    window['time'].update(str(hour)+':'+str(minute)+':'+str(second))



    
