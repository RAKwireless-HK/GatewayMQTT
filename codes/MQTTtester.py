"""
######################################################################################################################################
#
#    Description: This sample script is used to subscribe to the MQTT broker and receive messages from the RAKwireless Gateway.
#    Subscribed MQTT messages are then processed and stored in a CSV file.
#    Before you use the script below, login to the Gateway
#        1) Set up the Application
#        2) Register the sensor data to the Application
#        3) Activate the MQTT broker
#
#    Also configure the below parameters in the script in the section Constants, change these to match your setup
#
######################################################################################################################################
"""

# pip install paho-mqtt pandas

import json
import paho.mqtt.client as mqtt
from datetime import datetime
from CSV_Controller import CSV_Controller
from DeviceMessage import DeviceMessage
from Data_Converter import Data_Converter
import logging

# ------------ Constants, change these to match your setup ------------ 
IP_ADDRESS = "192.168.230.1" # IP address of the MQTT broker, RAKwireless Gateway IP address is 192.168.230.1 by default if using WiFi Connection
PORT = 1883 # Port number of the MQTT broker, which is 1883 by default for the RAKwireless Gateway
FREQUENCY_TO_GET_DATA = 60 # Frequency in seconds to get the data from the MQTT broker, 60 seconds 
APP_ID = "SENSO_LRS_TEST" # Application ID that you have set up in the Gateway for the sensor data, check the Application ID in the RAKwireless Gateway
DEV_EUI_LIST = ["70b3d58c90002c25", "70b3d58c90002c14"] # List of Device EUIs that you have registered in the Application, check the Device EUI in the RAKwireless Gateway
TIME_FORMAT = "%d-%m-%Y %H:%M:%S" # Format of the date and time, "DD-MM-YYYY HH:MM:SS"
PROCESSED_FILE_PATH = 'D:\\WORK\\PROCESSED_Result_V02.csv' # The path where the processed data is stored in the CSV file
RAW_FILE_PATH = 'D:\\WORK\\RAW_Result_V02.csv' # The path where the raw data is stored in the CSV file
LOG_FILE_PATH = 'D:\\WORK\\MQTT_LOG.txt' # The path where the log file is stored
# --------------------------------------------------------------------

# Setup logging, to log messages to a file
logging.basicConfig(level=logging.INFO, filename= LOG_FILE_PATH , filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create a list of topics to subscribe to by combining the application ID and device EUI, for both uplink and downlink messages
# For example, the topic for uplink messages from device with EUI 70b3d58c90002c25 in application SENSO_LRS_TEST is "application/SENSO_LRS_TEST/device/70b3d58c90002c25/rx"
# and the topic for downlink messages to the same device is "application/SENSO_LRS_TEST/device/70b3d58c90002c25/tx"
def get_topic_list(app_id, dev_eui_list):
    return [f"application/{app_id}/device/{dev_eui}/rx" for dev_eui in dev_eui_list] + \
           [f"application/{app_id}/device/{dev_eui}/tx" for dev_eui in dev_eui_list]

# Callback for when the client receives a connection response
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker!")
        logger.info("Connected to MQTT broker!")
        topics = get_topic_list(APP_ID, DEV_EUI_LIST)
        for topic in topics:
            client.subscribe(topic)
            print(f"Subscribed to {topic}")
            logger.info(f"Subscribed to {topic}")
    else:
        print(f"Failed to connect, return code {rc}")
        logger.error(f"Failed to connect, return code {rc}")

# Callback for when a message is received from the MQTT broker
def on_message(client, userdata, msg):
    try:
        message = msg.payload.decode("utf-8")  # Decode the message payload
        logger.info(f"Received message: '{message}' on topic: '{msg.topic}'")
        print(f"Received message: '{message}' on topic: '{msg.topic}'")
        
        # Parse the message as JSON
        data = json.loads(message)
        
        # Create a DeviceMessage object
        device_message = DeviceMessage.from_dict(msg.topic, data)

        # Convert the data to a readable format before store it in a CSV file
        Data_Converter = Data_Converter()
        # Get the current date and time
        current_datetime = Data_Converter.current_time(TIME_FORMAT)
        # Convert the timestamp to a readable format
        timestamp_readable = Data_Converter.timestamp_readable(device_message.timestamp, TIME_FORMAT)

        # Create instances of the CSV_Controller class for the raw and processed CSV files
        # Update the raw CSV file with the received message
        raw_CSV = CSV_Controller(RAW_FILE_PATH)
        # Update the processed CSV file with the received message
        processed_CSV = CSV_Controller(PROCESSED_FILE_PATH)
        # Update the raw and processed CSV files with the received message
        raw_CSV.update_csv_file_Raw(current_datetime, msg.topic, message)
        # Update the processed CSV file with the received message
        processed_CSV.update_csv_files_processed(device_message, current_datetime, timestamp_readable)
    except json.JSONDecodeError as e:
        logger.error(f"Failed to decode JSON message: {e}")
        print(f"Failed to decode JSON message: {e}")
    except ValueError as e:
        logger.error(f"Error processing message: {e}")
        print(f"Error processing message: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")


# Create a new MQTT client instance
client = mqtt.Client()

# Assign event callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(IP_ADDRESS, PORT, FREQUENCY_TO_GET_DATA)

# Blocking loop to process network traffic and dispatch callbacks
client.loop_forever()
