# Continous and Discrete Signals and Systems - Theory and computational examples

This repository contains a collection of [Jupyter](https://jupyter.org/) notebooks introducing the theory of linear time-invariant (LTI) signals and systems. The continous-time case, as well as the sampled (discrete-time) case is covered. The theory is accompanied by a series of computational examples and exercises written in [IPython 3](http://ipython.org/). Please take a look at the [static version](http://nbviewer.ipython.org/github/spatialaudio/signals-and-systems-lecture/blob/master/index.ipynb) for a first glance. The contents are provided as [Open Educational Resource](https://de.wikipedia.org/wiki/Open_Educational_Resources). You can give the project a [Star](https://github.com/spatialaudio/signals-and-systems-lecture/stargazers) if you like the notebooks.

The notebooks constitute the lecture notes to the bachelors course [Signals and Systems](http://www.int.uni-rostock.de/Signal-und-Systemtheorie.428.0.html) at the Universität Rostock given by [Sascha Spors](http://www.int.uni-rostock.de/Staff-Info.23+B6JmNIYXNoPWUxOTliMTNjY2U2MDcyZjJiZTI0YTc4MmFkYTE5NjQzJnR4X2pwc3RhZmZfcGkxJTVCYmFja0lkJTVEPTMmdHhfanBzdGFmZl9waTElNUJzaG93VWlkJTVEPTExMQ__.0.html).


## Getting Started

The Jupyter notebooks are accessible in various ways

* Online as [static web pages](http://nbviewer.ipython.org/github/spatialaudio/signals-and-systems-lecture/blob/master/index.ipynb)
* Online for [interactive use](https://mybinder.org/v2/gh/spatialaudio/signals-and-systems-lecture/master?filepath=index.ipynb) using [binder](https://mybinder.org/)
* Local for interactive use on your computer 

Also other online services (e.g. [google Colaboralory](https://colab.research.google.com), [Microsoft Azure](https://azure.microsoft.com/), ...) provide environments for interactive execution of Jupyter notebooks.
Local use on your computer requires a local Jupyter/IPython installation. The [Anaconda distribution](https://www.continuum.io/downloads) provides a good starting point. You have to [clone/download the notebooks from Github](http://github.com/spatialaudio/signals-and-systems-lecture). Use a [Git](http://git-scm.org/) client to clone the notebooks and then start your local Jupyter server. For manual installation under OS X/Linux please refer to your packet manager.


## Concept and Contents

An understanding of the underlying mechanisms and the limitations of basic signal processing methods is essential for the design of more complex techniques. These notebooks cover the fundamentals of linear time-invariant signals and systems. A focus is laid on a detailed mathematical treatise. The discussion of the mathematical background is important to understand the underlying principles in a more general manner. The materials contain a series of computational examples and exercises to interpret the theoretical findings and foster understanding. The examples are designed to be explored in an interactive manner. Furthermore, an outlook to practical applications is given whenever possible.

The materials are organized in two major blocks

* time-continuous and 
* sampled (time-discrete) 

signals and systems. Both blocks are connected by the discussion of the ideal sampling process and its implications on sampled signals. The contents for each block are quite similar:

* introduction into signals and systems
* standard signals and operations
* characterization of systems in the time-domain
* spectral representation of signals (Laplace, Fourier, z-, discrete Fourier Transform)
* spectral representation of systems
* properties of systems

This allows to observe the similarities and differences between the time-continuous and -discrete case. The part on time-discrete signals and systems may also be read without having studied the time-continuous case.


## Usage and Contributing

The contents are provided as [Open Educational Resource](https://de.wikipedia.org/wiki/Open_Educational_Resources). The text is licensed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), the code of the IPython examples under the [MIT license](https://opensource.org/licenses/MIT). Feel free to use the entire collection, parts or even single notebooks for your own purposes. I am very curious on the usage of the provided resources. Feel free to drop a line or report to [Sascha.Spors@uni-rostock.de](mailto:Sascha.Spors@uni-rostock.de).

Our vision is to lay the grounds for a **community driven concise resource** covering the entire theory of signals and systems. Open Educational Resources in combination with open source tools (Jupyter, Python) and well-established tools for data literacy (git) provide the unique possibility for collaborative and well-maintained resources. Jupyter has been chosen due to its seamless integration of text, math and code. The contents are represented future proov as simple markdown allowing for conversion into many formats (html, PDF, ...). The git version management system features tracking of the changes and authorship.

You are invited to contribute on different levels. The lowest level is to provide feedback in terms of a [Star](https://github.com/spatialaudio/signals-and-systems-lecture/stargazers) if you like the contents. Please consider reporting errors or suggestions for improvements as [issues](https://github.com/spatialaudio/digital-signal-processing-lecture/issues). However, we are also looking forward to new examples and exercises, as well as reformulation of existing and novel sub-sections or sections. Authorship of each considerable contribution will be clearly stated. One tracked way of reformulated or new material is to handle them as [pull request](https://github.com/spatialaudio/signals-and-systems-lecture/pulls).



## Build Status

The computational examples in the notebooks are automatically build and checked for errors by continuous integration using the [travis-ci.org](https://travis-ci.org/) service.

[![Build Status](https://travis-ci.org/spatialaudio/signals-and-systems-lecture.svg?branch=master)](https://travis-ci.org/spatialaudio/signals-and-systems-lecture)
