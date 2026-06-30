# ==========================================
#         NUMBER ANALYZER - VERSION 1
# ==========================================

# Input
num = int(input("Enter a Number: "))

# Store original value
original = num
temp = num
armstrong_temp = num

# Initialize variables
digit_sum = 0
product = 1
digit_count = 0
reverse = 0

max_digit = 0
min_digit = 9

even_count = 0
odd_count = 0

contains_zero = False

# ==========================================
# Digit Analysis
# ==========================================

while temp > 0:
    digit = temp % 10

    digit_sum += digit
    product *= digit
    digit_count += 1
    reverse = reverse * 10 + digit

    # Largest Digit
    if digit > max_digit:
        max_digit = digit

    # Smallest Digit
    if digit < min_digit:
        min_digit = digit

    # Even & Odd Count
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    # Contains Zero
    if digit == 0:
        contains_zero = True

    temp //= 10

# ==========================================
# Armstrong Number
# ==========================================

armstrong_number = 0

while armstrong_temp > 0:
    digit = armstrong_temp % 10
    armstrong_number += digit ** digit_count
    armstrong_temp //= 10

# ==========================================
# Prime Number
# ==========================================

is_prime = True

if original <= 1:
    is_prime = False
else:
    for i in range(2, original):
        if original % i == 0:
            is_prime = False
            break

# ==========================================
# Spy Number
# ==========================================

is_spy = (digit_sum == product)

# ==========================================
# Harshad Number
# ==========================================

if digit_sum != 0:
    is_harshad = (original % digit_sum == 0)
else:
    is_harshad = False

# ==========================================
# Palindrome
# ==========================================

is_palindrome = (reverse == original)

# ==========================================
# Armstrong
# ==========================================

is_armstrong = (armstrong_number == original)

# ==========================================
# Report
# ==========================================

print("\n======================================")
print("        NUMBER ANALYZER REPORT")
print("======================================")

print(f"Original Number     : {original}")
print(f"Reverse Number      : {reverse}")
print(f"Digit Count         : {digit_count}")
print(f"Sum of Digits       : {digit_sum}")
print(f"Product of Digits   : {product}")
print(f"Largest Digit       : {max_digit}")
print(f"Smallest Digit      : {min_digit}")
print(f"Even Digit Count    : {even_count}")
print(f"Odd Digit Count     : {odd_count}")
print(f"Contains Zero       : {'Yes' if contains_zero else 'No'}")

print("--------------------------------------")

print(f"Palindrome          : {'Yes' if is_palindrome else 'No'}")
print(f"Prime Number        : {'Yes' if is_prime else 'No'}")
print(f"Armstrong Number    : {'Yes' if is_armstrong else 'No'}")
print(f"Spy Number          : {'Yes' if is_spy else 'No'}")
print(f"Harshad Number      : {'Yes' if is_harshad else 'No'}")

print("======================================")