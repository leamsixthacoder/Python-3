def add_acronym():
    acronym = input("What acronym would you like to add? ")
    definition = input("What is the definition of the acronym? ")
    try:
        with open("acronyms.txt", "a") as file:
            file.write(f"{acronym} - {definition}\n")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return

def find_acronym():
    look_up = input("What software acronym would you like to look up? ")
    
    found = False
    try:
        with open('acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    if not found:
        print(f"{look_up} not found")

def main():
    while True:
        choice = input("Would you like to add an acronym or look up an acronym? (add/look up/quit) ")
        if choice == "add":
            add_acronym()
        elif choice == "look up":
            find_acronym()
        elif choice == "quit":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()