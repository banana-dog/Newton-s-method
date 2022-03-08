def f(x):
    return x**2-2

def f1(x):
    return 2*x

x=1
epsilon=0.00000001
print("Поиск квадратного корня из двух по методу Ньютона, изначальное значение x -", x)
print(f"Требуемая точность - {epsilon}")
for i in range(1, 100):
    xold=x
    x=x-f(x)/f1(x)
    delta=abs(xold-x)
    print(f"Шаг {i}, результат {x}, дельта", delta)
    if epsilon > delta:
        print(x, "Задача решена за", i, "шагов, дельта", delta)
        break

print("Значение корня из двух на калькуляторе -", 2**(1/2))