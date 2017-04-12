from ipykernel.kernelapp import IPKernelApp
from . import TclKernel

IPKernelApp.launch_instance(kernel_class=TdiKernel)
