import pulp

# Створення проблеми лінійного програмування
problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні
x = pulp.LpVariable('Limonad', lowBound=0, cat='Continuous')
y = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Цільова функція
problem += x + y, "Total_Products"

# Обмеження
problem += 2 * x + y <= 100, "Water_Constraint"  # Обмеження на воду
problem += x <= 50, "Sugar_Constraint"           # Обмеження на цукор
problem += x <= 30, "Lemon_Juice_Constraint"     # Обмеження на лимонний сік
problem += 2 * y <= 40, "Fruit_Puree_Constraint" # Обмеження на фруктове пюре

# Розв'язання проблеми
problem.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[problem.status]}")
print(f"Кількість виробленого Лимонаду: {x.varValue}")
print(f"Кількість виробленого Фруктового соку: {y.varValue}")
print(f"Загальна кількість продуктів: {pulp.value(problem.objective)}\n")

# Обчислення витрачених ресурсів
used_water = 2 * x.varValue + y.varValue
remaining_water = 100 - (2 * x.varValue + y.varValue)
used_sugar = x.varValue
remaining_sugar = 50 - x.varValue
used_lemon_juice = x.varValue
remaining_juice = 30 - x.varValue
used_fruit_puree = 2 * y.varValue
remaining_puree = 40 - (2 * y.varValue)

# Виведення витрачених ресурсів
print(f"Використано води: {used_water} одиниць. Залишилось: {remaining_water} одиниць.")
print(f"Використано цукру: {used_sugar} одиниць. Залишилось: {remaining_sugar} одиниць.")
print(f"Використано лимонного соку: {used_lemon_juice} одиниць. Залишилось: {remaining_juice} одиниць.")
print(f"Використано фруктового пюре: {used_fruit_puree} одиниць. Залишилось: {remaining_puree} одиниць.")
