
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
location1 = set_coords[0]
location2 = set_coords[0]
#print(location1)
#print(location2)

# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
import geopy.distance
dist = geopy.distance.geodesic(location1, location2).km
print("dist = ", dist)