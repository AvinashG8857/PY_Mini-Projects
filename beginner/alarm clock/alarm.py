import time

print("||||| Alarm clock |||||".upper())
alarm_time= input("Enter the alarm time (HH:MM in 24 hrs format) : ")

while True:
    current_time = time.strftime("%H:%M")
    if current_time == alarm_time:
        print("Wake UP buddy !!")
        break
    time.sleep(30)