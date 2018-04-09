import matplotlib.pyplot as plt
from osgeo import gdal, ogr
from skimage import measure, morphology
import numpy as np
import os





def make_taz(input_raster_name, output_shp_file_name, kernel_size=3):
    
    # Use gdal to read and write images to ensure that geographic information is not lost.
    # skimage does not support using gdal to save image
    print('read image')
    in_ds=gdal.Open(input_raster_name,1)

    geo_transform = in_ds.GetGeoTransform()
    proj = in_ds.GetProjection()
    rows = in_ds.RasterYSize
    cols = in_ds.RasterXSize

    band=in_ds.GetRasterBand(1)
    datatype=band.DataType
    road_img = band.ReadAsArray(0,0,cols,rows)


    
    print('segmentation')
    # segmentation
    selem = np.full((kernel_size,kernel_size), 1)
    dilation_road_img = morphology.dilation(road_img, selem)
    thin_road_img = morphology.thin(dilation_road_img)
    thin_road_img = thin_road_img.astype(np.int32)
    label_road_img = measure.label(thin_road_img, connectivity=1, background=1)


    
    # 栅格输出
    # driver=in_ds.GetDriver()
    # out_raster='./data/output/out2.tif'
    # out_ds = driver.Create(out_raster, cols,rows, 1, datatype)

    # out_ds.SetGeoTransform(geo_transform)    
    # out_ds.SetProjection(proj)

    # out_band = out_ds.GetRasterBand(1)
    # out_band.WriteArray(label_road_img,0,0)    
    # out_ds=None 

    print('vectorize')
    # vectorize the result
    raster_driver=driver = gdal.GetDriverByName('mem')
    raster_ds = raster_driver.Create('', cols, rows, 2, datatype)
    raster_ds.SetGeoTransform(geo_transform)
    raster_ds.SetProjection(proj)
    data_band = raster_ds.GetRasterBand(1)
    data_band.WriteArray(label_road_img, 0, 0)

    mask_array = (label_road_img > 0).astype(np.int32)
    mask_band = raster_ds.GetRasterBand(2)
    mask_band.WriteArray(mask_array, 0, 0)

    
    driver = ogr.GetDriverByName("ESRI Shapefile")
    out_shapefile = output_shp_file_name
    if os.path.exists(out_shapefile):
        driver.DeleteDataSource(out_shapefile)

    dest_srs = ogr.osr.SpatialReference(wkt=proj)
    out_ds = driver.CreateDataSource(out_shapefile)
    out_layer = out_ds.CreateLayer("polygonized", srs=dest_srs)
    new_field = ogr.FieldDefn('MYFLD', ogr.OFTInteger)
    out_layer.CreateField(new_field)


    gdal.Polygonize(data_band, mask_band, out_layer, 0, [], callback=None)
    print('ok')



if __name__ == '__main__':
    
    make_taz('./data/input/road_level_2.tif', './data/shp/taz_level2_1.shp')


    
    