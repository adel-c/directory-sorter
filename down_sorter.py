import os
from mimetypes import MimeTypes

type_map = {
    "video": ["mp4", "mkv", "avi"],
    "docs": ["odg", "doc", "epub", "txt", "docx", "pdf", "csv"],
    "archive": ["zip", "7z", "tar", "gz", "tgz", "tar.gz"],
    "iso": ["iso"],
    "images": ["img", "jpeg", "svg"]
}


def mmm(p):
    print(p)
    print(os.path.isfile(p))
    return os.path.isfile(p)


def list_all_files_in(directory):
    directory_with_tail_slash = os.path.join(directory, '')
    all_children = os.listdir(directory_with_tail_slash)
    absolute_path = list(map(lambda filename: directory_with_tail_slash + filename, all_children))
    f = filter(os.path.isfile, absolute_path)
    return list(f)


def list_all():
    mime = MimeTypes()

    listdir = list_all_files_in("/home/adel/Téléchargements")
    print(listdir)

    for f in listdir:
        print(f)
        print("\t\t" + str(mime.guess_type(f)))


if __name__ == '__main__':
    print("here")
    list_all()
