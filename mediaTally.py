import os
import subprocess
from progressbar import progressbar

CMD = "ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0".split()

library_dirs = [
        "/mnt/media/Movies",
        "/mnt/media/Shows",
        ]

destination = os.path.join(os.path.dirname(__file__), 'media.txt')


def get_resolution(path: str) -> str:
    if os.path.isfile(path):
        ret = subprocess.run(CMD + [path], stdout=subprocess.PIPE)
        return ret.stdout.decode('utf-8')[:-1]

    if os.path.isdir(path):
        for file in os.listdir(path):
            sub_path = os.path.join(path, file)
            res = get_resolution(sub_path)
            if res:
                return res

    return ''



def get_name(path) -> str:
    basename = os.path.join(path)

    if os.path.isdir(path):
        return basename

    if '.' not in basename:
        return basename

    return '.'.join(basename.split('.')[:-1])
    


def get_media_data() -> list:

    content = []

    for d in library_dirs:
        for file in progressbar(os.listdir(d), redirect_stdout=True):
            file_path = os.path.join(d, file)
            media_name = get_name(file)

            print(media_name)

            resolution = get_resolution(file_path)

            content.append((media_name, f"{resolution:<9} {media_name}\n"))

    return content


def data_to_file(data):
    with open(destination, 'w') as file:
        for _, entry in content:
            file.write(entry)


if __name__ == "__main__":
    content = get_media_data()

    print('Sorting Content')
    content.sort(key=lambda x: x[0])

    print(f'writing to {destination}')
    data_to_file(content)

    print('Done')
