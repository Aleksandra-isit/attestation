from datetime import datetime

class Note:
    __id = 0
    __name = ""
    __date = ""
    __content = ""

    def set_id(self, inpt):
        self.__id = inpt

    def set_name(self, inpt):
        self.__name = inpt

    def set_content(self, inpt):
        self.__content = inpt

    def get_id(self):
        return self.__id

    def get_name(self):

        return self.__name

    def get_content(self):
        return self.__content

    def date_control(self):
        self.__date = datetime.now().strftime('%Y, %B %d, %A || %H:%M')

    def get_date(self):
        return self.__date
