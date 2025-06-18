from abc import ABC, abstractmethod
from typing import List

class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, user: 'User'):
        pass

class User(ABC):
    def __init__(self, name: str, mediator: ChatMediator):
        self.name = name
        self.mediator = mediator
        self.received_messages: List[str] = []  # Лист лога сообщений для теста

    @abstractmethod
    def send(self, message: str):
        pass

    def receive(self, message: str):
        self.received_messages.append(message)  

class ChatServer(ChatMediator):
    def __init__(self):
        self.users: List[User] = []

    def add_user(self, user: User):
        self.users.append(user)

    def send_message(self, message: str, sender: User):
        for user in self.users:
            if user != sender:
                user.receive(f"{sender.name}: {message}")

class ChatUser(User):
    def send(self, message: str):
        self.mediator.send_message(message, self)