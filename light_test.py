import carla

# Tried with the code in the documentation and it still ended up in an error
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)
world = client.get_world()
# light_manager = world.get_lightmanager()
# my_lights = light_manager.get_light_group(carla.LightGroup.Building)
# light_manager.turn_on(my_lights)
# light_manager.set_color(my_lights,carla.Color(255,0,0))
# light_manager.set_intensities(my_lights,list_of_intensities)


# Get the light manager and lights
lmanager = world.get_lightmanager()

# Custom all lights - Gives off Aborted (core dumped)
mylights = lmanager.get_all_lights()
lmanager.turn_on(mylights)
lmanager.set_color(mylights,carla.Color(255,0,0))

# Custom a group of lights - Gives off AttributeError
my_lights = lmanager.get_light_group(carla.LightGroup.Street)
lmanager.turn_on(my_lights)
lmanager.set_color(my_lights,carla.Color(255,0,0))