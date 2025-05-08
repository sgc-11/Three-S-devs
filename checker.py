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
    
    # reg_ex = re.compile("\S+@([a-z]+)\.utv\.edu\.co")
    reg_ex = re.compile(r"""
        ^  # This means that the regex must match the start of the string, that is, there is nothing before
        [a-z]+  # capture the start of the email
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
    reg_exp = re.compile(r"^[a-z]+$", re.IGNORECASE)

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

# Testing purposes
# if __name__ == "__main__":
#     print("test 1: yeps@estudiante.utv.edu.co")
#     print(classify_email("yeps@estudiante.utv.edu.co"))

#     print("\ntest 2: yeps@utv.edu.co")
#     print(classify_email("yeps@utv.edu.co"))

#     print("\ntest 3: yeps@eia.edu.co")
#     print(classify_email("yeps@eia.edu.co"))
    # print(check_name("kadaksdkad"))
    # print(check_number("57 312 270 5388"))