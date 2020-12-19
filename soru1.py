mail = "ali.erbey@usak.edu.tr"

def emailControl(mail):
    control = False

    for e in mail:
        if e == "@":
            control = True
        if control and e == ".":
            return True

    return False

print(emailControl(mail))