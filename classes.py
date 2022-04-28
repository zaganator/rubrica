class Contact:
    def __init__(self, nome, cognome, telefono):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono

    def display(self):
        print(f"nome: {self.nome}\ncognome: {self.cognome}\ntelefono: {self.telefono}")

    def obj_to_csv(self):
        stringa = f"{self.nome},{self.cognome},{self.telefono}\n"
        return stringa

