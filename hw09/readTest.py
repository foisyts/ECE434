#!/usr/bin/python3
import os 

sensor1 = os.open("/sys/class/hwmon/hwmon0/temp1_input", os.O_RDONLY);
temp1 = os.read(sensor1, 6);
temp1 = temp1.decode("utf-8");
temp1 = int(temp1)/1000;

sensor2 = os.open("/sys/class/hwmon/hwmon1/temp1_input", os.O_RDONLY);
temp2 = os.read(sensor2, 6);
temp2 = temp2.decode("utf-8");
temp2 = int(temp2)/1000;

sensor3 = os.open("/sys/class/hwmon/hwmon2/temp1_input", os.O_RDONLY);
temp3 = os.read(sensor3, 6);
temp3 = temp3.decode("utf-8");
temp3 = int(temp3)/1000;

print(temp1, temp2, temp3)