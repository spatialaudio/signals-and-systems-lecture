# Continuous- and Discrete-Time Signals and Systems - Theory and Computational Examples

![Integration Test](https://github.com/spatialaudio//signals-and-systems-lecture/actions/workflows/notebook_ci.yml/badge.svg)

This repository collects didactically edited [Jupyter](https://jupyter.org/)
notebooks that introduce the theory of linear, time-invariant (LTI) signals and
systems.
Please take a look at the [static version](http://nbviewer.ipython.org/github/spatialaudio/signals-and-systems-lecture/blob/master/index.ipynb)
for a first glance.
The continuous-time case, as well as the temporally sampled (discrete-time)
case is covered.
The theory is accompanied by a series of computational examples and exercises
written in [IPython 3](http://ipython.org/).  

![System in the temporal and spectral domain](systems_spectral_domain/LTI_system_time_spectral_domain.png)

The notebooks constitute the lecture notes to the bachelor's course
[Signals and Systems](http://www.int.uni-rostock.de/Signal-und-Systemtheorie.428.0.html)
given by [Sascha Spors](http://www.int.uni-rostock.de/Staff-Info.23+B6JmNIYXNoPWUxOTliMTNjY2U2MDcyZjJiZTI0YTc4MmFkYTE5NjQzJnR4X2pwc3RhZmZfcGkxJTVCYmFja0lkJTVEPTMmdHhfanBzdGFmZl9waTElNUJzaG93VWlkJTVEPTExMQ__.0.html) at the University of Rostock, Germany.
The contents are provided as [Open Educational Resource](https://de.wikipedia.org/wiki/Open_Educational_Resources)
, so feel free to fork, share, teach and learn.
You can give the project a [Star](https://github.com/spatialaudio/signals-and-systems-lecture/stargazers)
if you like the notebooks.

## Getting Started

The Jupyter notebooks are accessible in various ways

* Online as [static web pages](http://nbviewer.ipython.org/github/spatialaudio/signals-and-systems-lecture/blob/master/index.ipynb)
* Online for [interactive usage](https://mybinder.org/v2/gh/spatialaudio/signals-and-systems-lecture/master?filepath=index.ipynb) with [binder](https://mybinder.org/)
* Local for interactive usage on your computer

Other online services (e.g. [Google Colaboratory](https://colab.research.google.com),
[Microsoft Azure](https://azure.microsoft.com/), ...) provide environments for
interactive execution of Jupyter notebooks as well.
Local execution on your computer requires a local Jupyter/IPython installation.
The [Anaconda distribution](https://www.continuum.io/downloads) can be
considered as a convenient starting point.
Then, you'd have to [clone/download the notebooks from Github](http://github.com/spatialaudio/signals-and-systems-lecture).
Use a [Git](http://git-scm.org/) client to clone the notebooks and then start
your local Jupyter server. For manual installation under OS X/Linux please
refer to your packet manager.


## Concept and Contents

An understanding of the underlying mechanisms and the limitations of basic
signal processing methods is essential for the design of more complex techniques,
such as for example the recent contributions on indirect [detection of supermassive
black holes](https://en.wikipedia.org/wiki/Messier_87)
heavily relying on system identification and image processing.

The present notebooks cover the fundamentals of linear and time-invariant
signals and systems.
A focus is laid on a detailed mathematical treatise.
The discussion of the mathematical background is important to understand the
underlying principles in a more general manner.
The materials contain a series of computational examples and exercises to
interpret the theoretical findings and foster understanding.
The examples are designed to be explored in an interactive manner.
Furthermore, an outlook to practical applications is given whenever possible.

The material is organized in two major blocks, namely

* continuous-time and
* discrete-time (temporal sampling)

signals and systems.
The two blocks become interrelated by the discussion of the ideal temporal
sampling process and its inherent implications on sampled signals.
The didactical layouts for the two blocks are quite similar:

* introduction into signals and LTI systems
* standard signals and operations
* characterization of LTI systems in the time-domain
* spectral representation of signals (Laplace and Fourier transform vs. z- and discrete-time Fourier transform)
* spectral representation of LTI systems
* properties of LTI systems

This allows to observe the similarities and differences between the
continuous- and discrete-time case but otherwise for reading a
block without having studied the other one.


## Usage and Contributing

The contents are provided as [Open Educational Resource](https://de.wikipedia.org/wiki/Open_Educational_Resources).
The text is licensed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/)
, the code of the IPython examples under the [MIT license](https://opensource.org/licenses/MIT).
Feel free to use the entire collection, parts or even single notebooks for your
own purposes.
I am curious on the usage of the provided resources, so feel free to drop a
line or report to [Sascha.Spors@uni-rostock.de](mailto:Sascha.Spors@uni-rostock.de).

Our long-term vision is to lay the grounds for a **community driven concise and
reliable resource** covering the entire theory of signals and systems revised
by research and engineering professionals.
We aim at linking the strengths of both, the good old-fashioned text books
and the interactive playground of computational environments.
Open Educational Resources in combination with open source tools (Jupyter,
Python) and well-established tools for data literacy (git) provide the unique
possibility for collaborative and well-maintained resources.
Jupyter has been chosen due to its seamless integration of text, math and code.
The contents are represented future prove, as simple markdown layout allows for
conversion into many other formats (html, PDF, ...).
The git version management system features tracking of the changes and
authorship.

You are invited to contribute on different levels.
The lowest level is to provide feedback in terms of a
[Star](https://github.com/spatialaudio/signals-and-systems-lecture/stargazers)
if you like the contents.
Please consider reporting errors or suggestions for improvements as
[issues](https://github.com/spatialaudio/digital-signal-processing-lecture/issues).
We are always looking forward to new examples and exercises, as well as
reformulation of existing and novel sub-sections or sections.
Authorship of each considerable contribution will be clearly stated.
One way of introducing reformulated and new material is to handle them as
a tracked [pull request](https://github.com/spatialaudio/signals-and-systems-lecture/pulls).

We are currently working on an accompanying
[exercise repository](https://github.com/spatialaudio/signals-and-systems-exercises)
to gain knowledge and experience on manual calculation of prototypical signal
and systems problems.
This will be online very soon.


## Build Status

The computational examples in the notebooks are automatically build and checked for errors by continuous integration using github actions.

![Integration Test](https://github.com/spatialaudio//signals-and-systems-lecture/actions/workflows/notebook_ci.yml/badge.svg)
