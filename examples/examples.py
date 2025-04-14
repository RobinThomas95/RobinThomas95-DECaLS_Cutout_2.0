from astropy.coordinates import SkyCoord
from decals.query import decals_cutout

dc=decals_cutout(output_dir="/your/path/for/saving/downloaded/data")  #Defining the path to save downloaded data 

#Query by region
coordinates = SkyCoord(ra=10.122,  dec=24.15, unit='deg')
dc.query_position(coordinates, size=size, download_type='jpg',layer='ls-dr9')
   
 #Query by name
dc.query_name("Name of object", size=size, download_type='fits',layer='ls-dr9-model') 


