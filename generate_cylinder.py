# Custom imports
from shapes_utils import *

### ************************************************
### Generate a cylinder from given inputs
filename       = 'shape'
n_pts          = 4
n_sampling_pts = 10
plot_pts       = True
mesh_domain    = True
magnify        = 2.0
cylinder       = True
shape_h        = 1.0
domain_h       = 1.0

# To generate shapes with homogeneous curvatures
radius         = [0.5528] # Optimal value using 4 points
edgy           = [0.5]

# Generate and mesh shape
shape = Shape(filename,
              None,
              n_pts,
              n_sampling_pts,
              radius,
              edgy)
shape.generate(magnify=magnify,
               cylinder=cylinder)
shape.mesh(mesh_domain=mesh_domain,
           shape_h=shape_h,
           domain_h=domain_h)
shape.generate_image(plot_pts=plot_pts)
shape.write_csv()
