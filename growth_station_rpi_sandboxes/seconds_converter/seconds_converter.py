# This simple script converts seconds into HH:MM:SS format.

try:
    seconds = int(input("Number of seconds: "))
except ValueError as ve:
    seconds = 60
    print("You did not enter an integer. Default value for seconds: " + str(seconds) + ".")
    pass

# TODO: Add the leading 0 to any unit that has 0-9 only
conv_seconds = seconds % 60
conv_minutes = int(seconds / 60) % 60
conv_hours = int(seconds / 3600)

if True:
    print("Conversion to time elapsed for " + str(seconds) + " seconds: " + str(conv_hours) + ":" + str(
        conv_minutes) + ":" + str(conv_seconds))
