
class Villa:

    def __init__(self,nom):
        self.nom = nom
    
    def nom(self):
        return self.nom

t = Villa("Toto")
print(t.nom)