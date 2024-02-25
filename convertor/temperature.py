def convert_C_to_F(t: str):
    c = int(t.replace('°C', ''))
    f = round(c * 9 / 5 + 32)
    F = str(f) + '°F'
    return F

def convert_F_to_C(t: str):
    f = int(t.replace('°F', ''))
    c = round(5 / 9 * (f - 32))
    C = str(c) + '°C'
    return C