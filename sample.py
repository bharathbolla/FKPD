numbers = [1,2,3,4] # add a breakpoint to this line
def square_num(mylist):
    total = 0
    print("This is my program")
    for num in mylist:
        for num in mylist:
            total+=num**3
        
    return total

sq_list = square_num(numbers)
print(sq_list)