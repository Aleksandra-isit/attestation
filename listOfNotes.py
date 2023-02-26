import pickle
from note import Note
from view import View

class ListOfNotes:
    __notes = []
    __viewers = View()
    __index = 0
    __stack_index = []

    def __init__(self):
        try:
            with open('notes.pkl', 'rb') as file:
                self.__notes = pickle.load(file)
                self.__index = len(self.__notes)
            with open('indexes.pkl', 'rb') as file:
                self.__stack_index = pickle.load(file)
        except EOFError:
            self.__notes = []
            self.__viewers = View()
            self.__index = 0
            self.__stack_index = []

    def add_note(self):
        note = Note()
        note.set_name(self.__viewers.input_name())
        note.set_content(self.__viewers.input_content())
        note.date_control()
        if len(self.__stack_index) == 0:
            note.set_id(self.__index+1)
        else:
            note.set_id(self.__stack_index.pop())
        self.__notes.append(note)
        self.__index = len(self.__notes)
        print("Add correctly")
        input("Нажмите любую кнопку, чтобы продолжить...")

    def delete_note(self):
        self.read_to_find()
        value = self.__viewers.input_number(len(self.__notes))
        flag = False
        for note in self.__notes:
            if note.get_id() == value:
                self.__stack_index.append(note.get_id())
                self.__notes.remove(note)
                if len(self.__notes) == 0:
                    self.__stack_index.clear()
                print("Delete correctly")
        if not flag:
            print("not found")
        input("Нажмите любую кнопку, чтобы продолжить...")

    def read_all_noteS(self):
        for note in self.__notes:
            self.__viewers.list_note(note)
        input("Нажмите любую кнопку, чтобы продолжить...")

    def read_to_find(self):
        for note in self.__notes:
            self.__viewers.list_notfull(note)

    def read_note(self):
        self.read_to_find()
        value = self.__viewers.input_number(len(self.__notes))
        flag = False
        for note in self.__notes:
            if note.get_id() == value:
                self.__viewers.list_note(note)
                flag = True
        if not flag:
            print("not found")
        input("Нажмите любую кнопку, чтобы продолжить...")

    def edit_note(self):
        self.read_to_find()
        value = self.__viewers.input_number(len(self.__notes))
        flag = False
        for note in self.__notes:
            if note.get_id() == value:
                self.__viewers.edit(note)
                flag = True
        if not flag:
            print("not found")
        input("Нажмите любую кнопку, чтобы продолжить...")

    def save_notes(self):
        with open('notes.pkl', 'wb') as file:
            pickle.dump(self.__notes, file,
                        protocol=pickle.HIGHEST_PROTOCOL)
        with open('indexes.pkl', 'wb') as file:
            pickle.dump(self.__stack_index, file,
                        protocol=pickle.HIGHEST_PROTOCOL)
        print("Информация о заметках успешно сохранена")