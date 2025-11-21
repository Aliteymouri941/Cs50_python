
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    digit_started = False
    for i in range(len(s)):
        char = s[i]

        if not char.isalnum():
            return False

        if char.isdigit():
            if not digit_started:
                digit_started = True
                if char == '0':
                    return False
        elif digit_started:
            return False  

    return True


main()