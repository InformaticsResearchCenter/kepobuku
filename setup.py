from distutils.core import setup
from Cython.Build import cythonize

setup(
<<<<<<< HEAD
    ext_modules = cythonize("kepo.py")
=======
    ext_modules = cythonize(["kepo.py", "kepointernship.py"])
>>>>>>> f3bde7251d0a2bdecbc321ee90a91e4923e42adf
)
