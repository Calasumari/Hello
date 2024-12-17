print("Hello")

def hello():
    print("Hello!")
    for i in range(0,12):
        print("Hello.")
    colour = input("Enter a colour: ").upper()
    if colour == "RED":
        print("That is a bad colour.")
    else:
        print(colour, " is a nice colour.")

hello()
        
