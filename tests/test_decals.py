import unittest
from astropy.coordinates import SkyCoord
from decals.query import decals_cutout  # or from your_package.decals_cutout import decals_cutout

class TestDecalsCutout(unittest.TestCase):
    def setUp(self):
        """
        Create a decals_cutout instance pointing to a 'test_downloads' directory.
        We'll use simple RA/Dec coordinates for testing.
        """
        self.cutout = decals_cutout(output_dir="test_downloads")
        self.coordinates = SkyCoord(ra=150.116, dec=2.205, unit='deg')

    def test_download_image(self):
        """
        Test the download_image method. 
        This should create test_downloads/images/test_galaxy.jpg if successful.
        """
        self.cutout.download_image(
            galid="test_galaxy",
            ra=self.coordinates.ra.deg,
            dec=self.coordinates.dec.deg,
            size=100
        )

    def test_download_fits(self):
        """
        Test the download_fits method.
        This should create test_downloads/fits/test_galaxy.fits if successful.
        """
        self.cutout.download_fits(
            galid="test_galaxy",
            ra=self.coordinates.ra.deg,
            dec=self.coordinates.dec.deg,
            size=100
        )

    def test_query_position(self):
        """
        Test the query_position method using both jpg and fits downloads.
        This should create files in test_downloads/images/ and test_downloads/fits/.
        """
        self.cutout.query_position(
            coordinates=self.coordinates,
            size=100,
            download_type='both',
            galid="test_galaxy_position"
        )

    def test_query_name(self):
        """
        Test the query_name method with a known object (M31).
        This resolves the name to coordinates and downloads the cutout(s).
        """
        self.cutout.query_name(
            obj_name="M31",
            size=100,
            download_type='jpg',  # only JPG to keep test quick
            galid="test_m31"
        )

if __name__ == "__main__":
    unittest.main()


