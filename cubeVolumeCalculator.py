#purpose of the program is to return the surface area and volume of a cube
#prompt user for edge of cube
#write cuber function that returns:
#surface_area_of_cube = 6*edge_of_cube**2
#volume_of_cube = edge_of_cube**3

def main():
    edge=float(input("Enter the length of the cube's edge. "))

    #call function and catch return values
    surfaceArea, volume = cuber(edge)

    #print and format to three decimal places
    print('The surface area of the cube is: ', format(surfaceArea, '.3f'))
    print('The volume of the cube is: ', format(volume, '.3f'))
    
def cuber(edge):
    cube_surface_area= 6*edge**2
    cube_volume=edge**3

    return cube_surface_area, cube_volume

main()
