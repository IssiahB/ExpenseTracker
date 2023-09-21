import tkinter as tk

class ExpenseTrackerGUI:
    def __init__(self, root) -> None:
        self.width = 900
        self.height = 600
        self.root = root
        self.root.title('Expense Tracker')
        self._center_window()
        self._build()

    def _center_window(self):
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate x and y coordinates to center window
        x = (screen_width - self.width) // 2
        y = (screen_height - self.height) // 2 - 30

        # set position
        self.root.geometry(f'{self.width}x{self.height}+{x}+{y}')

    def _build(self):
        # Calls the functions to build the gui
        self._build_frame()
    
    def _build_frame(self):
        main_frame = tk.Frame(self.root, bg='#AAD9EE')
        main_frame.grid(row=0, column=0, sticky='nsew', ipadx=10, ipady=10)

        left_frame = tk.Frame(main_frame, bg='#00ff00')
        left_frame.grid(row=0, column=0, sticky='nsew')

        right_frame = tk.Frame(main_frame, bg='#ff0000')
        right_frame.grid(row=0, column=1, sticky='nsew')

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        button_label = tk.Label(left_frame, text='Buttons Go Here')
        button_label.pack()

        misc_label = tk.Label(right_frame, text='Other Goes Here')
        misc_label.pack()