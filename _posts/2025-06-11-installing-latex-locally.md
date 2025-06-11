---
layout: post
title: How to install LaTeX locally on your PC
date: 2025-06-11 14:37:16
description: I describe how I installed MiKTeX on my PC. 
tags: latex miktex
categories: tutorials
toc:
  beginning: true
---

Hi, today I will describe how I installed MiKTeX, a TeX distribution, locally on my PC, along with my usual go-to workflow.
Often, I faced issues regarding compile time on Overleaf. Hence, why not locally work with LaTeX?

So, let's see the steps to install MiKTeX. I will also show how we can install packages, followed by a simple script to compile our project with multiple files without flooding our project directory. 


### Installation
1. Install [python](https://www.python.org/). (not needed for MiKTeX, but it is useful for the script I will be sharing).
2. Install [VSCode](https://code.visualstudio.com/) (I prefer this, but any other editor would work).
3. Go to [MiKTeX](https://miktex.org/download) and choose your OS and download.
 {% include figure.liquid path="/assets/img/local_latex_installation/image.png" class="img-fluid rounded z-depth-1" zoomable=true %}
4. Follow the steps at [https://miktex.org/howto/install-miktex](https://miktex.org/howto/install-miktex), they are pretty self explanatory.
5. Once MiKTeX is installed, you can search for MiKTeX Console on the Windows search bar and open it as administrator. 
 {% include figure.liquid path="/assets/img/local_latex_installation/image-1.png" class="img-fluid rounded z-depth-1" zoomable=true %}
6. Open Command Prompt, and type `where pdflatex`. If it shows a valid path under MiKTeX, your TeX Distribution has been installed!
 {% include figure.liquid path="/assets/img/local_latex_installation/image-3.png" class="img-fluid rounded z-depth-1" zoomable=true %}

### Installing Packages
Under the Packages tab, you can easily search for a package and install it.

{% include figure.liquid path="/assets/img/local_latex_installation/image-2.png" class="img-fluid rounded z-depth-1" zoomable=true %}

### Writing and Compiling a Project.
I will be using a sample project ([My Intro to Quantum Physics Assignment 2](/assets/zip/Quantum%20assignment%202.zip)). It contains subfiles and images so that it would be a good demonstration.

1. Open VSCode and create your project.
 {% include figure.liquid path="/assets/img/local_latex_installation/image-4.png" class="img-fluid rounded z-depth-1" zoomable=true %}
2. Create a file called [compile.py](/assets/py/compile_latex.py).
3. Now, all you need to do is open the terminal (press `` Ctrl + ` ``), and type in `compile.py main.tex`. Press `Enter` if any known errors come up. MiKTeX may also prompt you to install packages if needed. The compilation will continue.<br>
    <video controls src="/assets/video/local_latex_installation/20250611-1000-06.8188638.mp4" title="Title"></video>
4. Now, `main.pdf` will be saved in your project directory. You can also open the pdf in split screen view in VSCode to get more of an overleaf feel.
 {% include figure.liquid path="/assets/img/local_latex_installation/image-5.png" class="img-fluid rounded z-depth-1" zoomable=true %}

