

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, new_password):
        self.password = new_password

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}")

    # Relationships
    def create_post(self, post):
        self.post = post

    def add_comment(self, comment):
        self.comment = comment

    def send_message(self, message):
        self.message = message

    def show_post(self):
        print(f"{self.name} created the post: {self.post.title}")

    def show_comment(self):
        print(f"{self.name} commented: {self.comment.content}")

    def show_message(self):
        print(f"{self.name} sent: {self.message.content}")


def create_post(title, content, author):
    return Post(title, content, author)


def create_comment(content, author, post):
    return Comment(content, author, post)


def send_message(sender, receiver, content):
    return Message(sender, receiver, content)


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display_post(self):
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")
        print(f"Author: {self.author.name}")


class Comment:
    def __init__(self, content, author, post):
        self.content = content
        self.author = author
        self.post = post

    def display_comment(self):
        print(f"Comment: {self.content}")
        print(f"Author: {self.author.name}")
        print(f"On Post: {self.post.title}")


class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def display_message(self):
        print(f"From: {self.sender.name}")
        print(f"To: {self.receiver.name}")
        print(f"Message: {self.content}")


# Instances
user1 = User("Carlos", "carlos@email.com", "12345")
user2 = User("Ana", "ana@email.com", "67890")

post = create_post(
    "My First Post",
    "Hello everyone!",
    user1
)

comment = create_comment(
    "Nice post!",
    user2,
    post
)

message = send_message(
    user1,
    user2,
    "Hi Ana!"
)

# Creacion de relaciones
user1.create_post(post)
user2.add_comment(comment)
user1.send_message(message)

# Use the relationships
user1.show_post()
user2.show_comment()
user1.show_message()

# Display objects
print("\n--- Post ---")
post.display_post()

print("\n--- Comment ---")
comment.display_comment()

print("\n--- Message ---")
message.display_message()
