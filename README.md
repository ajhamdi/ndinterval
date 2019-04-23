# ND-Interval: Doing arithmetic on high dimensional intervals 

With ND-Interval, you can construct high dimensnional intervals as data structures and do aritmetic operations directly on these intervals   

# Overview
The ND-Interval Python package was written with fast use in mind. It provides the following key features

  - construct n dimensional intervals .
  - do operations on n dimensional intervals like AND and OR to construct complex intervals
  - measure sizres of high dimensional intervals  
  - batch operations on nd-intervals for scaling operations on intervals 


## Usage

In the following paragraphs, I am going to describe how you can get and use ndinterval for your own projects.

###  Getting it

To download ndinterval, either fork this github repo or simply use Pypi via pip.
```sh
$ pip install ndinterval
```

### Using it

ndinterval was programmed with ease-of-use in mind. First, import the package

```Python
import ndinterval as ndinterval
```

And you are ready to go! At this point, 

## Examples:
Here is a list of examples of operations that you can do with nd-intervals 

### 1.Construct ND-intervals 
Method: `ndinterval(a,b)`
Args: 
- `a`: iteratable-like left most corner point of the high dimensional interval   
- `b`:iteratable-like right most corner point of the high dimensional interval

```Python
interval_1 = ndinterval([0,2],[3,8]) ;  interval_2 = ndinterval([2,20],[30,50])
print('interval 1 : ',interval_1, "size:", interval_1.size() )
print('interval 2 : ',interval_2, "size:", interval_2.size() )

```
will output :
>interval 1 :  [interval([0.0, 3.0]), interval([2.0, 8.0])] size: 18.0
>interval 2 :  [interval([2.0, 30.0]), interval([20.0, 50.0])] size: 840.0
### 2.Union of n dimensional intervals 

```Python
interval_union = interval_1 | interval_2
print('union of interval 1 and 2 : ',interval_union )
```
will output :
>union of interval 1 and 2 :  [interval([0.0, 30.0]), interval([2.0, 8.0], [20.0, 50.0])]

### 3.Intersection of n dimensional intervals 
```Python
interval_intersection = interval_1 & interval_2
print('intersection of interval 1 and 2 : ',interval_intersection )
```
will output :
>intersection of interval 1 and 2 :  [interval([2.0, 3.0]), interval()]


License
----

MIT License

Copyright (c) 2019 Abdullah Hamdi


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
