from cx_Freeze import setup, Executable
base = None 

executables = [Executable("chercheur.py", base=base)]

packages = ["pandas"] 

options = {
    'build_exe': {    
        'packages':packages,
    },
}

setup(
    name = "Liseurcsv",
    options = options,
    version = "1.0",
    description = "Le programme affiche des valeurs d'un csv et le trie afin de pouvoir le lancer dans iramuteq",
    executables = executables
)