'''
Changes the map from the default list of maps
'''
import carla

if __name__ == "__main__":
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)

    world = client.get_world()

    # Get the current map
    current_map = world.get_map()

    # Get the list of available maps
    available_maps = client.get_available_maps()

    while True:
        print('==============================')
        print('Available maps:')
        for i, map in enumerate(available_maps):
            print(i, map)
        print('==============================')
        
        # Ask the user to select a map
        map_index = int(input('Select a map(-1 to quit)-> '))

        if map_index == -1:
            break

        # Check if the map is valid
        if map_index >= 0 and map_index < len(available_maps):
            if map_index == current_map:
                print('This is the current map, reloading it')
                client.reload_world()
                world = client.get_world()
            else:
                print('Loading map', available_maps[map_index])
                client.load_world(available_maps[map_index])
        else:
            print('Invalid map index')
            continue
        
