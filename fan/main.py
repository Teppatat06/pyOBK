import numpy as np

class coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


fan_data = np.genfromtxt('fan_position.csv', delimiter=',')
set_z = 16.72
flowrate = 1.63#3.19
fan_length = coordinate(0.5,2.0,0.5)
fan_coor_center = [coordinate(0,0,0) for i in range(len(fan_data))]
fan_coor_min = [coordinate(0,0,0) for i in range(len(fan_data))]
fan_coor_max = [coordinate(0,0,0) for i in range(len(fan_data))]


for i in range(len(fan_data)):
    fan_coor_center[i].x = fan_data[i,0]
    fan_coor_center[i].y = fan_data[i,1]
    fan_coor_center[i].z = set_z
    fan_coor_min[i].x = fan_coor_center[i].x - fan_length.x / 2
    fan_coor_min[i].y = fan_coor_center[i].y - fan_length.y / 2
    fan_coor_min[i].z = fan_coor_center[i].z - fan_length.z / 2
    fan_coor_max[i].x = fan_coor_center[i].x + fan_length.x / 2
    fan_coor_max[i].y = fan_coor_center[i].y + fan_length.y / 2
    fan_coor_max[i].z = fan_coor_center[i].z + fan_length.z / 2





# Open the output file in write mode
with open('jetfan_output.fds', 'w') as output_file:
    # Loop through each line in the input file
    for i in range(len(fan_data)):
        # Open the input file in read mode
        with open('jetfan.fds', 'r') as input_file:
            count_line = 0
            for line in input_file:
                # Check if the line needs to be modified
                count_line+=1
                line = line.replace('INDEXFAN', f'{i+1}')
                if count_line in [1, 2, 3]:
                    # Replace the old text with new text
                    line = line.replace('XMIN', f'{fan_coor_min[i].x:.4f}')
                    line = line.replace('XMAX', f'{fan_coor_max[i].x:.4f}')
                    line = line.replace('YMIN', f'{fan_coor_min[i].y:.4f}')
                    line = line.replace('YMAX', f'{fan_coor_max[i].y:.4f}')
                    line = line.replace('ZMIN', f'{fan_coor_min[i].z:.4f}')
                    line = line.replace('ZMAX', f'{fan_coor_max[i].z:.4f}')
                elif count_line == 6:
                    line = line.replace('MYFLOWRATE', f'{flowrate:.4f}')
                    line = line.replace('MYLENGTH', f'{fan_length.y:.4f}')
                else:
                    pass
                # Write the line to the output file
                output_file.write(line)
        output_file.write('\n')





