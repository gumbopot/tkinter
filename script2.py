from tkinter import*

window = Tk()


def kg():
	grams = float(kg_value.get()) * 1000
	pounds = float(kg_value.get()) * 2.20462
	ounces = float(kg_value.get()) * 35.274
	grams_t.insert(END, grams)
	pounds_t.insert(END, pounds)
	ounces_t.insert(END, ounces)


kg_t = Label(window, text='Kg', height=1, width=5)
kg_t.grid(row=0, column=0)

kg_value = StringVar()
kg = Entry(window, width=15, textvariable=kg_value)
kg.grid(row=0, column=1)

grams_t = Text(window, height=1, width=20)
grams_t.grid(row=2, column=1)

pounds_t = Text(window, height=1, width=20)
pounds_t.grid(row=2, column=2)

ounces_t = Text(window, height=1, width=20)
ounces_t.grid(row=2, column=3)

b1 = Button(window, text='Convert', command=kg)
#b1.pack()# adds widget; can also use .grid(more control over placement)
b1.grid(row=0, column=2)

window.mainloop()
