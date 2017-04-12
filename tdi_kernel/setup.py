from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='tdi_kernel',
    version='1.1',
    packages=['tdi_kernel'],
    description='MDSplus tdi kernel for Jupyter',
    long_description=readme,
    author='MDSplus Development Team',
    author_email='twf@mdsplus.org',
    url='https://github.com/MDSplus/tdi_kernel',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
)
