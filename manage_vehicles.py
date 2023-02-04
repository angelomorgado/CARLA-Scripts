'''
This script is used to spawn, delete, and modify vehicles properties in the simulation.
'''
import carla
import random
import time

def main_menu(world):
    while True:
        print('===========================================')
        print('Manage vehicles:')
        print('0 Spawn vehicles')
        print('1 Delete vehicles')
        print('2 Start autopilot')
        print('-1 Exit')
        print('===========================================')

        option = int(input('Insert option-> '))

        if option == 0:
            spawn_vehicle(world)
        elif option == 1:
            delete_vehicle()
        elif option == 2:
            start_autopilot()
        elif option == -1:
            quit(0)
        else:
            print('invalid value')

# Spawn vehicle
def spawn_vehicle(world):
    if world.get_actors().filter('vehicle.*'):
        print('There are vehicles already in the simulation')
        return

    # Ask how many vehicles to spawn
    num_vehicles = int(input('How many vehicles to spawn? -> '))
    
    # Random vehicles with random spawn points and random colors
    vehicle_bp = world.get_blueprint_library().filter('vehicle.*')
    spawn_points = world.get_map().get_spawn_points()
    for i in range(num_vehicles):
        vehicle = None
        while vehicle is None:
            spawn_point = random.choice(spawn_points)
            transform = carla.Transform(
                spawn_point.location,
                spawn_point.rotation
            )
            try:
                vehicle = world.try_spawn_actor(random.choice(vehicle_bp), transform)
            except:
                # try again if failed to spawn vehicle
                pass
        time.sleep(0.1)
    print('Successfully spawned {} vehicles!'.format(num_vehicles))

def delete_vehicle():
    for actor in world.get_actors().filter('vehicle.*'):
        actor.destroy()
    print('Successfully deleted all vehicles!')


def start_autopilot():
    for actor in world.get_actors().filter('vehicle.*'):
        actor.set_autopilot(True)
    print('Successfully started autopilot for all vehicles!')


if __name__ == '__main__':
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    world = client.get_world()
    main_menu(world)