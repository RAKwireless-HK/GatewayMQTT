# About RAK
![](https://res.rakwireless.com/tracked/rak/logo/blue-logo-registered-latest.svg)

RAKwireless is a leading player in the global IoT landscape, dedicated to simplifying design and accelerating time-to-market. 
We help everyone who needs IoT.
- System Integrator: Everything they need to build their own IoT solutions, from LoRaWAN® gateways to sensor hub devices and countless sensors.
- Network Provider: They can build an IoT network with RAK’s range of indoor and outdoor gateways.
- Sensor Device maker: They can use the RAK WisDuo Module to make your products compatible with the worldwide LoRaWAN® ecosystem, including networks like Helium and TTN.
- Solution Builder: They can focus on software, while RAK takes care of the IoT connection and so gets to market faster.

We help transform ideas into IoT solutions.
Whether you’re a lone developer or a large business, we have what you need to prototype ideas fast and realistically.

Please visit our website:
- [RAKwireless](https://www.rakwireless.com/)
- [Online Store of RAKwireless](https://store.rakwireless.com/)

This project will share the automation scripts related to the EMSD GWIN project, helping our customers deploy RAK products more efficiently. 

# GatewayMQTT

## About GatewayMQTT
Each RAKwireless Gateway comes with a built-in MQTT server. After a simple configuration, users can forward data from all sensors connected to the Gateway via MQTT to other devices, databases, or services.

GatewayMQTT is a project that provides sample code for RAKwireless users, demonstrating how to retrieve MQTT data from the RAK Gateway WisGate OS2.

## Before GatewayMQTT
Before using the script, login to the Gateway
1) Set up the Application
2) Register the sensor data to the Application
3) Activate the MQTT broker by following the [steps](https://docs.rakwireless.com/Knowledge-Hub/Learn/Use-the-MQTT-Broker-Like-a-Pro/)

## How to use GatewayMQTT
1) Download the project
2) Ensure the computer is still connected to the Gateway.
3) Your computer already installed Python
4) Extra module for pip install, please add below: pip install paho-mqtt pandas
5) Open MQTTtester.py and change the code parameters to ensure those parameters are good for your environment and Run the code. (Enjoy)
