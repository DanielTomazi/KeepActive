"""
Script para criar executável do KeepActive usando PyInstaller
"""
import os
import subprocess
import sys

def build_executable():
    print("🔨 Criando executável do KeepActive...")

    # Comando do PyInstaller
    cmd = [
        "pyinstaller",
        "--onefile",  # Um único arquivo executável
        "--windowed",  # Sem console (opcional)
        "--name=KeepActive",  # Nome do executável
        "--icon=NONE",  # Sem ícone por enquanto
        "--distpath=dist",  # Pasta de saída
        "--workpath=build",  # Pasta de trabalho
        "--specpath=.",  # Pasta do arquivo spec
        "KeepActive.py"
    ]

    try:
        # Executar PyInstaller
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ Executável criado com sucesso!")
        print(f"📁 Localização: {os.path.abspath('dist/KeepActive.exe')}")
        print("\n📋 Como usar o executável:")
        print("   • Execute KeepActive.exe diretamente")
        print("   • Ou use pelo terminal: KeepActive.exe [intervalo] [distancia]")
        print("   • Exemplo: KeepActive.exe 60 50")

    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao criar executável: {e}")
        print("Saída do erro:", e.stderr)
        return False
    except FileNotFoundError:
        print("❌ PyInstaller não encontrado!")
        print("Instale com: pip install pyinstaller")
        return False

    return True

if __name__ == "__main__":
    build_executable()
