# Description: This file contains the CSV_Controller class which is responsible for writing and appending data to CSV files.
# The CSV_Controller class provides methods to write headers to CSV files and append data to CSV files.

import csv
import os

class CSV_Controller:
    def __init__(self, in_file_path):
        self.file_path = in_file_path

    def write_csv_header(self, file_path, header):
        if not os.path.exists(file_path):
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)

    def append_to_csv(self, file_path, row):
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

    def update_csv_file_Raw(self,current_datetime, msg_topic, message):
        self.write_csv_header(self.file_path, ["datetime", "topic", "message"])
        self.append_to_csv(self.file_path, [current_datetime, msg_topic, message])

    def update_csv_files_processed(self,device_message, current_datetime, timestamp_readable):
            # Write headers if files do not exist
        self.write_csv_header(self.file_path, [
            "datetime",
            "topic",
            "applicationID",
            "applicationName",
            "devEUI",
            "deviceName",
            "timestamp",
            "fCnt",
            "fPort",
            "data",
            "data_encode",
            "adr",
            "rxInfo_gatewayID",
            "rxInfo_loRaSNR",
            "rxInfo_rssi",
            "rxInfo_location_latitude",
            "rxInfo_location_longitude",
            "rxInfo_location_altitude",
            "txInfo_frequency",
            "txInfo_dr"
        ])

        # Append the received message to the CSV files
        self.append_to_csv(self.file_path, [
            current_datetime,
            device_message.topic,
            device_message.applicationID,
            device_message.applicationName,
            device_message.devEUI,
            device_message.deviceName,
            timestamp_readable,
            device_message.fCnt,
            device_message.fPort,
            device_message.data,
            device_message.data_encode,
            device_message.adr,
            device_message.rxInfo_gatewayID,
            device_message.rxInfo_loRaSNR,
            device_message.rxInfo_rssi,
            device_message.rxInfo_location_latitude,
            device_message.rxInfo_location_longitude,
            device_message.rxInfo_location_altitude,
            device_message.txInfo_frequency,
            device_message.txInfo_dr
        ])
