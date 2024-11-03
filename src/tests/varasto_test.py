import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktorin_arvot_oikein(self):
        self.varasto2 = Varasto(10, 2)
        self.varasto3 = Varasto(10, -2)
        self.varasto4 = Varasto(-4)
        self.varasto5 = Varasto(2, 3)

        self.assertAlmostEqual(self.varasto2.saldo, 2)
        self.assertAlmostEqual(self.varasto3.saldo, 0)
        self.assertAlmostEqual(self.varasto4.tilavuus, 0)
        self.assertAlmostEqual(self.varasto5.saldo, 2)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_varastoon_lisataan_liikaa(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_varastosta_otetaan_liikaa(self):
        self.varasto.lisaa_varastoon(5)

        self.varasto.ota_varastosta(6)

        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_negatiivinen_maara_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-7)

        self.assertAlmostEqual(self.varasto.saldo, 0)

        self.varasto.lisaa_varastoon(2)

        self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(self.varasto.saldo, 2)

    def test_varaston_tekstiesitys_oikein(self):
        self.varasto.lisaa_varastoon(5)

        self.assertAlmostEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")
