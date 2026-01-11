#try except

try:
    # code that might cause an error
    result = 10 / 0
except:
    print("An error occurred!")

print("This will be printed regardless.")


try:
    result = 10 / 0
except Exception as error:
    print("Error:", error)