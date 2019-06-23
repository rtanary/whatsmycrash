import serial
import time
import json 

data = serial.Serial('COM5')
data.flushInput()
data_dump = {}
data_dump['collision'] = []
isNotCollision = True
count = 0

accel_raw = data.readline()
accel_val = accel_raw[0:len(accel_raw)-2].decode("UTF-8")
while accel_val == '9':
	accel_raw = data.readline()
	accel_val = accel_raw[0:len(accel_raw)-2].decode("UTF-8")

while accel_val != '9':
	accel_raw = data.readline()
	accel_val = accel_raw[0:len(accel_raw)-2].decode("UTF-8")
	print(accel_val)

	data_dump["collision"].append({
			"timestamp":int(time.time()),
			"acceleration": accel_val, 
			"result": 1
		})

print(data_dump)
with open('data.json',mode='w',encoding='utf-8') as outfile:
	json.dump(data_dump,outfile,skipkeys=False, ensure_ascii=True)
