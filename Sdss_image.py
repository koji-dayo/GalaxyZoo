import requests
import pandas as pd
import numpy as np
import cv2
import csv
import sys

def main(name):
    df = pd.read_csv(name)
    objid = df['dr7objid']
    ra = df['ra']
    dec = df['dec']
    ePetro = df['PETRO90_R']
    scale = 0.02 * ePetro
    l = scale/0.27

    url = "http://skyserver.sdss.org/dr16/SkyServerWS/ImgCutout/getjpeg?TaskName=Skyserver.Chart.List&"

    for i in range(len(df)):
        new_url = url + "ra=" + str(ra[i]) + "&dec=" + str(dec[i]) + "&scale=" + str(scale[i]) + "&width=" + str(l[i])+"&height=" + str(l[i]) + "&opt="
        response = requests.get(new_url)
        image = response.content
        file_name = str(objid[i]) + ".jpg"

        with open(file_name,"wb") as f:
            f.write(image);

if __name__ == '__main__':
    args = sys.argv
    if args == 'DataCSV/Elliptical':
        main('DataCSV/Elliptical.csv')
    elif args == 'DataCSV/Spiral':
        main('DataCSV/Spiral.csv')
