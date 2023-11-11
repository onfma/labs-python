class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        return f"Title: {self.title}\nItem ID: {self.item_id}\nStatus: {'Checked out' if self.checked_out else 'Available'}"

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is not checked out."

class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def display_info(self):
        return f"{super().display_info()}\nAuthor: {self.author}\nType: Book"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        return f"{super().display_info()}\nDirector: {self.director}\nDuration: {self.duration} minutes\nType: DVD"

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def display_info(self):
        return f"{super().display_info()}\nIssue Number: {self.issue_number}\nType: Magazine"

# Example usage:
book = Book("The Great Gatsby", 101, "F. Scott Fitzgerald")
print(book.display_info())
print(book.check_out())
print(book.return_item())

print("\n")

dvd = DVD("Inception", 201, "Christopher Nolan", 148)
print(dvd.display_info())
print(dvd.check_out())
print(dvd.check_out())
print(dvd.return_item())

print("\n")

magazine = Magazine("National Geographic", 301, 2022)
print(magazine.display_info())
print(magazine.check_out())
print(magazine.return_item())
