Lecture 3 | MIT 6.00 Into to CS

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

Lecture 4 | MIT 6.00 Into to CS
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
 
