import os
from mimetypes import MimeTypes

type_map = {
    "video": ["mp4", "mkv", "avi"],
    "docs": ["odg", "doc", "txt", "docx", "pdf", "csv"],
    "ebooks": ["epub"],
    "archive": ["zip", "7z", "tar", "gz", "tgz", "tar.gz"],
    "iso": ["iso"],
    "images": ["img", "jpeg", "svg"]
}


def list_all_files_in(directory):
    all_children = os.listdir(directory)
    absolute_path = list(map(lambda filename: directory + filename, all_children))
    f = filter(os.path.isfile, absolute_path)
    return list(f)


def list_all():
    mime = MimeTypes()
    directory = os.path.join("/home/adel/Téléchargements", '')
    listdir = list_all_files_in(directory)
    create_target_dirs(directory)

    print(listdir)

    for f in listdir:
        print(f)
        print("\t\t" + str(mime.guess_type(f)))


def create_target_dirs(directory):
    for dir in type_map.keys():
        target_dir = os.path.join(directory, dir)
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)


if __name__ == '__main__':
    print("here")
    list_all()
