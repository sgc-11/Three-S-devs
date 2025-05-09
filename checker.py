import re

"""
Checks if the email comforms to any of these forms:
    xxxx@utv.edu.co or xxxx@estudiante.utv.edu.co
and classyfies it into either professor or student

Args:
    email (str): the email to check

Returns:
    0: if unvalid email
    1: if professor email
    2: if student email
"""
def classify_email(email: str) -> int:
#     reg_ex = re.compile(r"""
# \S+    # get any character preceding the @
# @      # Capture the @
# (\w?)  # capture the inmidiate word after the @ (estudiante), it may or may not be there, and save it into a group
# \.utv\.edu\.co
# """, re.VERBOSE)
    
    reg_ex = re.compile(r"""
        ^  # This means that the regex must match the start of the string, that is, there is nothing before
        [a-z0-9!#$%&'*+/=?^_`{|}~\.]+  # capture the start of the email
        @  # capture the @
        (estudiante)?  # 'estudiante' may or not be there, if it is there save it into group
        \.?utv\.edu\.co  # check the rest of the email ending (the '\.' is to capture the '.', else it 
                        # would be a wildcard). (the '\.?' is because, since if the email is not 'estudiante',
                        # there won't be a '.', so the '.' may or may not be there)
        $  # this means, that it must match the end of the string. That is, there is nothing after the email
           # The '^' and '$' combined, means that the whole string must match the regex
                        """, (re.IGNORECASE | re.VERBOSE))  # we want to ignore case (re.IGNORECASE), and 
                            # to be able to comment the regex and make it in more than one line (re.VERBOSE)

    result = reg_ex.match(email)  # Match the regular expression to the received email

    if not result:  # no match means not valid email
        return 0
    
    if result.group(1):  # if group 1 exists, means that a 'estudiante' after the '@' was found
        return 2
    
    return 1  # email valid, but not student, return professor


"""
Checks if a name is valid
    That means, the name just consists of letters, the case does not matter.

Args:
    name (str): the name

Returns:
    True: valid name
    False: unvalid name
"""
def is_valid_name(name: str):
    reg_exp = re.compile(r"^[a-z ]+$", re.IGNORECASE)

    result = reg_exp.match(name)

    return result is not None


"""
Checks if a number is valid
    It takes into account the international indicator '+' and the country code (any of those can or cannot be).
    That means that "+57 ..." is valid, "57 ..." is valid, "+ ..." is valid, and "..." is 
    also valid (the space is not needed)

Args:
    number (str): the number as a string

Returns:
    True: valid number
    False: unvalid number
"""
def is_valid_number(number: str):
    reg_exp = re.compile(r"^\+?\d{0,3}\d{10}$")

    result = reg_exp.match(number.replace(" ", ""))

    return result is not None


"""
Checks if the user input in the menu is a valid option. It asumes the options in
    the menu are in a number range, that means, the options will be [1, 2, 3, 4], 
    not [10, 32, 86, 102]. And in case the input is a valid option, in will return
    the selected option.

Arguments:
    user_input(str): is the value the user typed
    starting_range(int): is the start of the range, inclusive
    ending_range(int): is the end of the range, inclusive

Returns:
    bool: if the option is false
    int: the selected option
"""
def check_valid_option(user_input: str, starting_range: int, ending_range: int) -> int | bool:
    user_input = user_input.strip()
    if not user_input.isdecimal():
        return False
    
    user_input = int(user_input)
    if user_input > ending_range or user_input < starting_range:
        return False
    
    return user_input


"""
Checks if an input email is a substring of the actual email, but it does it by checking the input local part (before the @) 
    as a substring, and the domain part (after the @) as equals

Args:
    input_email(str): the presumed substring we want to check
    actual_email(str): the email we want to check it to

Returns:
    True if the input is a substring, else false.
"""
def is_partial_email(input_email: str, actual_email: str) -> bool:
    reg_exp = re.compile(r"""
        ^
        (?P<local_part>[a-z0-9!#$%&'*+/=?^_`{|}~\.]+)
        @
        (?:estudiante.)?
        (?P<domain_part>[a-z0-9-\.]+)
        $
        """, re.VERBOSE | re.IGNORECASE)
    
    input_match = reg_exp.match(input_email)

    if not input_match:
        raise ValueError("The input email is not valid")

    actual_match = reg_exp.match(actual_email)

    if not actual_match:
        raise ValueError("The actual email is not valid")
    
    return (input_match.group("local_part") in actual_match.group("local_part") and 
        input_match.group("domain_part") == actual_match.group("domain_part"))


# Testing purposes
# if __name__ == "__main__":
#     print("test 1: yeps@estudiante.utv.edu.co")
    # print(classify_email("simon.gomez56@estudiante.utv.edu.co"))

#     print("\ntest 2: yeps@utv.edu.co")
#     print(classify_email("yeps@utv.edu.co"))

#     print("\ntest 3: yeps@eia.edu.co")
#     print(classify_email("yeps@eia.edu.co"))
    # print(check_name("kadaksdkad"))
    # print(check_number("57 312 270 5388"))
    # print(is_partial_email("s@utv.edu.co", "simon.gomez@estudiante.utv.edu.co"))