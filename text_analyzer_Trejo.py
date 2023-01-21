# Anthony Trejo
# Homework 5: File Analyzer


'''
Algorithm:
introduction
ask user for text file
show error message if previous step done wrong
choice = 0
show options
    choice 1 = count number of characters
    choice 2 = count number of vowels
    choice 3 = count the number of words
    choice 4 = extract a portion of the file
    choice 5 = print the characters of the file backwards
    choice 6 = quit
thank you message
'''
import textwrap

# Intrduction
def print_welcome():
    print("*"*60)
    print("Text File Analyzer".center(60))
    print("*"*60)
    print()
    print("This program will first ask you for the name of a file. It will")
    print("load the file into memory. It will then show a list of options to")
    print("choose from that will enable you to discovcer more about the file.")
    print()

# Outro
def print_goodbye():
    print()
    print("*"*60)
    print("Thank you for using this program.".center(60))
    print("*"*60)

# Choices
def print_menu():
    print("Here are your choices: ")
    print("1. Count the number of characters.")
    print("2. Count the number of vowels.")
    print("3. Count the number of words.")
    print("4. Extract a portion of the file.")
    print("5. Print the characters of the file backwards.")
    print("6. Quit.")

    
# Main

print_welcome()

fname = input("Enter the name of the file to open: ")

success = False

while success == False:
    try:
        fvar = open(fname,"r")
        success = True
        print()
        print("The file has been loaded into memory.")
        print()
    except Exception as e:
        print("This error occurred: ")
        print(e)
        fname = input("Enter the name of a file: ")

text = ""
for line in fvar:
    line = line.strip()
    text = text + line + " "
text = text.strip()

fvar.close()

choice = 0
while choice != 6:
    print_menu()
    choice = int(input("Enter the number of your choice: "))
    if choice == 1:
        # count the number of characters
        num_of_chara = 0
        for line in text:
            len(text)
            num_of_chara = num_of_chara + 1
        print("There where %d characters in that file." % num_of_chara)
    elif choice == 2:
        # count the number of vowels
        vowel_count = 0
        for ch in text.lower():
            if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
                vowel_count = vowel_count + 1
        print("There where %d vowels in that file." % vowel_count)
    elif choice == 3:
        # count the number of words
        word_count = 0
        for line in text:
            words = text.split(" ")
            word_count =+ len(words)
        print("There where %d words in the file." % word_count)
    elif choice == 4:
        # extract a portion of the file
        result = ""
        first = int(input("Enter index of first character to include: "))
        last = int(input("Enter index of last character to include: "))
        for i in range(first, last+1):
            result = result + text[i]
        print("Here is the extract: ",result)
    elif choice == 5:
        reversed = ""
        count = 0
        for i in range(len(text)-1,-1,-1):
            reversed = reversed + text[i]
        print("Here is the text in reverse, printed 70 characters per line: ")
        print(textwrap.fill(reversed, width=70))
    else:
        # Try again
        if choice != 6:
            print("Please try again.")
        else:
            print_goodbye()



