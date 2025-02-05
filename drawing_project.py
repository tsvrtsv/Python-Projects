while True:
    # Step 1: Display a menu to the user
    print("🌟 Welcome to the Python Pattern Drawing Program!")
    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")

    # Step 2: Get the user's choice
    choice = int(input("Enter the number corresponding to your choice: "))

    # Step 3: Get dimensions based on choice
    if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
        rows = int(input("Enter the number of rows: "))
    elif choice in [2, 5]:  # Patterns that need size
        size = int(input("Enter the size of the square/rectangle: "))

    # Step 4: Generate the selected pattern
    if choice == 1:  # Right-angled Triangle
        for row in range(rows + 1):
            print(f'{"*" * row}')

    elif choice == 2:  # Square with Hollow Center
        for row in range(1, size + 1):
            for col in range(1, size + 1):
                if row == 1 or row == size or col == 1 or col == size:
                    print("*", end='')
                else:
                    print(" ", end='')
            print()

    elif choice == 3:  # Diamond
        for row in range(rows):
            print(" " * (rows - row), "*" * (2 * row + 1))
        for row in range(rows - 2, -1, -1):
            print(" " * (rows - row), "*" * (2 * row + 1))

    elif choice == 4:  # Left-angled Triangle
        for row in range(rows + 1, -1, -1):
            print(f'{"*" * row}')

    elif choice == 5:  # Hollow Square
        for row in range(1, size + 1):
            for col in range(1, size + 1):
                if row == 1 or row == size or col == 1 or col == size:
                    print("*", end='')
                else:
                    print(" ", end='')
            print()

    elif choice == 6:  # Pyramid
        for row in range(rows):
            print(" " * (rows - row), "*" * (2 * row + 1))

    elif choice == 7:  # Reverse Pyramid
        for row in range(rows - 2, -1, -1):
            print(" " * (rows - row), "*" * (2 * row + 1))

    elif choice == 8:  # Rectangle with Hollow Center
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        for col in range(1, height + 1):
            for row in range(1, width + 1):
                if row == 1 or row == width or col == 1 or col == height:
                    print("*", end='')
                else:
                    print(" ", end='')
            print()

    else:
        print("❌ Invalid choice! Please restart the program.")

    # Step 5: Allow the user to restart or exit

    restart = input("Would you like to restart? (y/n)")
    if restart == "y":
        continue
    elif restart == "n":
        print("Program terminated.")
        break
