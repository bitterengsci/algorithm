
[Haskell](http://learnyouahaskell.com/chapters)

Haskell is a purely functional programming language. 
In imperative languages you get things done by giving the computer a sequence of tasks and then it executes them. While executing them, it can change state.

Haskell is statically typed.

Haskell uses a very good type system that has type inference.

```bash
> ghci   # to invoke the interactive mode

```
Haskell Function Syntax: FUNCTION PARAMETERS
```haskell
-- prefix function
succ 9
min 9 10
max 9 10
div 19 3
19 `div` 3     -- infix function
```

doubleMe x = x + x
doubleUs x y = x * 2 + y * 2

```bash
# load example.hs script
> :l example
```

# List & List Comprehension

In Haskell, lists are a homogenous data structure. It stores several elements of the same type. 
use the let keyword to define a name in GHCI. 
Doing let a = 1 inside GHCI is the equivalent of writing a = 1 in a script and then loading it.
```bash
ghci> let lostNumbers = [4,8,15,16,23,42]  
ghci> lostNumbers  
[4,8,15,16,23,42]  
```

Strings are regarded as lists of characters. ("hello" is just syntactic sugar for ['h','e','l','l','o'])

++ operator
: operator (cons operator)

!!: get an element out of a list by index (indices start at 0)

<, <=, >, >= to compare lists (in lexicographical order)

takes a list and returns its head
> head [5, 4, 3, 2, 1]
5 
takes a list and returns its tail (chops off list's head)
> tail [5, 4, 3, 2, 1]
[4, 3, 2, 1]
takes a list and returns its last element
> last [5, 4, 3, 2, 1]
1
takes a list and returns everything except its last element
> init [5, 4, 3, 2, 1]
[5, 4, 3, 2]

Tuple

# Types and Typeclasses

# Functions

Syntax
Pattern Matching
case

# Recursion


# Higher Order Functions


# Module

# Advanced


# Input and Output


Functor
Monad


Zipper