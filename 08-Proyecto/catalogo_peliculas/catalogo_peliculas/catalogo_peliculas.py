import tkinter as tk
from client.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title('Catalogo de Peliculas')
    root.iconbitmap('img/logo.ico')
    root.resizable(0,0)
    
    #Crear un frame
    # frame = tk.Frame(root)
    # frame.pack()
    # frame.config(width=480, height=320, bg='blue')
  
  
    barra_menu(root)

    #usando herencia
    app = Frame(root = root)
    
    root.mainloop()

if __name__ == '__main__':
    main()
