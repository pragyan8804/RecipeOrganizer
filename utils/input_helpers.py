def get_valid_number_input(prompt):
    """Helper function to get valid numeric input"""
    while True:
        try:
            value = input(prompt)
            if not value.strip():
                print("Input cannot be empty. Please enter a number.")
                continue
            number = float(value)
            if number <= 0:
                print("Please enter a positive number.")
                continue
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")