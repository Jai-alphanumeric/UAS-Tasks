# UAS Task 1
# Jai A17/01
import math

file_1 = open(r'File_1.txt', 'r')
file_2 = open(r'File_2.txt', 'r')

velocity_x, velocity_y, height = 0, 0, 0    # Defining the velocity and height variables


def distance(f1, f2):
    a11 = f1.read()  # Reading data from both files
    a21 = f2.read()
    a12 = a11.split(',')  # Converting it into a list
    a22 = a21.split(',')

    lat_p = float(a12[0])  # Extracting data from the list
    lat_target = float(a22[0])  # and storing it into the co-ordinate variables
    lon_p = float(a12[1])
    lon_target = float(a22[1])
    global velocity_x, velocity_y, height     # Making them global variable
    velocity_x = float(a12[2])  # in m/s
    velocity_y = float(a12[3])  # in m/s
    height = float(a12[4])  # in meters

    earth_radius = 6371e3  # metres
    d1 = lat_p * math.pi / 180  # d1, d2 in radians
    d2 = lat_target * math.pi / 180
    d = (lat_target - lat_p) * math.pi / 180
    e = (lon_target - lon_p) * math.pi / 180
    # Now using Haversine Formula to find the distance between 2 points on earth
    a = math.sin(d / 2) * math.sin(d / 2) + math.cos(d1) * math.cos(d2) * math.sin(e / 2) * math.sin(e / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    d = earth_radius * c  # in metres
    return d


dis_between = distance(file_1, file_2)  # calling the distance function for the required files

g = 9.8  # acceleration due to gravity
velocity = math.sqrt(velocity_x**2 + velocity_y**2)
wind_speed = 2  # in m/s
r = velocity * (math.sqrt(height * 2 / g))
# r1 = velocity * velocity / g  # The formula for angular projectile

if r == dis_between:
    print("The UAV dropped the weight at the right position")
elif (r > (dis_between - 150)) and (r < (dis_between + 150)):
    print("The UAV dropped the package near the drop package i.e. %s meters" % (r - dis_between))
else:
    print('The UAV dropped the package at wrong position')
