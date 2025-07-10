# KeepActive

Uma aplicação para manter seu computador ativo automaticamente.

## Uso Rápido

Para usar imediatamente sem instalar Python:

1. Baixe o projeto do GitHub
2. Acesse a pasta `dist/`
3. Execute `KeepActive.exe`

## Funcionalidades

- Movimenta o mouse automaticamente em intervalos regulares
- Simula pressionamento de teclas (Scroll Lock)
- Previne que o Windows entre em modo de suspensão
- Interface de linha de comando simples e intuitiva
- Failsafe integrado para parar a aplicação rapidamente

## Requisitos

### Para usar o executável (recomendado)
- Nenhum requisito adicional
- Baixe o projeto e execute `dist/KeepActive.exe`

### Para executar o código Python
- Python 3.6+
- pyautogui

## Instalação

### Opção 1: Executável (mais simples)
```bash
# Baixe o projeto do GitHub
# Navegue até a pasta dist/
# Execute KeepActive.exe
```

### Opção 2: Python
```bash
pip install pyautogui
```

## Como usar

### Usando o executável
```bash
# Na pasta dist/
KeepActive.exe
```

### Executando o código Python
```bash
python KeepActive.py
```

### Personalizando configurações

```bash
python KeepActive.py [intervalo_segundos] [distancia_pixels]
```

Exemplo:
```bash
python KeepActive.py 60 50
```

### Executável (alternativa ao Python)

Para quem prefere não instalar Python, é possível criar um executável:

Execute o arquivo `criar_executavel.bat` ou use:

```bash
pip install pyinstaller
pyinstaller --onefile --name=KeepActive KeepActive.py
```

O executável será criado em `dist/KeepActive.exe` e pode ser usado sem ter Python instalado.

## Configurações Padrão

- Intervalo: 60 segundos
- Distância: 50 pixels
- Prevenção de suspensão: Ativa

## Como parar

- Ctrl+C no terminal
- Mover o mouse para o canto superior esquerdo (failsafe)
