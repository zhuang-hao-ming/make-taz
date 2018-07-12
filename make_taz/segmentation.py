
import os

import numpy as np
import rasterio
from skimage import measure, morphology


def make_taz(input_raster_name, output_raster_name, kernel_size=3, low_frequency_threshold=9):
    '''
    make taz from road image

    Parameters:
    -----------------
    input_raster_name: str
        filename of input raster. it must be a tif file with one band.
        it must have just two value 1 and 0, within, 1 stands for road, and 0 stands for any other thing.
    
    output_raster_name: str
        filename of output raster. 
    
    kernel_size: int
        morphology kernel
    
    low_frequency_threshold: int
        region with amount of cell less than threshold will be excluede.
    
    Returns:
    -------------
    save raster to the destination path.

    '''
    
    # Use gdal to read and write images to ensure that geographic information is not lost.
    # skimage does not support using gdal to save image
    print('read image')
    src = rasterio.open(input_raster_name)
    road_img = src.read(1)
    

    # segmentation
    print('segmentation')
    selem = np.full((kernel_size,kernel_size), 1)
    dilation_road_img = morphology.dilation(road_img, selem)
    thin_road_img = morphology.thin(dilation_road_img)
    thin_road_img = thin_road_img.astype(np.int32)
    label_road_img = measure.label(thin_road_img, connectivity=1, background=1)


    # exclude low frequency region
    exclude_items = []
    unique, counts = np.unique(label_road_img, return_counts=True)
    item_count_dict = dict(zip(unique, counts))
    for item,count in item_count_dict.items():
        if count < low_frequency_threshold:
            exclude_items.append(item)
            
    
    for item in exclude_items:
        label_road_img[label_road_img==item] = 0

    # exclude zero value
    # to produce better polygon
    while np.count_nonzero(label_road_img==0) > 0:
        # row+1
        label_road_img = np.where(label_road_img == 0, np.roll(label_road_img, 1, axis=0), label_road_img)
        # row-1
        label_road_img = np.where(label_road_img == 0, np.roll(label_road_img, -1, axis=0), label_road_img)
        # col+1
        label_road_img = np.where(label_road_img == 0, np.roll(label_road_img, 1, axis=1), label_road_img)
        # col-1
        label_road_img = np.where(label_road_img == 0, np.roll(label_road_img, -1, axis=1), label_road_img)


    # output
    profile = src.profile
    profile.update(dtype=rasterio.int32, count=1, nodata=-9999)

    
    with rasterio.open(output_raster_name, 'w', **profile) as dst:
        dst.write(label_road_img.astype(rasterio.int32), 1)

    src.close()


if __name__ == '__main__':
    make_taz('../test/data/input/road_level_2.tif', '../test/data/result/out.tif')
