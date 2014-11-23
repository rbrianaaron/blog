Title: Arrays in Python and R
Tags: Python, R
Slug: arrays-in-python-r
Author: Brian Aaron
Summary: Reflection on how to construct an array in Python and R

This post is a learning reflection on arrays in Python versus R. It is to help me sort out the differeces and similariteis betweent two in my mind.

In basic Python, there is no array. There are lists though. One could create two lists and then iterate over them, add the two numbers together, and place them in list.
For example:

```
a = [1,2,3]
b = [4,5,6]
new = []
for i, item in enumerate(c):
    new.append(a[i] + b[i]) 
print new

[5, 7, 9]
```

With Python Numpy, arrays are much simpler. One imports numpy and passes a list of numbers to the array function, for example:

```
a = np.array([1,2,3])
b = np.array([4,5,6])
print a+b

[5 7 9]
```
The result seems like list, but upon calling type() and inpecting it is also a numpy array.

In R, the following is the syntax:

```
> a <- c(1, 2, 3)
> b <- c(4,5,6)
> a + b
[1] 5 7 9
```

I am not sure how R holds the results of arrays that are added together. Hmmmm

How about other types of operations, for example a boolean comparison. The syntax appears to be the same. In Python Numpy:

```
a = np.array([1,2,3])
b = np.array([4,5,6])
print a == b
```

In R:

```
> a <- c(1, 2, 3)
> b <- c(4,5,6)
> a == b
[1] FALSE FALSE FALSE
```

Square root in Python Numpy:

```
print np.sqrt(a)
```

In R:

```
> sqrt(a)
```
