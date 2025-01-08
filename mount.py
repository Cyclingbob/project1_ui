import subprocess
def get_connected_devices():
    device_dir = "/dev/disk/by-label"
    found_files = os.listdir(device_dir)
    filtered_files = [] # disks that are found
    for file in found_files:
        if not file == "rootfs" and not file == "bootfs": #remove os disks
            filtered_files.append(file)
    connected_devices = []
    for file in filtered_files:
        linked_path = device_dir + "/" + file
        actual_file = os.readlink(linked_path)
        block_device = "/dev/" + actual_file.split("/")[2]
        connected_devices.append((file, block_device)) #name of the usb disk, then the sdx (block device)
    return connected_devices
def get_mounted(): #all mounts remembered by the pi, even if they've since been disconnected
    mount_file = "/proc/mounts"
    mounts = open(mount_file).read().split('\n')
    filtered_mounts = []
    for mount in mounts:
        if "/dev/sd" in mount:
           filtered_mounts.append(mount)
    mount_list = []
    for mount in filtered_mounts:
        split_mount = mount.split(" ")
        block_device = split_mount[0]
        directory = split_mount[1]
        mount_list.append((directory, block_device))
    return mount_list
def mount_disk(block_device, mount_dir):
    if not os.path.isdir(mount_dir):
        os.mkdir(mount_dir) #make a directory to mount to if it dosen't exist
    print(f"mounting {block_device} to {mount_dir}")
    result = subprocess.run(["mount", block_device, mount_dir], stdout=subprocess.PIPE, check=True)
    print(result.stdout.decode("utf-8"))
#    print(block_device, device_name)
def check_and_mount():
    connected_devices = get_connected_devices()
    print("connected devices: ")
    print(connected_devices)
    currently_mounted = get_mounted()
    print("currently mounted: ")
    print(currently_mounted)
    for connected_device in connected_devices:
        found = False
        count = len(currently_mounted)
        while found == False and count > 0:
            if currently_mounted[count-1][1] == connected_device[1]:
                found = True #already mounted
        if found == False:
            mount_disk(connected_device[1], "/media/pi/" + connected_device[0])
if __name__ == "__main__":
    check_and_mount()
