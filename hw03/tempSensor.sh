#!/bin/bash

# Pulls from i2c bus for both tmp101 sensors (2 addresses)
temp1=$(sudo i2cget -y 2 0x48 0)
temp2=$(sudo i2cget -y 2 0x4a 0)

# Conversion to Farenheit and printing
final1=$(($temp1 *9/5 +32))
final2=$(($temp2 *9/5 +32))
echo "First sensor: $final1 Second sensor: $final2"