# Nuit Du Hack CTF Quals 2017 You have been terminated
### Category: Steganography, 50 points

> You found this strange image on a computer, I heard there is a hidden message in it... Can you find it ?
> Hint 1: I heard a cat... Hint 2: There are multiple implementations of this algorithm

### Write-up

We start off with a picture like this.




![Chill out](http://i.imgur.com/s4gzIhh.jpg)

The first hint points us toward an algorithm called [Arnold's Cat Map](https://en.wikipedia.org/wiki/Arnold%27s_cat_map)

As hint 2 mentions, there are multiple implementations and some doens't seem to work.

First off I tried Jason Davies [Catmap](https://www.jasondavies.com/catmap/)
But it didn't seem to work. 

After that I found [Zhanxw Cat](https://github.com/zhanxw/cat)

However it's four years old so some modifications had to be done to make it running.


Here's the modified script

```python
import PIL.Image
from numpy import *
#from scipy.misc import lena,imsave
#from scipy.misc import imsave

# load image
im = array(PIL.Image.open("o.jpg"))
N = 56

# create x and y components of Arnold's cat mapping
x,y = meshgrid(range(N),range(N))
xmap = (2*x+y) % N
ymap = (x+y) % N

for i in xrange(N+1):
 result = PIL.Image.fromarray(im)
 result.save("cat_%03d.png" % i)
 im = im[xmap,ymap]
```
Each frame is saved as an individuall png.

> $ python2.7 cat.py

![25 Hour Fitness](i.imgur.com/v3wyAdQ.gif)

> $-->calif0rnia_g0vern0r<--$