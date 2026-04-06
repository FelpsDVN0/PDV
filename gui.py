import tkinter as tk
from tkinter import ttk, messagebox
from database import get_product

class POSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema PDV - Supermercado")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Lista de itens na compra atual
        self.cart = []
        self.total_value = 0.0
        
        self.setup_ui()
        self.barcode_entry.focus_set()
        
        # Bind da tecla Enter para processar o código de barras
        self.root.bind('<Return>', self.process_barcode)

    def setup_ui(self):
        # Cabeçalho
        header = tk.Frame(self.root, bg="#2c3e50", height=60)
        header.pack(fill="x")
        tk.Label(header, text="CAIXA LIVRE", font=("Arial", 24, "bold"), fg="white", bg="#2c3e50").pack(pady=10)
        
        # Área Central - Tabela de Itens
        self.tree_frame = tk.Frame(self.root, bg="white")
        self.tree_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        columns = ("Item", "Qtd", "Preço Unit.", "Subtotal")
        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show="headings")
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        
        self.tree.pack(fill="both", expand=True)
        
        # Rodapé - Entrada e Total
        footer = tk.Frame(self.root, bg="#ecf0f1", height=100)
        footer.pack(fill="x", side="bottom")
        
        # Campo de entrada de código de barras (invisível ou focado)
        tk.Label(footer, text="Código de Barras:", font=("Arial", 12), bg="#ecf0f1").pack(side="left", padx=10)
        self.barcode_entry = tk.Entry(footer, font=("Arial", 14), width=20)
        self.barcode_entry.pack(side="left", padx=10)
        
        # Botões de Ação
        btn_frame = tk.Frame(footer, bg="#ecf0f1")
        btn_frame.pack(side="left", padx=20)
        
        tk.Button(btn_frame, text="Nova Venda (F1)", command=self.new_sale, bg="#2ecc71", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Remover Item (Del)", command=self.remove_item, bg="#e74c3c", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        
        # Exibição do Total
        self.total_label = tk.Label(footer, text="TOTAL: R$ 0,00", font=("Arial", 28, "bold"), fg="#e74c3c", bg="#ecf0f1")
        self.total_label.pack(side="right", padx=20)
        
        # Binds de Teclado Adicionais
        self.root.bind('<F1>', lambda e: self.new_sale())
        self.root.bind('<Delete>', lambda e: self.remove_item())

    def process_barcode(self, event=None):
        barcode = self.barcode_entry.get().strip()
        if not barcode:
            return
        
        product = get_product(barcode)
        if product:
            name, price = product
            self.add_to_cart(name, price)
        else:
            messagebox.showwarning("Produto não encontrado", f"Código {barcode} não cadastrado.")
        
        self.barcode_entry.delete(0, tk.END)

    def add_to_cart(self, name, price):
        # Por simplicidade, adicionamos 1 unidade por vez
        subtotal = price * 1
        self.cart.append((name, 1, price, subtotal))
        self.tree.insert("", "end", values=(name, "1", f"R$ {price:.2f}", f"R$ {subtotal:.2f}"))
        
        self.total_value += subtotal
        self.total_label.config(text=f"TOTAL: R$ {self.total_value:.2f}")
        
        # Scroll para o último item
        self.tree.yview_moveto(1)

    def new_sale(self):
        """Limpa o carrinho para uma nova venda."""
        if messagebox.askyesno("Nova Venda", "Deseja iniciar uma nova venda?"):
            self.cart = []
            self.total_value = 0.0
            for item in self.tree.get_children():
                self.tree.delete(item)
            self.total_label.config(text="TOTAL: R$ 0,00")
            self.barcode_entry.delete(0, tk.END)
            self.barcode_entry.focus_set()

    def remove_item(self):
        """Remove o item selecionado da lista."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Remover Item", "Selecione um item na lista para remover.")
            return
        
        for item in selected_item:
            values = self.tree.item(item, "values")
            # Extrair o subtotal do texto "R$ XX.XX"
            subtotal = float(values[3].replace("R$ ", ""))
            self.total_value -= subtotal
            self.tree.delete(item)
        
        self.total_label.config(text=f"TOTAL: R$ {self.total_value:.2f}")
        self.barcode_entry.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = POSApp(root)
    root.mainloop()
