from ipykernel.kernelapp import IPKernelApp
from . import MdstclKernel

IPKernelApp.launch_instance(kernel_class=MdstclKernel)
