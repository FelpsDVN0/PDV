#!/bin/bash

# Script de Instalação do Sistema PDV para Raspberry Pi Zero

# Atualizar o sistema
echo "Atualizando o sistema..."
sudo apt update && sudo apt upgrade -y

# Instalar Python3 e pip (se não estiverem instalados)
echo "Verificando e instalando Python3 e pip..."
sudo apt install python3 python3-pip -y

# Instalar Tkinter (se não estiver instalado)
echo "Verificando e instalando Tkinter..."
sudo apt install python3-tk -y

# Criar diretório para o projeto
PROJECT_DIR="/home/ubuntu/pdv_system"
mkdir -p $PROJECT_DIR

# Copiar arquivos do projeto
echo "Copiando arquivos do projeto para $PROJECT_DIR..."
cp main.py $PROJECT_DIR/
cp gui.py $PROJECT_DIR/
cp database.py $PROJECT_DIR/
cp requirements.txt $PROJECT_DIR/

# Instalar dependências Python
echo "Instalando dependências Python..."
sudo pip3 install -r $PROJECT_DIR/requirements.txt

# Dar permissão de execução ao script principal
chmod +x $PROJECT_DIR/main.py

# Configurar inicialização automática (opcional - exemplo básico)
# Para inicializar automaticamente na inicialização do sistema, você pode adicionar uma linha ao crontab
# ou criar um serviço systemd. Este é um exemplo simples para crontab.
# echo "@reboot python3 $PROJECT_DIR/main.py &" | crontab -

echo "Instalação concluída!"
echo "Para iniciar o sistema, navegue até $PROJECT_DIR e execute: python3 main.py"
