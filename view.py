
class View:
    def menu_show(self):
        print("Выберите пункт меню:\n"
              "1. Создать заметку\n"
              "2. Редактировать заметку\n"
              "3. Удалить заметку\n"
              "4. Прочитать заметку\n"
              "5. Вывести список из всех заметок\n"
              "6. Сохранить заметки\n"
              "7. Выход\n")

    def list_notfull(self, note):
        ready_to_print = f"ID: {str(note.get_id())}\t"
        ready_to_print += f"Name: {str(note.get_name())}\n"
        print(ready_to_print)

    def list_note(self, note):
        ready_to_print = f"ID: {str(note.get_id())}\n"
        ready_to_print += f"Date: {str(note.get_date())}\n"
        ready_to_print += f"Name: {str(note.get_name())}\n"
        ready_to_print += f"Content: {str(note.get_content())}\n"
        print(ready_to_print)

    def input_name(self):
        return input(f"Введите название заметки: ")

    def input_content(self):
        return input(f"Текст заметки: ")

    def edit(self, note):
        note.set_content(self.input_content())
        note.date_control()
        print("Заметка была успешно отредактирована.")

    def input_number(self, limit):
        value = 0
        while True:
            try:
                value = int(input("Пожалуйста, введите номер: "))
            except ValueError:
                print("Typing error... Try again")
                continue
            if 0 <= value <= limit:
                break
        return value

    def exit(self):
        print("Exiting...")