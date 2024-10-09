from datetime import datetime


def calculate_discounted_price(price, discount):
    return price * (1 - discount / 100)


def calculate_dimensions(length, width, height):
    return length * width * height


def fullname(firstname, lastname):
    return f"{firstname} {lastname}"


def get_year_of_birth(age):
    return datetime.now().year - age
