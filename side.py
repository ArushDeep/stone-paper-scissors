def print_in_box(text):
    # Determine the width of the box based on the string length
    box_width = len(text) + 4

    # Print the top border
    print("+" + "-" * (box_width - 2) + "+")
    
    # Print the string inside the box
    print(f"| {text} |")
    
    # Print the bottom border
    print("+" + "-" * (box_width - 2) + "+")
