# LAB data downloader and processor

This Python script downloads data from the (LAB survey website)[https://www.astro.uni-bonn.de/hisurvey/AllSky_profiles/index.php] and finds the maximum velocity using statistical variance. It does this for Galactic longitudes `0.00, 10.00, 20.00, 30.00, 40.00, 50.00, 60.00, 70.00, 80.00, 90.00, -10.00, -20.00, -30.00, -40.00, -50.00, -60.00, -70.00, -80.00, -90.00` degrees. It prints out the max velocities and saves the spectra as images.

## Requirements
- Python 3
- These Python modules: matplotlib, statistics, requests
