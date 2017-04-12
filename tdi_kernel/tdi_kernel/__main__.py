from ipykernel.kernelapp import IPKernelApp
from . import TdiKernel

IPKernelApp.launch_instance(kernel_class=TdiKernel)
