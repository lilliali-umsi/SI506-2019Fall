# SI 506 Midterm Exam - Practical Question 1

# Fill in the missing places in the code below to write a function named <filter_and_sort_strings>
# that takes two arguments. The first argument is a list of strings called <str_list>, and the
# second argument is an integer called <maximum_len>. Give the <maximum_len> argument a default
# value of 5. The function should loop through <str_list>, append all the elements with *less
# than or equal to* <maximum length> to a new list called <filtered>. Then, the code should return
# <filtered>, but sorted alphabetically.

# The final few lines of this code are provided by us to test your code. If done correctly,
# after this code is executed, the following should be the value of <result> and
# printed out to the terminal:

# ['Idaho', 'Iowa', 'Maine', 'Texas']

# The following is the framework of the code you should write...fill in the places where
# prompted below.

# # # # START CODING HERE # # # # # # # # # # # # # # # # # # # # #

# Fill in the correct arguments to the below function definition. Don't
# forget the default argument!
def filter_and_sort_strings(REPLACE_ME): # <-- Write the proper arguments here.
    filtered = []

    # Use a "for" loop to loop through each element of <str_list>.
    # You will need to come up with a variable that contains the looped values
    # from <str_list>.
    REPLACE_ME# <-- Write your "for" statement here.

        # Now, use an "if" conditional to check if each element of <str_list> has *less than or
        # equal to* the number of characters specified by maximum_len.
        REPLACE_ME # <-- Write your "if" statement here.

            # Now, append any elements of <str_list> that meet the above criteria (the
            # "if" statement) to the list <filtered>
            REPLACE_ME # <-- Write your code here.

    # Finally, use "return" and "sorted" to return a sorted list of the elements that
    # met the criteria from your "if" statement.
    REPLACE_ME # <-- Write your "return" statement here. Don't forget to sort the <filtered> list!

# # # # STOP CODING HERE # # # # # # # # # # # # # # # # # # # # #
# Don't change anything below this line!

# Use the below lines test your function. DO NOT CHANGE ANYTHING BELOW THIS LINE.

states = ['Michigan','Indiana','Iowa','Washington','Texas',
          'Florida','Wyoming','Maine','Idaho','Nevada']

result = filter_and_sort_strings(states)
print(f"\nResultant list: {result}\n")
