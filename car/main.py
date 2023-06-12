import numpy as np
import random
import random

class coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


car_data = np.genfromtxt('car_position.csv', delimiter=',')
length = 4.88
width = 2.44
height = 1.5
ref_z = 14.6 # ground level
set_z = ref_z+height/2
ncar = len(car_data)
car_coor_center = [coordinate(0,0,0) for i in range(ncar)]
car_coor_min = [coordinate(0,0,0) for i in range(ncar)]
car_coor_max = [coordinate(0,0,0) for i in range(ncar)]

for i in range(ncar):
    car_coor_center[i].x = car_data[i,0]
    car_coor_center[i].y = car_data[i,1]
    car_coor_center[i].z = set_z
    if i <= (28-1):
        car_dim = coordinate(width, length, height) # Vertical
        #car_dim = coordinate(length, width, height) # Horizontal
    else:
        #car_dim = coordinate(width, length, height) # Vertical
        car_dim = coordinate(length, width, height) # Horizontal

    car_coor_min[i].x = car_coor_center[i].x - car_dim.x / 2
    car_coor_min[i].y = car_coor_center[i].y - car_dim.y / 2
    car_coor_min[i].z = car_coor_center[i].z - car_dim.z / 2
    car_coor_max[i].x = car_coor_center[i].x + car_dim.x / 2
    car_coor_max[i].y = car_coor_center[i].y + car_dim.y / 2
    car_coor_max[i].z = car_coor_center[i].z + car_dim.z / 2


# Generate a list of dataset1
dataset1 = list(range(ncar))

# Randomly select numbers from the list without replacement
dataset2 = random.sample(dataset1, int(ncar/2))


# Remove the numbers selected in dataset1 from the list
for num in dataset2:
    dataset1.remove(num)


car_coor_min_h = [coordinate(0,0,0) for i in range(len(dataset1))]
car_coor_max_h = [coordinate(0,0,0) for i in range(len(dataset1))]
car_coor_min_c = [coordinate(0,0,0) for i in range(len(dataset2))]
car_coor_max_c = [coordinate(0,0,0) for i in range(len(dataset2))]

k = 0
for i in dataset1:
    car_coor_min_h[k] = car_coor_min[i]
    car_coor_max_h[k] = car_coor_max[i]
    k += 1

k = 0
for i in dataset2:
    car_coor_min_c[k] = car_coor_min[i]
    car_coor_max_c[k] = car_coor_max[i]
    k += 1

# Open the output file in write mode
with open('hotcar_output.fds', 'w') as output_file:
    # Loop through each line in the input file
    for i in range(len(dataset1)):
        # Open the input file in read mode
        with open('hotcar.fds', 'r') as input_file:
            count_line = 0
            for line in input_file:
                # Check if the line needs to be modified
                count_line+=1
                line = line.replace('INDEX', f'H{i+1}')
                # Replace the old text with new text
                line = line.replace('XMIN', f'{car_coor_min_h[i].x:.4f}')
                line = line.replace('XMAX', f'{car_coor_max_h[i].x:.4f}')
                line = line.replace('YMIN', f'{car_coor_min_h[i].y:.4f}')
                line = line.replace('YMAX', f'{car_coor_max_h[i].y:.4f}')
                line = line.replace('ZMIN', f'{car_coor_min_h[i].z:.4f}')
                line = line.replace('ZMAX', f'{car_coor_max_h[i].z:.4f}')
                # Write the line to the output file
                output_file.write(line)

        output_file.write('\n')

# Open the output file in write mode
with open('coldcar_output.fds', 'w') as output_file:
    # Loop through each line in the input file
    for i in range(len(dataset2)):
        # Open the input file in read mode
        with open('coldcar.fds', 'r') as input_file:
            count_line = 0
            for line in input_file:
                # Check if the line needs to be modified
                count_line+=1
                line = line.replace('INDEX', f'C{i+1}')
                # Replace the old text with new text
                line = line.replace('XMIN', f'{car_coor_min_c[i].x:.4f}')
                line = line.replace('XMAX', f'{car_coor_max_c[i].x:.4f}')
                line = line.replace('YMIN', f'{car_coor_min_c[i].y:.4f}')
                line = line.replace('YMAX', f'{car_coor_max_c[i].y:.4f}')
                line = line.replace('ZMIN', f'{car_coor_min_c[i].z:.4f}')
                line = line.replace('ZMAX', f'{car_coor_max_c[i].z:.4f}')
                # Write the line to the output file
                output_file.write(line)

        output_file.write('\n')




