# Python code to
# demonstrate readlines()
 
L = ["Geeks\n", "for\n", "Geeks\n"]
 
# Using readlines()
file1 = open('Assignment01/airlinehub2.in', 'r')
lines = file1.readlines()
number_lines = len(lines)
 
count = 0
sets = []
while count < number_lines:
    n1 = int(lines[0])
    print(n1)
    all_coordinates_str = lines[1:n1+1]
    latitudes = []
    longitudes = []

    for c in all_coordinates_str:
        coordinate = c.split()
        latitudes.append(float(coordinate[0]))
        longitudes.append(float(coordinate[1]))

    print(latitudes)
    print(longitudes)
