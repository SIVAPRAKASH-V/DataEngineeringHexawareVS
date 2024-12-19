def sum_even_odd(start, end):
    sum_even = 0
    sum_odd = 0
    
    for num in range(start, end + 1):
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    return sum_even, sum_odd


start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
  
sum_even, sum_odd = sum_even_odd(start, end)
    
print("Sum of even numbers between {} and {}: {}".format(start,end,sum_even))
print("Sum of odd numbers between {} and {}: {}".format(start,end,sum_odd))
