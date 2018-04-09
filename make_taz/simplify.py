import fiona
from shapely.geometry import shape, mapping



def simplify_polygon(input_file_name, output_file_name, tolerance):
    '''
    simplify polygons

    Parameters:
    -----------
    input_file_name : str
        input file name, must be a shapefile
    output_file_name : str
        output file name
    tolerance : float
        simplify tolerance
    
    '''
    c = fiona.open(input_file_name)
    out_c = fiona.open(output_file_name, 'w', **c.meta)
    for feature in c:
        shapely_geometry = shape(feature['geometry'])
        shapely_geometry = shapely_geometry.simplify(tolerance)
        feature['geometry'] = mapping(shapely_geometry)
        out_c.write(feature)
    c.close()
    out_c.close()
    print('ok')


if __name__ == '__main__':
    simplify('./data/shp/taz_level3.shp', './data/shp/taz_level3_simplify1.shp', 30)
    
    