score = 81

if score >= 80:
   print("A")
   print(f"score is {score}")
else:
   print("B")
   print(f"score is {score}")

# multiple conditions

if score >= 90:
    print("A")
    print(f"score is {score}")
elif score >= 80:
    print("B")
    print(f"score is {score}")
elif score >= 70:
    print("C")
    print(f"score is {score}")
else:
    print("D")
    print(f"score is {score}")

# nested conditions
if score >= 80:
    if score >= 90:
        print("A")
        print(f"score is {score}")
    else:
        print("B")
        print(f"score is {score}")

# no tenary operator
# shorthand if-else

is_grade_a = True if score >= 80 else False