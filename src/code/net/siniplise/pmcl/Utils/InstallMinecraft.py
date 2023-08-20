import minecraft_launcher_lib


def install(Dminecraft, mcVersion):  # str.Dminecraft str.mcVersion

    minecraft_launcher_lib.install.install_minecraft_version(mcVersion, Dminecraft)

if __name__ == '__main__':
    install('..\\..\\..\\..\\..\\run\\.minecraft','1.12.2')