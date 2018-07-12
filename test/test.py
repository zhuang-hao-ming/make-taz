from make_taz import make_taz, simplify_polygon


if __name__ == '__main__':
    make_taz('../test/data/input/road_level_2.tif', '../test/data/result/out.tif')
    # simplify_polygon('./data/shp/taz_level2_3.shp', './data/shp/taz_level2_sim.shp', 30)