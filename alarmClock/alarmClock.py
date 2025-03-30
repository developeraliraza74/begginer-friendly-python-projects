# from datetime import datetime
# from playsound import playsound
# flag = False
# alarm_time = input("Enter Time for Alarm (hh mm ss period): ")
# # alarm_time = ""
# alarm_hour = alarm_time[0:2]
# alarm_min = alarm_time[3:5]
# alarm_sec = alarm_time[6:8]
# alarm_period = alarm_time[9:11].upper()

# if(current_hour >= 0 and current_hour <= 12):
#     if(current_min >= 0 and current_min <= 60):
#         if(current_sec >= 0 and current_sec <= 60):
#             if(current_period == "AM" or current_period == "PM"):
#                 flag = True
# else:
#     print("Wrong Creditionals! Follow this format : HH:MM:SS:#M")


# print("Setting alarm Up....")

# while True:
#     now = datetime.now()
#     current_hour = now.strftime("%I")
#     current_min = now.strftime("%M")
#     current_sec = now.strftime("%S")
#     current_period = now.strftime("%p")
#     if(alarm_period == current_period):
#         if(alarm_hour == current_hour):
#             if(alarm_min == current_min):
#                 if(alarm_sec == current_sec):
#                     print("Wake Up!")
#                     playsound('clock.mp3')
#                     break
  



# Upgraded way

from datetime import datetime
from playsound import playsound

flag = False
alarm_time = input("Enter Time for Alarm (hh mm ss period): ")

# Split input time into hour, minute, second, and period
try:
    alarm_hour, alarm_min, alarm_sec, alarm_period = alarm_time.split()
    alarm_hour = int(alarm_hour)
    alarm_min = int(alarm_min)
    alarm_sec = int(alarm_sec)
    alarm_period = alarm_period.upper()
except ValueError:
    print("Invalid format! Please enter time in 'hh mm ss AM/PM' format.")
    exit(1)

# Validate alarm time range
if not (1 <= alarm_hour <= 12 and 0 <= alarm_min < 60 and 0 <= alarm_sec < 60 and alarm_period in ["AM", "PM"]):
    print("Wrong Credentials! Follow this format: HH MM SS AM/PM")
    exit(1)

print("Setting alarm Up....")

while True:
    # Get current time
    now = datetime.now()
    current_hour = int(now.strftime("%I"))  # Hour in 12-hour format (integer)
    current_min = int(now.strftime("%M"))  # Minute (integer)
    current_sec = int(now.strftime("%S"))  # Second (integer)
    current_period = now.strftime("%p").upper()  # AM or PM

    # Check if current time matches the alarm time
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Wake Up!")
                    playsound('clock.mp3')  # Replace 'clock.mp3' with the correct file path
                    break


