from krange.krange import Range

def main():
    """
        Serves as the main entry point of the application.
    """

    print("Welcome to the application!")
    input_range = input("Enter the range you want to work with: ")    
    try:
        rng = Range(input_range)
        while (True):
            print("Select an operation: \n")
            print("1. Contains integers \n",
                  "2. GetAllPoints \n",
                  "3. ContainsRange \n",
                  "4. EndPoints \n",
                  "5. OverlapsRange \n",
                  "6. Equals \n", 
                  "7. Exit \n"
                   )

            options = input("save") 
            _response = []

            if(options == '1'):
                print("Insert the elements separated by commas (,)")
                _response = input()
                rng.contains(_response)
                break
            elif (options == '2'):
               pass
            elif (options == '3'):
               pass
            elif (options == 4):
               pass
            elif (options == 5):
               pass
            elif (options == 6):
               pass
            elif (options == 7):
               pass
            else:
                print("Invalid option")
            break
            pass
        pass
    except (Exception, ValueError, SyntaxError, TypeError) as e:
        print(f"\nAn error has ocurred: {e}")
        pass

    return 0

if __name__ == "__main__":
    main()
    pass