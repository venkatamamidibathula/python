def integercheck():
    while True:
        try:
            i=int(input("Enter a number"))
        except:
            print("Entered number is not a valid entry")
        else:
            print(f"Valid number {i}")
            break
integercheck()
