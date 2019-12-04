range_lower = 265275
range_upper = 781584

def possible_password(password):
    '''Returns true if it's a possible password'''
    digits = [i for i in str(password)]
    if not len(digits) > len(set(digits)):
        return False # Does not have a repeat digit

    if not ''.join(sorted(digits)) == str(password):
        return False # Digits are not in the correct order

    return True

    
possible_passwords = [pw for pw in range(range_lower, range_upper)
                      if possible_password(pw)]

print(f'Part 1: No. possible passwords {len(possible_passwords)}')

def part_2_possible_password(password):
    '''Feed in previous possibles only for further vetting'''
    for digit in set(str(password)):
        if str(password).count(digit) == 2:
            return True
    return False

possible_passwords = [pw for pw in possible_passwords
                      if part_2_possible_password(pw)]


print(f'Part 2: No. possible passwords {len(possible_passwords)}')
