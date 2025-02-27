def make_email_from_name(name):
    formated_name = name.lower().replace(" ", ".")
    return f"{formated_name}@gmail.com"
