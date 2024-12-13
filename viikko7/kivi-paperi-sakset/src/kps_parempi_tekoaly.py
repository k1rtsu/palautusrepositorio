from tekoaly_parannettu import TekoalyParannettu
from kivipaperisakset import KiviPaperiSakset

class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)


    def _toisen_siirto(self, ensimmaisen_siirto = None):
        tokan_siirto = self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)

        return tokan_siirto
