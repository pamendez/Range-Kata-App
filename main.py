from unicodedata import name
from krange.krange import Range
import os

def main():
    """
        Serves as the main entry point of the application.
    """

    print("Welcome to the application!")
    input_range = input("Enter the range you want to work with: ")    
    try:
        primary_range = Range(input_range)
        while (True):
            os.system('cls') if (os.name == "nt") else os.system('clear')
            print(f"Current range is: {primary_range.to_string()}")
            print("Select an operation:")
            option = input("\n1. Contains integers" +
                  "\n2. GetAllPoints" +
                  "\n3. ContainsRange" +
                  "\n4. EndPoints" +
                  "\n5. OverlapsRange" +
                  "\n6. Equals" +
                  "\n7. Exit" +
                  "\n\n>")

            if(option == '1'):
                input_elements = [x.strip() for x in input("Insert the elements separated by commas: ").split(",")]

                result = primary_range.contains(set(input_elements))
                print(f"{result}")
                pass

            elif (option == '2'):

                result = primary_range.getAllPoints()
                print(f"{result}")
                pass

            elif (option == '3'):
                input_range2 = input("Insert the range to evaluate")
                secondary_range = Range(input_range2)
                result = primary_range.contains(secondary_range)
                print(f"{result}")
                pass

            elif (option == '4'):
                result = primary_range.endpoints
                print(f"{result}")
                pass

            elif (option == '5'):
               pass

            elif (option == '6'):
               pass

            elif (option == '7'):
               print("Exiting application...")
               break


            else:
                input("Invalid option.")
            pass

            input("Press ENTER to continue.")
        pass

    except (Exception, ValueError, SyntaxError, TypeError) as e:
        print(f"\nAn error has ocurred: {e}")
        pass

    return 0

if __name__ == "__main__":
    main()
    pass