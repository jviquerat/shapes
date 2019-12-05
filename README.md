# bezier_shapes

Tools to generate random shapes using Bezier curves (images and meshes), controlling the number of points and the local curvature. It is also possible to generate shapes by joining specified points using an in-house csv format.

## CSV format

```
n_pts n_splg_pts
x1 y1 r1 e1
x2 y2 r2 e2
...
xn yn rn en
```

- ```n_ctrl_pts``` is the actual number of points you control on the shape. Each such point is joined with the next one using a cubic Bezier curve
- ```n_splg_pts``` is the number of sampling points between two control points
- ```xi yi``` are the coordinates of the control points
- ```ri``` is the local radius around control point ```i```. It measures how far the local control points are from the point you provided
- ```ei``` is a local measure of sharpness

Give a look at the examples below for a better understanding of the effects of radius and sharpness parameters.

## Shape examples

The best approximation of a cylinder using 4 points:

```
4 30
1.0 1.0 0.5587 1.0
-1.0 1.0 0.5587 1.0
-1.0 -1.0 0.5587 1.0
1.0 -1.0 0.5587 1.0
```

<img width="430" alt="" src="https://user-images.githubusercontent.com/44053700/70216021-03a8e400-173f-11ea-8a25-b2a5ee1867fa.png"> <img width="430" alt="" src="https://user-images.githubusercontent.com/44053700/70216014-00155d00-173f-11ea-96fa-c1357e9f14ec.png">

Increasing radius on top left, while decreasing it on bottom right:

```
4 30
1.0 1.0 0.5587 1.0
-1.0 1.0 1.0 1.0
-1.0 -1.0 0.5587 1.0
1.0 -1.0 0.0 1.0
```

<img width="430" alt="" src="https://user-images.githubusercontent.com/44053700/70216167-45d22580-173f-11ea-987b-8c7f3624bc6a.png"> <img width="430" alt="" src="https://user-images.githubusercontent.com/44053700/70216198-55ea0500-173f-11ea-803d-b5ebe7363552.png">

Making a sharp edge on bottom right:

```
4 30
1.0 1.0 0.5587 1.0
-1.0 1.0 0.5587 1.0
-1.0 -1.0 0.5587 1.0
1.0 -1.0 0.5587 0.0
```
<img width="430" alt="" src="https://user-images.githubusercontent.com/44053700/70215840-a4e36a80-173e-11ea-9300-30b6bd9b6299.png"> <img width="430" alt="" src="https://user-images.githubusercontent.com/44053700/70215882-bdec1b80-173e-11ea-8a1c-a492b8a98ce3.png">

## Random shape

Generated using ```python3 generate_shape_random.py```:

```
10 10
-0.22344386973718572 -0.11579347020968898 0.5 1.0
-1.086703349116176 0.056471511909076864 0.5 1.0
0.33918645130375696 -0.6285322803621614 0.5 1.0
0.09673486000147186 0.020665843303720587 0.5 1.0
0.7184144807034846 0.07933772977561572 0.5 1.0
0.658776975915066 -0.5602669680651731 0.5 1.0
-0.5629917814532847 0.37355108023884465 0.5 1.0
-0.5526944074292542 0.6349363861837116 0.5 1.0
0.44487187686581814 -0.19528679943835178 0.5 1.0
0.16784876294630274 0.3349169666644063 0.5 1.0
```

<img width="430" alt="" src="https://user-images.githubusercontent.com/44053700/69552201-598ec680-0f9e-11ea-941d-747dda258a97.png"> <img width="430" alt="" src="https://user-images.githubusercontent.com/44053700/69552144-3d8b2500-0f9e-11ea-91e2-03dd8127c7d4.png">

## Shape generated from file

Generated using ```python3 generate_shape_from_file.py myfile.csv```:

```
4 30
-1.0 0.0 0.5 1.0
0.0 0.1 0.5 1.0
1.0 0.0 0.5 1.0
-0.5 0.4 0.5 1.0
```

<img width="430" alt="" src="https://user-images.githubusercontent.com/44053700/69552480-d0c45a80-0f9e-11ea-90b4-811aafc39dcd.png"> <img width="430" alt="" src="https://user-images.githubusercontent.com/44053700/69552712-357fb500-0f9f-11ea-8008-2277b9cd6a60.png">
