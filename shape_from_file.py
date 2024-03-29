# Generic imports
import os
import sys
import pygmsh, meshio

# Custom imports
from shapes import *

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
shape.generate(ccws=True,
               centering=True)
shape.mesh()
shape.generate_image(plot_pts=True,
                     show_quadrants=False,
                     xmin=-2.0, xmax=2.0,
                     ymin=-2.0, ymax=2.0)
