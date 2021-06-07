
cont = "yes"

while cont == "yes":
    calc = input("type in your maths problem:\n")
    print ("Answer: " + str(eval(calc)))
    cont = input("continue?(yes/no) ")