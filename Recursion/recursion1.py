def recursive_fuction(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursive_fuction(n-1)
        print(n)

recursive_fuction(4)