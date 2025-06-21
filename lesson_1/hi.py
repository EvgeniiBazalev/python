import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, master):
        # Настройка основного окна
        self.master = master
        self.master.title("Угадай число")
        self.master.geometry("400x300")
        
        # Загадываем число и инициализируем счетчик попыток
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        
        # Создаем элементы интерфейса
        self.label = tk.Label(master, text="Я загадал число от 1 до 100. Попробуй угадать!")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)
        
        self.guess_button = tk.Button(master, text="Проверить", command=self.check_guess)
        self.guess_button.pack(pady=5)
        
        self.reset_button = tk.Button(master, text="Новая игра", command=self.reset_game)
        self.reset_button.pack(pady=5)
    
    def check_guess(self):
        """Проверяет введенное пользователем число"""
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            
            if guess < self.secret_number:
                messagebox.showinfo("Результат", "Слишком мало! Попробуй ещё раз.")
            elif guess > self.secret_number:
                messagebox.showinfo("Результат", "Слишком много! Попробуй ещё раз.")
            else:
                messagebox.showinfo("Победа!", f"Поздравляю! Ты угадал число {self.secret_number} за {self.attempts} попыток!")
                self.reset_game()
        
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, вводи только числа!")
            self.entry.delete(0, tk.END)
    
    def reset_game(self):
        """Начинает новую игру"""
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.label.config(text="Я загадал число от 1 до 100. Попробуй угадать!")

# Создаем и запускаем приложение
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()