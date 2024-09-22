# exception handling

a = 10
b = 0
try:
    result = a / b
except Exception as e:
    # excute when error occurs
    print(f"error: {e}")
else:
    # excute when no error
    print(result)
finally:
    # always excuted
    print("done") 
