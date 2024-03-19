def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = [el.strip() for el in file.readlines()]
            
            info_list = []

            for curent_line in lines:
                new_curent_line = curent_line.split(',')

                cat_id = new_curent_line[0]
                cat_name = new_curent_line[1]
                cat_age = new_curent_line[2]

                current_cat_info = {
                    'id': cat_id,
                    'name': cat_name,
                    'age': cat_age
                }

                info_list.append(current_cat_info)

            return info_list

    except FileNotFoundError as err:
        print('Файл не знайдено: ', err)

        return []


cats_info = get_cats_info('./second_task/cats_info.txt')

print(cats_info)