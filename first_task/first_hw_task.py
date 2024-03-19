def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = [el.strip() for el in file.readlines()]

            total = 0
            average = 0

            for curent_line in lines:
                new_curent_line = curent_line.split(',')
                new_salary = int(new_curent_line[1])
                total += new_salary

            average = total / len(lines)

            return (total, average)

    except FileNotFoundError as err:
        print('Файл не знайдено: ', err)

        return (0, 0)


total, average = total_salary('./first_task/salary_file.txt')

print(f'Загальна сума заробітної плати: {total}$, Середня заробітна плата: {average}$')