from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    testi1(mehua, olutta)
    testi2(olutta)
    testi3(mehua)
    testi4()
    testi5(olutta)
    testi6(mehua)
    testi7(olutta)
    testi8(mehua)

def testi1(mehua, olutta):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

def testi2(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def testi3(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def testi4():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def testi5(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

def testi6(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

def testi7(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

def testi8(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


if __name__ == "__main__":
    main()
