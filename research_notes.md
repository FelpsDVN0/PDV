# Pesquisa Técnica: PDV para Raspberry Pi Zero

## Hardware: Raspberry Pi Zero
- **Processador:** 1GHz single-core CPU.
- **RAM:** 512MB.
- **Limitações:** Recursos de CPU e RAM limitados. Interfaces gráficas pesadas (como PyQt6 ou Electron) podem ser lentas.
- **Recomendação:** Usar **Tkinter** para a GUI, pois é leve, nativo do Python e consome poucos recursos.

## Leitor de Código de Barras (Barcode Scanner)
- **Modo de Operação:** A maioria dos leitores USB funciona como um **dispositivo de entrada de teclado (HID)**.
- **Funcionamento:** Quando um código é lido, o leitor "digita" os números seguidos de uma tecla `Enter` (CR/LF).
- **Integração Python:** 
    - Capturar eventos de teclado na janela principal da GUI.
    - Alternativamente, usar a biblioteca `evdev` para ler diretamente do dispositivo `/dev/input/eventX` se o foco da janela for um problema.

## Banco de Dados
- **Opção:** **SQLite3**.
- **Vantagens:** Arquivo único, leve, sem necessidade de servidor separado, ideal para sistemas embarcados.

## Estrutura do Sistema
- **Linguagem:** Python 3.
- **GUI:** Tkinter.
- **DB:** SQLite.
- **Barcode:** Eventos de teclado (Tkinter `bind`).
