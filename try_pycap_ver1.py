#!/usr/bin/python
# Filename: try_pycap_ver1.py

# Import PyCap module

from redcap import Project, RedcapError

# Define the URL of our REDCap installation and the token of the project we are requesting a response.

URL = 'https://poa-redcap.med.yale.edu/api/'
TOKEN = '0BD89F3E896E72920DF3CFAC8DD739D7'

TOKEN2 = 'CAF3713EF2307C80BAD789DBAFBAA8C7'
# Call PyCap Project function

project = Project(URL, TOKEN)
project2 = Project(URL, TOKEN2)
#project2 = Project(URL, TOKEN2)

# Get the metatdata of the project

metadata = project.export_metadata()
metadata2 = project2.export_metadata()
#metatdata2 = project2.export_metadata()

for field in metadata:
	print "%s (%s) ---> %s" % (field['field_name'], field['field_type'], field['field_label'])


#project2 = Project(URL, TOKEN2)
#metadata2 = project2.export_metadata()
for field in metadata2:
	print "%s (%s) ---> %s" % (field['field_name'], field['field_type'], field['field_label'])

# Get the data of the project

data = project.export_records()
data2 = project2.export_records()
print "The first project has %d records" % len(data)
print "The second project has %d records" % len(data2)
#print "Each record has the following keys: %s." % ', '.join(data[0].keys())


print

#print "But our metadata structure has the following fields: %s!" % ','.join(field['field_name'] for field in metadata)
print


