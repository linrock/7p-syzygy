import os

TB_URL="https://tablebase.lichess.ovh/tables/standard/7/"
DATA_DIRS = {
    '~/data/syzygy',
    '/dev/shm',
}

TB_SIZES = {}
with open('7p-tb-list.txt', 'r') as f:
    for row in f:
        pieces, data_size_bytes = row.split()
        TB_SIZES[pieces] = int(data_size_bytes)

def get_emptiest_dir():
    emptiest_dir, most_disk_space = DATA_DIRS[0], 0
    for data_dir in DATA_DIRS:
        statvfs = os.statvfs(d)
        disk_avail = statvfs.f_frsize * statvfs.f_bavail
        if disk_avail > most_disk_space:
            most_disk_space = disk_avail
            emptiest_dir = data_dir
    return data_dir

