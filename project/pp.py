from lecture3 import schooles


def make_student(name, age):
    return schooles.Student.make_premium_student(name, age)


# make_student("John Doe", 20)