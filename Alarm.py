# import necessary libraries
import time
# for producing sound
import winsound as ws


# define a function for alarm
def alarm():
    try:
        # Give the frequency of your alarm
        frequency = int(input("Enter the frequency of your alarm in Hz (3500 recommended): "))

        # Give the duration of your alarm
        duration = int(
            input("Enter the duration in milliseconds (ms) for which you want the alarm to ring (2000 recommended) : "))

        # Input time from the user
        time_gap = list(
            map(int, input("Enter time in hh mm ss format after which you want the alarm to ring: ").split()))

        # If format is correct
        if len(time_gap) == 3:
            # Convert the time entered in hh mm ss format to seconds
            time_in_secs = time_gap[0] * 60 * 60 + time_gap[1] * 60 + time_gap[2]

            # Nothing will happen for the input number of seconds
            time.sleep(time_in_secs)

            # The function which produces beep sound of given frequency and duration
            ws.Beep(frequency, duration)

        # If format is incorrect
        else:
            print("Enter time in correct format!!!")
            alarm()
    except Exception as e:
        print("This is an exception\n", e, "Please enter correct details!!!")
        alarm()


alarm()
