import sys

import minecraft_launcher_lib.java_utils

import net.siniplise.pmcl.model.Application_Initialization as Appint


def look_for_java(mode):  # auto or mare

    if mode == "auto":

        javalist = minecraft_launcher_lib.java_utils.find_system_java_versions()
        return javalist

    elif mode == "mare":
        pass
    else:
        sys.exit(0xc000012)


print(minecraft_launcher_lib.command.get_minecraft_command(minecraft_directory="wda", version="1.19.2",
                                                           options=Appint.config_data))
minecraft_launcher_lib.install.install_minecraft_version()
