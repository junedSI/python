
def my_function():      # This is a function definition. Note the colon (:)
      a = 2                   # This line belongs to the function because it's indented
      return a                # This line also belongs to the same function
print(my_function())    # This line is OUTSIDE the function block


a=2
b=3
if a > b:                # If block starts here
    print(a)                  # This is part of the if block
else:                   # else must be at the same level as if
      print(b)                # This line is part of the else block

# or we can do it inline but this is valid for only one statement
if a > b:print(a)
else: print(b) 

# Python 3 disallows mixing the use of tabs and spaces for indentation. 
# In such case a compile-time error is
# generated: Inconsistent use of tabs and spaces in indentation and the program will not run.
# where as python2 allows the mixed use of tabs and spaces.

