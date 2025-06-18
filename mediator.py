from abc import ABC, abstractmethod

class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, user: 'User'):
        pass

class User(ABC):
    def __init__(self, name: str, mediator: ChatMediator):
        self.name = name
        self.mediator = mediator

    @abstractmethod
    def send(self, message: str):
        pass

    @abstractmethod
    def receive(self, message: str):
        pass

class ChatServer(ChatMediator):
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def send_message(self, message: str, sender: User):
        for user in self.users:
            if user != sender:
                user.receive(f"{sender.name}: {message}")

class ChatUser(User):
    def send(self, message: str):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message: str):
        print(f"{self.name} received: {message}")