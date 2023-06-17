def add_time(start, duration, day = False):
    day_passed = 0
    day_str = ''
    meridiem = 'AM'

    weak = {
        "Monday":1,
        "Tuesday":2,
        "Wednesday":3,
        "Thursday":4,
        "Friday":5,
        "Saturday":6,
        "Sunday":7,
    }

    start_time = [int(start.split(":")[0]),int(start.split(":")[-1].split(" ")[0]),start.split(" ")[-1]]
    time_duration = [int(duration.split(":")[0]),int(duration.split(":")[-1])]

    #changing to 24 hour
    if start_time[-1] == 'PM':
        start_time[0] +=12
        start_time.pop(-1)

    else:
        start_time.pop(-1)

    total_min = start_time[1]+time_duration[1]
    total_hour = start_time[0]+time_duration[0]

    if total_min >= 60:
        total_hour += int(total_min/60)
        total_min = total_min - 60
    
    if total_hour >= 24:
        day_passed += int(total_hour/24)
        total_hour = total_hour - (24*int(total_hour/24))
        
    if day:
        day_no = weak[day.capitalize()]
        day_no +=day_passed

        if day_passed == 0:
            day_str = ", "+day
        
        else:
            if day_no > 7:
                day_no = day_no - (7*int(day_no/7))
            for key, value in weak.items():
                if day_no == value:
                    day_str = ", "+key

    
    if day_passed == 1:
        day_str += ' (next day)'
    elif day_passed >1:
        day_str += f" ({day_passed} days later)"
    
    if total_hour ==12:
        meridiem = 'PM'

    elif total_hour == 0:
        total_hour = 12

    elif total_hour > 12:
        total_hour = total_hour - 12
        meridiem = 'PM'

    return f"{total_hour:02}:{total_min:02} {meridiem}{day_str}"
