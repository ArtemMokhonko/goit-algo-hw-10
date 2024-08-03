import pulp

# Створення проблеми лінійного програмування
problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні
x = pulp.LpVariable('Limonad', lowBound=0, cat='Continuous')
y = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Цільова функція
problem += x + y, "Total_Products"


# Обмеження
problem += 2 * x + y <= 100, "Water_Constraint"
problem += x <= 50, "Sugar_Constraint"
problem += x <= 30, "Lemon_Juice_Constraint"
problem += 2 * y <= 40, "Fruit_Puree_Constraint"


# Розв'язання проблеми
problem.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[problem.status]}")
print(f"Кількість виробленого Лимонаду: {x.varValue}")
print(f"Кількість виробленого Фруктового соку: {y.varValue}")
print(f"Загальна кількість продуктів: {pulp.value(problem.objective)}")
