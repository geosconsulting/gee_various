#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 04:43:51 2017
@author: fabio
"""
import datetime
import ee
import ee.mapclient

ee.Initialize()

collection = (ee.ImageCollection('LE7_L1T')
                .filterDate(datetime.datetime(2002, 11, 1),
                            datetime.datetime(2002, 12, 1)))

def NDVI(image):
    return image.expression('float(b("B4") - b("B3")) - (b("B4") + b("B3"))')


def SAVI(image):
    """A function to compute Soil Adjusted Vegetation Index."""
    return ee.Image(0).expression(
        '(1 + L) * float(nir - red)/ (nir + red + L)',
            {
            'nir': image.select('B4'),
            'red': image.select('B3'),
            'L': 0.2
      })

    
vis = {
    'min': 0,
    'max': 1,
    'palette': [
        'FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163',
        '99B718', '74A901', '66A000', '529400', '3E8601',
        '207401', '056201', '004C00', '023B01', '012E01',
        '011D01', '011301'
    ]}

ee.mapclient.addToMap(collection.map(NDVI).mean(), vis)
ee.mapclient.addToMap(collection.map(SAVI).mean(), vis)
ee.mapclient.centerMap(-93.7848, 30.3252, 11)