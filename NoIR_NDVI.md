NoIR Plant Photosynthesis Measurement
================

A Raspberry Pi with NoIR camera can be used to measure photosynthesis in plants. The infrared block filter (NoIR) has been removed from the camera. Adding a filter to block red light, allows the "red" channel of the camera to instead measure near-infrared light. Since chlorophyll absorbs blue and red light, but not green or infrared. The difference in red light absorption and near infrared reflectance indicates the amount of photosynthesis. Photos from the NOIR camera with red block filter can be processed into false-colored *Normalized Difference Vegetation Index* (NDVI) images using a free online tool, Infragram by Public Lab. <https://publiclab.org/wiki/infragram>
![alt text](figures/PlantReflection.png)

Raspberry Pi and NoIR camera
----------------------------

![alt text](figures/RPi_NoIR.jpg)

![alt text](figures/NoIR.png)

<https://www.raspberrypi.org/blog/whats-that-blue-thing-doing-here/>

Normalized Difference Vegetation Index
--------------------------------------

![alt text](figures/NDVI.jpg)

<https://publiclab.org/wiki/ndvi>
![alt text](figures/IMG-split.png)

Photosynthesis
--------------

Plant photosynthesis is part of the carbon cycle. Plants use energy from sunlight to combine carbon dioxide (CO<sub>2</sub>) and water (H<sub>2</sub>O) to form carbohydrates. Oxygen (O<sub>2</sub>) is released as a byproduct.

![alt text](figures/Carbon_cycle.jpg)

This diagram of the fast carbon cycle shows the movement of carbon between land, atmosphere, and oceans in billions of tons per year. Yellow numbers are natural fluxes, red are human contributions, white indicate stored carbon. Note this diagram does not account for volcanic and tectonic activity, which also sequesters and releases carbon. <https://en.wikipedia.org/wiki/Carbon_cycle>

### Calvin cycle - C<sub>3</sub> pathway

CO<sub>2</sub> is added to a phosphorylated 5-carbon sugar, ribulose biphosphate. This reaction is catalyzed by the enzyme ribulose biphosphate carboxylase oxygenase (RuBisCO). The resulting 6-carbon compound breaks down into 2 molecules of 3-phosphoglyceric acid (PGA). These are used to produce gulcose and other food.

### Photorespiration - C<sub>2</sub> cycle

RuBisCO can also add O<sub>2</sub> to ribulose biphosphate liberating CO<sub>2</sub> in the process. High light intensities and high temperatures (above ~ 30 C) favor this process over photosynthesis.

### C<sub>4</sub> plants

C<sub>4</sub> plants minimize water loss to transpiration. In mesophyll cells of C<sub>4</sub> plants CO<sub>2</sub> is added to 3-carbon phosphoenolpyruvic acid (PEP) to form 4-carbon oxaloacetic acid (C<sub>4</sub>). This is converted to malic or aspartic acid and tranported into a bundle sheath cell. These cells are often deep in the leaf with low levels of oxygen. In the sheath cells the 4-carbon acids are broken down into CO<sub>2</sub> which enters the Calvin cycle or pyruvic acid which is transported back to a mesophyll cell where it is converted back into PEP.

![alt text](figures/C4anatomy.gif)

-   crassulacean acid metabolism (CAM) plants segregate C<sub>4</sub> and C<sub>3</sub> pathways in time
-   at night they take in CO<sub>2</sub> through their stomata and produce malic acid
-   in the morning stomata close and malic acid is broken down to release CO<sub>2</sub> to the Calvin (C<sub>3</sub>) cycle
-   cacti, Bryophyllum, pineapple, sedums, "ice plant" are well adapted to high temperatures and sunlight and low moisture
-   other plants segregate these pathways in different parts of the leaf
-   tobacco has C<sub>4</sub> cells near veins

Results
-------
