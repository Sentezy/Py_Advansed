import tkinter as tk


class Calculator(tk.Frame):
    CANVAS_WIDTH = 350
    CANVAS_HEIGHT = 400

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.log = ''
        self._create_main_interface()
        self._create_buttons()
        self._create_log()
        self._create_display()

    def _create_main_interface(self):

        self.main_canvas = tk.Canvas(self,
                                     width=self.CANVAS_WIDTH,
                                     height=self.CANVAS_HEIGHT)
        self.main_canvas["bg"] = "#808080"

        self.main_canvas.pack()

    def _create_display(self):

        self.display_frame = tk.Frame(self.main_canvas,
                                      bg='#000',
                                      bd=5)

        self.display_frame.place(relx=0.5,
                                 rely=0.4,
                                 relwidth=0.98,
                                 relheight=0.15,
                                 anchor='n')

        self.display = tk.Entry(self.display_frame,
                                bg='#808080',
                                bd=5, foreground="#fff",
                                font=("Palatino Linotype", 17, "bold"),
                                relief='ridge',
                                justify='l')

        self.display.place(relx=0.5, rely=0.05,
                           relwidth=1.01,
                           relheight=0.95,
                           anchor='n')

        self.display.focus()

    def _create_log(self):

        self.log_frame = tk.Frame(self.main_canvas,
                                  bg='#808080',
                                  bd=5)

        self.log_frame.place(relx=0.5, rely=0.01,
                             relwidth=0.99,
                             relheight=0.39,
                             anchor='n')

        self.log_label = tk.Label(self.log_frame,
                                  bg='#000',
                                  bd=5,
                                  foreground="#fff",
                                  font=("Palatino Linotype", 15, "bold"),
                                  anchor='sw')

        self.log_label.place(relx=0.5, rely=0.01,
                             relwidth=1.02,
                             relheight=1,
                             anchor='n')

    def _create_buttons(self):

        self.button_frame = tk.Frame(self.main_canvas,
                                     bg='#000',
                                     bd=5)

        self.button_frame.place(relx=0.5, rely=0.56,
                                relwidth=0.98,
                                relheight=0.42,
                                anchor='n')

        btns = [
            '7', '8', '9', 'C', 'CE',
            '4', '5', '6', '+', '-',
            '1', '2', '3', '*', '/',
            '.', '0', '()', 'xⁿ', '='
        ]
        row = 1
        col = 0
        for bt in btns:
            cmd = lambda x=bt: self._calculations(x)
            tk.Button(self.button_frame, text=bt, bg="#fff",
                      font=("Times New Roman", 13),
                      command=cmd, width=3, height=1).grid(row=row,
                                                           column=col,
                                                           pady=3,
                                                           padx=5)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def _calculations(self, op):
        display_input = self.display.get()
        if op == '=':
            try:
                result = round(eval(display_input), 2)
                log_out = f'{display_input} = {result} '
            except ZeroDivisionError:
                log_out = " No way!"
            except SyntaxError:
                log_out = "Only numbers!"
            except TypeError:
                log_out = " Error!"
            except NameError:
                log_out = 'Its just calculator! '
            finally:
                self.log += f'\n{log_out}'
                self.log_label.configure(text=self.log)
                self.display.delete(0, 'end')

        elif op == 'C':
            self.display.delete(0, 'end')

        elif op == 'CE':
            self.display.delete(0, 'end')
            self.log = ''
            self.log_label.config(text=self.log)

        elif op == "xⁿ":
            self.display.insert('end', "**")

        else:
            if "=" in self.display.get():
                self.display.delete(0, 'end')
            self.display.insert('end', op)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Calculator')
    root.resizable(width=False, height=False)
    app = Calculator(master=root)
    app.mainloop()
