import geopy.distance
import numpy as np
import math

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



def make_dist_matrix(set_coords):
    dist_matrix = np.zeros((len(set_coords),len(set_coords)))

    for i in range(0,len(set_coords)):
        #print("i:",i)
        location1 = set_coords[i]
        for j in range(0,len(set_coords)):
            location2 = set_coords[j]
            #print("i =",i,"j =",j,":")
            #print("location1:", location1, " - location2:", location2)
            
            #dist = geopy.distance.geodesic(location1, location2).km
            dist = math.dist(location1,location2)

            dist_matrix[i][j] = dist
    return dist_matrix

def find_min_max_dist_location(dist_matrix, set_coords):
    #print("dist_matrix = \n", dist_matrix)
    #print("Sum of each column:")
    accumulated_dist_list = np.sum(dist_matrix, axis=0)

    min_max_dist = 9999999999999999
    for i in range(0,len(accumulated_dist_list)):
        #print(i)
        if min_max_dist >= accumulated_dist_list[i]:
            min_max_dist = accumulated_dist_list[i]
            min_max_dist_location = set_coords[i]
    return min_max_dist_location

def find_all_min_max_dist_location(filepath):
    sets = read_data(filepath)
    #print("sets: ", sets)
    min_max_dist_locations = []
    for set_ in sets:
        set_coords = set_[1]
        dist_matrix = make_dist_matrix(set_coords)
        min_max_dist_location = find_min_max_dist_location(dist_matrix, set_coords)
        min_max_dist_locations.append(min_max_dist_location)
    
    return min_max_dist_locations

def make_output_file(input_filepath, outfut_filepath):
    min_max_dist_locations = find_all_min_max_dist_location(input_filepath)
    with open(outfut_filepath, 'w') as f:
        for l in min_max_dist_locations:
            line = "{:.2f} {:.2f}".format(l[0],l[1])
            f.write(line)
            f.write('\n')

make_output_file('Assignment01/airlinehub.in', 'Assignment01/my_airlinehub.ans')