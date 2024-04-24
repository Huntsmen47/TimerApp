import time
import pygame

def countdown_timer(seconds):
    while seconds > 0:
	    hours = seconds/3600
	    minutes = seconds/60
	    rounded_min = round(minutes,2)
	    rounded_hour = round(hours,2)
	    if hours >= 1:
	    	print("Time remaining:",rounded_hour,"hours",rounded_min,"minutes", seconds, "seconds")
	    elif minutes >= 1:
	    	print("Time remaining:",rounded_min,"minutes", seconds, "seconds")
	    else:
	    	print("Time remaining:",seconds, "seconds")
	    time.sleep(1)
	    seconds -= 1

def start_timer():
    hours = int(input("Enter hours: ")) 
    mins = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    hour_sec = 3600*hours
    min_sec = 60*mins
    total = min_sec + seconds + hour_sec
    try:
    	countdown_timer(total)
    except KeyboardInterrupt:
    	print(f"You started with {hours} hours, {mins} mins, and {seconds} seconds.")
    print("Timer finished!")
    pygame.mixer.init()
    pygame.mixer.music.load("Documents/TimerApp/Timer/beep.mp3")
    pygame.mixer.music.play()

# Main program loop
while True:
    print("\nSelect an option:")
    print("1. Start Timer")
    print("2. Exit")
    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        start_timer()
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please try again.")

