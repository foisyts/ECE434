#!/usr/bin/env python3
import smbus

bus= smbus.SMBus(2)
addrOne = 0x48
addrTwo = 0x4a

tempOne = bus.read_byte_data(addrOne, 0)
tempTwo = bus.read_byte_data(addrTwo, 0)
valOne = tempOne*9/5 +32
valTwo = tempTwo*9/5 +32

print("First sensor: " + str(valOne) + " Second sensor: " + str(valTwo))
