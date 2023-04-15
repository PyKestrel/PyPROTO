#! /usr/bin/env python
'''
The Cisco Discovery Protocol (CDP) is a proprietary protocol developed by Cisco Systems that runs on Cisco devices such as routers, switches, and bridges.
It allows these devices to share information about their presence, capabilities, and status with other devices on the same network.

CDP can discover other Cisco devices directly connected to the network and gather information about their interfaces, including the device type, IOS software version, IP address, and subnet mask. 
This information can be useful for network administrators in managing the network and troubleshooting issues.

CDP runs by default on all Cisco devices and can be enabled or disabled on a per-interface basis. 
It operates at the data link layer of the OSI model and uses multicast addresses to send and receive CDP packets.


Version: 1.0
Authors: 
    Ariel Torres (PyKestrel)

'''

import socket
import sys
import struct

# Type-Length-Value (TLV) Definitions

# This refers to information that includes the network addresses of both the sender and the receiver devices.
TLV_DEST_ADDR = ""

TLV_SEND_ADDR = ""

# It pertains to a method for transmitting an application-specific type-length-value (TLV) via the Cisco Discovery Protocol.
TLV_APPLICATION = ""

# This refers to a feature that identifies the type of device, indicating its functional capabilities, such as being a switch, router, or other type of network device.
TLV_CAPABILITIES = ""

# This pertains to a feature that identifies the name of a device using a string of characters.
TLV_DEVID = ""

# This refers to a feature that shows the duplex configuration of the Cisco Discovery Protocol broadcast interface.
TLV_DUPLEX = ""

# This pertains to information that includes a list of network prefixes to which a sending device can forward IP packets.
# Each prefix in the list includes the interface protocol and the port number, such as Ethernet 1/0.
TLV_INET_PREFIX = ""

# This refers to a process that delivers location-based information to endpoint devices by utilizing access devices, such as switches or routers, and the Cisco Discovery Protocol.
TLV_LOCATION = ""

# This pertains to a method that enables location servers to transfer necessary information to adjacent devices.
TLV_LOCATION_SRV = ""

# This refers to a feature that specifies, for each interface, the assumed VLAN for untagged packets on that interface.
TLV_NATIVE_VLAN = ""

# This pertains to a feature that identifies the hardware platform of a device.
TLV_PLATFORM = ""

# This refers to a feature that identifies the port through which a Cisco Discovery Protocol packet is transmitted.
TLV_PORTID = ""

# This pertains to the release details of the device's software.
TLV_VERSION = ""

# This refers to an information block that broadcasts the configured VLAN Trunking Protocol (VTP) management domain name of the system.
TLV_VTP = ""

'''
Checking for OS Platform

This will help us when trying to get interface information.
'''

print(sys.platform)
n = 0
for interface in socket.if_nameindex():
    print(f'[%s] ' % n + interface[1])
    n += 1
chosenint = input("Select Interface From Above List (Ex. 0): ")


# Building CDP Frame Format
# Ethernet Format
DEST_ADDR = b'\x01\x00\x0C\xCC\xCC\xCC'
SEND_ADDR = b''

# LLC Format
DSAP = b'\xAA'
SSAP = b'\xAA'
CTRL = b'\x03'
OUI = b'\x00\x00\x0C'
PID = b'\x20\x00'

# CDP Format
DEVICE_ID = b'\x00\x01'
ADDRESSES = b'\x00\x02'
PORT_ID = b'\x00\x03'
CAPABILITIES = b'\x00\x04'
SOFTWARE_VERSION = b'\x00\x05'
PLATFORM = b'\x00\x06'
PROTOCOL_HELO = b'\x00\x08'
VTP_MANAGEMENT_DOMAIN = b'\x00\x09'
TRUST_BITMAP = b'\x00\x12'
UNTRUSTED_PORT_COS = b'\x00\x13'
MANAGEMENT_ADDRESSES = b'\x00\x16'
NATIVE_VLAN = b'\x00\x0a'
DUPLEX = b'\x00\x0b'
POWER_AVAILABLE = b'\x00\x1a'

# Get System Type & Build Socket Object Accordingly

if (sys.platform == "win32"):
    # Building the Raw Socket Object
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
elif (sys.platform == "Linux"):
    # Building the Raw Socket Object
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
else:
    print("Unsupported Operating System")
    sys.exit()
# Binding the Socket
s.bind()


# Close Socket
s.close()
