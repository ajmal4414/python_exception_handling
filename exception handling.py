class Error(Exception):
    pass
class valuetoosmallerrors(Error):
    pass

class valuetoolargeerrors(Error):
    pass

while(True):
    try:
        num=int(input("enter any value in 10 to 50 range"))
        if num<10:
            raise valuetoosmallerrors
        elif num>50:
            raise valuetoolargeerrors
        break
    except valuetoosmallerrors:
        print("value is below range..try again")
    except valuetoolargeerrors:
        print("value out of range..try again")

print("great ,value in correct range")
