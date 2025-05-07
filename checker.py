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
    # reg_ex = "\S+@^From(\S[.])utv[.]edu[.]co"
    reg_ex = "\S+@^From (\S+)"
    print(re.findall(reg_ex, email))
    

if __name__ == "__main__":
    print("hello")
    classify_email("yeps@estudiante.utv.edu.co")