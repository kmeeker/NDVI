NoIR Plant Photosynthesis Measurement
================

take a NDVI picture of a plant to measure its photosynthesis
------------------------------------------------------------

A Raspberry Pi with NoIR camera can be used to measure photosynthesis in plants. The NoIR camera has its infrared block filter removed. The addition of a filter to block red light, allows the "red" channel of the camera to instead measure "near-infrared" light. Since chlorophyll absorbs blue and red light, but not green or infrared. The difference in reflection of infrared and blue light from a plant indicates the amount of photosynthesis. Photos from the NOIR camera with red block filter can be processed into false-colored "Normalized Difference Vegetation Index" (NDVI) images using a free online tool, Infragram by Public Lab.

<https://www.raspberrypi.org/blog/whats-that-blue-thing-doing-here/>
<https://publiclab.org/wiki/infragram>
<https://publiclab.org/wiki/ndvi>

Including Code
--------------

You can include R code in the document as follows:

``` r
summary(cars)
```

    ##      speed           dist       
    ##  Min.   : 4.0   Min.   :  2.00  
    ##  1st Qu.:12.0   1st Qu.: 26.00  
    ##  Median :15.0   Median : 36.00  
    ##  Mean   :15.4   Mean   : 42.98  
    ##  3rd Qu.:19.0   3rd Qu.: 56.00  
    ##  Max.   :25.0   Max.   :120.00

Including Plots
---------------

You can also embed plots, for example:

![](Readme_files/figure-markdown_github/pressure-1.png)

Note that the `echo = FALSE` parameter was added to the code chunk to prevent printing of the R code that generated the plot.
