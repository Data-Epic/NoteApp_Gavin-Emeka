# 1. Creating my Base class called 'Note', I have:
class Note:

    # Constructors: Seting all the attributes/properties of the Note object, I have:
    def __init__(self, content, created_at):
        self.content = content
        self.created_at = created_at 

    # Display Method: Setting the Note object processes, i.e the Note details, I have:
    def display_details(self):
        print("Gavin's Note content is: ", self.content)
        print("Gavin's Note was created at: ", self.created_at)

# Creating Note objects, I have:
note1 = Note("I arrived Port Harcout on Wednesday, 5th February, 2025 at 03:35pm.", "Sunday 9th Feb 2025. 06:07pm")
note2 = Note("I have Spent the last two weeks, learning and participating in a research study.", "Thursday 6th Feb, 2025. 8:00pm")

# Accessing the Note objects attributes, I have:
print(note1.content, note1.created_at)
note1.display_details()
note2.display_details()





# 2. Extending my Base class and Creating my Sub classes called 'TextNote' and 'ReminderNote', I have:
""" A subclass of Note that inherits the behavior of the Note class and extends
    functionality to include a reminder time.

    Attributes:
        content (str): The content of the note.
        reminder_time (str): The time set for the reminder.
        created_at (datetime): Inherited from Note, stores when the note was created.

    Methods:
        display(): This will Overrides the display() method to show both the reminder time and the note details.
"""
class TextNote(Note):
    def display_details(self):
        return super().display_details()
    
TN1 = TextNote("The 4 fundamental concepts of OOP, are Abstraction, Encapsulation, Inheritance, and Polymorphism.", "Friday 6th June 2025. 06:07pm")
TN2 = TextNote("An object is anything of interest to the program we want to build.", "Thursday 6th Feb, 2025. 8:00pm")

# Accessing the TextNote objects attributes, I have:
TN1.display_details()




# Creating my ReminderNote class, I have:
class ReminderNote(Note):
    def __init__(self, content, created_at, reminder_time):
        super().__init__(content, created_at)
        self.reminder_time = reminder_time

    def display_details(self):
        print("Gavin's Reminder Note content is: ", self.content)
        print("Gavin's Reminder Note was created at: ", self.created_at)
        print("Gavin's Reminder Note time is: ", self.reminder_time)

# Creating ReminderNote objects, I have:

RN1 = ReminderNote("I'll meet you at 9am tomorrow.", "Friday 6th June 2025. 06:07pm", "9:00am")
RN2 = ReminderNote("I'll be on the phone with my family at 3pm.", "Thursday 6th Feb, 2025. 8:00pm", "3:00pm")

# Accessing the ReminderNote objects attributes, I have:
RN1.display_details()
RN2.display_details()




# 3. Implementing my Notes Manager class, to include 'add notes', 'delete notes, 'show notes', and 'search notes', I have:
class NotesManager:
    def __init__(self):
        self.notes = []
