import sys
from PIL import Image

def main():
    if len(sys.argv) < 2:
        print("Usage: posaics <input_image>")
        print("Posaics accepts input image as an argument.")
        sys.exit(1)

    input_file_name = sys.argv[1]
    input_image = Image.open(input_file_name)

if __name__ == "__main__":
    main()
