# Linear Algebra

Algebra is arithmetic that includes non-numerical entities like x.

```text
2x + 5 = 25
```

If equation has no exponential term, it is Linear algebra.

If it has an exponential term, it isn't linear algebra, e.g.:

> 2 x<sup>2</sup> + 5 = 25

***Linear Algebra is solving for unkowns within system of Linear equations.***

> **Note**  
> In linear algebra, as lines will be always straight, so there will be options:
>
> * No Solution (Lines are parallel.)
> * Exactly one solution (Lines intercept at one point)
> * Many solutions (Lines are exactly on top of eachother.)

---

## Machine Learning House

<img src="images/machine-learning-house.jpeg" alt="machine-learning-house" style="width: 400px;">

---

## Tensors

Tensor is ML generalization of vectors and matrices to any number of dimensions.  

A tensor is a structured collection of values arranged in 0D, 1D, 2D, or higher dimensions, used to represent data in machine learning.
They are the core data structure in frameworks like TensorFlow and PyTorch.

<img src="images/tensors.jpeg" alt="tensors" style="width: 700px;">

---

## Scalars

* No dimensions
* Single number
* Denoted in lowercase, italics, e.g.: *x*
* Should be typed, like all other tensors: e.g., int, float32

---

## Vectors

* One-dimensional array of numbers
* Denoted in lowercase, italics, bold, e.g.: ***x***
  * Arranged in an order, so element can be accessed by its index
  * Elements are scalars so not bold, e.g., second element of x is x2
* Representing a point in space:
  * Vector of length two, represents location in 2D matrix (shown below)
  * Length of three represents location in 3D cube
  * Length of n represents location in n-dimensional tensor

<img src="images/vectors.jpeg" alt="vectors" style="width: 400px;">

---

## Vector Transposition

<img src="images/vector-transposition.jpeg" alt="vector-transposition" style="width: 500px;">

---

## Zero Vectors

Have no effect if added to another vector.

```text
[0., 0., 0.]
```

---

## Norms

* Vectors represent a magnitude and direction from origin.

* **Norms** are functions that quantify vector magnitude.

> Note:- Magnitude is length of a vector.

<img src="images/norms.jpeg" alt="norms" style="width: 500px;">

---

## L<sup>2</sup> Norm

* Measures simple (Euclidean) disyance from the origin.

* Most common norm in machine learning.
  * Instead of ||***x***||<sub>2</sub>, it can be denoted as ||***x***||

<img src="images/l2norm-formula.jpeg" alt="l2norm-formula" style="width: 300px;">

---

## Unit Vectors

* Special case of vector where its length is equal to one
* Technically, ***x*** is a unit vector with "unit norm", i.e.: ||***x***||<sub>2</sub> = 1

<img src="images/unit-vector.jpeg" alt="unit-vector" style="width: 500px;">

---

## L<sup>1</sup> Norm

* Another common norm in ML
* Varies linearly at all locations whether near or far from origin
* Used whenever difference between zero and non-zero is key

<img src="images/l1norm-formula.jpeg" alt="l1norm-formula" style="width: 300px;">

---

## Squared L<sup>2</sup> Norm

* Computationally cheaper to use than L<sup>2</sup> norm because:
  * Squared L<sup>2</sup> norm equals simply x<sup>T</sup>x.
  * Derivative (used to train many ML algorithms) of element x requires that element alone, whereas L<sup>2</sup> norm requires X vector.
* Downside is it grows slowly near origin so can't be used if distinguishing between zero and near-zero is important.

<img src="images/l2-square-norm-formula.jpeg" alt="l2-square-norm-formula" style="width: 300px;">

---

## Max Norm (or L<sup>∞</sup> Norm)

* Final norm we'll discuss; also occurs frequently in ML.
* Returns the absolute value of the largest-magnitude element.

<img src="images/max-norm-formula.jpeg" alt="max-norm-formula" style="width: 300px;">

---

## Generalized L<sup>p</sup> Norm

* p must be:
* Can derive L<sup>1</sup>, L<sup>2</sup>, and L<sup>∞</sup> norm formulae by substituting for p.
* Norms, particularly L<sup>1</sup> and L<sup>2</sup>, used to regularize objective functions

<img src="images/generalized-lp-norm-formula.jpeg" alt="generalized-lp-norm-formula" style="width: 250px;">

---

## Basis Vectors

* Can be scaled to represent any vector in given vector space.
* Typically use unit vectors along axis of vector space.

<img src="images/basis-vector.jpeg" alt="basis-vector" style="width: 700px;">

---

## Orthogonal Vectors

* x and y are orthogonal vectors if x<sup>T</sup>y = 0.
* Are at 90° angle to each other (assuming non-zero norms).
* n-dimensional space has max n mutually orthogonal vectors (again, assuming non-zero norms)
* Orthonormal vectors are orthogonal and all have unit norm.
  * Basis vectors are an example.

<img src="images/orthogonal-vectors.jpeg" alt="orthogonal-vectors" style="width: 300px;">

