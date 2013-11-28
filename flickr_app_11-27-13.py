import flickrapi

import xml.etree.ElementTree as ET

import psycopg2


#import geopy

#from geopy.point import Point

#create a connection the localhost database 
#conn = psycopg2.connect(database='flickr_photos', user='wayne', password='smallbar')
#create a cursor for the database connection
#cur = conn.cursor


#boxlist = [[-122.523763, 37.696404, -122.331622, 37.831665]]

flickr = flickrapi.FlickrAPI('c83487f5d94759be0bcbe9a480be02c8', format='etree')

box = '-122.523763, 37.696404, -122.331622, 37.831665'


def get_totals(boundingbox):
    search = flickr.photos_search(min_upload_date='2013-01-01',
                                  bbox=boundingbox,
                                  accuracy=16,
                                  extras='geo,date_taken,tags')
    root = ET.fromstringlist(search, parser=None)
    for child in root:
        print child.tag, child.attrib
    #pages = root.tag
    #total =
    #return pages, total


print get_totals(box)


#get the page total from the xml return
#pages = search.find('photos').attrib['pages']
#print pages , " number of pages for search"
#this will get the total number of phots from the search
#total = search.find('photos').attrib['total']
#print total , " total photos for bbox"
#variable that will be used the track the number of pages
'''
curpage = 1
pages = 0

while curpage <= 5:
    search = flickr.photos_search(min_upload_date='2013-01-01',
                            bbox = '-122.523763, 37.696404, -122.331622, 37.83166',
                            accuracy=16,
                            page = curpage,
                            extras='geo,date_taken,tags',
                            perpage = 250)
    pages = search.find('photos').attrib['pages']
    print pages , " pages"
    total = search.find('photos').attrib['total']
    print total , " total photos for bbox"
    for photo in search:
        pid = photo.find('photo').attrib['id']
        print pid ," id"
        owner = photo.find('photo').attrib['owner']
        try:
            title = photo.find('photo').attrib['title']
        except UnicodeEncodeError:
            title = ("UnicodeEncodeError")
        lat = photo.find('photo').attrib['latitude']
        lon = photo.find('photo').attrib['longitude']
        placeid = photo.find('photo').attrib['place_id']
        print placeid
        woeid = photo.find('photo').attrib['woeid']
        try:
            tag = photo.find('photo').attrib['tags']
        except UnicodeEncodeError:
            tag = ("Unicode Error")
        date_taken = photo.find('photo').attrib['datetaken']
        xy  = geopy.Point(lat,lon)
        #lat,lon,alt = xy
        #print xy , "second"
        #print xy'''
#try:
#	cur.execute("INSERT INTO photos VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (pid, owner, title, lat, lon, placeid, woeid, tag, date_taken, xy))
#conn.commit()
#except (psycopg2.IntegrityError, psycopg2.DataError):
#	errors = errors + 1
#conn.commit()'''
#curpage = curpage + 1






