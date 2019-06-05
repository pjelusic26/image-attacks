# image-attacks
A series of geometrical image attacks, prepared for batch editing.

----------

In order to evaluate a certain watermarking method, large amount of image files are supposed to go through a series of geometrical attacks such as:
- scaling
- rotation
- affine transformation
- 2d convolution
- gaussian blur

The idea is to have a single Python script to run all transformations at once, while also saving transformed photos into appropriate folders.

Similarly to my previous projects, I used five photos taken in the Philippines, because you can never have too much Summer, even if it's just on the screen :)

----------

Resources I found useful for the project:

https://gist.github.com/agalea91/80fa59d7ebc6491ae5a18941be2924eb

https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html

https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html
