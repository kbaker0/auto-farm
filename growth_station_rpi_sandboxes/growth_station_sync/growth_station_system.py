# The growth station system lives here

# This system sends the information from the growth stations to the farmer

import pymysql

# Setting up the databases

# First, we set up the connection to the local host (the growth station)
gs_db = pymysql.connect("localhost", "cosc497", "EnvS#310", "envdb")
gs_cursor = gs_db.cursor()

# Change the number of the growth station to match the right Raspberry Pi
gs_number = 1

# Then, we set up the connection to the farmer (room's server)
farmer_ip = "localhost"
farmer_db = pymysql.connect(farmer_ip, "cosc497", "EnvS#310", "farmdb")
farmer_cursor = farmer_db.cursor()

# Testing the connection to the growth station
# gs_cursor.execute("SELECT VERSION()")
# data = gs_cursor.fetchone()
# print("Database version : %s " % data)
# print("Getting data from each station")

# Testing the connection to the farmer
# farmer_cursor.execute("SELECT VERSION()")
# data = farmer_cursor.fetchone()
# print("Database version : %s " % data)
# print("Getting data from each station")

# Getting all the data from the growth station database that has not yet been updated
query = "SELECT id, source, value, tstamp FROM readings WHERE backup = 0;"
gs_cursor.execute(query)
data = gs_cursor.fetchall()
id_list = []

for d in data:
    # Reading each record into different attributes
    record_id = str(d[0])
    record_source = d[1]
    record_value = str(float(d[2]))
    record_timestamp = str(d[3])
    # print(d)

    # Sending the record to the farmer
    farmer_query = "INSERT INTO sensor_readings (gstation_id, reading_id, source, value, tstamp_ori) VALUES "
    farmer_query += "(" + str(gs_number) + ", " + record_id + ", '" + record_source + "', " + record_value
    farmer_query += ", '" + record_timestamp + "')"
    # print(farmer_query)
    farmer_cursor.execute(farmer_query)

    # Adding the ID to the list of ids that will have to be updated as transfered
    id_list.append(record_id)

farmer_db.commit()

# Use the list of IDs to set the flag for backup to true
# UPDATE readings SET backup = 1 WHERE id = (the ID stored in the list)
# print("List of IDs")
for id in id_list:
    # Updating the record in the growth station's DB
    update_query = "UPDATE readings SET backup = 1 WHERE id = " + id
    # print("Update Query: " + update_query)
    gs_cursor.execute(update_query)

gs_db.commit()

gs_db.close()
farmer_db.close()
