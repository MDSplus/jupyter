mdstcl_kernel
===========

``mdstcl_kernel`` is a simple example of a Jupyter kernel. Find the documentation on wrapper kernels here:

http://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html

Installation
------------
To install ``mdstcl_kernel`` ::

    git clone http://github.com/MDSplus/jupyter
    cd jupyter/tcl_kernel
    python setup.py install
    python -m mdstcl_kernel.install

Using the TDI kernel
---------------------
**Notebook**: The *New* menu in the notebook should show an option for a tcl notebook.

**Console frontends**: To use it with the console frontends, add ``--kernel mdstcl`` to
their command line arguments.
