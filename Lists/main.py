# Filename: main.py
from linked_list import LinkedList
from utils import clear_screen, get_number, wait_for_input

def show_menu():
    """ Displays the option menu """
    valid_choices = ["1", "2", "3", "4", "5"]
    ans = "0"

    while ans not in valid_choices:
        clear_screen()
        print("\n\n")
        print("*** MAIN MENU ***")
        print("-----------------")
        print("1. Insert Node")
        print("2. Delete Node")
        print("3. Search Value")
        print("4. Print List")
        print("5. Exit")
        ans = input("Choice: ")

    return ans

def main():
    sll = LinkedList()
    
    while True:
        ans = show_menu()
        
        if ans == "1":     # Insert
            num = get_number()
            sll.insert_node(num)
            
        elif ans == "2":   # Delete
            num = get_number()
            sll.remove_node(num)
            
        elif ans == "3":   # Search
            num = get_number()
            if sll.find_node(num):
                print(f"\n Value {num} Found!")
            else:
                print(f"\n Value {num} was not found in the list!")
            wait_for_input()
            
        elif ans == "4":   # Print
            sll.print_list()
            
        elif ans == "5":   # Exit
            print("\n\nEnd of program!")
            wait_for_input()
            break

if __name__ == "__main__":
    main()