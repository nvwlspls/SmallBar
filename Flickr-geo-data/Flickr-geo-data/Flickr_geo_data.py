import flickrapi 

import xml.etree.ElementTree as ET #not sure if this is needed, imports the xml etree format

f = open('flickr-data-4', 'w') #open file

flickr = flickrapi.FlickrAPI('c83487f5d94759be0bcbe9a480be02c8', format='etree')

'''the .walk method does a search through a set of data and 
returns every result.  Normally you need to go through the 
pages, but the flickrapi takes care of this. 
'''

#this list will be the set of values that we will use for the bounding box
bboxlist = ['-122.523763, 37.696404, -122.331622, 37.831665']


walker = flickr.walk(min_upload_date=2013-01-01,
						 bbox='-122.523763, 37.696404, -122.331622, 37.831665', 
						 accuracy=16, 
						 extras='geo,date_taken,tags')

for e in bboxlist:
    nophotos = e.get('photos')
    if nophotos >= 10000:
           

for photo in walker:
	pid = photo.get('id') #pid = photoid, this gets the XML element labled id from the method above
	pids = str(pid)        #changes the data type of pid into a string
	f.write('"'+ pids + '"' + ';')	   #writes the string and a semi-colon to the file 'f'
	owner = photo.get('owner')
	owners= str(owner)
	f.write('"' + owners + '";')
	try:						#any unicode errors in the title will have Unicodeerror as their title.
		title = photo.get('title')
		titles = str(title)
		f.write('"' + titles + '";')
	except UnicodeEncodeError:
		f.write('"UnicodeEncodeError";')			
	lat = photo.get('latitude')
	lats = str(lat)
	f.write('"' + lats + '";')
	lon = photo.get('longitude') 
	lons = str(lon)
	f.write('"' + lons +'";')
	placeid = photo.get('place_id')
	placeids = str(placeid)
	f.write('"' + placeids + '";')
	woeid = photo.get('woeid')
	woeids = str(woeid)
	f.write('"' + woeids + '";')
	try:				#same as above but with tags
		tag = photo.get('tags')
		tags = str(tag)
		f.write('"'  + tags + '";')
	except UnicodeEncodeError:
		f.write('"UnicodeEncodeError";')	
	date_taken = photo.get('datetaken')
	date_takens = str(date_taken)
	f.write('"' + date_takens + '"\n')   # the \n moves it down to the next line to start the next photo.


f.close()

