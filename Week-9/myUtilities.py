from datetime import datetime, date, time, timedelta
import numpy as np
import random
import matplotlib.pyplot as plt

def get_meeting_dates(period_as_timedelta, time_of_day, number_of_meetings, start_date=datetime.now()):
    if number_of_meetings > period_as_timedelta.days:
        raise ValueError('Too many meetings!')
    
    day_deltas = np.linspace(0, period_as_timedelta.days - 1, number_of_meetings, dtype=int)

    base_time_of_day = datetime.combine(start_date, time_of_day)

    number_of_attendents = []
    list_of_meetings = []
    for day_delta in day_deltas:
        list_of_meetings.append(base_time_of_day + timedelta(int(day_delta)))
        number_of_attendents.append(random.randint(1,15))
    
    plt.bar(list_of_meetings, number_of_attendents, width=0.5, align='center')
    title = 'Distribution of number of attendents for each meeting'
    plt.title(title, fontsize=12)
    plt.xlabel("Meetings", fontsize=10)
    plt.ylabel("Number of attendents", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.show()

    return list_of_meetings

print(get_meeting_dates(timedelta(days=9),time(12,30),4,datetime.now()))
