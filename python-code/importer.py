import csv
import math
from datetime import datetime

from db import InfluxDBUploader

uploader = InfluxDBUploader()
points = []

with open('/data/body_data.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        PIT = float(row[0])
        PIB = float(row[1])
        PISE = float(row[2])
        PICI = float(row[3])
        Weight = float(row[4])
        Height = float(row[5])
        Date = datetime(int(row[6]), int(row[7]), 1, 0, 0, 0, 0)
        BMI = Weight / (Height ** 2)
        Body_Dentsity = 1.1765 - 0.0744 * math.log10(PIT + PIB + PISE + PICI)
        Fat_Percentage = ((495 / Body_Dentsity) - 450)
        Fat_kg = (Weight / 100) * Fat_Percentage
        Muscle_kg = Weight - Fat_kg
        Muscle_Percentage = 100 - Fat_Percentage
        points.append(uploader.create_point('PIT', Date, {'value': row[0]}, None))
        points.append(uploader.create_point('PIB', Date, {'value': row[1]}, None))
        points.append(uploader.create_point('PISE', Date, {'value': row[2]}, None))
        points.append(uploader.create_point('PICI', Date, {'value': row[3]}, None))
        points.append(uploader.create_point('Weight', Date, {'value': row[4]}, None))
        points.append(uploader.create_point('Height', Date, {'value': row[5]}, None))
        points.append(uploader.create_point('BMI', Date, {'value': BMI}, None))
        points.append(uploader.create_point('Body_Dentsity', Date, {'value': Body_Dentsity}, None))
        points.append(uploader.create_point('Fat_Percentage', Date, {'value': Fat_Percentage}, None))
        points.append(uploader.create_point('Fat_kg', Date, {'value': Fat_kg}, None))
        points.append(uploader.create_point('Muscle_Percentage', Date, {'value': Muscle_Percentage}, None))
        points.append(uploader.create_point('Muscle_kg', Date, {'value': Muscle_kg}, None))

uploader.upload(points)
