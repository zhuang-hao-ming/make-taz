

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
make_taz('../test/data/input/road_level_2.tif', '../test/data/result/out.tif')


```

## example

![result](https://github.com/zhuang-hao-ming/make-taz/blob/master/images/segmentation_result.jpg)


## 版本

### 0.1版本

请查看提交记录

### 0.2版本
1. 因为不希望在python中直接使用`gdal`，在0.2版本中改用`rasterio`进行栅格文件读写
2. 由于取消了对gdal的依赖，无法利用gdal的*栅格转矢量*功能，建议使用arcgis或者其他工具进行转换。
3. 改进了边界的处理，原先的输出结果中边界被标记为0，这导致在做栅格转矢量操作时，不同的交通小区之间存在较大的缝隙，
为了改进这个问题，在区域标记结束后，将所有的0值替换为邻近区域的值
4. 增加了小区域过滤参数，可以直接过滤栅格数目小于一定阈值的区域，程序自动将它合并到邻近的大区域。

![result](https://github.com/zhuang-hao-ming/make-taz/blob/master/images/new_segmentation.jpg)




## refer

1. [Segmentation of Urban Areas Using Road Networks](https://www.microsoft.com/en-us/research/publication/segmentation-of-urban-areas-using-road-networks/)

