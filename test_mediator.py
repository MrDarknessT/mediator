from mediator import ChatServer, ChatUser

def test_message_received_by_other_user():
    server = ChatServer()
    user0 = ChatUser("user0", server)
    user1 = ChatUser("user1", server)
    server.add_user(user0)
    server.add_user(user1)

    user0.send("Hello user1!")
    
    assert len(user1.received_messages) == 1
    assert "user0: Hello user1!" in user1.received_messages
    assert len(user0.received_messages) == 0 

def test_message_not_sent_to_sender():
    server = ChatServer()
    user0 = ChatUser("user0", server)
    server.add_user(user0)

    user0.send("Hello me")  
    
    assert len(user0.received_messages) == 0

def test_multiple_users_receive_messages():
    server = ChatServer()
    users = [ChatUser(f"user{i}", server) for i in range(3)]
    for user in users:
        server.add_user(user)

    users[0].send("Hi all!")
    
    assert len(users[0].received_messages) == 0
    assert len(users[1].received_messages) == 1
    assert len(users[2].received_messages) == 1