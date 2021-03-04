# Panoramic Mosaicing

### Steps to Run Locally on your System
1. `git clone https://github.com/trunc8/panoramic-mosaicing.git`
2. `pip install -r requirements.txt`

### Usage
1. Stitching two images: 
```
$ cd panoramic-mosaicing/
$ python3 code/pano-auto.py <path-to-directory-containing-2-images>
(e.g.) python3 code/pano-auto.py data/auto/campus/
```
2. Generalized mosaicing of 'n' images:
```
$ cd panoramic-mosaicing/
$ python3 pano-general.py <path-to-directory-of-images> <index-to-reference-image>
(e.g.) python3 code/pano-general.py data/general/mountain/ 3
```

### Demo
**Example-1**  
Input Images
<p align="center"> 
![Input-1](data/general/yosemite/1.jpg){:height="100px"}
![Input-2](data/general/yosemite/2.jpg){:height="100px"}
![Input-3](data/general/yosemite/3.jpg){:height="100px"}
![Input-4](data/general/yosemite/4.jpg){:height="100px"}
</p>
Panorama Mosaic Image
<p align="center"> 
![Yosemite](results/pano-general-results/yosemite/auto_yosemite_ref_2.jpg){:height="200px"}
</p>

**Example-2**  
Input Images
<p align="center"> 
![Input-1](data/general/yard/1.jpg){:height="100px"}
![Input-2](data/general/yard/2.jpg){:height="100px"}
![Input-3](data/general/yard/3.jpg){:height="100px"}
![Input-4](data/general/yard/4.jpg){:height="100px"}
![Input-5](data/general/yard/5.jpg){:height="100px"}
</p>
Panorama Mosaic Image
<p align="center"> 
![Yard](results/pano-general-results/yard/auto_yard_ref_3.jpg){:height="200px"}
</p>

**Example-3**  
Input Images
<p align="center"> 
![Input-1](data/auto/society/1.jpg){:width="200px"}
![Input-2](data/auto/society/2.jpg){:width="200px"}
</p>
Panorama Mosaic Image
<p align="center"> 
![Yard](results/pano-auto-results/society/auto_society_I1_reference.jpg){:width="400px"}
</p>

### Authors

* **Siddharth Saha** - [trunc8](https://github.com/trunc8)

<p align='center'>Created with :heart: by <a href="https://www.linkedin.com/in/sahasiddharth611/">Siddharth</a></p>