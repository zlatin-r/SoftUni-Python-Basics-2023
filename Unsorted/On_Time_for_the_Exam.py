hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

exam_all_minutes = (hour_exam * 60) + minute_exam

arrival_all_minutes = (hour_arrival * 60) + minute_arrival

diff = abs(exam_all_minutes - arrival_all_minutes)

if arrival_all_minutes > exam_all_minutes:
    print("Late")

    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hour = diff // 60
        minutes = diff % 60

        if minutes < 10:
            print(f"{hour}:0{minutes} hours after the start")
        else:
            print(f"{hour}:{minutes} hours after the start")

elif arrival_all_minutes == exam_all_minutes or diff <= 30:
    print("On time")

    if 1 <= diff <= 30:
        print(f"{diff} minutes before the start")
else:
    print("Early")
    if diff < 60:
        print(f"{diff} minutes before the start")
    else:
        hour = diff // 60
        minutes = diff % 60
        if minutes < 10:
            print(f"{hour}:0{minutes} hours before the start")
        else:
            print(f"{hour}:{minutes} hours before the start")