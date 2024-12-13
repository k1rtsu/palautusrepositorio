from tekoaly import Tekoaly
from kivipaperisakset import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmainen_siirto = None):
        tokan_siirto = self.tekoaly.anna_siirto()

        return tokan_siirto
