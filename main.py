# import utils
# from lecture3 import schooles

# print(utils.make_email_from_name("John Doe"))  #
# student = schooles.Student.make_premium_student("John Doe", 20)
# schol =  schooles.School("SMA 1", "Jl. Sudirman")
# print(student)
# from project.pp import make_student
import requests

response = requests.get("https://dummyjson.com/products")
print(response.json())
