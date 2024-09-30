# Description: This file contains the class definition for DeviceMessage
# The DeviceMessage class is used to store the details of a message received from a device via MQTT
# The class provides a method to create an instance of the class from a dictionary

class DeviceMessage:
    def __init__(self, topic, applicationID, applicationName, devEUI, deviceName, timestamp, fCnt, fPort, data, data_encode, adr, rxInfo, txInfo):
        self.topic = topic
        self.applicationID = applicationID
        self.applicationName = applicationName
        self.devEUI = devEUI
        self.deviceName = deviceName
        self.timestamp = timestamp
        self.fCnt = fCnt
        self.fPort = fPort
        self.data = data
        self.data_encode = data_encode
        self.adr = adr
        self.rxInfo = rxInfo
        self.txInfo = txInfo

        # Extract rxInfo details
        if rxInfo and len(rxInfo) > 0:
            self.rxInfo_gatewayID = rxInfo[0].get("gatewayID")
            self.rxInfo_loRaSNR = rxInfo[0].get("loRaSNR")
            self.rxInfo_rssi = rxInfo[0].get("rssi")
            self.rxInfo_location_latitude = rxInfo[0].get("location", {}).get("latitude")
            self.rxInfo_location_longitude = rxInfo[0].get("location", {}).get("longitude")
            self.rxInfo_location_altitude = rxInfo[0].get("location", {}).get("altitude")
        else:
            self.rxInfo_gatewayID = None
            self.rxInfo_loRaSNR = None
            self.rxInfo_rssi = None
            self.rxInfo_location_latitude = None
            self.rxInfo_location_longitude = None
            self.rxInfo_location_altitude = None

        # Extract txInfo details
        self.txInfo_frequency = txInfo.get("frequency")
        self.txInfo_dr = txInfo.get("dr")

    @classmethod
    def from_dict(cls, topic, data):
        try:
            return cls(
                topic=topic,
                applicationID=data.get("applicationID"),
                applicationName=data.get("applicationName"),
                devEUI=data.get("devEUI"),
                deviceName=data.get("deviceName"),
                timestamp=data.get("timestamp"),
                fCnt=data.get("fCnt"),
                fPort=data.get("fPort"),
                data=data.get("data"),
                data_encode=data.get("data_encode"),
                adr=data.get("adr"),
                rxInfo=data.get("rxInfo"),
                txInfo=data.get("txInfo")
            )
        except KeyError as e:
            raise ValueError(f"Missing required field in data: {e}")

