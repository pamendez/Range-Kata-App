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
            print("Select an operation:")
            print("1. ")
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