---

## Matrices

* Two-dimensional array of numbers.
* Denoted in uppercase, italics, bold, e.g.: ***X***
* Height given priority ahead of width in notation, i.e.: (n<sub>row</sub>, n<sub>col</sub>)
* If ***X*** has three rows and two columns, its shape is (3, 2).
* Individual scalar elements denoted in uppercase, italics only.
  * Element in top-right corner of matrix ***X*** above would be *X*<sub>1</sub>, <sub>2</sub>
* Colon represents an entire row or column:
  * Left column of matrix ***X*** is *X*<sub>:</sub>, <sub>1</sub>
  * Middle row of matrix ***X*** is *X*<sub>2</sub>, <sub>:</sub>

<img src="images/matrices.jpeg" alt="matrices" style="width: 300px;">

---

## Generic Tensor Notation

* Upper-case, bold, italics, sans serif, e.g., ***X***
* In a 4 tensor X, element at position (i, j, k, l) denoted as *X* <sub>(i, j, k, l)</sub>
* Rank 4 tensors are common for images.

---

## Tensor Transposition

* Transpose of scalar is itself, e.g.: x<sup>T</sup> = x
* Transpose of vector, seen earlier, converts column to row (and vice versa)
* Scalar and vector transposition are special cases of matrix transposition:
  * Flip of axes over main diagonal such that:  
  
    (***X***<sup>T</sup>)<sub>i, j</sub> = ***X***<sub>j, i</sub>

<img src="images/matrix-transpose.jpeg" alt="matrix-transpose" style="width: 500px;">

---

## Hadamard product Or element-wise product or Schur product

* A mathematical operation on two matrices of the same dimensions. It returns a new matrix of the same size, where each element is the product of the corresponding elements from the original matrices.
* For two matrices A and B of size m × n, their Hadamard product produces a matrix C of the same size.  

<img src="images/hadamard-product.jpeg" alt="hadamard-product" style="width: 200px;">

---

## The Dot Product

* If we have two vectors (say, x and y) with the same length n, we can calculate the dot product between them. This is annotated several different ways, including the following:
  * x . y
  * x<sup>T</sup> y

* Regardless which notation you use (I prefer the first), the calculation is the same; we calculate products in an element-wise fashion and then sum reductively across the products to a scalar value.
* The dot product is ubiquitous in deep learning: It is performed at every artificial neuron in a deep neural network, which may be made up of millions (or orders of magnitude more) of these neurons.

---

## Solving Linear Systems - Using Elimination Method

* Typically best option if no variable in system has coefficient of 1
* Use addition property of equations to eliminate variables
  * If necessary, multiply one or both equations to make elimination of a variable possible
* For example, solve for the unknowns in the following system:  

  2x - 3y = 15  
  4x + 10y = 14
* ..by multiplying the first equation by -2 and adding the equations.

---

## Matrix Multiplication

<img src="images/matrix-multiplication.jpeg" alt="matrix-multiplication" style="width: 500px;">

---

## Symmetric Matrix

* Special matrix case with following properties:
  * It's always a square matrix
  * ***X***<sup>T</sup> = ***X***

<img src="images/symmetric-matrix.jpeg" alt="symmetric-matrix" style="width: 250px;">

---

## Identity Matrix

* Symmetric matrix where:
  * Every element along main diagonal is 1
  * All other elements are 0
  * Notation: I<sub>n</sub> where n = height (or width)
  * n-length vector unchanged if multiplied by ***I***<sub>n</sub>

<img src="images/identity-matrix.jpeg" alt="identity-matrix" style="width: 250px;">

---

## Frobenius Norm

* Analogous to L<sup>2</sup> norm of vector
* Measures the size of matrix in terms of Euclidean distance
  * It's the sum of the magnitude of all the vectors in ***X***

<img src="images/frobenius-norm.jpeg" alt="frobenius-norm" style="width: 350px;">

---

## Matrix Inversion

* Clever, convenient approach for solving linear equations
* An alternative to manually solving with substitution or elimination

* **Matrix inverse** of ***X*** is denoted as ***X<sup>-1</sup>***
  * Satistles: ***X<sup>-1</sup> X*** = ***I***<sub>n</sub>

<img src="images/identity-matrix.jpeg" alt="identity-matrix" style="width: 250px;">

---

## Solve Using Matrix Inversion

<img src="images/solve-using-matrix-inversion-1.jpeg" alt="solve-using-matrix-inversion-1" style="width: 650px;">

<img src="images/solve-using-matrix-inversion-2.jpeg" alt="solve-using-matrix-inversion-2" style="width: 650px;">

<img src="images/solve-using-matrix-inversion-3.jpeg" alt="solve-using-matrix-inversion-3" style="width: 650px;">

---

## Matrix Inversion Limitations

