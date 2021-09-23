#!/bin/bash
temp1=$(sudo i2cget -y 2 0x48 0)
temp2=$(sudo i2cget -y 2 0x4a 0)

final1=$(($temp1 *9/5 +32))
final2=$(($temp2 *9/5 +32))

echo "First sensor: $final1 Second sensor: $final2"