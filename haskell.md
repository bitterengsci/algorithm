<!-- TOC -->

- [1. List](#1-list)
    - [1.1. ranges](#11-ranges)
    - [1.2. List Comprehension](#12-list-comprehension)
- [2. Tuple](#2-tuple)
- [3. Types and Typeclasses](#3-types-and-typeclasses)
- [4. Functions](#4-functions)
- [5. Recursion](#5-recursion)
- [6. Higher Order Functions](#6-higher-order-functions)
- [7. Module](#7-module)
- [8. Advanced](#8-advanced)
- [9. Input and Output](#9-input-and-output)

<!-- /TOC -->
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

# List

In Haskell, lists are a homogenous data structure, denoted by square brackets, and the values in the lists are separated by comma. It stores several elements of the same type. 
use the let keyword to define a name in GHCI. 
Doing let a = 1 inside GHCI is the equivalent of writing a = 1 in a script and then loading it.
```bash
ghci> let lostNumbers = [4,8,15,16,23,42]  
ghci> lostNumbers  
[4,8,15,16,23,42]  
```

Strings are regarded as lists of characters. ("hello" is just syntactic sugar for ['h','e','l','l','o'])

++ operator put together two lists
: operator (cons operator) put sth at the beginning of a list
!! get an element out of a list by index (indices start at 0)
<, <=, >, >= to compare lists (in lexicographical order)

`head` takes a list and returns its head
> head [5, 4, 3, 2, 1]
5 
`tail` takes a list and returns its tail (chops off list's head)
> tail [5, 4, 3, 2, 1]
[4, 3, 2, 1]
`last` takes a list and returns its last element
> last [5, 4, 3, 2, 1]
1
`init` takes a list and returns everything except its last element
> init [5, 4, 3, 2, 1]
[5, 4, 3, 2]
`length` takes a list and returns its length, obviously.
> length [5,4,3,2,1]  
5  
`null` checks if a list is empty. If it is, it returns True, otherwise it returns False. Use this function instead of xs == []
> null [1,2,3]  
False  
> null []  
True  
`reverse` reverses a list.
> reverse [5,4,3,2,1]  
[1,2,3,4,5]  
`take` takes number and a list. It extracts that many elements from the beginning of the list. Watch.
> take 3 [5,4,3,2,1]  
[5,4,3]  
> take 1 [3,9,3]  
[3]  
> take 5 [1,2]  
[1,2]  
> take 0 [6,6,6]  
[]  
If we try to take more elements than there are in the list, it just returns the list. 
If we try to take 0 elements, we get an empty list.

`drop` works in a similar way, only it drops the number of elements from the beginning of a list.
> drop 3 [8,4,2,1,5,6]  
[1,5,6]  
> drop 0 [1,2,3,4]  
[1,2,3,4]  
> drop 100 [1,2,3,4]  
[]

`maximum` takes a list of stuff that can be put in some kind of order and returns the biggest element.
`minimum` returns the smallest.
> minimum [8,4,2,1,5,6]  
1  
> maximum [1,9,2,3,4]  
9   
`sum` takes a list of numbers and returns their sum.
`product` takes a list of numbers and returns their product.
> sum [5,2,1,6,3,2,5,7]  
31  
> product [6,2,1,2]  
24  
> product [1,2,5,6,7,9,2,0]  
0

`elem` takes a thing and a list of things and tells us if that thing is an element of the list. It's usually called as an infix function because it's easier to read that way.
> 4 `elem` [3,4,5,6]  
True  
> 10 `elem` [3,4,5,6]  
False  

## ranges
Ranges are a way of making lists that are arithmetic sequences of elements that can be enumerated. 
Numbers can be enumerated. 
Characters can also be enumerated. The alphabet is an enumeration of characters from A to Z.
> [1..10]  
[1,2,3,4,5,6,7,8,9,10]  
> ['a'..'z']  
"abcdefghijklmnopqrstuvwxyz"  
> ['K'..'Z']  
"KLMNOPQRSTUVWXYZ"

> [2,4..10]  
[2,4,6,8,10]  
> [3,6..20]  
[3,6,9,12,15,18]   
It's simply a matter of separating the first two elements with a comma and then specifying what the upper limit is. While pretty smart, ranges with steps aren't as smart as some people expect them to be. You can't do [1,2,4,8,16..100] and expect to get all the powers of 2. Firstly because you can only specify one step. And secondly because some sequences that aren't arithmetic are ambiguous if given only by a few of their first terms.

To make a list with all the numbers from 20 to 1, you have to do [20,19..1].

Watch out when using floating point numbers in ranges! Because they are not completely precise (by definition), their use in ranges can yield some pretty funky results.
> [0.1, 0.3 .. 1]  
[0.1,0.3,0.5,0.7,0.8999999999999999,1.0999999999999999]  
My advice is not to use them in list ranges.

You can also use ranges to make infinite lists by just not specifying an upper limit.
You could do [13,26..24*13] to get the first 24 multiples of 13. 
But there's a better way: take 24 [13,26..]. Because Haskell is lazy, it won't try to evaluate the infinite list immediately because it would never finish. It'll wait to see what you want to get out of that infinite lists. And here it sees you just want the first 24 elements and it gladly obliges.

Functions that produce infinite lists:
`cycle` takes a list and cycles it into an infinite list. If you just try to display the result, it will go on forever so you have to slice it off somewhere.
> take 10 (cycle [1,2,3])  
[1,2,3,1,2,3,1,2,3,1]  
> take 12 (cycle "LOL ")  
"LOL LOL LOL "
`repeat` takes an element and produces an infinite list of just that element. It's like cycling a list with only one element.
> take 10 (repeat 5)  
[5,5,5,5,5,5,5,5,5,5]  
`replicate` returns some number of the same element in a list. 
> replicate 3 10
[10,10,10]

## List Comprehension
> [x*2 | x <- [1..10]]  -- x is drawn from [1..10] and for every element in [1..10] (which we have bound to x), get that element and double
[2,4,6,8,10,12,14,16,18,20]  
> [x*2 | x <- [1..10], x*2 >= 12]   -- we want only the elements which, doubled, are greater than or equal to 12
[12,14,16,18,20] 
The part before the pipe is called the output function, x is the variable, [1..10] is the input set, x*2 >= 12 is the predicate
    Predicates/conditions go after the binding parts and are separated from them by a comma.

> [ x | x <- [50..100], x `mod` 7 == 3]  
[52,59,66,73,80,87,94]   
Weeding out lists by predicates is also called filtering. We took a list of numbers and we filtered them by the predicate. 

* We can put that comprehension inside a function so we can easily reuse it.
boomBangs xs = [ if x < 10 then "BOOM!" else "BANG!" | x <- xs, odd x]   
The function odd (predicate) returns True on an odd number and False on an even one. 
The element is included in the list only if all the predicates evaluate to True.
> boomBangs [7..13]  
["BOOM!","BOOM!","BANG!","BANG!"]
* multiple predicates in list comprehensions (an element must satisfy all the predicates to be included in the resulting list) 
> [ x | x <- [10..20], x /= 13, x /= 15, x /= 19]
[10,11,12,14,16,17,18,20]
* When drawing from several lists, comprehensions produce all combinations of the given lists and then join them by the output function we supply.
If we have two lists, [2,5,10] and [8,10,11] and we want to get the products of all the possible combinations between numbers in those lists.
> [ x*y | x <- [2,5,10], y <- [8,10,11]]
[16,20,22,40,50,55,80,100,110]   
> [ x*y | x <- [2,5,10], y <- [8,10,11], x*y > 50]  
[55,80,100,110]   

length xs = sum [1 | _ <- xs]   
_ means that we don't care what we'll draw from the list anyway so instead of writing a variable name that we'll never use, we just write _. This function replaces every element of a list with 1 and then sums that up. This means that the resulting sum will be the length of our list.

Because strings are lists, we can use list comprehensions to process and produce strings.
removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]   
> removeNonUppercase "Hahaha! Ahahaha!"  
"HA"

* Nested list comprehensions are also possible if you're operating on lists that contain lists.
> let xxs = [[1,3,5,2,3,1,2,4,5],[1,2,3,4,5,6,7,8,9],[1,2,4,2,1,6,3,1,3,2,3,6]]  
> [ [ x | x <- xs, even x ] | xs <- xxs]  -- remove all odd numbers without flattening the list
[[2,2,4],[2,4,6,8],[2,4,2,6,2,6]]  

You can write list comprehensions across several lines. So if you're not in GHCI, it's better to split longer list comprehensions across multiple lines, especially if they're nested.

# Tuple
Tuples are denoted with parentheses and their components are separated by commas. A tuple can contain a combination of several types(not homogenous); but how many values and the types of those values are fixed.

In some ways, tuples are like lists — they are a way to store several values into a single value.
- A list of numbers is a list of numbers. That's its type and it doesn't matter if it has only one number in it or an infinite amount of numbers. 
- Tuples are used when you know exactly how many values you want to combine and its type depends on how many components it has and the types of the components.
- Tuples can also contain lists.

Use tuples when you know in advance how many components some piece of data should have. 
Tuples are much more rigid because each different size of tuple is its own type, so you can't write a general function to append an element to a tuple.

While there are singleton lists, there's no such thing as a singleton tuple. It doesn't really make much sense when you think about it. A singleton tuple would just be the value it contains and as such would have no benefit to us.

Like lists, tuples can be compared with each other if their components can be compared. Only you can't compare two tuples of different sizes, whereas you can compare two lists of different sizes. 

Two useful functions that operate on pairs (only!):
`fst` takes a pair and returns its first component.
> fst (8,11)  
8  
> fst ("Wow", False)  
"Wow"  
`snd` takes a pair and returns its second component.
> snd (8,11)  
11  
> snd ("Wow", False)  
False  

zip produces a list of pairs. 
It pairs up the elements from two lists and zips them together into one list by joining the matching elements into pairs.
It's useful when you want to combine two lists in a way or traverse two lists simultaneously.
> zip [1,2,3,4,5] [5,5,5,5,5]  
[(1,5),(2,5),(3,5),(4,5),(5,5)]  
> zip [1 .. 5] ["one", "two", "three", "four", "five"]  
[(1,"one"),(2,"two"),(3,"three"),(4,"four"),(5,"five")]

zip can take two lists that contain different types and zip them up. Also can take two lists whose lengths of the lists don't match
> zip [5,3,2,6,2,7,2,5,4,6,6] ["im","a","turtle"]  
[(5,"im"),(3,"a"),(2,"turtle")]  
The longer list simply gets cut off to match the length of the shorter one. Because Haskell is lazy, we can zip finite lists with infinite lists:

ghci> zip [1..] ["apple", "orange", "cherry", "mango"]  
[(1,"apple"),(2,"orange"),(3,"cherry"),(4,"mango")]  
look at meee
Here's a problem that combines tuples and list comprehensions: which right triangle that has integers for all sides and all sides equal to or smaller than 10 has a perimeter of 24? First, let's try generating all triangles with sides equal to or smaller than 10:

ghci> let triangles = [ (a,b,c) | c <- [1..10], b <- [1..10], a <- [1..10] ]   
We're just drawing from three lists and our output function is combining them into a triple. If you evaluate that by typing out triangles in GHCI, you'll get a list of all possible triangles with sides under or equal to 10. Next, we'll add a condition that they all have to be right triangles. We'll also modify this function by taking into consideration that side b isn't larger than the hypothenuse and that side a isn't larger than side b.

ghci> let rightTriangles = [ (a,b,c) | c <- [1..10], b <- [1..c], a <- [1..b], a^2 + b^2 == c^2]   
We're almost done. Now, we just modify the function by saying that we want the ones where the perimeter is 24.

ghci> let rightTriangles' = [ (a,b,c) | c <- [1..10], b <- [1..c], a <- [1..b], a^2 + b^2 == c^2, a+b+c == 24]  
ghci> rightTriangles'  
[(6,8,10)]  
And there's our answer! This is a common pattern in functional programming. You take a starting set of solutions and then you apply transformations to those solutions and filter them until you get the right ones.


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