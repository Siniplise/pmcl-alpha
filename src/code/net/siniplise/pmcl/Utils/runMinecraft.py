import subprocess

import minecraft_launcher_lib


def run(Dminecraft, Djava, Xms, Xmx, mcVersion,
        playerInfo):  # str.Dminecraft str.Djava int.Xms int.Xmx str.mcVersion dic.playerInfo

    batch = minecraft_launcher_lib.command.get_minecraft_command(mcVersion, Dminecraft, playerInfo)
    subprocess.Popen(batch)
