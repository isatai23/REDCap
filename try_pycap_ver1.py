
# Filename: try_pycap_ver1.py

# Import PyCap module

from redcap import Project, RedcapError
import csv

# Define the URL of our REDCap installation and the token of the project we are requesting a response.

URL = 'https://poa-redcap.med.yale.edu/api/'
TOKEN = '0BD89F3E896E72920DF3CFAC8DD739D7'
TOKEN2 = 'CAF3713EF2307C80BAD789DBAFBAA8C7'
# Call PyCap Project function

family = Project(URL, TOKEN)
srs = Project(URL, TOKEN2)


# Get the metatdata of the project

#metadata = family.export_metadata()
#metadata2 = srs.export_metadata()


#for field in metadata:
#	print "%s (%s) ---> %s" % (field['field_name'], field['field_type'], field['field_label'])



#for field in metadata2:
#	print "%s (%s) ---> %s" % (field['field_name'], field['field_type'], field['field_label'])

# Get the data of the project

family_fields_intrst = ['individual_id', 'sex']
srs_fields_intrst = ['individual_id', 'srs2_tscore']

familyData = family.export_records(fields = family_fields_intrst)
srsData = srs.export_records(fields = srs_fields_intrst)
print "The first project has %d records" % len(familyData)
print "The second project has %d records" % len(srsData)

def csv_writer(data, path):
    '''
    
    Write data to a CSV file path.
    '''
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
            
            
'''iterate the records

The output of export_records is a list of dictionaries

for each dictionary in familyData list
    for each dictionary in srsData list
        if family individual id == srs individual id
            if sex = male
                print individual id, sex, srs2 total T score'''
data = [['individual_id','sex','individual_id','srs2_tscore']]
for i in range(0, len(familyData)):
    for j in range(0, len(srsData)):
        if familyData[i]['individual_id'] == srsData[j]['record_id']:
            if familyData[i]['sex'] == '0':
                new_data=[ familyData[i]['individual_id'], familyData[i]['sex'], srsData[j]['record_id'], srsData[j]['srs2_tscore']]
                data.append(new_data)
                
            
path  = "query_output.csv"
csv_writer(data, path)
         
           
    






