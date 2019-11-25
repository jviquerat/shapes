# Generic imports
import os
import sys
import matplotlib.pyplot as plt

# Imports with probable installation required
try:
    import pygmsh, meshio
except ImportError:
    print('*** Missing required packages, I will install them for you ***')
    os.system('pip3 install pygmsh meshio')
    import pygmsh, meshio

# Custom imports
from shapes_utils import *

### ************************************************
### Generate a shape from in-house csv format
# Check number of input arguments
if (len(sys.argv) != 2):
    print('Incorrect number of input arguments')
    print('Correct usage :')
    print(' python3 generate_shape_from_file.py filename')
    sys.exit(0)

# Retrieve input arguments
filename = sys.argv[1]
if (not os.path.isfile(filename)):
    print('Input file does not exist')
    quit()

# Generate shape
shape = Shape()
shape.read_csv(filename)
shape.generate(ccws=False)
shape.mesh()
shape.generate_image(plot_pts=True)
#shape.write_csv()
