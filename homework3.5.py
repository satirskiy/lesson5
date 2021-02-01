with open("text_3.txt", 'r') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняя заработная плата {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'оклад меньше 20000{[e[0] for e in employees_dict.items() if e[1] < 20000]}')
