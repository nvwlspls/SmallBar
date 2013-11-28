import flickrapi 

#not sure if this is needed, imports the xml etree format
import xml.etree.ElementTree as ET

import psycopg2

# f = open('flickr-data-4', 'w') #open file
#create a connection the localhost database 
conn = psycopg2.connect("host=localhost dbname=postgres port=5423 user=wayne password=smallbar")
#create a cursor for the database connection
cur = conn.cursor()

flickr = flickrapi.FlickrAPI('c83487f5d94759be0bcbe9a480be02c8', format='etree')

'''the .walk method does a search through a set of data and 
returns every result.  Normally you need to go through the 
pages, but the flickrapi takes care of this. 
'''
#check to see how  an photos the bbox has and make a smaller box if necesary
#this list will be the set of values that we will use for the bounding box
bboxlist = [[-122.523763, 37.696404, -122.331622, 37.831665]]

for e in bboxlist:
    #half the height of the box 
    h = (abs(e[3] - e[1])* .5) 
    #half the width of the box
    w = (abs(e[0] - e[2])* .5)
    walker = flickr.walk(min_upload_date=2013-01-01,
                         bbox=e[:],
                         accuracy=16,
                         extras='geo,date_taken,tags')
    nophotos = walker.get('photos')
    """this will check the number of photos returned is greate then 10000 and if it is it will 
       draw a smaller box until the number of photos returned is less then 10000
    """
    if nophotos >= 10000:
        nb1 = [e[0] , (e[1] + h) , (e[0] + w) , e[3]]
        bboxlist.append(nb1)
        nb2 = [(e[0] + w) , (e[1] + h) , e[2] , e[3]]
        bboxlist.append(nb2)
        nb3 = [e[0] , e[1] , (e[0]+ w) , (e[1] + h)]
        bboxlist.append(nb3)
        nb4 = [(e[2] - w) , e[1] , e[2] , (e[1] + h)]
        bboxlist.append(nb4)
        bboxlist.pop()


        for photo in walker:
            pid = photo.get('id')
            owner = photo.get('owner')
            try:						
                title = photo.get('title')
            except UnicodeEncodeError:
                title = ("UnicodeEncodeError")
            lat = photo.get('latitude')
            str_lat = str(lat)
            lon = photo.get('longitude')
            str_lon = str(lon)
            placeid = photo.get('place_id')
            woeid = photo.get('woeid')
            try:
                tag = photo.get('tags')
            except UnicodeEncodeError:
                tag = ("Unicode Error")
            date_taken = photo.get('datetaken')
            xy = (str_lon + "," + str_lat )
            cur.execute("INSERT INTO photos VALUES (%(pid)s), %(owner)s, %(title)s, %(lat)s, %(lon)s, %(placeid)s, %(woeid)s, %(tag)s, %(date_taken), %(xy);")
            conn.committ()
            cur.close()
conn.close()