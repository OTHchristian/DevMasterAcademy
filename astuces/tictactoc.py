from tkinter import Tk, Canvas

def drow_croix(canva):
    pass

def draw_cercle():
    pass

window = Tk()
window.title('TIC TAC TOC')
window.geometry('500x600')
canva = Canvas(window, width=500, height=600)
canva.create_line((250-135,300-135),(250+135,300-135),(250+135,300+135),(250-135,300+135),(250-135,300-135),fill='black', width=2)
canva.create_line((250-45,300-135),(250-45,300+135),fill='black', width=2)
canva.create_line((250+45,300-135),(250+45,300+135),fill='black', width=2)
canva.create_line((250-135,300-45),(250+135,300-45),fill='black', width=2)
canva.create_line((250-135,300+45),(250+135,300+45),fill='black', width=2)
canva.create_oval((250-20,390+20),(250+20,390-20),fill='blue',width=2)
canva.create_oval((250+90-20,390+20),(250+90+20,390-20),fill='blue',width=2)
canva.create_oval((250-90-20,390+20),(250+20-90,390-20),fill='blue',width=2)
canva.create_line((250+90,300+90),(250-90,300+90),fill='red',width=4)

canva.create_line((250-25,300-25),(250+25,300+25),fill='red',width=4)
canva.create_line((250+25,300-25),(250-25,300+25),fill='red',width=4)

canva.create_line((250-25+90,300-25-90),(250+25+90,300+25-90),fill='red',width=4)
canva.create_line((250+25+90,300-25-90),(250-25+90,300+25-90),fill='red',width=4)

canva.create_line((250-25-90,300-25-90),(250+25-90,300+25-90),fill='red',width=4)
canva.create_line((250+25-90,300-25-90),(250-25-90,300+25-90),fill='red',width=4)

canva.create_text((250,500),text='JOUEUR 2 WIN',fill='blue',font=10)
canva.pack()
window.mainloop()