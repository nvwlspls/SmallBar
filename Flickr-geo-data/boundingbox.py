import flickrapi 

#not sure if this is needed, imports the xml etree format
import xml.etree.ElementTree as ET

bboxlist = [[-122.523763, 37.696404, -122.331622, 37.831665]]

for e in bboxlist:
    #half the height of the box 
    h = (abs(e[3] - e[1])* .5) 
    #half the width of the box
    w = (abs(e[0] - e[2])* .5)
    walker = flickr.photos_search(min_upload_date=2013-01-01,
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
print bboxlist