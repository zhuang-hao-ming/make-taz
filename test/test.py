from make_taz import make_taz, simplify_polygon


if __name__ == '__main__':
    make_taz('./data/input/road_level_2.tif', './data/shp/taz_level2_3.shp')
    simplify_polygon('./data/shp/taz_level2_3.shp', './data/shp/taz_level2_sim.shp', 30)