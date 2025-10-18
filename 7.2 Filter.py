# Example 1
fib = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # Fibonacci sequence (where each number is the sum of the two before it).
result = filter(lambda x: x % 2, fib) # % means modulus, which gives the remainder after dividing by 2.
list(result)

# Example 2
fib = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # Fibonacci sequence (where each number is the sum of the two before it).
result1 = filter (lambda x: x % 2 ==0, fib) # x % 2 == 0 means the number is even.
list(result1)