'''
Changes all kinds of lights, street and vehicle.
It has a weird bug, because even the code presented in the documentation gives the error
'''
import carla

def main_menu(light_manager):
    while True:
        print('===========================================')
        print('Change lights:')
        print('0 Street lights')
        print('1 Vehicle lights')
        print('-1 Exit')
        print('===========================================')

        option = int(input('Insert option-> '))

        if option == 0:
            street_menu(light_manager)
        elif option == 1:
            vehicle_menu(light_manager)
        elif option == -1:
            quit(0)
        else:
            print('invalid value')

def street_menu(light_manager):
    while True:
        print('===========================================')
        print('Street lights:')
        print('0 Turn on/off')
        print('1 Change color')
        print('2 Set intensity')
        print('-1 Return')
        print('===========================================')

        option = int(input('Insert option-> '))
        
        # Get all street lights
        street_lights = light_manager.get_light_group(carla.LightGroup.Street)

        # Get a list of carla.Light objects
        lights = street_lights.lights
        
        # Turn on/off
        if option == 0:
            is_on = light_manager.is_active(lights[0])
            if is_on == True:
                light_manager.turn_off(street_lights)
            else:
                light_manager.turn_on(street_lights)
        # Color
        elif option == 1:
            color = get_color()
            light_manager.set_color(lights, color)
        # Intensity
        elif option == 2:
            intensity = get_intensity()
            intensities = [intensity for i in range(len(lights))]
            light_manager.set_intensities(lights, intensities)
        elif option == -1:
            return
        else:
            print('invalid value')

def vehicle_menu(light_manager):
    while True:
        print('===========================================')
        print('Vehicle lights:')
        print('0 Turn on/off')
        print('1 Change color')
        print('2 Set intensity')
        print('-1 Return')
        print('===========================================')

        option = int(input('Insert option-> '))

        # Get all vehicle lights
        vehicle_lights = light_manager.get_light_group(carla.LightGroup.Vehicle)

        # Turn on/off
        if option == 0:
            is_on = light_manager.is_active(vehicle_lights)
            for i, l in enumerate(vehicle_lights):
                if is_on[i] == True:
                    l.turn_off()
                else:
                    l.turn_on()
        # Color
        elif option == 1:
            color = get_color()
            light_manager.set_color(vehicle_lights, color)
        # Intensity
        elif option == 2:
            intensity = get_intensity()
            intensities = [intensity for i in range(len(vehicle_lights))]
            light_manager.set_intensities(vehicle_lights, intensities)
        elif option == -1:
            return
        else:
            print('invalid value')

def get_color():
    print('===========================================')
    print('Choose a color::')
    print('0 White')
    print('1 Red')
    print('2 Blue')
    print('3 Green')
    print('4 Yellow')

    option = int(input('-> '))

    color_list = [carla.Color(255,255,255), carla.Color(255,0,0), carla.Color(0,0,255), carla.Color(0,255,0), carla.Color(255,255,0)]

    if option >= 0 and option < len(color_list):
        return color_list[option]
    else:
        print('Invalid weather index, defaulting to white')
        return color_list[0]

def get_intensity():
    print('Choose an intensity (0-100):')
    option = int(input('-> '))

    if option >= 0 and option <=100:
        return option
    else:
        print('Invalid intensity, defaulting to 100')

if __name__ == '__main__':
    # Initialize client
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)

    # Initialize world
    world = client.get_world()

    light_manager = world.get_lightmanager()

    main_menu(light_manager)