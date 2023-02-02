import carla

# List of weather presets
preset_list = {
    0 : carla.WeatherParameters.ClearNoon,
    1 : carla.WeatherParameters.CloudyNoon,
    2 : carla.WeatherParameters.WetNoon,
    3 : carla.WeatherParameters.WetCloudyNoon,
    4 : carla.WeatherParameters.SoftRainNoon,
    5 : carla.WeatherParameters.MidRainyNoon,
    6 : carla.WeatherParameters.HardRainNoon,
    7 : carla.WeatherParameters.ClearSunset,
    8 : carla.WeatherParameters.CloudySunset,
    9 : carla.WeatherParameters.WetSunset,
    10 : carla.WeatherParameters.WetCloudySunset,
    11 : carla.WeatherParameters.SoftRainSunset,
    12 : carla.WeatherParameters.MidRainSunset,
    13 : carla.WeatherParameters.HardRainSunset,
}

name_list = [
    "ClearNoon",
    "CloudyNoon",
    "WetNoon",
    "WetCloudyNoon",
    "SoftRainNoon",
    "MidRainyNoon",
    "HardRainNoon",
    "ClearSunset",
    "CloudySunset",
    "WetSunset",
    "WetCloudySunset",
    "SoftRainSunset",
    "MidRainSunset",
    "HardRainSunset",
]

#TODO: Change the physics manually to the appropriate weather
if __name__ == "__main__":
    # Initialize client
    client = carla.Client("localhost", 2000)
    client.set_timeout(10.0)

    # Initialize world
    world = client.get_world()

    while True:
        print('====================================')
        for k in preset_list:
            print(k, name_list[k])
        print('====================================')
        index = int(input('Select a map(-1 to quit)-> '))

        if index == -1:
            break

        # Check if the map is valid
        if index >= 0 and index < len(preset_list):
            world.set_weather(preset_list[index])
        else:
            print('Invalid weather index')