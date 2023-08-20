import json
import os

config_data = {

    "player": {
        "mode": "undefined",
        "name": "",
        "skin": "",
    },
    "game": {
        "Dminecraft": "",
        "Djava": "",
        "sedVersion": ""
    },
    "java": {
        "Xms": 0,
        "Xmx": 0
    },
    "options": {
        "username": "",
        "uuid": "",
        "token": "",
        "executablePath": "",
        "defaultExecutablePath": "",
        "jvmArguments": [],
        "launcherName": "",
        "launcherVersion": "",
        "gameDirectory": "",
        "demo": False,
        "customResolution": False,
        "resolutionWidth": 0,
        "resolutionHeight": 0,
        "server": "",
        "port": "",
        "nativesDirectory": "",
        "enableLoggingConfig": False,
        "disableMultiplayer": False,
        "disableChat": False,
        "quickPlayPath": None,
        "quickPlaySingleplayer": None,
        "quickPlayMultiplayer": None,
        "quickPlayRealms": None,

    }
}


def app_init(cachedir):
    if not os.path.isdir(cachedir):
        os.makedirs(cachedir)
    if not os.path.isfile(cachedir + "\\pmcl_config.json"):
        with open(cachedir + "\\pmcl_config.json", 'w') as file:
            json.dump(config_data, file)


'''
        "username": None,
        "uuid": None,
        "token": None,

        # This is optional
        "executablePath": "java",  # The path to the java executable
        "defaultExecutablePath": "java",  # The path to the java executable if the version.json has none
        "jvmArguments": [],  # The jvmArguments
        "launcherName": "minecraft-launcher-lib",  # The name of your launcher
        "launcherVersion": "1.0",  # The version of your launcher
        "gameDirectory": "/home/user/.minecraft",  # The gameDirectory (default is the path given in arguments)
        "demo": False,  # Run Minecraft in demo mode
        "customResolution": False,  # Enable custom resolution
        "resolutionWidth": "854",  # The resolution width
        "resolutionHeight": "480",  # The resolution heigth
        "server": "example.com",  # The IP of a server where Minecraft connect to after start
        "port": "123",  # The port of a server where Minecraft connect to after start
        "nativesDirectory": "minecraft_directory/versions/version/natives",  # The natives directory
        "enableLoggingConfig": False,  # Enable use of the log4j configuration file
        "disableMultiplayer": False,  # Disables the multiplayer
        "disableChat": False,  # Disables the chat
        "quickPlayPath": None,  # The Quick Play Path
        "quickPlaySingleplayer": None,  # The Quick Play Singleplayer
        "quickPlayMultiplayer": None,  # The Quick Play Multiplayer
        "quickPlayRealms": None,  # The Quick Play Realms
'''
