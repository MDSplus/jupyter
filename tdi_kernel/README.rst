echo_kernel
===========

``tdi_kernel`` is a simple example of a Jupyter kernel. Find the documentation on wrapper kernels here:

http://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html

Installation
------------
To install ``tdi_kernel`` ::

    git clone http://github.com/MDSplus/jupyter
    cd tdi_kernel
    python setup.py install
    python -m twf_kernel.install

Using the TDI kernel
---------------------
**Notebook**: The *New* menu in the notebook should show an option for an Echo notebook.

**Console frontends**: To use it with the console frontends, add ``--kernel tdi`` to
their command line arguments.
