# Generic imports
import os
import random
import shutil
from   datetime import datetime

# Imports with probable installation required
try:
    import progress.bar
except ImportError:
    print('*** Missing required packages, I will install them for you ***')
    os.system('pip3 install progress')
    import progress.bar

# Custom imports
from shapes_utils import *
from meshes_utils import *

### ************************************************
### Generate full dataset
# Parameters
n_sampling_pts = 50
mesh_domain    = False
plot_pts       = True
show_quadrants = True
n_shapes       = 200
time           = datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
dataset_dir    = 'dataset_'+time+'/'
mesh_dir       = dataset_dir+'meshes/'
img_dir        = dataset_dir+'images/'
filename       = 'shape'
magnify        = 1.0
xmin           =-2.0
xmax           = 2.0
ymin           =-2.0
ymax           = 2.0
n_tri_max      = 5000

# Create directories if necessary
if not os.path.exists(mesh_dir):
    os.makedirs(mesh_dir)
if not os.path.exists(img_dir):
    os.makedirs(img_dir)

# Generate dataset
bar = progress.bar.Bar('Generating shapes', max=n_shapes)
for i in range(0,n_shapes):

    generated = False
    while (not generated):

        #n_pts  = random.randint(3, 7)
        n_pts = 4
        radius = np.random.uniform(0.0, 1.0, size=n_pts)
        edgy   = np.random.uniform(0.0, 1.0, size=n_pts)
        shape  = Shape(filename+'_'+str(i),
                       None,
                       n_pts,
                       n_sampling_pts,
                       radius,
                       edgy)

        shape.generate(magnify=1.0,
                       xmin=xmin,
                       xmax=xmax,
                       ymin=ymin,
                       ymax=ymax)
        meshed, n_tri = shape.mesh()

        if (meshed and (n_tri < n_tri_max)):
            shape.generate_image(plot_pts=plot_pts,
                                 xmin=xmin,
                                 xmax=xmax,
                                 ymin=ymin,
                                 ymax=ymax,
                                 show_quadrants=True)
            img  = filename+'_'+str(i)+'.png'
            mesh = filename+'_'+str(i)+'.mesh'
            shutil.move(img,  img_dir)
            shutil.move(mesh, mesh_dir)
            generated = True

    bar.next()

# End bar
bar.finish()
