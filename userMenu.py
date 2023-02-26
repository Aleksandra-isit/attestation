from listOfNotes import ListOfNotes
from view import View

class UserMenu:
    __viewers = View()
    __notes = ListOfNotes()

    def start(self):
        while(1):
            self.__viewers.menu_show()
            choose = self.__viewers.input_number(7)
            if choose == 7:
                self.__viewers.exit()
                break
            else:
                if choose == 1:
                    self.__notes.add_note()
                elif choose == 2:
                    self.__notes.edit_note()
                elif choose == 3:
                    self.__notes.delete_note()
                elif choose == 4:
                    self.__notes.read_note()
                elif choose == 5:
                    self.__notes.read_all_noteS()
                elif choose == 6:
                    self.__notes.save_notes()

