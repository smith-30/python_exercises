# -  *  - coding:utf-8 -  *  -

if __name__ == "__main__":
    names = ("Bill", "Anne", "Angy", "Cony", "Daniel", "Occhan")
    for i, n in enumerate(names):
        if n == "Angy":
            print("{0}.My name is {1}".format(i, n))
        else:
            print("{0}.{1} is my classmate".format(i, n))
