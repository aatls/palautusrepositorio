class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception(f"Annettu kapasiteetti '{kapasiteetti}' ei ole positiivinen kokonaisluku")
        
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception(f"Annettu kasvatuskoko '{kasvatuskoko}' ei ole positiivinen kokonaisluku")
        
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lista = self._luo_lista(self.kapasiteetti)
        self.koko = 0

    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def kuuluu(self, n):
        return self.etsi(n) != -1
    
    def etsi(self, n):
        for i in range(self.koko):
            if self.lista[i] == n:
                return i
        return -1
        
    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        
        if self.koko == self.kapasiteetti:
            self.kasvata_kapasiteettia()

        self.lista[self.koko] = n
        self.koko += 1
        return True

    def kasvata_kapasiteettia(self):
        self.kapasiteetti += self.kasvatuskoko
        uusi_lista = self._luo_lista(self.kapasiteetti)
        self.kopioi_lista(self.lista, uusi_lista)
        self.lista = uusi_lista

    def poista(self, n):
        index = self.etsi(n)
        if index == -1:
            return

        for i in range(index, self.koko - 1):
            self.lista[i] = self.lista[i + 1]

        self.koko -= 1
        self.lista[self.koko] = 0

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.koko

    def to_int_list(self):
        taulu = self._luo_lista(self.koko)

        for i in range(0, len(taulu)):
            taulu[i] = self.lista[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        sisalto = ""

        for i in range(self.koko):
            sisalto += f"{self.lista[i]}"
            if i != self.koko - 1:
                sisalto += ", "
        
        return "{" + sisalto + "}"
