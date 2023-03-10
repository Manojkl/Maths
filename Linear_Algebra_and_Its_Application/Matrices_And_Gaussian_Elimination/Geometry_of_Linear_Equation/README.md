# Geometry of linear equations

Given two equation and two unknown, find the value of the ubknwon.

Two equations <br>
2x - y = 1 <br>
x +y= 5 <br>

Ans: x = 2, y = 3

First approach

In the first form of equation the line passes through (2,3). The intersecting points between the two lines. Solving these equation by adding and subtracting leads us to (2,3).

Second approach involve column form of the equation. 
Column form is given by

$$
x*\left(\begin{array}{cc} 
2 \\
1 
\end{array}\right) + y*
\left(\begin{array}{cc} 
-1 \\ 
1 
\end{array}\right) = 
\left(\begin{array}{cc} 
1 \\ 
5 
\end{array}\right)
$$

The vectors (2,1) and (-1, 1) are represented by bold lines. The unknown are the numbers x and y that multiply the column vector. if we multiply 2 times the column 1 and 3 times the column 2 will result in parallelogram meeting at point (1, 5). Right side of the equation.

For a 3 variable equation lot of varities of data can be made. 

1. 2u + v + w = 5
2. 4u - 6v    = -2
3. -2u+7v+2w = 9

The first equation of plane meets the three cooridnates at (5/2, 0,0), (0,5,0), (0,0,5). 
If we multiply the right hand side 5 by 2, 2u +v +w = 10 will give a plane parallel to the first plane. If right hand side is zero then the plane goes through the origin.

Second equation is also a plane, even though the coefficients of w is zero. The second plane intersect with the first plane and the intersection is a line. 

The third plane intersect the first two planes at a point u = 1, v = 1, and w = 2. Thats is the solution of three equations.

n equations contains n unknwons.

For visualization see [3D planes intersection](https://www.geogebra.org/m/pjczxakm#)

 
 [3D plot](https://www.geogebra.org/3d?lang=en)

 If time is the fourth dimension, then the plane t = 0 cuts throuth the four-dimensional space and produces the three-dimensional universe we live in. Another plane is z=0, which is also 3D.

First equation produces an (n-1) dimensional plane in n dimensions. And 2nd equation intersects and reduce the dimension by n-2 in n dimensions. Every equation reduces the dimensions, given they intersect.

# Column Vectors and Linear Combinations

The three equations

1. 2u + v + w = 5
2. 4u - 6v    = -2
3. -2u+7v+2w = 9

can be written in vector form

$$
u*\left(\begin{array}{cc} 
2 \\
4 \\
-2 
\end{array}\right) + v*
\left(\begin{array}{cc} 
1 \\ 
-6 \\
7
\end{array}\right) + w*
\left(\begin{array}{cc} 
1 \\ 
0 \\
2
\end{array}\right) = 
\left(\begin{array}{cc} 
5 \\ 
-2 \\
9
\end{array}\right) = b
$$

- The vector is represented with (5, -2, 9)
- Descartes matched the three dimensional point to a vector.
- The result [5, -2, 9] is the linear combination of [5, 0, 0] + [0, -2, 0] + [0, 0, 9].
- The result [5, -2, 9] is also a linear combination of 1*[2, 4, -2] + 1*[1, -6, 7] + 2*[1, 0, 2]. This is obtained by multiplying the vector by a scalar.
- With n equations and n unknowns, there are n planes and n vectors in the column picture. 

- Some times there exist a linear combination and sometimes not. When there does not exist a linear combination, it is called as the singular case.

# The Singular Case

- Parallel plane give no solution
- There are four conditions for three planes, two parallel plane intersect with the third plane
- No intersection of planes, however, two planes intersect and the intersection is a line. And the intersection lines are parallel to each other.

1. u + v + w = 2
2. 2u + 3w = 5
3. 3u+v+4w = 6

- The above system is a singular case, since no solution available.
- The equations are inconsistent. Systematically shown by Gaussian elimination.
- Another singular system has infinity of solutions.
- 





