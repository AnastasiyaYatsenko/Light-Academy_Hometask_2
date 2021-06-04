#Anastasiia Yatsenko
import turtle


def hilbert_curve(order):
    path = ["A"]
    a = ["+", "B", "F", "−", "A", "F", "A", "−", "F", "B", "+"]
    b = ["−", "A", "F", "+", "B", "F", "B", "+", "F", "A", "−"]
    for i in range(order-1):
        j = 0
        while j < len(path):
            if path[j] == "A":
                path.pop(j)
                for elem_a in a:
                    path.insert(j, elem_a)
                    j += 1
                j += 1
            elif path[j] == "B":
                path.pop(j)
                for elem_b in b:
                    path.insert(j, elem_b)
                    j += 1
                j += 1
            else:
                j += 1

    turtle.reset()
    turtle.up()
    turtle.goto(-100, 0)
    turtle.down()
    for elem in path:
        if elem == "F":
            turtle.forward(10)
        elif elem == "+":
            turtle.left(90)
        elif elem == "−":
            turtle.right(90)
    turtle.mainloop()


def dragon_curve(order):
    path = ["F"]
    f = ["F", "+", "G"]
    g = ["F", "-", "G"]
    for i in range(order-1):
        j = 0
        while j < len(path):
            if path[j] == "F":
                path.pop(j)
                for elem_f in f:
                    path.insert(j, elem_f)
                    j += 1
                j += 1
            elif path[j] == "G":
                path.pop(j)
                for elem_g in g:
                    path.insert(j, elem_g)
                    j += 1
                j += 1
            else:
                j += 1

    turtle.reset()
    turtle.up()
    turtle.goto(-100, 0)
    turtle.down()
    for elem in path:
        if elem == "+":
            turtle.left(90)
        elif elem == "-":
            turtle.right(90)
        else:
            turtle.forward(10)
    turtle.mainloop()


#hilbert_curve(4)
dragon_curve(10)
