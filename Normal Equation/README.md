<h3>NORMAL EQUATION FOR LINEAR REGRESSION</h3>

Normal equation is the method(basically an equation) that uses Linear Algebra to compute the weights for our features.
(Analytical Solution to regression)

<br><br>
<b>
Normal Equation :  
<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=(X^{T}X)^{-1}X^{T}Y" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(X^{T}X)^{-1}X^{T}Y" title="(X^{T}X)^{-1}X^{T}Y" /></a>
</p>
</b>
<h4>Deriving the normal equation :</h4>


Cost function for linear regression is :
<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=J(\theta)&space;=&space;\frac{1}{2m}\sum_{i=1}^{m}[h_{\theta&space;}(X)&space;-&space;Y]^{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J(\theta)&space;=&space;\frac{1}{2m}\sum_{i=1}^{m}[h_{\theta&space;}(X)&space;-&space;Y]^{2}" title="J(\theta) = \frac{1}{2m}\sum_{i=1}^{m}[h_{\theta }(X) - Y]^{2}" /></a>
</p>
Writing the equation in matrix notation, we have,
<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=J(\theta)&space;=&space;\frac{1}{2m}(\theta^{T}X-Y)^{T}(\theta^{T}X-Y)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J(\theta)&space;=&space;\frac{1}{2m}(\theta^{T}X-Y)^{T}(\theta^{T}X-Y)" title="J(\theta) = \frac{1}{2m}(\theta^{T}X-Y)^{T}(\theta^{T}X-Y)" /></a>
</p>
Simplifying the above equation,

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=J(\theta)&space;=&space;\frac{1}{2m}(\theta^{T}X^{T}X\theta-2\theta^{T}X^{T}Y&plus;Y^{T}Y)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J(\theta)&space;=&space;\frac{1}{2m}(\theta^{T}X^{T}X\theta-2\theta^{T}X^{T}Y&plus;Y^{T}Y)" title="J(\theta) = \frac{1}{2m}(\theta^{T}X^{T}X\theta-2\theta^{T}X^{T}Y+Y^{T}Y)" /></a>
</p>
To minimize the cost function, we differentiate the cost function,

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;J(\theta)}{\partial&space;\theta}&space;=X^{T}X\theta-2X^{T}Y&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;J(\theta)}{\partial&space;\theta}&space;=X^{T}X\theta-2X^{T}Y&space;=&space;0" title="\frac{\partial J(\theta)}{\partial \theta} =X^{T}X\theta-2X^{T}Y = 0" /></a>
</p>
<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=X^{T}X\theta=X^{T}Y" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X^{T}X\theta=X^{T}Y" title="X^{T}X\theta=X^{T}Y" /></a>
</p>

Solving for theta, we get,

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=\theta=(X^{T}X)^{-1}X^{T}Y" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta=(X^{T}X)^{-1}X^{T}Y" title="\theta=(X^{T}X)^{-1}X^{T}Y" /></a>
</p>

So, we can directly use this equation for finding the weights(theta) required to make predictions.


<br><br><br>
<h5>Pros :</h5>
1. Easier to calculate.<br>
2. Gives exact weights values.

<h5>Cons :</h5>
1. For huge dataset, may take a lot of time to compute as the time complexity to find inverse is O(N^3). (N is the dimension of the matrix)

<h5>Note(Caution) :</h5>
The inverse may not always exist. So, we find pseudoinverse for calculation.
Using Regularization guarantees the existense of inverse.
