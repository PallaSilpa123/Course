name = input("Enter your name: ")
first_letters = ['A','B','C','D','E','F','G','H']
second_letters = ['I','J','K','L','M','N','O','P']
third_letters = ['Q','R','S','T','U','V','W','X','Y','Z']

def dummy_fun_course(name):
    if name[0].upper() in first_letters:
        print("name: ",str(name))
        print("Git module from course1")
        print("The module explains about various git commands and its usage")
    elif name[0].upper() in second_letters:
        print("name: ",str(name))
        print("open source module from course2")
        print("The module explains about various open source repositories and its usage")
    elif name[0].upper() in third_letters:
        print("name: ",str(name))
        print("advance git module from course3")
        print("The module explains about advance concepts in git and its usage")
    else:
        print("Not matching")

dummy_fun_course(name)
