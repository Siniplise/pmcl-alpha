import json


def set_profile(filePath, profile):  # str.filePath dic.profile

    with open(filePath, 'w') as file:
        json.dump(file, profile)
