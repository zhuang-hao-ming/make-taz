

## 

Proporcionamos dos herramientas. `make_taz` segmenta las áreas urbanas en regiones mediante redes viales.
`simplify_polygon` simplifica el polígono resultante.

`make_taz` utiliza el algoritmo propuesto en el artículo [Segmentation of Urban Areas Using Road Networks](https://www.microsoft.com/en-us/research/publication/segmentation-of-urban-areas-using-road-networks/).

`simplify_polygon` utiliza el método `simplify` de Shapely.

## instalación

```
pip install make-taz

```

## cómo usar

```python

from make_taz import make_taz, simplify_polygon
make_taz('../test/data/input/road_level_2.tif', '../test/data/result/out.tif')


```

## ejemplo

![result](https://github.com/zhuang-hao-ming/make-taz/blob/master/images/segmentation_result.jpg)


## versiones

### Versión 0.1

Consulte el historial de commits

### Versión 0.2
1. Para evitar el uso directo de `gdal` en Python, en la versión 0.2 se cambia a `rasterio` para la lectura y escritura de archivos raster.
2. Dado que se eliminó la dependencia de gdal, ya no se puede aprovechar la función de *raster a vector* de gdal, por lo que se recomienda utilizar ArcGIS u otras herramientas para la conversión.
3. Se mejoró el manejo de los bordes. En los resultados anteriores, los bordes se marcaban como 0, lo que generaba grandes huecos entre diferentes zonas de tráfico al realizar la conversión de raster a vector. Para solucionar esto, después de la asignación de etiquetas de región, todos los valores 0 se reemplazan por el valor de la región vecina.
4. Se añadió un parámetro para filtrar regiones pequeñas, que permite excluir directamente los conjuntos de celdas raster por debajo de un umbral determinado. El programa los fusiona automáticamente con la región grande adyacente.

![result](https://github.com/zhuang-hao-ming/make-taz/blob/master/images/new_segmentation.jpg)




## referencias

1. [Segmentation of Urban Areas Using Road Networks](https://www.microsoft.com/en-us/research/publication/segmentation-of-urban-areas-using-road-networks/)
