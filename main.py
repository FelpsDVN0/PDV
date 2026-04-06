import tkinter as tk
from database import init_db
from gui import POSApp

def main():
    # Inicializa o banco de dados
    init_db()
    
    # Cria a janela principal do Tkinter
    root = tk.Tk()
    
    # Configurações para Raspberry Pi Zero (opcionalmente tela cheia)
    # root.attributes('-fullscreen', True)
    # root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))
    
    # Inicializa a aplicação PDV
    app = POSApp(root)
    
    # Inicia o loop principal da interface gráfica
    root.mainloop()

if __name__ == "__main__":
    main()
