import tkinter, random
from nltk.corpus import words

def skontroluj_vstup():
    global hladane_slovo
    global hladane_slovo_s_medzerami
    global hladane_slovo_zakodovane
    global pocet_zlych_vstupov
    vstup_nacitany_z_entry = vstup.get()
    if len(vstup_nacitany_z_entry) == 1 and vstup_nacitany_z_entry.isalpha()==True and pocet_zlych_vstupov < 10:
        nespravne_pismena = 0

        for i in range(0,len(hladane_slovo)):
            if hladane_slovo[i].lower() == vstup_nacitany_z_entry.lower():
                hladane_slovo_zakodovane = hladane_slovo_zakodovane[0:2*i+1] + vstup_nacitany_z_entry.upper() + hladane_slovo_zakodovane[2*i+2:]
                platno.itemconfigure(zobrazene, text=hladane_slovo_zakodovane)
            else:
                nespravne_pismena += 1

        if nespravne_pismena == len(hladane_slovo):
            kresli_obesenca()

        if hladane_slovo_s_medzerami.upper() == hladane_slovo_zakodovane:
            platno.create_image(vzdialenost + 3/4*a, vzdialenost + 5/16*a, image=emotikony_zivy)
    vstup.set('')

def kliknutie_na_label_obrazok(event):
    okno.quit()

def kresli_obesenca():
    global pocet_zlych_vstupov
    global hladane_slovo_s_medzerami
    pocet_zlych_vstupov += 1
    if pocet_zlych_vstupov == 1:
        platno.create_line(vzdialenost, vzdialenost + a, vzdialenost + a/2, vzdialenost + a, width=5, fill=prva_farba) #zaklad
    elif pocet_zlych_vstupov == 2:
        platno.create_line(vzdialenost + a/4, vzdialenost + a, vzdialenost + a/4, vzdialenost, width=5, fill=prva_farba) #stlp
    elif pocet_zlych_vstupov == 3:
        platno.create_line(vzdialenost + a/4, vzdialenost, vzdialenost + 3/4*a, vzdialenost, width=5, fill=prva_farba) #rameno
    elif pocet_zlych_vstupov == 4:
        platno.create_line(vzdialenost + 3/4*a, vzdialenost, vzdialenost + 3/4*a, vzdialenost + a/4, width=5, fill=prva_farba) #slucka
    elif pocet_zlych_vstupov == 5:
        platno.create_oval(vzdialenost + 11/16*a, vzdialenost + a/4, vzdialenost + 13/16*a, vzdialenost + 3/8*a, width=5, outline=prva_farba) #hlava
    elif pocet_zlych_vstupov == 6:
        platno.create_line(vzdialenost + 3/4*a, vzdialenost + 3/8*a, vzdialenost + 3/4*a, vzdialenost + 5/8*a, width=5, fill=prva_farba) #telo
    elif pocet_zlych_vstupov == 7:
        platno.create_line(vzdialenost + 3/4*a, vzdialenost + 7/16*a, vzdialenost + 7/8*a, vzdialenost + 11/16*a, width=5, fill=prva_farba) #prava ruka
    elif pocet_zlych_vstupov == 8:
        platno.create_line(vzdialenost + 3/4*a, vzdialenost + 7/16*a, vzdialenost + 5/8*a, vzdialenost + 11/16*a, width=5, fill=prva_farba) #lava ruka
    elif pocet_zlych_vstupov == 9:
        platno.create_line(vzdialenost + 3/4*a, vzdialenost + 5/8*a, vzdialenost + 7/8*a, vzdialenost + 7/8*a, width=5, fill=prva_farba) #prava noha
    else:
        platno.create_line(vzdialenost + 3/4*a, vzdialenost + 5/8*a, vzdialenost + 5/8*a, vzdialenost + 7/8*a, width=5, fill=prva_farba) #lava noha
        platno.create_image(vzdialenost + 3/4*a, vzdialenost + 5/16*a, image=emotikony_mrtvy)
        platno.itemconfigure(zobrazene, text=hladane_slovo_s_medzerami.upper())


