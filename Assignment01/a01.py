
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
        latitudes = []
        longitudes = []

        for c in all_coordinates_str:
            #print("c:", c)
            coordinate = c.split()
            #print("coordinate:", coordinate)
            latitudes.append(float(coordinate[0]))
            longitudes.append(float(coordinate[1]))

        #print("lat:", latitudes)
        #print("lon:", longitudes)

        sets.append([n,latitudes,longitudes])

        count = count + n + 1

    #("sets: ", sets)
    return sets

sets = read_data('Assignment01/airlinehub2.in')

set_ = sets[0]
set_lat = set_[1]
set_lon = set_[2] 
location1 = (set_lat[0],set_lon[0])
location2 = (set_lat[1],set_lon[1])
print(location1)
print(location2)

# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
import geopy.distance
dist = geopy.distance.geodesic(location1, location2).km
