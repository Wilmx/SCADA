
def psi_kilos_cm2(psi):  # Psi a kilos
    kilos_cm2 = psi / 14.22
    return kilos_cm2


def kilos_cm2_psi(kilos_cm2):  # Kilos a Psi
    psi = kilos_cm2 * 14.22
    return psi


def barriles_litros(barriles):  # Barriles a litros
    litros = barriles * 158.99
    return litros


def litros_barriles(litros):  # Litros a barriles
    barriles = litros / 158.99
    return barriles


def litros_m3(litros):  # Litros a M3
    m3 = litros / 1000
    return m3


def m3_litros(m3):  # M3 a litros
    litros = m3 * 1000
    return litros


def m3_barriles(m3):  # M3 a barriles
    barriles = m3 / 6.29
    return barriles


def barriles_m3(barriles): # Barriles a M3
    m3 = barriles * 6.29
    return m3
