import sqlite3

def init_db():
    """Inicializa o banco de dados e cria a tabela de produtos se não existir."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            barcode TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Adicionar alguns produtos de exemplo se a tabela estiver vazia
    cursor.execute('SELECT COUNT(*) FROM products')
    if cursor.fetchone()[0] == 0:
        sample_products = [
            ('7891000100103', 'Arroz 5kg', 25.50),
            ('7891000100202', 'Feijão 1kg', 8.90),
            ('7891000100301', 'Óleo de Soja', 6.75),
            ('7891000100400', 'Açúcar 1kg', 4.20),
            ('7891000100509', 'Leite Integral 1L', 5.30)
        ]
        cursor.executemany('INSERT INTO products VALUES (?, ?, ?)', sample_products)
    
    conn.commit()
    conn.close()

def get_product(barcode):
    """Busca um produto pelo código de barras."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, price FROM products WHERE barcode = ?', (barcode,))
    product = cursor.fetchone()
    conn.close()
    return product

def add_product(barcode, name, price):
    """Adiciona um novo produto ao banco de dados."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO products (barcode, name, price) VALUES (?, ?, ?)', (barcode, name, price))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def list_all_products():
    """Retorna todos os produtos cadastrados."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

if __name__ == "__main__":
    init_db()
    print("Banco de dados inicializado com sucesso.")
