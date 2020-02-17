# LAB data downloader and processor

This Python script downloads data from the [LAB survey website](https://www.astro.uni-bonn.de/hisurvey/AllSky_profiles/index.php) and finds the maximum velocity using statistical variance. It does this for Galactic longitudes `-90.00` through `90.00` degrees in 10 degree intervals. The script prints out the max velocities and saves the spectra as images.

## Requirements
- Python 3
- These Python modules: matplotlib, statistics, requests
