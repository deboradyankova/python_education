from datetime import datetime, timedelta

DELTA = timedelta(minutes=30)

hour_exam = int(input('hour exam'))
mins_exam = int(input('mins exam'))
hour_arrival = int(input('hour arrival'))
mins_arrival = int(input('mins arrival'))

exam_hour = datetime(year=2021, month=11, day=1, hour=hour_exam, minute=mins_exam)
arrival_hour = datetime(year=2021, month=11, day=1, hour=hour_arrival, minute=mins_arrival)

if arrival_hour > exam_hour:
    print('Late')
    late = str(arrival_hour - exam_hour)
    hours, mins, _ = late.split(':')
    if int(hours):
        print(f'{hours}:{mins} hours after the start')
    else:
        print(f'{mins} minutes after the start')
elif arrival_hour < exam_hour - DELTA:
    print('Early')
    early = str(exam_hour - arrival_hour)
    hours, mins, _ = early.split(':')
    if int(hours):
        print(f'{hours}:{mins} hours before the start')
    else:
        print(f'{mins} minutes before the start')
else:
    print('On time')
    early = str(exam_hour - arrival_hour)
    hours, mins, _ = early.split(':')

    if int(mins):
        print(f'{mins} minutes before the start')
