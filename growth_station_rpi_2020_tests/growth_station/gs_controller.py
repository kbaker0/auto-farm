import datetime
import time
import json

# Global variables
protocol_id = "---"
growth_station_id = "---"

# Directories
logs_dir = "../logs/"

# TODO
def load_settings():
    global protocol_id, growth_station_id
    output_log("Loading the Settings file...")

    # TODO: Check if the settings file has been updated.
    # https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python
    # http://www.learningaboutelectronics.com/Articles/How-to-get-the-last-modified-date-of-a-file-in-Python.php
    # https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file

    try:
        with open('gs_settings.json') as json_settings_file:
            settings = json.load(json_settings_file)
            # print(settings)
            my_cicle = settings['growth_cycle']
            protocol_id = settings['protocol_id']
            growth_station_id = settings['growth_station_id']
            # print("Time off: " + my_cicle['time_off'])
            # print("Time on: " + my_cicle['time_on'])
            # print("Light color: " + my_cicle['led_color'])
        output_log("Load complete.")
        return True
    except:
        output_log("An error occurred loading the settings file.")
        return False

# TODO
def check_serial_connection():
    print("Make sure the Arduino is connected")
    # https://pyserial.readthedocs.io/en/latest/pyserial_api.html
    # Look into timeouts, in case the peripheral is not responding

    # IMPORTANT: Have this method send something to the Arduino. If the
    # device is "compatible" with this system, it will respond in a
    # particular way (ex: send 'n', receive '(n*n)-n')
    # Send "cityFolks" and expect "justDontGetIt" as a response

    # https://pyserial.readthedocs.io/en/latest/pyserial_api.html

    # Show the list of USB devices
    # ls /dev/ttyACM*
    # https://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/

# TODO
def test_lights():
    print("Testing the lights")
    print("Red")
    time.sleep(1)
    print("Green")
    time.sleep(1)
    print("Blue")
    time.sleep(1)
    print("White")
    time.sleep(1)
    print("Lights off")

# TODO
def setup_database():
    print("Create DB if it does not exist")
    print("Protocol: " + protocol_id)
    print("Growth Station ID: " + growth_station_id)

# Possibly ready...
def output_log(msg):
    tstamp = datetime.datetime.now()
    logfilename = logs_dir + str(tstamp.date()) + ".log"

    logfile = open(logfilename, "a")
    logfile.write(str(tstamp) + " | " + str(msg) + "\n")
    logfile.close()

# Working...
def main():
    output_log("Starting up...")
    # Wait some time to make sure the system gets an accurate timestamp?
    run_ok = load_settings()

    if run_ok:
        check_serial_connection()
        test_lights()
        setup_database()
        # The rest goes in a loop that executes every so often (1 min?)
        # Each time, check for the serial connection
    else:
        print("Something is not right. Check the log file.")

if __name__ == "__main__":
    main()
