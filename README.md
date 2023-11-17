# ***Introduction***
+ For this mutation testing I used MutPy, a mutation tool that is used by python. Mutation testing is used to detect whether the test cases in place can detect the changes(mutations) being made to the source code. In this case, our soure code is in the Polynomial.py and our test cases are in Polytest.py. The goal of this testing is to make sure it is able to identify the faults in the code efficiently. How MutPy works is that it creates mutated versions of the source code and then it runs the test cases against each mutated version. 
# ***List of defined mutation operators***
+ Arithmetic Operators - Mutate the arithmetic operators in mathematical expressions:
  + Replace '+' with '-'
  + Replace '-' with '+'
  + Replace '*' with '/'
  + Replace '/' with '*'

+ Comparison Operators - Mutate the comparison operators in conditional statements:
  + Replace '==' with '!='
  + Replace '!=' with '=='
  + Replace '<' with '>'
  + Replace '>' with '<'
  + Replace '<=' with '>='
  + Replace '>=' with '<='

+ Logical Operators - Mutate the logical operators in boolean expressions
  + Replace 'and' with 'or'
  + Replace 'or' with 'and'
  + Replace 'not' with an empty string(remove 'not')

+ Unary Operators - Mutate unary operators like '-' and '+' in expressions
  + Replace '-' with '+'
  + Replace '+' with '-'

+ Variable Mutations - Mutate variable assignments
  + Replace a variable with another variable in the same scope

+ Function Call Mutations - Mutate function calls
  + Replace function arguments with different values.

+ Statement Deletion
  + Delete statements to test the robustness of the code.

+ Boundary Value Mutations - Mutate boundary values.
  + Change numeric constants to slightly different values.

+ Return Value Mutations - Mutate return values in functions.
  + Change the return value to a different constant or expression.

+ Method Call Mutations - Mutate method calls.
  + Replace method arguments with different values.

# ***Description of applied mutations and their impact***
+ 
# ***Summary of mutant survival and killing***
+ Summary of Mutant Survial and Killing with original PolyTest.py

  ![image](https://github.com/mabraham2o24/Mutation-Testing-HW1/assets/143213640/f306f222-505a-4222-beb3-7eca080c61b5)

+ Summary of Mutant Survival and Killing with Test Suite Revision(s):

   ![image](https://github.com/mabraham2o24/Mutation-Testing-HW1/assets/143213640/8175f707-f662-448e-9f6d-4472d540e47d)


# ***Analysis of the test suite's effectiveness***
# ***Recommendations for improving the test suite***
# ***Conclusion***


