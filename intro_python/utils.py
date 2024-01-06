# print("out of main block!")
# print("__name__ is {}".format(__name__))

def sep(part):
    print("="*15 + str(part) + "="*15)

if __name__ == "__main__": 
   # __name__ is __main__ when the script is executed directly, not imported
    print("inside main block")
