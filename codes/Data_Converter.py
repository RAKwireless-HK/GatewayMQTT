# Description: This file contains the Data_Converter class which is used to convert data from one format to another.
# If the data needs to convert before storing it in a CSV file, the Data_Converter class can be used to convert the data to a readable format. 

import datetime

class Data_Converter:
    def __init__(self):
        return

    def current_time(display_format):
        return datetime.now().strftime(display_format)
    
    def timestamp_readable(timestamp, display_format):
        return datetime.fromtimestamp(timestamp).strftime(display_format)
