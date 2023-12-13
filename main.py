import tkinter as tk
from tkinter import messagebox

input_file_path = 'grades.txt'
output_file_path = 'grades_output.txt'
def show_error_popup(message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    messagebox.showerror("Error", message)

    root.destroy()
    exit(1)
def extract_grades():
    try:
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            for line in input_file:
                last_letters = line[-3:]
                output_file.write(last_letters)

        # Open output file in read mode and print output
        with open(output_file_path, 'r') as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        show_error_popup("File not found.")
    except IsADirectoryError:
        show_error_popup("Specified file is a directory.")
    except:
        show_error_popup("Unknown error has occurred please try again. ")
def calculate_arithmetic_mean():
    grades_sum = 0
    count = -1
    with open(output_file_path, 'r') as file:
        for line in file:
            grades_sum += int(line)
            count += 1

    mean = (grades_sum/count)
    print(f"Total number of grades: {count}")
    print(f"Total sum: {grades_sum}")
    print(f"Arithmetic mean: {mean}")

def main():

    extract_grades()
    calculate_arithmetic_mean()


if __name__ == "__main__":
    main()
