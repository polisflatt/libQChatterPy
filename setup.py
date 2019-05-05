import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='libQChatterPy',  
     version='0.5',
     packages=['libqchatterpy'],
     author="Polis Flatt",
     author_email="polisflatt@gmail.com",
     url="https://github.com/polisflatt/libQChatterPy",
     description="A Python library for interfacing with the QChatterServer service.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='GPL v3',
 )