
import flickrapi 

import xml.etree.ElementTree as ET

import psycopg2

#create a connection the localhost database 
conn = psycopg2.connect(database='flickr_photos', user='wayne', password='smallbar')
#create a cursor for the database connection
cur = conn.cursor()

blist = [[-122.523763, 37.696404, -122.331622, 37.831665]]

flickr = flickrapi.FlickrAPI('c83487f5d94759be0bcbe9a480be02c8', format='etree')
def get_small_boxes (bboxlist):
    smallboxes = []
    for e in bboxlist:
        currentbox = str(e).strip("[]")
        #print str(currentbox + "current box")
        #half the height of the box
        h = (abs(e[3] - e[1])*.5)
        #half the width of the box
        w = (abs(e[0] - e[2])*.5)
        search = flickr.photos_search(min_upload_date=2013-01-01,
                             bbox=currentbox,
                             accuracy=16,
                             extras='geo,date_taken,tags')
    
        #.attrib['stat'] => 'ok'
        #print (nophotos + "total")
        search.attrib['stat'] = 'ok'
        total = search.find('photos').attrib['total']
        print total + " total"
        nophotos = int(float(total))
        #check = nophotos/100
        #print check
        #this will check the number of photos returned is greater then 10000 and if it is it will
        #draw a smaller box until the number of photos returned is less then 10000
        if nophotos >4000:
            print "Too many photos in box"
            new_lat = e[1] + h
            new_lon = e[0] + w
            nb1 = [e[0] , new_lat , new_lon, e[3]]
            bboxlist.append(nb1)            
            nb2 = [new_lon, new_lat, e[2], e[3]]
            bboxlist.append(nb2)
            nb3 = [e[0], e[1], new_lon, new_lat]
            bboxlist.append(nb3)
            nb4 = [new_lon, e[1], e[2], new_lat]
            bboxlist.append(nb4)
            bboxlist.pop(0)
        else:
            print "This box is small enough"
            smallboxes.append(e) 
            bboxlist.pop(0)
        #print ('smallboxes' , smallboxes)
        return smallboxes

newboxlist = get_small_boxes(blist)

for e in newboxlist:
    errors = 0
    currentbox= str(e).strip("[]")
    results = flick.photos_search(min_upload_date=2013-01-01,
                             bbox=currentbox,
                             accuracy=16,
                             extras='geo,date_taken,tags')
        search.attrib['stat'] = 'ok'
        total = search.find('photos').attrib['total']    


    
   


      
cur.close()
conn.close()


#print get_small_boxes(bboxlist)
#(photo_id, photo_owner, photo_title, photo_lat, photo_long, photo_place_id, photo_woe_id, photo_tags, photo_date_taken, xy)
