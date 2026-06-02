from colorama import init, Fore, Style

init()

print(Fore.CYAN + """
╔══════════════════════════════════════╗
║      SISTEM INFORMASI MAHASISWA      ║
╚══════════════════════════════════════╝
""" + Style.RESET_ALL)

print(Fore.GREEN + "[1] Tambah Data")
print(Fore.YELLOW + "[2] Lihat Data")
print(Fore.BLUE + "[3] Cari Data")
print(Fore.RED + "[4] Keluar")