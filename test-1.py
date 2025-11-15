def table():
    
    data = int(input('Enter the number you want to print a table for: '))
    for i in range(1, 1000):
        print(f"{data} x {i} = {data * i}")

table()