# Custom imports
from shapes import *

### ************************************************
### Generate a random shape from given inputs
filename       = 'shape'
n_pts          = 4
n_sampling_pts = 50
plot_pts       = True
mesh_domain    = False
magnify        = 1.0
domain_h       = 0.2
xmin           =-2.0
xmax           = 5.0
ymin           =-2.0
ymax           = 2.0

# To generate shapes with homogeneous curvatures
radius         = [0.5]
edgy           = [1.0]

# To generate shapes with random curvatures
#radius         = np.random.uniform(low=0.0, high=1.0, size=n_pts)
#edgy           = np.random.uniform(low=0.0, high=1.0, size=n_pts)

# Generate and mesh shape
shape = Shape(filename,
              None,
              n_pts,
              n_sampling_pts,
              radius,
              edgy)
shape.generate(magnify = magnify)
shape.mesh(    mesh_domain = mesh_domain,
               domain_h    = domain_h,
               xmin        = xmin,
               xmax        = xmax,
               ymin        = ymin,
               ymax        = ymax)
shape.generate_image(plot_pts = plot_pts,
                     xmin     = xmin,
                     xmax     = xmax,
                     ymin     = ymin,
                     ymax     = ymax,
                     show_quadrants = True)
shape.write_csv()
