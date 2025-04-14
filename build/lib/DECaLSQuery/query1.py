from astroquery.query import BaseQuery
from astropy.coordinates import SkyCoord
import requests
import shutil
import os

class DECaLSQuery(BaseQuery):
    """
    DECaLS Query class for downloading cutouts from the DECaLS viewer.
    """
    # Notice we add {layer} to the URL instead of hardcoding 'ls-dr9-resid'.
    URL_TEMPLATE_JPG  = "https://www.legacysurvey.org/viewer/cutout.jpg?ra={ra}&dec={dec}&pix=0.25&layer={layer}&size={size}"
    URL_TEMPLATE_FITS = "https://www.legacysurvey.org/viewer/cutout.fits?ra={ra}&dec={dec}&pix=0.25&layer={layer}&size={size}"

    def __init__(self, output_dir="downloads"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

        # Subdirectories for organizing images vs. fits.
        self.image_dir = os.path.join(self.output_dir, "images")
        self.fits_dir  = os.path.join(self.output_dir, "fits")
        os.makedirs(self.image_dir, exist_ok=True)
        os.makedirs(self.fits_dir, exist_ok=True)

    def _get_cutout_url(self, ra, dec, size, filetype='jpg', layer='ls-dr9-resid'):
        """
        Construct the URL for the DECaLS cutout service.

        Parameters
        ----------
        ra : float
            Right Ascension in degrees
        dec : float
            Declination in degrees
        size : int
            Cutout size in pixels
        filetype : str, optional
            Either 'jpg' or 'fits'
        layer : str, optional
            DECaLS layer to use. Common examples:
              - 'ls-dr9'       (regular color image)
              - 'ls-dr9-resid' (residual)
              - 'ls-dr9-model' (model image)
            Defaults to 'ls-dr9-resid'.
        """
        if filetype == 'jpg':
            return self.URL_TEMPLATE_JPG.format(ra=ra, dec=dec, size=size, layer=layer)
        elif filetype == 'fits':
            return self.URL_TEMPLATE_FITS.format(ra=ra, dec=dec, size=size, layer=layer)
        else:
            raise ValueError(f"Unsupported file type: {filetype}")

    def download_image(self, galid, ra, dec, size, layer='ls-dr9-resid'):
        """
        Download a JPG image cutout.

        Parameters
        ----------
        galid : str
            Identifier to name the output file
        ra, dec : float
            Coordinates in degrees
        size : int
            Cutout size in pixels
        layer : str
            DECaLS layer, e.g. 'ls-dr9' or 'ls-dr9-resid'
        """
        url = self._get_cutout_url(ra, dec, size, filetype='jpg', layer=layer)
        file_name = os.path.join(self.image_dir, f"{galid}.jpg")
        self._download_file(url, file_name)

    def download_fits(self, galid, ra, dec, size, layer='ls-dr9-resid'):
        """
        Download a FITS image cutout.

        Parameters
        ----------
        galid : str
            Identifier to name the output file
        ra, dec : float
            Coordinates in degrees
        size : int
            Cutout size in pixels
        layer : str
            DECaLS layer, e.g. 'ls-dr9' or 'ls-dr9-resid'
        """
        url = self._get_cutout_url(ra, dec, size, filetype='fits', layer=layer)
        file_name = os.path.join(self.fits_dir, f"{galid}.fits")
        self._download_file(url, file_name)

    def _download_file(self, url, file_name):
        """Download a file from the given URL."""
        print(f"Downloading from {url}")
        res = requests.get(url, stream=True)
        if res.status_code == 200:
            with open(file_name, 'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print(f"File successfully downloaded: {file_name}")
        else:
            print(f"File could not be retrieved from {url}")


    def query_position(self, coordinates, size, download_type='both', galid=None):
        """
        Query the DECaLS cutout service for a region.

        Parameters:
        - coordinates: Astropy SkyCoord object
        - size: int, cutout size in pixels
        - download_type: 'jpg', 'fits', or 'both'
        - galid: str, unique identifier for the galaxy
	        """
        ra = coordinates.ra.deg
        dec = coordinates.dec.deg
        galid = galid or f"decals_{ra}_{dec}"
        if download_type in ('jpg', 'both'):
            self.download_image(galid, ra, dec, size)
        if download_type in ('fits', 'both'):
            self.download_fits(galid, ra, dec, size)

    def query_name(self, obj_name, size, download_type='both', galid=None):
    
        coords=SkyCoord.from_name(obj_name)     
        galid = galid or obj_name

        self.query_position(coords, size=size, download_type='both', galid=galid)

