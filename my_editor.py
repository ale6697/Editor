#Import delle librerie necessarie
import tkinter as tk 
from tkinter import ttk,filedialog
from tkinter import messagebox

#Classe per il widget menu file
class Menu:
    def __init__(self,parent,menubar):

        #Set tendina per menu file
        file_dropdown = tk.Menu(menubar, tearoff=0)

        #Aggiunta comandi menu file
        file_dropdown.add_command(label="new",accelerator="Ctrl+n", command=parent.new_file)
        file_dropdown.add_command(label="open",accelerator="Ctrl+o",command=parent.open_file)
        file_dropdown.add_command(label="save",accelerator="Ctrl+s",command=parent.save_file)
        file_dropdown.add_command(label="save as",accelerator="Ctrl+Shift+s",command=parent.save_as_file)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Esc",accelerator="Ctrl+e", command=parent.master.destroy)
        
        #Set tendina per menu about
        about_dropdown = tk.Menu(menubar, tearoff=0)

        #Aggiunta comandi menu about
        about_dropdown.add_command(label="About",command=self.show_about_message)
        about_dropdown.add_command(label="Release note",command=self.show_about_release)

        #Aggiunta cascata per menu file e about
        menubar.add_cascade(label="file",menu=file_dropdown)
        menubar.add_cascade(label="About",menu=about_dropdown)


    def show_about_message(self):
        box_message = "Text editor coded in python with Tkinter"
        box_title = "About Pytext"
        messagebox.showinfo(box_title,box_message)

    def show_about_release(self):
        box_message = "Version v1.0"
        box_title = "Release note"
        messagebox.showinfo(box_title,box_message)


        




#Classe per ottenere lo status del sistema
class Statusbar:

    def __init__(self,parent):
        
        #Definizione dello status tramite il widget StringVar
        self.status =tk.StringVar()

        #Inizializzazione dello status
        self.status.set("Status bar")

        #Definizione etichetta con padre , testo , colore scritta , colore sfondo , ancoraggio a sudovest- in basso a sx
        label = tk.Label(parent.text,textvariable=self.status,fg="black",bg="White",anchor="sw")

        #Posizionamento dell'etichetta con il metodo pack , situato in basso con side= e espanso con fill
        label.pack(side=tk.BOTTOM,fill=tk.BOTH)

    #Definizione del metodo per aggiornare lo status da usare come callback
    #per l'evento key del widget text
    def update_status(self,*args):

        #Se il file è stato salvato args[0] è un booleano 
        if isinstance(args[0],bool):
            self.status.set("File saved")
        else:
            self.status.set("Pytext")


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

        #Set statusbar
        self.statusbar = Statusbar(self)    

        #Set shortcuts
        self.shortcuts()

        #Configurazione dei vari menu
        self.menu = Menu(self,menubar)


    # Funzione per settare il nome del file nell'intestazione dell'editor
    def set_window_title(self, name=None):
        if name:
            self.master.title(name)
        else:
            self.master.title("Untitled")

    #Funzione per creare un file ex novo
    def new_file(self,*args):
        self.text.delete(1.0,tk.END)
        self.filename = None
        self.set_window_title()

    #Funzione per aprire un file esistente
    def open_file(self,*args):
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
    def save_file(self,*args):
        if self.filename:
            try:
                content = self.text.get(1.0,tk.END)
                with open(self.filename,"w") as f:
                    f.write(content)
                    self.statusbar.update_status(True)
            except Exception as e:
                print(e)
        else:
            self.save_as_file()
    
    #Funzione per salvare un file selezionando l'estensione
    def save_as_file(self,*args):
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
                self.statusbar.update_status(True)
        except Exception as e:
            print(e)

    #Funzione per definizione shortcuts
    def shortcuts(self):
        self.text.bind('<Control-n>',self.new_file)
        self.text.bind('<Control-o>',self.open_file)
        self.text.bind('<Control-s>',self.save_file)
        self.text.bind('<Control-Shift-s>',self.save_as_file)
        self.text.bind('<Key>',self.statusbar.update_status)


#Inizializzazione di master come la finestra principale
master = tk.Tk()

#Creazione dell'istanza Pytext chiamata pt..
#Passando l'attributo master alla classe si permette a pytext di interagire con la finestra principale master
pt = pyText(master)

#Mainloop per tenere l'editor aperto
master.mainloop()