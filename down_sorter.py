import os
import shutil
import sys

download_path = "/home/adel/Téléchargements"
if len(sys.argv) > 1:
    print("change directory to", sys.argv[1])
    download_path = sys.argv[1]
type_map = {
    "video": ["mp4", "mkv", "avi"],
    "audio": ["mp3"],
    "docs": ["odg", "doc", "txt", "docx", "pdf", "csv", "json", "py", "js", "java"],
    "ebooks": ["epub"],
    "archive": ["zip", "7z", "tar", "gz", "tgz", "tar.gz"],
    "iso": ["iso"],
    "images": ["img", "jpeg", "svg", "jpg"]
}


def list_all_files_in(directory):
    all_children = os.listdir(directory)
    absolute_path = list(map(lambda filename: directory + filename, all_children))
    f = filter(os.path.isfile, absolute_path)
    return list(f)


def list_all():
    directory = os.path.join(download_path, '')
    listdir = list_all_files_in(directory)
    create_target_dirs(directory)

    for f in listdir:
        extension = extract_extension(f)
        dest = find_destination_dir_for_extention(extension)
        if dest:
            try:
                shutil.move(f, os.path.join(directory, dest))
                print("move " + f + " to  " + os.path.join(directory, dest))
            except OSError as e:
                print("Can't move file " + f, e)

        else:
            print("file " + f + " with extension " + extension + " not mapped")


def find_destination_dir_for_extention(extension):
    for dest, values in type_map.items():
        if extension in values:
            return dest
    return ""


def extract_extension(f):
    extension = os.path.splitext(f)[1]
    extension = extension.removeprefix('.')
    return extension


def create_target_dirs(directory):
    for dir in type_map.keys():
        target_dir = os.path.join(directory, dir)
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)


if __name__ == '__main__':
    print("sorting", download_path)
    list_all()
