from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy
import subprocess

proc_libs = subprocess.check_output("pkg-config --libs opencv".split())
proc_incs = subprocess.check_output("pkg-config --cflags opencv".split())
# libs = [lib for lib in str(proc_libs, "utf-8").split()]
libs = [lib for lib in str(proc_libs).split()]
#print("OPENCV LIBS=", libs)

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = cythonize(Extension("opencvsample",
                                      sources = ["opencvsample.pyx"],
                                      language = "c++",
                                      include_dirs=[numpy.get_include(), "/usr/local/Cellar/opencv/2.4.5/include/"],
                                      extra_link_args=libs
                                      )
                            )
)