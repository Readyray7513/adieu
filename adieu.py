import inflect

def main():
    # Create an instance of the inflect engine
    p = inflect.engine()
    names = []  # List to store names
    
    # Get input from the user
    try:
        while True:
            name = input("Name: ")
            names.append(name)  # Add name to the list
    except EOFError:  # Handle Ctrl+C
        pass  # Exit the loop gracefully

    # Print the result
    farewell = p.join(names)
    print(f"\nAdieu, adieu, to {farewell}")

if __name__ == "__main__":
    main()





#In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d.
#Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, 
# three names with two commas and one and, and names with commas and one and, as in the below:

