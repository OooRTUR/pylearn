import json
import  requests


response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# Соотношение userId с числом выполненных пользователем задач.
todos_by_user = {}

# Увеличение выполненных задач каждым пользователем.
for todo in todos:
    if todo["completed"]:
        try:
            # Увеличение количества существующих пользователей.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # Новый пользователь, ставим кол-во 1.
            todos_by_user[todo["userId"]] = 1

# Создание отсортированного списка пар (userId, num_complete).
top_users = sorted(todos_by_user.items(),
                   key=lambda x: x[1], reverse=True)

# Получение максимального количества выполненных задач.
max_complete = top_users[0][1]

# Создание списка всех пользователей, которые выполнили
# максимальное количество задач.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)


def keep(todo):
    is_complete = todo["completed"]
    has_max_count = todo["userId"] in users
    return is_complete and has_max_count


# Записать отфильтрованные задачи в файл
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)


