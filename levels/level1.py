# Script to create bandito1 user and level environment
import os
import bandito_lib
import level2



def main():
    # Set constant for level
    LEVEL = 1

    # Generate level password and create user
    password = bandito_lib.add_user(LEVEL)

    # Give level SSH access
    bandito_lib.ssh_access(LEVEL)

    # Create flag readme file
    os.system("touch /home/bandito0/readme")
    os.system(f"echo '{password}' >> /home/bandito0/readme")
    os.system("chown bandito1:bandito0 /home/bandito0/readme")
    os.system("chmod 640 /home/bandito0/readme")

    # Restrict home folder permisisons
    bandito_lib.read_only_home_folder(LEVEL)

    # Transition into level 2 configuration
    level2.main()



if __name__ == '__main__':
    main()