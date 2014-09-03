
# Filename: try_pycap_ver1.py

# Import PyCap module

from redcap import Project, RedcapError

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



print familyData[0]
print srsData[0]

#iterate the records



