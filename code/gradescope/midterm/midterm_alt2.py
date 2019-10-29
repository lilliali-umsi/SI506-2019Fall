# SI 506 Midterm Exam - Practical Question 2

# Fill in the missing places in the code below to write a function named <write_planets> that
# takes two (2) arguments, a list of strings called <contents> and a string called <filename>.
# The <contents> list will be a list of celestial objects in the following format:

# ["name-type","name-type",...etc]

# The function should loop through <contents>, and for each element that has a type of 'planet', write its
# name to the file specified by <filename>.

# The final several lines of this file are provided by us for you to test your code.
# If done correctly, after this code is executed, the contents of "midterm.txt" should contain
# three lines of text, in the following order:

"""Mercury
Venus
Earth
Mars
"""

# The following is the framework of the code you should write...fill in the places where
# prompted below.

def write_planets(contents,filename):

# # # # START CODING HERE # # # # # # # # # # # # # # # # # # # # #

    # Use a "with" statement in the below line to open the file that you will write to.
    # Use the argument variable name, not the actual file name in your open() statement.
    # You will need to come up with a file object variable.
    REPLACE_ME # <-- Write the "with" statement here.

        # Now initiate a for-loop over <contents>.
        # You will need to come up with a variable that contains the looped values from <contents>.
        REPLACE_ME # <-- Write the "for" statement here.

            # Now, split each element in <contents> on the hyphen ("-") so that you
            # have a list containing two strings, the name and type of the celestial object.
            REPLACE_ME # <-- Write your "split" statement here.

            # Now, check if the the current element of the list is type 'planet' or not by using
            # an "if" conditional. You will need to use list slicing here.
            REPLACE_ME # <-- Write your "if" statement here.

                # Finally, write the name of each element that passed the above conditional to
                # the file specified by <filename>. Don't forget to add a newline character
                # ("\n") to the end of each string that you write!
                REPLACE_ME # <-- Write the "write" statement here.

# # # # STOP CODING HERE # # # # # # # # # # # # # # # # # # # # #
# Don't change anything below this line!

    return None # There are no returned variables for this function.

# Feel free to add a print statement within <write_long_strings> to check if what you are writing
# to <filename> is correct. You may also want to open the file you created to check.

# Use the below lines test your function. DO NOT CHANGE ANYTHING BELOW THIS LINE.

celestial_objects = ["Titan-satellite",
                     "Mercury-planet",
                     "Halley's Comet-comet",
                     "Venus-planet",
                     "Pluto-protoplanet",
                     "Earth-planet",
                     "Ganymede-satellite",
                     "Mars-planet"]

write_planets(celestial_objects,"midterm.txt")
