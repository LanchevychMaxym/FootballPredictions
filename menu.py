from alrogithm import *
from tkinter import *
from tkinter.ttk import Combobox


class Menu:

    def display_prediction(self):
        self.result_text1.delete(1.0, END)
        self.result_text2.delete(1.0, END)
        resultt = self.calc_res(self.name1_entry.get(), self.name2_entry.get())
        self.result_text1.insert(END, str(resultt[0]))
        self.result_text2.insert(END, str(resultt[1]))

    def __init__(self):
        self.root = Tk()
        self.root.title("ПРОГНОЗИ НА ФУТБОЛ")
        self.root.geometry("800x100")

        self.teams = Frame(self.root)
        self.name1_label = Label(self.teams, text="Команда №1:")
        self.name2_label = Label(self.teams, text="Команда №2:")

        self.name1_label.pack(side=TOP)
        self.name2_label.pack(side=TOP)
        self.teams.pack(side=LEFT)


        self.entry_frame = Frame(self.root)
        self.name1_entry = Combobox(self.entry_frame)
        self.name2_entry = Combobox(self.entry_frame)
        self.teams = self.list_of_teams_names()
        self.name1_entry['values'] = self.teams
        self.name2_entry['values'] = self.teams
        self.name1_entry.current(0)
        self.name2_entry.current(0)
        self.name1_entry.pack(side=TOP, padx=5, pady=5)
        self.name2_entry.pack(side=TOP, padx=5, pady=5)
        self.entry_frame.pack(side=LEFT, fill=X, expand=YES)

        self.res_button = Button(self.root, text="Отримати Результат", command=self.display_prediction)
        self.res_button.pack(side=LEFT, fill=X, padx=5, pady=5, expand=YES)

        self.result_frame1 = Frame(self.root)

        self.name1_label = Label(self.result_frame1, text="Ймовірність перемоги першої:")
        self.name2_label = Label(self.result_frame1, text="Ймовірність перемоги другої::")

        self.name1_label.pack(side=TOP)
        self.name2_label.pack(side=TOP)
        self.result_frame1.pack(side=LEFT, fill=X, expand=YES)

        self.result_frame2 = Frame(self.root)
        self.result_text1 = Text(self.result_frame2, bd=1, height=1, width=15)
        self.result_text1.pack(side=TOP, padx=5, pady=5)
        self.result_text2 = Text(self.result_frame2, bd=1, height=1, width=15)
        self.result_text2.pack(side=TOP, padx=5, pady=5)
        self.result_frame2.pack(side=LEFT, fill=X, expand=YES)

        self.root.mainloop()

    def calc_res(self, name_of_first_team, name_of_second_team):
        self.name1 = name_of_first_team
        self.name2 = name_of_second_team
        self.result = predict(name_of_first_team, name_of_second_team)
        return self.result[0], self.result[1]

    def list_of_teams_names(self):
        listt_of_teams = parse_web()
        res_list = [key for key in listt_of_teams.keys()]
        return res_list