okno = tkinter.Tk()
okno.title('Hra Obesenec')
okno['bg'] = 'white'
#okno.iconbitmap('Ikonka.ico')
okno.overrideredirect(1)

a = 300
vzdialenost = 50
sirka = 2.5*vzdialenost + 7/8*a
vyska = 3*vzdialenost + a
slova = words.words()
prva_farba = 'royal blue'
druha_farba = 'ivory2'

hladane_slovo = random.choice(slova)
hladane_slovo_zakodovane = ''
hladane_slovo_s_medzerami = ''
for i in hladane_slovo:
    hladane_slovo_zakodovane += ' _'
    hladane_slovo_s_medzerami += ' ' + i


pocet_zlych_vstupov = 0

platno = tkinter.Canvas(bg='white', highlightbackground=prva_farba, width=sirka, height=vyska)
platno.grid(row=1, column=0, columnspan=2)

platno.create_line(vzdialenost, vzdialenost + a, vzdialenost + a/2, vzdialenost + a, width=5, fill=druha_farba) #zaklad
platno.create_line(vzdialenost + a/4, vzdialenost + a, vzdialenost + a/4, vzdialenost, width=5, fill=druha_farba) #stlp
platno.create_line(vzdialenost + a/4, vzdialenost, vzdialenost + 3/4*a, vzdialenost, width=5, fill=druha_farba) #rameno
platno.create_line(vzdialenost + 3/4*a, vzdialenost, vzdialenost + 3/4*a, vzdialenost + a/4, width=5, fill=druha_farba) #slucka
platno.create_oval(vzdialenost + 11/16*a, vzdialenost + a/4, vzdialenost + 13/16*a, vzdialenost + 3/8*a, width=5, outline=druha_farba) #hlava
platno.create_line(vzdialenost + 3/4*a, vzdialenost + 3/8*a, vzdialenost + 3/4*a, vzdialenost + 5/8*a, width=5, fill=druha_farba) #telo
platno.create_line(vzdialenost + 3/4*a, vzdialenost + 7/16*a, vzdialenost + 7/8*a, vzdialenost + 11/16*a, width=5, fill=druha_farba) #prava ruka
platno.create_line(vzdialenost + 3/4*a, vzdialenost + 7/16*a, vzdialenost + 5/8*a, vzdialenost + 11/16*a, width=5, fill=druha_farba) #lava ruka
platno.create_line(vzdialenost + 3/4*a, vzdialenost + 5/8*a, vzdialenost + 7/8*a, vzdialenost + 7/8*a, width=5, fill=druha_farba) #prava noha
platno.create_line(vzdialenost + 3/4*a, vzdialenost + 5/8*a, vzdialenost + 5/8*a, vzdialenost + 7/8*a, width=5, fill=druha_farba) #lava noha

zobrazene = platno.create_text(sirka/2, 2*vzdialenost + a, text=hladane_slovo_zakodovane, fill=prva_farba, font='arial 20 bold')

vstup = tkinter.StringVar()
tkinter.Entry(textvariable=vstup, bg=prva_farba, fg='white', font='arial 10 bold').grid(row=2, column=0, sticky='eswn')

tlacidlo = tkinter.Button(text='Hádaj písmeno!', command=skontroluj_vstup, bg=prva_farba, fg='white', font='arial 10 bold').grid(row=2, column=1, sticky='eswn')

emotikony_mrtvy = tkinter.PhotoImage(file='emotikony_mrtvy_upravene.png')
emotikony_zivy = tkinter.PhotoImage(file='emotikony_zivy_upravene.png')


koniec = tkinter.PhotoImage(file='escape3.png')

# label s obrazkom na zatvorenie okna
label_obrazok = tkinter.Label(okno, image=koniec, bd=0)
label_obrazok.grid(row=0, column=1, sticky='e')
label_obrazok.bind('<Button-1>', kliknutie_na_label_obrazok)
label_obrazok.bind('<Button-3>', kliknutie_na_label_obrazok)

tkinter.mainloop()
