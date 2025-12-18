import re
import json
from abc import ABC, abstractmethod
from typing import List

class User(ABC):
    def __init__(self, uid: int, first_name: str, last_name: str, email: str):
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @abstractmethod
    def get_full_name(self):
        pass

    @abstractmethod
    def is_email_valid(self):
        pass

class CSVUser(User):
    def __init__(self, data: str):
        uid, full_name, email = data.split(';')
        first_name, last_name = full_name.split()
        super().__init__(int(uid), first_name, last_name, email)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name} {self.email}"

    def is_email_valid(self):
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", self.email))

class JSONUser(User):
    def __init__(self, data: str):
        data_dict = json.loads(data)
        first_name = data_dict["first_name"]
        last_name = data_dict["last_name"]
        email = data_dict["contacts"]["email"]
        super().__init__(data_dict["uid"], first_name, last_name, email)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name} {self.email}"

    def is_email_valid(self):
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", self.email))

class RawUser(User):
    def __init__(self, data: str):
        parts = data.split()
        first_name = parts[1]
        last_name = parts[0]
        email = parts[2]
        super().__init__(None, first_name, last_name, email)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name} {self.email}"

    def is_email_valid(self):
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", self.email))

class UserCollection:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def get_all_emails(self):
        return [user.email for user in self.users]

    def find_by_name(self, name: str):
        return [user for user in self.users if name in user.first_name or name in user.last_name]

    def find_invalid_emails(self):
        return [user for user in self.users if not user.is_email_valid()]

    def print_users(self):
        for user in self.users:
            print(user.get_full_name())

def parse_user(data: str) -> User:
    if data.startswith('csv'):
        return CSVUser(data[4:])
    elif data.startswith('json'):
        return JSONUser(data[5:])
    elif data.startswith('raw'):
        return RawUser(data[4:])
    else:
        raise ValueError(f"Unknown user format: {data}")

def process_command(users: UserCollection, command: str):
    if command == "emails":
        emails = users.get_all_emails()
        for email in emails:
            print(email)
    elif command.startswith("find "):
        name = command.split('=')[1]
        found_users = users.find_by_name(name)
        if found_users:
            for user in found_users:
                print(user.get_full_name())
        else:
            print("No users found.")
    elif command == "invalid":
        invalid_users = users.find_invalid_emails()
        if invalid_users:
            for user in invalid_users:
                print(user.get_full_name())
        else:
            print("All emails are valid.")
    else:
        print(f"Unknown command: {command}")

def main():
    users_data = [
        "csv 123;Иван Иванов;ivan@example.com",
        'json {"uid": 42, "first_name": "Petr", "last_name": "Petrov", "contacts": {"email": "petr@example.com"}}',
        "raw Иванов Иван ivanov@example.com"
    ]

    users = UserCollection()

    for data in users_data:
        user = parse_user(data)
        users.add_user(user)

    print("Все пользователи:")
    users.print_users()
    
    print("\nКоманда: emails")
    process_command(users, "emails")
    
    print("\nКоманда: find name=Иван")
    process_command(users, "find name=Иван")
    
    print("\nКоманда: invalid")
    process_command(users, "invalid")

if __name__ == "__main__":
    main()
