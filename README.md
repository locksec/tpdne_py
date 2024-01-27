# Overview
This script automatically downloads and crops images (to remove watermark) from https://www.thispersondoesnotexist.com.

# Prerequisites
## Installing Python
If you don't have Python installed, download and install the latest version from python.org.

##Recommended Setup: Using Anaconda
Anaconda simplifies package management and deployment. It's recommended for managing Python dependencies for this project. You can download Anaconda [here](https://www.anaconda.com/download/).

1. Create a new Conda environment:

``` bash
conda create --name myenv python=3.10.6
```

2. Activate the environment:

```bash
conda activate myenv
```
## Installing Required Libraries
### With Anaconda (Recommended)
Within your Conda environment, install the necessary libraries:

```bash
conda install requests
conda install Pillow
```
### Using pip
Alternatively, if you're not using Anaconda, install the libraries using pip:

```bash
pip install requests
pip install Pillow
```
# Usage
To use the script, navigate to the directory containing tpdne.py and run:

```bash
python tpdne.py -n [number_of_images]
```

Replace [number_of_images] with the number of images you want to fetch and process.

The script saves the images in the current directory, naming them in the format `image_{number}_{timestamp}.jpg`.