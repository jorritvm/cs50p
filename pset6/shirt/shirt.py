import sys
from os.path import exists
from PIL import Image, ImageOps


def check_amount_of_arguments(n):
    n = n + 1  # python script is always first arg
    if len(sys.argv) < n:
        sys.exit("Too few commandline arguments")
    elif len(sys.argv) > n:
        sys.exit("Too many commandline arguments")


def check_argument_fp(i, new=False):
    fp = sys.argv[i]
    if fp.endswith(".jpg") or fp.endswith(".jpeg") or fp.endswith(".png"):
        if not exists(fp) and not new:
            sys.exit("File does not exist")
        return fp
    else:
        sys.exit("Not an image file")


def main():
    check_amount_of_arguments(2)
    fp_in = check_argument_fp(1, new=False)
    fp_out = check_argument_fp(2, new=True)

    print(fp_in)
    print(fp_out)

    if fp_in[-4:] != fp_out[-4:]:
        sys.exit("Input and output file extensions must match")

    input = Image.open(fp_in)

    im_shirt = Image.open("shirt.png")
    input = ImageOps.fit(input, im_shirt.size)

    input.paste(im_shirt, im_shirt)
    input.save(fp_out)


if __name__ == "__main__":
    main()
