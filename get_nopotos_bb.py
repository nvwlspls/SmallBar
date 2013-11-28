import flickrapi

flickr = flickrapi.FlickrAPI('c83487f5d94759be0bcbe9a480be02c8', format='etree')

search = flickr.photos_search(min_upload_date='2013-01-01',
							bbox = '-122.523763, 37.696404, -122.331622, 37.83166',
							accuracy=16,
							extras='geo,date_taken,tags')

total = search.find('photos').attrib['total']
print total , "total photos for bbox"