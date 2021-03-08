import pandas as pd
import csv
from astropy import units as u
from astropy.coordinates import SkyCoord

def latitude(df_sdss):
    c_icrs = []
    for i in range(len(df_sdss)):
        c = SkyCoord(df_sdss['ra'][i]*u.degree,df_sdss['dec'][i]*u.degree,frame='icrs')
        c = c.galactic
        c = c.to_string('decimal')[8:10]
        c = float(c)
        c = abs(c)
        c_icrs.append(c)
    return c_icrs

def label_class(df_sdss):
    list_class = []
    for i in range(len(df_sdss)):
        if df_sdss['gz2_class'][i][0:2] in 'Sa':
            list_class.append(1)
        elif df_sdss['gz2_class'][i][0:2] in 'Sb':
            list_class.append(1)
        elif df_sdss['gz2_class'][i][0:2] in 'Sd':
            list_class.append(1)
        elif df_sdss['gz2_class'][i][0:2] in 'Sc':
            list_class.append(1)
        elif df_sdss['gz2_class'][i][0:2] in 'SB':
            list_class.append(1)
        elif df_sdss['gz2_class'][i][0:1] in 'E':
            list_class.append(0)
        else:
            list_class.append(2)
    return list_class



def dataLimited(df_sdss):
    df_sdss = df_sdss[df_sdss['K']>=20]
    df_sdss = df_sdss[df_sdss['PETROMAG_R']<17.78]
    df_sdss = df_sdss[df_sdss['REDSHIFT']<0.1]
    df_sdss = df_sdss[df_sdss['REDSHIFT']>0.03]
    df_sdss = df_sdss.reset_index()
    c_icrs = latitude(df_sdss)
    list_class = label_class(df_sdss)
    list_class = pd.DataFrame(list_class)
    list_class = list_class.rename(columns={0:'class'})
    df = pd.concat([df_sdss,a],axis=1)
    df = df[df['glon']>=30]

    ellip = []
    spir = []
    elliptical = df[df['class']==0].reset_index()
    spiral = df[df['class']==1].reset_index()
    
    for i in range(len(elliptical)):
        str_name = "Elliptical/" + str(elliptical['dr7objid'][i]) +".jpg"
        ellip.append(str_name)
        
    for i in range(len(spiral)):
        str_nameS = "Spiral/" + str(spiral['dr7objid'][i]) +".jpg"
        spir.append(str_nameS)

    ellip = pd.DataFrame(ellip)
    spir = pd.DataFrame(spir)
    
    df_spiral = pd.concat([spiral,spir],axis = 1)
    df_ellip = pd.concat([elliptical,ellip],axis = 1)

    df_ellip = df_ellip.rename(columns={0:'PATH'})
    df_spiral = df_spiral.rename(columns={0:'PATH'})
    df_spiral.to_csv("DataCSV/Spiral.csv")
    df_ellip.to_csv("DataCSV/Elliptical.csv")
    
def main():
    dfmain = pd.read_csv('zoo2MainSpecz.csv')
    dfsampe = pd.read_csv('gz2sample.csv')
    dfbarc = pd.read_csv('Barchi19_Morph-catalog_670k-galaxies.csv')
    dfsample = dfsample.rename(columns={'OBJID':'dr7objid'})
    df = dfmain.combine_first(dfmain.merge(dfsample,on='dr7objid'))
    df_sdss = pd.merge(df,dfbarc,on='dr7objid')
    df_sdss = df_sdss[['dr7objid','ra','dec','gz2_class','PETROR90_R','K','C','A','S','G2','H','PETROMAG_R','REDSHIFT']]
    dataLimited(df_sdss)

if __name__ == '__main__':
    main()
