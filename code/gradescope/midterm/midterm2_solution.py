# SI 506 Midterm Exam - Practical Question 2

# Fill in the missing places in the code below to write a function named <write_long_strings>
# that takes two (2) arguments, a list of strings called <contents> and
# a string called <filename>. Assign the argument <filename> a default value of "midterm.txt".
# The function should loop through <contents>, and for each element that has *greater than* 20
# characters, write it out to the file specified by <filename>. Finally, be sure to add a newline
# character (i.e. "\n") after each string you write.

# If done correctly, after this code is executed, the contents of "midterm.txt" should contain
# three lines of text, in the following order:

"""University of Michigan
Halloween is my favorite holiday.
It was really windy last night.
"""

# The following is the framework of the code you should write...fill in the places where
# prompted below.

# # # # START CODING HERE # # # # # # # # # # # # # # # # # # # # #

def write_long_strings(contents,filename="midterm.txt"): # Include the correct arguments on this line, including the default argument.

    # Use a "with" statement in the below line to open the file that you will write to.
    # Use the argument variable name, not the actual file name in your open() statement.
    # You will need to come up with a file object variable.
    with open(filename,'w') as f: # <-- Write the "with" statement here.

        # Now initiate a for-loop over <contents>.
        # You will need to come up with a variable that contains the looped values from <contents>.
        for item in contents: # <-- Write the "for" statement here.

            # Now write a conditional ("if") statement to check if the number of characters in
            # each item in <contents> is *greater than* 20.
            if len(item) > 20: # <-- Write the "if" statement here.

                # Now, write each string item that met the criteria of the conditional statement to
                # the file specified by <filename>. Add a newline character ('\n')to the end of the string.
                f.write(item+"\n") # <-- Write the "write" statement here.

 # # # # STOP CODING HERE # # # # # # # # # # # # # # # # # # # # #
# Don't change anything below this line!

    return None # There are no returned variables for this function.

# Feel free to add a print statement within <write_long_strings> to check if what you are writing
# to <filename> is correct. You may also want to open the file you created to check.

# Use the below lines test your function. DO NOT CHANGE ANYTHING BELOW THIS LINE.

test = ['Ann Arbor - Michigan',
        'Hello, how are you?',
        'University of Michigan',
        'Halloween is my favorite holiday.',
        'What is your name?',
        'It was really windy last night.']

write_long_strings(test)
