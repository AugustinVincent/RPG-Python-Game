import tkinter

mainapp = tkinter.Tk()
mainapp.title = 'RPG GAME'

screen_x = int(mainapp.winfo_screenwidth())
screen_y = int(mainapp.winfo_screenheight())

window_x = 800
window_y = 600

posX = (screen_x // 2) - (window_x // 2)
posY = (screen_y // 2) - (window_y // 2)

geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
mainapp.geometry(geo)


mainapp.mainloop()
