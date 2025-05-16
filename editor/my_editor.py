#Import delle librerie necessarie
import tkinter as tk 
from tkinter import ttk,filedialog


#Classe per il widget menu file
class Menufile:

    def __init__(self,parent,menubar):

        #Set tendina per sottomenu
        file_dropdown = tk.Menu(menubar, tearoff=0)

        #Aggiunta comandi menu file
        file_dropdown.add_command(label="new", command=parent.new_file)
        file_dropdown.add_command(label="open",command=parent.open_file)
        file_dropdown.add_command(label="save",command=parent.save_file)
        file_dropdown.add_command(label="save as",command=parent.save_as_file)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Esc", command=parent.master.destroy)
        
        #Aggiunta cascata per menu file
        menubar.add_cascade(label="file",menu=file_dropdown)
        



    
#Classe per il widget menu view
class Menuview:

    def __init__(self,parent,menubar):

        #set tendina menu view
        view_dropdown = tk.Menu(menubar,tearoff=0)

        #Aggiunta comandi menu view
        view_dropdown.add_command(label="View as")
        view_dropdown.add_separator()
        view_dropdown.add_command(label="Esc",command=parent.master.destroy)

        #Aggiunta cascata per menu view
        menubar.add_cascade(label="View",menu=view_dropdown)






class Menusearch:

    def __init__(self,parent,menubar):

        #Set tendina menu search
        serach_dropdown = tk.Menu(menubar,tearoff=0)
       
        #Aggiunta comandi menu search
        serach_dropdown.add_command(label="Search")
        serach_dropdown.add_command(label="Substitute")
        serach_dropdown.add_separator()
        serach_dropdown.add_command(label="Esc",command=parent.master.destroy)

        #Aggiunta cascata per menu search
        menubar.add_cascade(label="Search",menu=serach_dropdown)        







class pyText:

    #Definizione del dunder init della classe pytext
    def __init__(self, master):

        #Inizializzazione testo e geometria della finestra di master come la finestra principale
        master.title("Pytext")
        master.geometry("1200x700")
        
        #Inizializzazione di self.master
        self.master = master

        #Inizializzazione variabile filename 
        self.filename = None

        #Inizializzazione de widget text e scrollbar
        self.text = tk.Text(master)  
        self.scrollbar = tk.Scrollbar(master, command=self.text.yview)
        
        #Uso .pack per mostrarli a schermo
        self.text.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #Configurazione per permettere lo scrolling del file di testo
        self.text.configure(yscrollcommand=self.scrollbar.set)

        #Creazione barre menu     
        menubar = tk.Menu(master)
        master.config(menu=menubar)

        #Configurazione dei vari menu
        self.menu = Menufile(self, menubar)
        self.menu2 = Menuview(self,menubar)
        self.menu3 = Menusearch(self,menubar)

    # Funzione per settare il nome del file nell'intestazione dell'editor
    def set_window_title(self, name=None):
        if name:
            self.master.title(name)
        else:
            self.master.title("Untitled")

    #Funzione per creare un file ex novo
    def new_file(self):
        self.text.delete(1.0,tk.END)
        self.filename = None
        self.set_window_title()

    #Funzione per aprire un file esistente
    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),
                                                                                      ("Text files","*.txt"),
                                                                                      ("Python scripts","*.py"),
                                                                                      ("Markdown Text","*.md")])
        if self.filename:
            self.text.delete(1.0,tk.END)
            with open(self.filename,"r") as f:
                self.text.insert(1.0,f.read())
                self.set_window_title(self.filename)
    #Funzione per salvare un file 
    def save_file(self):
        if self.filename:
            try:
                content = self.text.get(1.0,tk.END)
                with open(self.filename,"w") as f:
                    f.write(content)
            except Exception as e:
                print(e)
        else:
            self.save_as_file()
    
    #Funzione per salvare un file selezionando l'estensione
    def save_as_file(self):
        try:
            new_file = filedialog.asksaveasfilename(initialfile="Untitled.txt",defaultextension="*.txt",filetypes=[("All files type","*.*"),
                                                                                                                   ("Text files","*.txt"),
                                                                                                                   ("Python scripts","*.py"),
                                                                                                                   ("Markdown test","*.md")])
            content = self.text.get(1.0,tk.END)
            with open(new_file,"w") as f:
                f.write(content)
                self.filename = new_file
                self.set_window_title(new_file)
        except Exception as e:
            print(e)








#Inizializzazione di master come la finestra principale
master = tk.Tk()

#Creazione dell'istanza Pytext chiamata pt..
#Passando l'attributo master alla classe si permette a pytext di interagire con la finestra principale master
pt = pyText(master)

#Mainloop per tenere l'editor aperto
master.mainloop()