import os


def rename_files():
    folder = ''
    for count, filename in enumerate(os.listdir(folder)):
        if filename.endswith('.jpg'):
            file_ext = '.jpg'
            img_des = ' {}{}'.format(count, file_ext)
            source = '{}/{}'.format(folder, filename)
            des = '{}/{}'.format(folder, img_des)
            os.rename(source, des)
        else:
            file_ext = '.png'
            img_des = ' {}{}'.format(count, file_ext)
            source = '{}/{}'.format(folder, filename)
            des = '{}/{}'.format(folder, img_des)
            os.rename(source, des)


if __name__ == '__main__':
    rename_files()
