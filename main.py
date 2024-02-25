import csv
import convertor
import argparse

def main(filename: str, target_t: str, target_d: str):

    data = []
    with open(filename) as file:
        reader = csv.DictReader(file, delimiter=",")
        headers = next(reader)
        for col in reader:
            data.append(col)

    data_correct_temperature = data[:]
    for dic in data_correct_temperature:
        t = dic['Reading']
        if t[-1] != target_t:
            if target_t == "C":
                dic['Reading'] = convertor.temperature.convert_F_to_C(t)
            elif target_t == "F":
                dic['Reading'] = convertor.temperature.convert_C_to_F(t)
    # return data_correct_temperature

    data_correct_temp_dist = data_correct_temperature[:]
    for dic in data_correct_temp_dist:
        d = dic['Distance']
        if d[-1] != target_d[-1]:
            if target_d == "m":
                dic['Distance'] = convertor.distance.convert_feet_to_meters(d)
            elif target_d == "ft":
                dic['Distance'] = convertor.distance.convert_meters_to_feet(d)
    return data_correct_temp_dist

# new_data = main('database3.csv', 'C', 'm')

parser = argparse.ArgumentParser(description = "Return data with correct temperature")
parser.add_argument("filename", type = str, help = "Name of file with database (for example: database.csv)")
parser.add_argument("target_t", type = str, help = "Celsius or Fahrenheit (C/F)")
parser.add_argument("target_d", type = str, help = "Meters or feet (m/ft)")
args = parser.parse_args()

filename = args.filename
target_t = args.target_t
target_d = args.target_d

new_data = main(filename, target_t, target_d)

with open('database_correct.csv ', 'w+', newline='') as file:
    writer = csv.DictWriter(file, fieldnames = new_data[0])
    writer.writeheader()
    writer.writerows(new_data)
        
# python main.py database3.csv F ft
