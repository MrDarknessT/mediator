from mediator import ChatServer, ChatUser

def test_chat_message_received():
    server = ChatServer()
    user1 = ChatUser("Alice", server)
    user2 = ChatUser("Bob", server)
    server.add_user(user1)
    server.add_user(user2)

    user1.send("Hello Bob!")

def test_multiple_users_receive_message():
    server = ChatServer()
    users = [ChatUser(f"User{i}", server) for i in range(3)]
    for user in users:
        server.add_user(user)

    users[0].send("Hi all!")