import csv
import json

###################################################################################################################
# Converts the device inventory csv file to json for used with device operational and configuration check scripts #
###################################################################################################################





#Opens .csv and converts to list
with open('Keider_Device_Converter_json.csv','r', encoding= 'utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)

    for item in rows:

        del(item['\ufeffHostname'])#Deletes Hostname Fieldname
        print(item)



with open('customer_device.json', 'w') as f:
    json.dump(rows, f, indent=2)




















