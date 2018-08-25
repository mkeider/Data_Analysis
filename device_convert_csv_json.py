import csv
import json

###################################################################################################################
# Converts the device inventory csv file to json for used with device operational and configuration check scripts #
###################################################################################################################


#Opens .csv and converts to list
with open('Keider_Device_Converter_json.csv','r') as new_file:
    reader = csv.DictReader(new_file)
    rows = list(reader)


#Write 'customer_device.json" file to json format
with open('customer_device.json','w') as device_file:
    json.dump(rows, device_file, indent=2)

#Opens same json file to create DATA varialble
with open('customer_device.json','r') as f:
    data = json.load(f)


#Cleans data by removing the 'Hostname" key with is not required
for element in data:
    element.pop('\u00ef\u00bb\u00bfHostname',None)


#Saved cleaned data in 'customer_device.json' file#
with open('customer_device.json','w')as f:
    data = json.dump(data, f, indent=2)






