from json import load
from tkinter import Tk, Entry, Button, Text, messagebox
from difflib import get_close_matches


def search(key, dictionary):
    text.delete(1.0, "end")
    if key.lower() in dictionary.keys():
        answers = dictionary[key.lower()]
    elif key.title() in dictionary.keys():
        answers = dictionary[key.title()]
    elif key.upper() in dictionary.keys():
        answers = dictionary[key.upper()]
    else:
        close_match = get_close_matches(key, dictionary.keys(), 1, 0.8)
        if close_match:
            response = messagebox.askyesno(title="Did you mean...", message=f"Did you mean {close_match[0]}?")
            if response is True:
                entry.delete(0, "end")
                entry.insert(0, close_match)
                text.focus()
                search(close_match[0], dictionary)
            else:
                text.insert(1.0, "Word not found")
        return
    i = 0
    message = ""
    for answer in answers:
        i += 1
        message += (str(i) + ". " + answer + "\n")
    text.insert(1.0, message)


vocabulary = load(open("data.json", "r"))
root = Tk()
root.title("English dictionary")
root.resizable(0, 0)
entry = Entry(root)
entry.pack()
search_button = Button(root, text="Search", command=lambda: search(entry.get(), vocabulary))
search_button.pack()
text = Text(root, width=40, height=10, wrap="word")
text.pack()
root.mainloop()
