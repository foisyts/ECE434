#!/usr/bin/env python3
import smbus

# Setup for the bus and the 2 addresses where i2c tmp101 sensors are found
bus= smbus.SMBus(2)
addrOne = 0x48
addrTwo = 0x4a

# reading i2c bus
tempOne = bus.read_byte_data(addrOne, 0)
tempTwo = bus.read_byte_data(addrTwo, 0)

# conversion to Farenheit and printing
valOne = tempOne*9/5 +32
valTwo = tempTwo*9/5 +32
print("First sensor: " + str(valOne) + " Second sensor: " + str(valTwo))
