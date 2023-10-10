import geopy.distance
import numpy as np


def read_data(filepath):
    file = open(filepath, 'r')
    lines = file.readlines()
    number_lines = len(lines)
    #print("number of lines: ", number_lines)

    count = 0
    sets = []
    while count < number_lines:
        #print("count = ", count)

        n = int(lines[count])
        #print("n = ", n) 
        
        all_coordinates_str = lines[1+count:1+count+n]
        #print("all_coordinates_str:\n", all_coordinates_str)
        coordinates = []

        for coord_str in all_coordinates_str:
            coord_list = coord_str.split()
            coordinates.append((float(coord_list[0]),float(coord_list[1])))

        sets.append([n,coordinates])

        count = count + n + 1

    return sets

sets = read_data('Assignment01/airlinehub2.in')
print("sets: ", sets)

set_ = sets[0]
set_coords = set_[1]

dist_matrix = np.zeros((len(set_coords),len(set_coords)))

for i in range(0,len(set_coords)):
    print("i:",i)
    location1 = set_coords[i]
    for j in range(0,len(set_coords)):
        location2 = set_coords[j]
        print("i =",i,"j =",j,":")
        print("location1:", location1, " - location2:", location2)
        dist = geopy.distance.geodesic(location1, location2).km
        dist_matrix[i][j] = dist

print("dist_matrix = \n", dist_matrix)
print("Sum of each column:")
print(np.sum(dist_matrix, axis=0))
