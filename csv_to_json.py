import csv
import json

###################################################################################################################
# Converts the device inventory csv file to json for used with device operational and configuration check scripts #
###################################################################################################################


ios = []
nxos = []

#Opens .csv and converts to list
with open('device_inventory.csv','r', encoding= 'utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)

    for item in rows:

        del(item['\ufeffHostname'])#Deletes Hostname Fieldname

        if item['device_type'] == 'cisco_ios':
            ios.append(item)

        elif item['device_type'] == 'cisco_nxos':
            nxos.append(item)

        else:
            print('Not Cisco Device it is:',item['device_type'])


with open('device_ios.json', 'w') as f:
    json.dump(ios, f, indent=2)

with open('device_nxos.json', 'w') as f:
    json.dump(nxos, f, indent=2)


print(ios)

print(nxos)










