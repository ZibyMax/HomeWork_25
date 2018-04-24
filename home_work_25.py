import os
import subprocess

def resize_image(images, input_dir, output_dir):
    programm = 'convert.exe'
    operator = '-resize 200'
    for image in images:
        source = os.path.join(input_dir, image)
        destination = os.path.join(output_dir, image)
        process = subprocess.run(programm + ' ' + source + ' ' + operator + ' ' + destination)

def get_jpg_files(path, input_dir):
    images = []
    for root, dirs, files_in_dir in os.walk(os.path.join(path, input_dir)):
        for filename in files_in_dir:
            if filename[-4:] == '.jpg':
                images.append(filename)
    return images

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(path, 'Source\\')
    output_dir = os.path.join(path, 'Result\\')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    images = get_jpg_files(path, input_dir)
    resize_image(images, input_dir, output_dir)

if __name__ == '__main__':
    main()