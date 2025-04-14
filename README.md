# DECaLS_Cutout
=================================================================================================

DECaLS_Cutout is a Python package that allows users to query the DECaLS catalog for image cutouts. This package provides an easy-to-use interface for downloading JPG and FITS images of galaxies from the DECaLS survey. It is an updated version of the DECaLSQuery package (https://github.com/akhilkrishnar0/DECaLSQuery), developed by akhilkrishnar0. 

The previous version had multiple dependency issues and reduced functionality. We present an updated version of the package, renamed to DECaLS_Cutout for easy identification. 

## Updates

1. **Reorganized code**
   - Reorganized the directories and merged functionalities into a single .py file.
2. **Option to download various DECaLS image types using the 'Layer' parameter**
   - Added the ability to choose between the actual image (layer: ls-dr9), residual image (layer: ls-dr9-resid) and model (ls-dr9-model). This enables the user to choose between the images based on their science case. The default is ls-dr9-resid.
3. **Provision to search objects with help of the object identifier**
   - DECaLS_Cutout now provides you the option of searching for objects by using the object name, as identified in any catalogue
4. **Option to specify Download path**
   - Added functionality to mention the Download path to save the FITS/jpg images.

You may contact the author for any clarifications at **robinthomas546@gmail.com**.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RobinThomas95/DECaLS_Cutout_2.0
   cd DECaLSQuery



2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Install the package:
   ```bash
   python3 -m pip install .
   OR
   pip install .

5. Usage:
   ```bash
   from astropy.coordinates import SkyCoord
   from decals.query import decals_cutout

   dc=decals_cutout(output_dir="/your/path/for/saving/downloaded/data")  #Defining the path to save downloaded data 

   #Query by region
   coordinates = SkyCoord(ra=10.122,  dec=24.15, unit='deg')
   dc.query_position(coordinates, size=size, download_type='jpg/fits/both',layer='ls-dr9/ls-dr9-resid/ls-dr9-model')
   
   #Query by name
   dc.query_name("Name of object", size=size, download_type='jpg/fits/both',layer='ls-dr9/ls-dr9-resid/ls-dr9-model') 



6. Add `requirements.txt`:
This file contains the necessary dependencies.

```txt
   astroquery
   astropy
   requests


