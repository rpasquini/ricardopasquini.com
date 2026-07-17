---
title: "Installing H3 on a Linux Subsystem in Windows 10"
date: "2020-02-12"
slug: "installing-h3-on-windows-10"
lang: "es"
categories: ["Coding Notes"]
tags: ["conda", "Geospatial analysis", "h3", "hexagons", "Jupyter", "python", "ubuntu"]
excerpt: ""
draft: false
---

Installing H3 on a Linux Subsystem in Windows 10


# Installing H3 on a Linux Subsystem in Windows 10

[H3](https://github.com/uber/h3) is a library developed by the Uber team, that implements spatial analysis based on indexed hexagons. Hexagons have especially interesting properties for spatial operations. [See more here](https://uber.github.io/h3/#/documentation/overview/use-cases).

My experience installing H3 on Windows was not good. H3 did not work, and errors were not clear on the causes either. After some googling I reached the conclusion that crafting that installation could become a headache.

So I decided to test the alternative way of using Linux as a subsystem of Windows. This turn out very well.

I collect in this post the steps for the complete setup:

## 1. Install the Linux subsystem

The procedure for this installation is simple and [explained here] (<https://docs.microsoft.com/en-us/windows/wsl/install-win10>). The steps:

1. Using Windows Powershell (wich is available on Windows), enter the command that authorizes the execution of the subsystem:
2. Restart
3. Install a Linux distribution. The distributions can be found at Microsoft Store. In my case I downloaded and installed Ubuntu 18.04 LTS. Just download and install. No special configurations required here.
4. Once installed we will have access to Ubuntu through a shortcut:

![image-20200211235838092](https://www.dropbox.com/s/qgigxn8q85b0t9b/image-20200211235838092.png?dl=1)

## **2. Preparing the installation of h3 in Ubuntu**

According to the specifications, [H3 for Python](https://pypi.org/project/h3/) needs the compiler [cc](https://www.geeksforgeeks.org/cc-command-in-linux- with-examples /), [make](https://askubuntu.com/questions/398489/how-to-install-build-essential) and [cmake](https://cgold.readthedocs.io/en/latest /overview/cmake-can.html), installed. Using the sudo command, from Ubuntu, install cc and make at once, calling the build-essential installation

```
sudo apt updateSudo apt install build-essential
```

The *which* command allows to verify what is installed. If it finds the command, it returns the path:

```
ricardo@DESKTOP:~$ which cc
/usr/bin/cc
ricardo@DESKTOP:~$ which make
/usr/bin/make
```

You can verify that cmake does not return anything. It is necessary to specify the installation of cmake separately:

```
sudo apt-get -y install cmake
```

## 3. Installing h3 together with other spatial analysis libraries using conda and pip

The actual installation of h3 can be done with [pip](https://pypi.org/project/pip/).

Before doing this installation, I prefer to use [conda](https://docs.conda.io/en/latest/miniconda.html) to generate a specific virtual environment for this installation. A virtual environment manager allows you to have different combinations of libraries in separate environments, so that you only need to “activate” a desired environment for your particular work session.
To install the latest version of miniconda from Ubuntu:

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.shbash Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

Now to install everything using conda. I can install all necessary libraries by specifying them as part of an .yml file.

It is necessary to write this file specifying the versions. The content of my requirements.yml file is as follows:

```
name: twitteranalysis
dependencies:
  - python=3.6
  - pandas=0.24.2
  - numpy=1.16.4
  - pymongo=3.7.2
  - shapely=1.6.4
  - matplotlib=3.1.0
  - seaborn=0.9.0
  - statsmodels=0.9.0
  - ipykernel=5.1.0
  - pip
  - jupiter
  - pip:
    - h3==3.1.0
    - area==1.1.1
    - folium==0.7.0
    - geopandas==0.5.0
    - geojson==2.4.1
```

Note that the first thing you specify is the name I want to give the environment.

What follows are the dependencies. The dependencies are all libraries with their specific versions, which in this case are specific for my project (they are shown as an example), they are not specific to H3. All these dependencies are managed by conda, using conda-based repositories.

Finally, you can add the packages that will be installed through pip. According to the conda documentation it is preferable to first specify the dependencies that can be managed by conda and then add pip facilities. H3 is not in count. For this reason it appears as part of the pip facilities.

One comment related to the location of the yml file. I would like to write that file in the same folder I was working when using Windows. Ubuntu can access to the Windows based folders by using /mnt. For instance, in my case I would use cd to navigate to my project folder at c:/Users/Richard/Drive as follows:

```
rick@DESKTOP:$ cd /mnt/c/Users/Richard/Drive
rick@DESKTOP:/mnt/c/Users/Richard/Drive$
```

To run the full installation using conda from Ubuntu:

```
conda env create -f environment.yml
```

Once installation has been completed, the virtual environment is activated using conda activate:

```
rick@DESKTOP:$ conda activate twitteranalysis
(twitteranalysis) rick@DESKTOP:$
```

Last step is to create an ipykernel, which will allow using the new virtual environment in Jupyter. It is necessary to specify the virtual environment name and to provide a name to be displayed within jupyter.

```
python -m ipykernel install --user --name twitteranalysis --display-name "Python (twitteranalysis)"

Installed kernelspec twitteranalysis in 
/home/rick/.local/share/jupyter/kernels/twitteranalysis
```

## 4. Checking that H3 works

Launch jupyter from the same session at Ubuntu:

```
rick@DESKTOP:$jupyter notebook
```

A few commands to check it is working

![image-20200212001246684](https://www.dropbox.com/s/7oirg90601iuwth/image-20200212001246684.png?dl=1)
