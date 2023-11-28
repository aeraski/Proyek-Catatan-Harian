import os
import json

#initialize the data structure of the record
notes = []
#function to add new notes
def add_notes():
    title = input("Input your title: ")
    contents = input("Input your contents: ")
    
    #Generate Unique ID for number notes right now
    id_notes = len(notes) + 1
    new_notes = {
        "id": id_notes,
        "title": title,
        "contents": contents,
    }
    notes.append(new_notes)
    print("Notes successfully added!")
    
#function to display all notes
def show_all_notes():
    for note in notes:
        print(f"\nID: {note['id']}")
        print(f"title: {note['title']}")
        print(f"contents: {note['contents']}")
        print("-" * 30)

#Function to delete records based on ID
def delete_notes():
    delete_id= int(input("Enter the ID of the note you want to delete: "))
    notes_deleted = None
    
    for note in notes:
        if note['id'] == delete_id:
            notes_deleted = note
            break
    
    if notes_deleted:
        notes.remove(notes_deleted)
        print(f"Notes with ID {delete_id} deleted successfully.")  
    else:
        print(f"No record with ID {delete_id}.")

#Function to save notes into a JSON file
def save_to_file():
    with open("notes.json", "w") as file:
        json.dump(notes, file)
        
#Function to read notes from JSON file
def read_from_file():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            return json.load(file)    
    return []

#main program
#read notes from file when program started
notes = read_from_file()

while True:
    print("====== Notes Application ======")
    print("1. Add Notes")
    print("2. Show All Notes")
    print("3. Delete Notes")
    print("4. Exit")
    
    choose = input("Select Menu (1/2/3/4): ")
    
    if choose == "1":
        add_notes()
    elif choose == "2":
        show_all_notes()
    elif choose == "3":
        delete_notes()
    elif choose == "4":
        #Save Notes to a file before exiting
        save_to_file()
        print("Thank You! Program stopped.")
        break
    else:
        print("Invalid selection, Please Try Again!.")
