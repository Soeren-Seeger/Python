# f'(x) = -(5 (x^5)^(1/3) sin((x^5)^(1/3)) + 3 cos((x^5)^(1/3)))/(3 x^2)
import re

function_expression = input("Gib die Funktion ein : ")


def get_next_bracket(index_target, direction):
    if direction == "left":
        counter = 0  # erhöht sich, wenn die andere Klammerrichtung gefunden wurde bsp ( relevant(gehörtaucdazu) )
        for i in reversed(range(index_target)):
            if function_expression[i] == "(":
                if counter == 0:
                    print(i)
                    return int(i)
                else:
                    counter -= 1  # Innere Klammre wieder geschlossen
            if function_expression[i] == ")":  # innere Klammer gefunden!!
                counter += 1

    if direction == "right":
        counter = 0
        for i in (range(index_target, (len(function_expression)))):
            if function_expression[i] == ")":
                if counter == 0:
                    print(i)
                    return int(i)
                else:
                    counter -= 1
            if function_expression[i] == "(":  # innere Klammer gefunden!!
                counter += 1


def pow_function(f1):
    for index in range(len(f1)):
        if f1[index] == "^":
            left =  get_next_bracket(index, "left")
            right = get_next_bracket(index, "right")
            base = f1[left + 1:index]  # linke Klammer bis ^
            exponent = f1[index + 1: right]  # ^ bis zur rechten Klammer
            f1 = f1.replace(f1[left: right + 1],
                            "Math.pow(" + base + " , " + exponent + ")")  # Tausche das ganze mit Math.pow(basis, exponent)
    return f1


function_expression = pow_function(function_expression)
print(function_expression)
# p = re.compile("[(][abc]*[)]")
# print((p.sub('sub', 'halloich(a)bin')))
# hallo(ich(nicht)bin^wichtig(nicht)du)schon
