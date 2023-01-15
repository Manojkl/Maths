# System of linear equation

Given two equation and two unknown, find the value of the ubknwon.

Two equations <br>
1x + 2y = 3 <br>
4x +5y= 6 <br>

Ans: x = -1, y = 2

# Gaussian Elimination

Equation

$$
\left(\begin{array}{cc} 
1 & 2\\
4 & 5
\end{array}\right) =
\left(\begin{array}{cc} 
3 \\ 
6 
\end{array}\right)
$$

$$ x = 
det\left(\begin{array}{cc} 
3 & 2\\
6 & 5
\end{array}\right) /det \left(\begin{array}{cc} 
1 & 2\\
4 & 5
\end{array}\right) = (15- 12)/(5-8) = -1$$

$$ y = 
det\left(\begin{array}{cc} 
1 & 3\\
4 & 6
\end{array}\right) /det \left(\begin{array}{cc} 
1 & 2\\
4 & 5
\end{array}\right) = (6 - 12)/(5 - 8) = 2$$

Four aspectes are addressed in this chapter

- Geometry of planes: Visualizing the geometry with the moving into the linear algebra domain?
- Matrix notation: Writing n unknown as a vector x and the n equation as Ax = b. Elimination matrices are the one that makes certain values in the matrix goes zero after multiplying with it, thereby we can get the lower triangular and upper triangular matrix. Every matrix has a transpose. A matrix has inverse if the determinant is not zero. 

Factorization

$$
\left(\begin{array}{cc} 
1 & 2\\
4 & 5
\end{array}\right) =
\left(\begin{array}{cc} 
1 & 0\\ 
4 & 1
\end{array}\right)
\left(\begin{array}{cc} 
1 & 2\\ 
0 & -3
\end{array}\right) = L times U
$$

Ax = b form

$$
\left(\begin{array}{cc} 
1 & 2\\
4 & 5
\end{array}\right)\left(\begin{array}{cc} 
x \\ 
y 
\end{array}\right) =
\left(\begin{array}{cc} 
3 \\ 
6 
\end{array}\right)
$$

- Matrix is singular if it is not invertible.

- Why Gaussian elimination is needed when we can do normal subtraction or addition of equation to find the solution?

- Number of elimination steps needed to solve system of size n. The cost computing and accuracy is the major issue with normal subtraction and addition to solve n equation. n being very large. 
- 100 equations need 1/3 million steps. As the number of equations grows and reaches million steps then roundoff error comes into picture. So to solve large number of equations without compromising on the accuracy and computation cost Gaussian elimination is the algorithm. 
- AI found news ways to multiply two matrices efficiently. [Disovering novel algorithms with AlphaTensor](https://www.deepmind.com/blog/discovering-novel-algorithms-with-alphatensor?utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform).




