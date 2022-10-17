{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b630792d",
   "metadata": {},
   "source": [
    "# ASSIGNMENT 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8a3bad34",
   "metadata": {},
   "source": [
    "# Problem Statement1: Write a Python program to multiply a M × N matrix by N × A matrix and create a real matrix product."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "b44a0987",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "M x N matrix:\n",
      "[[0.36910578 0.85800456 0.24650185]\n",
      " [0.00465381 0.01192472 0.18626309]\n",
      " [0.54400063 0.32288508 0.29200923]\n",
      " [0.1317586  0.45209927 0.00994235]\n",
      " [0.66512824 0.57206007 0.47739533]]\n",
      "N x A matrix:\n",
      "[[0.18547276 0.32953909]\n",
      " [0.40233136 0.96140757]\n",
      " [0.62183382 0.37417787]]\n",
      "Real matrix product:\n",
      "[[0.56694439 1.0387624 ]\n",
      " [0.12148553 0.08269366]\n",
      " [0.41238531 0.59895703]\n",
      " [0.21251383 0.48179147]\n",
      " [0.65038143 0.94779941]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "m = 5\n",
    "n = 3\n",
    "a = 2\n",
    "x = np.random.random((m,n))\n",
    "print(\"M x N matrix:\")\n",
    "print(x)\n",
    "y = np.random.random((n,a))\n",
    "print(\"N x A matrix:\")\n",
    "print(y)\n",
    "z = np.dot(x, y)\n",
    "print(\"Real matrix product:\")\n",
    "print(z)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0078fc71",
   "metadata": {},
   "source": [
    "# Problem Statement2: Write a NumPy program to check if each element of an array of your choice is composed of digits, lower case letters, and upper case letters only."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "c431ee97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Array:\n",
      "['Python' 'PHP' 'JS' 'Examples' 'html5' '5']\n",
      "Digits only = [False False False False False  True]\n",
      "Lower cases only = [False False False False  True False]\n",
      "Upper cases only = [False  True  True False False False]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x = np.array(['Python', 'PHP', 'JS', 'Examples', 'html5', '5'])\n",
    "print(\"Original Array:\")\n",
    "print(x)\n",
    "r1 = np.char.isdigit(x)\n",
    "r2 = np.char.islower(x)\n",
    "r3 = np.char.isupper(x)\n",
    "print(\"Digits only =\", r1)\n",
    "print(\"Lower cases only =\", r2)\n",
    "print(\"Upper cases only =\", r3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eafdf878",
   "metadata": {},
   "source": [
    "# Problem Statement3: Write a program that reads two space-separated positive integers X and Y as input and perform the following tasks:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "678d1378",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "list 1\n",
      "[1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61]\n",
      "list 2\n",
      "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]\n",
      "Numpy array NP1\n",
      "[ 1  5  9 13 17 21 25 29 33 37 41 45 49 53 57 61]\n",
      "Numpy array NP2\n",
      "[ 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31]\n",
      "NP1 4x4 matrix\n",
      "[[ 1  5  9 13]\n",
      " [17 21 25 29]\n",
      " [33 37 41 45]\n",
      " [49 53 57 61]]\n",
      "NP2 4x4 matrix\n",
      "[[ 1  3  5  7]\n",
      " [ 9 11 13 15]\n",
      " [17 19 21 23]\n",
      " [25 27 29 31]]\n",
      "NP3 matrix\n",
      "[[ 0  2  4  6]\n",
      " [ 8 10 12 14]\n",
      " [16 18 20 22]\n",
      " [24 26 28 30]]\n",
      "convert NP3 into list\n",
      "[ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28 30]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x = 4\n",
    "lst1 = list((range(1,x*16,x)))\n",
    "print(\"list 1\")\n",
    "print(lst1)\n",
    "\n",
    "y = 2\n",
    "lst2 = list((range(1,y*16,y)))\n",
    "print(\"list 2\")\n",
    "print(lst2)\n",
    "\n",
    "np1 = np.array(lst1)\n",
    "print(\"Numpy array NP1\")\n",
    "print(np1)\n",
    "\n",
    "np2 = np.array(lst2)\n",
    "print(\"Numpy array NP2\")\n",
    "print(np2)\n",
    "\n",
    "np1 = np1.reshape(4,4)\n",
    "print(\"NP1 4x4 matrix\")\n",
    "print(np1)\n",
    "\n",
    "np2 = np2.reshape(4,4)\n",
    "print(\"NP2 4x4 matrix\")\n",
    "print(np2)\n",
    "\n",
    "np3 = np1 - np2\n",
    "print(\"NP3 matrix\")\n",
    "print(np3)\n",
    "\n",
    "lst1 = np.ravel(np3)\n",
    "print(\"convert NP3 into list\")\n",
    "print(lst1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b9c41015",
   "metadata": {},
   "source": [
    "# Problem Statement4: Write a Python program thattakes two integer-NumPy arrays, P and Q of shape [3∗3]and performthe following task:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "719d39e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "P matrix\n",
      "[[20  2 58]\n",
      " [42  5  4]\n",
      " [25 28 56]]\n",
      "Q matrix\n",
      "[[26 39 20]\n",
      " [71 19 18]\n",
      " [79 19 42]]\n",
      "difference of the matrix P and Q\n",
      "[[ -6 -37  38]\n",
      " [-29 -14 -14]\n",
      " [-54   9  14]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "P = np.random.randint(0,100,(3,3))\n",
    "print(\"P matrix\")\n",
    "print(P)\n",
    "\n",
    "Q = np.random.randint(0,100,(3,3))\n",
    "print(\"Q matrix\")\n",
    "print(Q)\n",
    "\n",
    "R = P - Q\n",
    "print(\"difference of the matrix P and Q\")\n",
    "print(R)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
