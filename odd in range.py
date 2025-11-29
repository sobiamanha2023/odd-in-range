start = 1
end = 30

print(f"Odd numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num % 2 != 0: 
        print(num)