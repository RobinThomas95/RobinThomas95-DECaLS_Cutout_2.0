from setuptools import setup, find_packages

setup(
    name="DECaLSQuery",
    version="2.0",
    packages=find_packages(),
    install_requires=[
        'astroquery',
        'astropy',
        'requests'
    ],
    description="A package for querying the DECaLS catalog and downloading image cutouts.",
    author="RT",
    author_email="robinthomas546@gmail.com",
    url="underconstruction.com",
)
