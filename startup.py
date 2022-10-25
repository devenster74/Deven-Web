import os

print("""
██████╗░███████╗██╗░░░██╗███████╗███╗░░██╗  ░█████╗░░██████╗
██╔══██╗██╔════╝██║░░░██║██╔════╝████╗░██║  ██╔══██╗██╔════╝
██║░░██║█████╗░░╚██╗░██╔╝█████╗░░██╔██╗██║  ██║░░██║╚█████╗░
██║░░██║██╔══╝░░░╚████╔╝░██╔══╝░░██║╚████║  ██║░░██║░╚═══██╗
██████╔╝███████╗░░╚██╔╝░░███████╗██║░╚███║  ╚█████╔╝██████╔╝
╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝  ░╚════╝░╚═════╝░""")
print("""
[1] Use previous login
[2] Login with a new user""")
setup = int(input("[?]: "))
if setup == 1:
    print("Welcome back, Deven.")
    name = 0
if setup == 2:
    name = input(str("Username: "))
    password = input(str("Password: "))
    print("Welcome,", name)
print("Booting up Deven OS.")

print("""
██████╗░███████╗██╗░░░██╗███████╗███╗░░██╗  ░█████╗░░██████╗
██╔══██╗██╔════╝██║░░░██║██╔════╝████╗░██║  ██╔══██╗██╔════╝
██║░░██║█████╗░░╚██╗░██╔╝█████╗░░██╔██╗██║  ██║░░██║╚█████╗░
██║░░██║██╔══╝░░░╚████╔╝░██╔══╝░░██║╚████║  ██║░░██║░╚═══██╗
██████╔╝███████╗░░╚██╔╝░░███████╗██║░╚███║  ╚█████╔╝██████╔╝
╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝  ░╚════╝░╚═════╝░""")
print("""
[1] Open Deven Web
[2] Open Settings
[3] Shut down""")
setup2 = int(input("[?]: "))
if setup2 == 1:
    os.startfile("browser.py")
if setup2 == 2:
    print("""
    [1] About this PC
    [2] User""")
    settings = int(input("[?]: "))
    if settings == 1:
        print("""
        [1] Device specifications
        [2] OS specifications""")
        specifications = int(input("[?]: "))
        if specifications == 1:
            print("""           Device name	dev-computer
            Processor	Intel(R) Core(TM) i5-1035G1 CPU @ 1.00GHz   1.19 GHz
            Installed RAM	8.00 GB (7.79 GB usable)
            Device ID	16E68EAC-7ACE-4FAC-ADF9-42CD57F4E282
            Product ID	00356-02306-43792-AAOEM
            System type	64-bit operating system, x64-based processor
            Pen and touch	No pen or touch input is available for this display""")
        if specifications == 2:
            print("""           Edition	Windows 11 Home
            Version	21H2
            Installed on 21/10/2021
            OS build	22000.1098
            Experience	Windows Feature Experience Pack 1000.22000.1098.0""")
    if settings == 2:
        if name == 0:
            print("Username: Deven")
            print("Password: greenlamb07")
        else:
            print("Username:", name)
            print("Password:", password)
if setup2 == 3:
    print("Logging out")
    print("""
    ██████╗░███████╗██╗░░░██╗███████╗███╗░░██╗  ░█████╗░░██████╗
    ██╔══██╗██╔════╝██║░░░██║██╔════╝████╗░██║  ██╔══██╗██╔════╝
    ██║░░██║█████╗░░╚██╗░██╔╝█████╗░░██╔██╗██║  ██║░░██║╚█████╗░
    ██║░░██║██╔══╝░░░╚████╔╝░██╔══╝░░██║╚████║  ██║░░██║░╚═══██╗
    ██████╔╝███████╗░░╚██╔╝░░███████╗██║░╚███║  ╚█████╔╝██████╔╝
    ╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝  ░╚════╝░╚═════╝░""")
    print("Alt + F4 to close the system.")