* Nifty trick, but can only be calculated if:
  * Matrix is square: n<sub>row</sub> == n<sub>col</sub>
    * Avoid **overdetermination**: n<sub>row</sub> > n<sub>col</sub>
    * Avoid **underdetermination**: n<sub>row</sub> < n<sub>col</sub>
  * Matrix isn't "singular"
  * That is, all columns of matrix must be linearly independent
    * E.g., if a column is [1, 2], another can't be [2, 4]. This indicates that we have lines running in parallel to each other.
    * E.g., if a column is [1, 2], another can't be [1, 2]. In this case we will have infinite number of silutions.

<img src="images/overdetermined-underdetermined.jpeg" alt="overdetermined-underdetermined" style="width:700px;">

<img src="images/matrix-inversion-limitations.jpeg" alt="matrix-inversion-limitations" style="width:700px;">

---

## Diagnoal Matrix

* Nonzero elements along main diagonal; zeros everywhere else
* Identity matrix is an example
* If square, denoted as diag(x) where x is vector of main-diagonal elements
* Computationally efficient:
  * Multiplication: diag(x)y = x dot-product y
  * Inversion: diag(x)<sup>-1</sup> = diag[1/x<sub>1</sub>, ..., 1/x<sub>n</sub>]<sup>T</sup>

---

## Orthogonal Matrices

* Recall orthonormal vectors from earlier:  

<img src="images/orthogonal-vectors.jpeg" alt="orthogonal-vectors" style="width: 300px;">

* In orthogonal matrices, orthonormal vectors:
  * Make up all rows
  * Make up all columns
* This means: A<sup>-T</sup>A = AA<sup>T</sup> = ***I***
* Which also means: A<sup>T</sup> = A<sup>-1</sup> ***I*** = A<sup>-1</sup>
* Calculating A<sup>T</sup> is cheap, therefore so is calculating A<sup>-1</sup>

---

## Trace Operator

* Denoted as Tr(***A***)
* Simply the sum of the diagnoal elements of a matrix

<img src="images/trace-operation.jpeg" alt="trace-operation" style="width: 100px;">

* In particular, the trace operator can provide a convenient way to calculate a matrix's Frobenius norm:

<img src="images/trace-frobenius.jpeg" alt="trace-frobenius" style="width: 300px;">

---

## Eigen Vectors

<img src="images/eigen-vectors-monaliza-1.jpeg" alt="eigen-vectors-monaliza-1" style="width: 800px;">

<img src="images/eigen-vectors-monaliza-2.jpeg" alt="eigen-vectors-monaliza-2" style="width: 800px;">

---

## Eigen Values

<img src="images/eigen-values-monaliza.jpeg" alt="eigen-values-monaliza" style="width: 800px;">

<img src="images/eigen-values-monaliza-2.jpeg" alt="eigen-values-monaliza-2" style="width: 800px;">

---

## Eigen Vector

* An eigenvector (eigen is German for "typical"; we could translate eigenvector to "characteristic vector") is a special vector x  such that when it is transformed by some matrix (let's say A), the product Ax has the exact same direction as x.

---

## Eigen Value

* An eigenvalue is a scalar (traditionally represented as λ) that simply scales the eigenvector x such that the following equation is satisfied:  
Ax = λx

---

## Matrix Determinants

* Map square matrix to scalar
* Enable us to determine whether matrix can be inverted

* For matrix X, denoted as det(X)
* If det(X) = 0:
  * Matrix X<sup>-1</sup> can't be computed because: X<sup>-1</sup> has 1/det (X) = 1/0 
  * Matrix X is singular: It contains linearly-dependent columns
* det(x) easiest to calculate for 2x2 matrix...

<img src="images/determinant-matrix-2by2.jpeg" alt="determinant-matrix-2by2" style="width: 600px;">

---

## Generalizing Determinants: Recursion

* We can only measure for square matrix.

<img src="images/determinant-matrix-recursion.jpeg" alt="determinant-matrix-recursion" style="width: 700px;">

<img src="images/determinant-matrix-recursion-3by3.jpeg" alt="determinant-matrix-recursion-3by3" style="width: 700px;">

---

## Determinants & Eigenvalues

* det(X) = product of all eigenvalues of X

* |det(X)| quantifies volume change as a result of applying X:
  * If det(X) = 0, then X collapses space completely in at least one dimension, thereby eliminating all volume
  * If 0 < det(X) < 1, then X contracts volume to some extent
  * If det(X) = 1, then X preserves volume exactly
  * If det(X) > 1, then X expands volume

---

## Eigen Decomposition

* The decomposition of a matrix into eigenvectors and eigenvalues reveals characteristics of the matrix, e.g.:
  * Matrix is singular if and only if any of its eigenvalues are zero
  * Under specific conditions (see §2.7 of Goodfellow et al., 2016), can optimize quadratic expressions:
    * Maximum of f(x) = largest eigenvalue
    * Minimum of f(x) = smallest eigenvalue

<img src="images/matrix-type.jpeg" alt="matrix-type" style="width: 500px;">

* Applying a matrix of a particular type to some vector x can have a characteristic impact (again, see §2.7 of Goodfellow et al., 2016).