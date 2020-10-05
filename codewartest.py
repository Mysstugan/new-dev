num = int(input("Enter a nr: "))
def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))

## How to print return value of function  
print(descending_order(num))


print(int("".join(sorted(str(num), reverse=True))))