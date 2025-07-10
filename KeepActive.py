import pyautogui
import time
import sys
import threading
from datetime import datetime
import ctypes
from ctypes import wintypes

class KeepActiveCLI:
    def __init__(self, interval=60, distance=50):  # 1 minuto e 50 pixels
        self.running = False
        self.interval = interval  # segundos entre movimentos
        self.distance = distance  # pixels para mover

        # Configurações do pyautogui
        pyautogui.FAILSAFE = True  # Move o mouse para o canto superior esquerdo para parar
        pyautogui.PAUSE = 0.1

        # Configurar prevenção de suspensão no Windows
        self.setup_windows_prevention()

    def setup_windows_prevention(self):

        try:
            # Constantes do Windows para prevenção de suspensão
            self.ES_CONTINUOUS = 0x80000000
            self.ES_SYSTEM_REQUIRED = 0x00000001
            self.ES_DISPLAY_REQUIRED = 0x00000002

            # Impedir que o sistema durma
            ctypes.windll.kernel32.SetThreadExecutionState(
                self.ES_CONTINUOUS | self.ES_SYSTEM_REQUIRED | self.ES_DISPLAY_REQUIRED
            )
            print("✅ Prevenção de suspensão do Windows ativada")
        except Exception as e:
            print(f"⚠️  Aviso: Não foi possível ativar prevenção de suspensão: {e}")

    def restore_windows_settings(self):

        try:
            ctypes.windll.kernel32.SetThreadExecutionState(self.ES_CONTINUOUS)
            print("✅ Configurações de suspensão restauradas")
        except:
            pass

    def simulate_activity(self):
        try:
            # 1. Movimento do mouse (mais visível)
            current_x, current_y = pyautogui.position()
            pyautogui.moveRel(self.distance, 0, duration=0.2)
            time.sleep(0.1)
            pyautogui.moveRel(-self.distance, 0, duration=0.2)

            # 2. Pressionar e soltar tecla Scroll Lock (não interfere em nada)
            pyautogui.press('scrolllock')
            time.sleep(0.1)
            pyautogui.press('scrolllock')  # Volta ao estado original

            return True
        except Exception as e:
            print(f"⚠️  Erro ao simular atividade: {e}")
            return False

    def move_mouse(self):
        movement_count = 0

        print(f"Iniciando simulação de atividade a cada {self.interval} segundos...")
        print("Métodos: Movimento do mouse + Tecla Scroll Lock + Prevenção de suspensão")
        print("Para parar: pressione Ctrl+C ou mova o mouse para o canto superior esquerdo")
        print("-" * 70)

        while self.running:
            try:
                # Simular atividade do usuário (mouse + teclado)
                if self.simulate_activity():
                    movement_count += 1
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    print(f"[{timestamp}] Atividade #{movement_count} - Sistema mantido ativo")
                else:
                    print(f"[{timestamp}] ⚠️  Falha na simulação de atividade")

                # Aguardar o intervalo configurado
                for i in range(self.interval):
                    if not self.running:
                        break
                    time.sleep(1)

            except pyautogui.FailSafeException:
                # Mouse movido para o canto - parar por segurança
                print("\n⚠️  FailSafe ativado! Mouse movido para o canto superior esquerdo.")
                print("Aplicação parada por segurança.")
                self.stop()
                break
            except KeyboardInterrupt:
                print("\n⚠️  Interrompido pelo usuário (Ctrl+C)")
                self.stop()
                break
            except Exception as e:
                print(f"\n❌ Erro inesperado: {e}")
                self.stop()
                break

    def start(self):
        if self.running:
            print("❌ Aplicação já está rodando!")
            return

        print("🚀 Keep Active CLI - Mantenha seu notebook ativo!")
        print(f"⚙️  Configurações:")
        print(f"   • Intervalo: {self.interval} segundos")
        print(f"   • Distância: {self.distance} pixels")
        print()

        self.running = True
        try:
            self.move_mouse()
        except KeyboardInterrupt:
            print("\n⚠️  Aplicação interrompida pelo usuário")
        finally:
            self.stop()

    def stop(self):
        self.running = False
        self.restore_windows_settings()
        print("\n🛑 Aplicação parada. Notebook pode entrar em modo inativo novamente.")

def main():
    print("=" * 60)
    print("  KEEP ACTIVE CLI - Mantenha seu Status Ativo no Teams")
    print("=" * 60)

    # Configurações padrão otimizadas para Teams
    interval = 60  # 1 minuto - ideal para Teams
    distance = 50   # 50 pixels - movimento mais visível

    # Verificar argumentos de linha de comando
    if len(sys.argv) > 1:
        try:
            interval = int(sys.argv[1])
            if len(sys.argv) > 2:
                distance = int(sys.argv[2])
        except ValueError:
            print("❌ Erro: Argumentos devem ser números inteiros")
            print("Uso: python keep_active_cli.py [intervalo_segundos] [distancia_pixels]")
            print("Exemplo: python keep_active_cli.py 60 10")
            return

    print(f"📖 Como usar:")
    print(f"   • A aplicação vai mover o mouse {distance} pixels a cada {interval} segundos")
    print(f"   • Para parar: pressione Ctrl+C ou mova o mouse para o canto superior esquerdo")
    print(f"   • Para personalizar: python keep_active_cli.py [segundos] [pixels]")
    print()

    try:
        input("Pressione ENTER para iniciar ou Ctrl+C para cancelar...")
    except KeyboardInterrupt:
        print("\n❌ Operação cancelada pelo usuário")
        return

    app = KeepActiveCLI(interval, distance)
    app.start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Aplicação encerrada pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro ao executar aplicação: {e}")
