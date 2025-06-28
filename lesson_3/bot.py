from tkinter import * # import from library all

root = Tk()
root.title('Bot on minimal')

entry = Entry(root, width=150)
entry.pack(pady = 200)

def respond():
    user_input = entry.get()
    if user_input.lower() == 'hi':
        answer = 'Hi and you friend'

    elif user_input.lower() == 'by':
        answer = 'By and you friend'

    else:
        answer = 'i dont know'
    
    lable.config(text=answer)



buton = Button(root, text='Ask me', command=respond)
buton.pack()

lable = Label(root, text ='', fg = 'red')
lable.pack()

lable.pack(pady=10)



root.mainloop()