## Lecture 3 | MIT 6.00 Into to CS

- Data            Operations            Commands
Num             +, *                  Assignment
Strings         and, or               input/output
Booleans                            conditionals
                                    loop mechanisms (while)

- Good Progamming Style
Use comments
Type disipline
Decsriptive use of variable names
Branch testing

- Iteative Program Steps
1. choose variable that is going to count
2. initialize outside the loop
3. set-up and test (end test)
4. construct block of code 
  4.1 change variable
5. what to do when done

- Flow charts for program design

## Lecture 4 | MIT 6.00 Into to CS
Decomposition and abstraction through functions; into to recursion

We have   Turring Complete
  Assignment
  Conditonals
  input/output
  looping constructs (for/loop)
  
We dont have
  - Decomposition - way of structure onto the code
  - Abstraction - suppress details, treat comuption like a black box
  
Functions
  break-up into modules
  suppress detail
  create 'new primitives'

Sytax of function:
  def - keyword
  name(x) ~ defines formal parameters
  'def name(x)'
  return - keyword

Invoke function by passing in value or the parameters
sprt(16)
binds x to 16 ~ local binding / ans is also only bound locally
local bindings do not affect any global bindings

interperter - global bindings 
call function
  creates local table within global 
    for sqrt x/ans bound local
    
Include Specifications with """..."""" at start of function.

Farmyard Problem
  20 heads, 56 legs
  numPigs + numChick = 20
  4*numPigs + 2*numChick = 56
  
 Brutte force algotrithm - enumerate & check
 
 pigs, chickens & spiders
 
 Recursion
 - Base case...simple soultion
 - inductive step
    break problem into simpler version of same problem with other steps
  
 Fibonacci Number
  Pairs(0) = 1
  Pairs(1) = 1
  Pairs(n) = pairs(n-1) + pairs(n-2)
  
## Lecture 5 | MIT 6.00 Intro to CS
  Floating point numbers, successive refinement, finding roots.
  
  Numbers
  int = whole numbers
  arbitrary precision - Long and short int
  
  Floating Point - real numbers
  IEEE Floating point Standard
  variant of scientific notation
  mantissa (significant) - exponent
  1 <= Mantissa <+ 2
 Exponent -1022 : 1023
 64 Bits
  1 bit sign
  11 exponenet
  52 for mantissa
  17 decimal digits of percision

1/8 = 0.125
Base 10: 1.25 x 10 ^-1
Base 2: 1.0 x 2 ^-3 (.001)

1/10: 1 x 10^-1
Base 2: Approximation, no finite number

Worry about == on floats (never use as a test of equality)
abs(a * a - 2.0) < epsilon

Square roots
Might not be an exact answer
can't enumerate all guesses
  reals are uncountable
Guess, check and improve

Successive approximation
Guess = initial guess
for iter in range(100):
  if f(guess) close enough: return guess
  else: guess = better guess
Error

Bisection method
  Liner arrangement of answers
  start in middle, is answer to left or right of current position
  
## Lecture 6 | MIT 6.00 Intro to CS
  Bisection methods, Newton/Raplhson, introduction to lists

Create fucntion for test cases
Regression Testing - Trying to make sure a program has not regressed
