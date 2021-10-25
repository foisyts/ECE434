#! /bin/bash

echo Temperature Readings! Exit using ctrl+c
cd /sys/class/i2c-adapter/i2c-1/1-0048/hwmon/hwmon0
while true; do
    cat temp1_input | tr -s '\n\r'
    echo "*10^-3 C"
done