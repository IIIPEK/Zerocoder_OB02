# User Management System

Этот проект представляет собой простую систему управления пользователями с использованием классов Python. В системе есть два типа пользователей: обычные пользователи (`User`) и администраторы (`Admin`). Администраторы обладают расширенными привилегиями, такими как добавление и удаление пользователей.

## Структура проекта

Проект состоит из двух основных файлов:

1. **`user_classes.py`**: Содержит классы `Privileges`, `User` и `Admin`, которые реализуют функциональность системы управления пользователями.
2. **`main.py`**: Основной скрипт, который демонстрирует использование классов из `user_classes.py`.

## Классы

### Класс `Privileges`

Класс `Privileges` управляет привилегиями пользователей. Привилегии представлены в виде битовой маски, где каждый бит соответствует определенной привилегии:

- `can_change_name`
- `can_change_email`
- `can_change_password`
- `can_add_user`
- `can_delete_user`

Методы класса:

- `privileges_to_mask(privileges_list: list)`: Преобразует список привилегий в битовую маску.
- `show_privileges()`: Выводит текущие привилегии пользователя.
- `get_privileges()`: Возвращает текущие привилегии.
- `set_privileges(privileges)`: Устанавливает привилегии.

### Класс `User`

Класс `User` представляет обычного пользователя. Каждый пользователь имеет имя, email, пароль и набор привилегий.

Методы класса:

- `get_privileges()`: Возвращает объект `Privileges` пользователя.
- `set_privileges(privileges)`: Устанавливает привилегии пользователя.
- `get_name()`, `get_email()`, `check_password(password)`, `change_password(password)`, `change_name(name)`, `change_email(email)`: Методы для управления данными пользователя.
- `get_info()`: Выводит информацию о пользователе и его привилегиях.

### Класс `Admin`

Класс `Admin` наследует от класса `User` и представляет администратора. Администратор имеет все привилегии по умолчанию.

Методы класса:

- `add_user(users: [User])`: Добавляет пользователей в систему.
- `delete_user(username, users: [User])`: Удаляет пользователя из системы по имени.

## Использование

Пример использования классов можно увидеть в файле `main.py`. В этом скрипте создается администратор, добавляются несколько пользователей, а затем один из пользователей удаляется.

```python
from users_classes import Admin, User

def print_delimiter():
    print('=' * 50)

users = []
admin = Admin("Admin", "admin@example.com", "securepassword")
admin.get_info()
print_delimiter()

users.append(admin)

print_delimiter()

users.extend(admin.add_user(
    [
        User("John Doe", "john.doe@example.com", "password123"),
        User("Jane Doe", "jane.doe@example.com", "password123"),
        User("Bob Doe", "bob.doe@example.com", "password123"),
    ]
))
print_delimiter()

for user in users:
    user.get_info()
    print_delimiter()

print_delimiter()
admin.delete_user("John Doe", users)
print_delimiter()

for user in users:
    user.get_info()
    print_delimiter()

```
## Запуск проекта

Для запуска проекта выполните команду:

```bash
python main.py
```

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности см. в файле `LICENSE`.
```
