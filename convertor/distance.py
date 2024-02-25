def convert_meters_to_feet(distance: str):
    m = int(distance.replace('m', ''))
    f = round(m / 0.3048)
    feet = str(f) + 'ft'
    return feet

def convert_feet_to_meters(distance: str):
    f = int(distance.replace('ft', ''))
    m = round(f * 0.3048)
    meters = str(m) + 'm'
    return meters