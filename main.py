from person import Person
from diet import Diet

def main():
    guy = Person(30,260,"73","male")
    print(guy.bmi_calc())
    diet = Diet(30,20,160,"healthy","male","active",73)
    print(diet.calories())

main()