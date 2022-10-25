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
            print("insert your information here")
        if specifications == 2:
            print("insert your information here")
    if settings == 2:
        if name == 0:
            print("Username: (the main user)")
            print("Password: (the main user's password)")
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
