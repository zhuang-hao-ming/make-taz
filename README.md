

## 

We provide two tools. `make_taz` segment urban areas into regions by road networks.
`simplify_polygon` simplify the result polygon.

`make_taz` uses the algorithm proposed in paper [Segmentation of Urban Areas Using Road Networks](https://www.microsoft.com/en-us/research/publication/segmentation-of-urban-areas-using-road-networks/).

`simplify_polygon` uses shapely's simplify method.

## install

```
pip install make-taz

```

## how to use

```python

from make_taz import make_taz, simplify_polygon
make_taz('./data/input/road_level_2.tif', './data/shp/taz_level2_3.shp')
simplify_polygon('./data/shp/taz_level2_3.shp', './data/shp/taz_level2_sim.shp', 30)

```

## example

![result](https://github.com/zhuang-hao-ming/make-taz/blob/master/images/segmentation_result.jpg)


## refer

1. [Segmentation of Urban Areas Using Road Networks](https://www.microsoft.com/en-us/research/publication/segmentation-of-urban-areas-using-road-networks/)

