def psi_kilos__cm2(psi):
    kilos_cm2 = psi / 14.22
    return kilos_cm2


def kilos_cm2__psi(kilos_cm2):
    psi = kilos_cm2 * 14.22
    return psi


def barriles__litros(barriles):
    litros = barriles * 158.99
    return litros


def litros__barriles(litros):
    barriles = litros / 158.99
    return barriles


def litros__m3(litros):
    m3 = litros / 1000
    return m3


def m3__litros(m3):
    litros = m3 * 1000
    return litros


def m3__barriles(m3):
    barriles = m3 / 6.29
    return barriles


def barriles__m3(barriles):
    m3 = barriles * 6.29
    return m3
