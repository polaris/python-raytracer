#!/usr/bin/env python3

''' Raytracer - A simple raytracer written in Python '''


def render():
    ''' Renders the scene '''
    image_width = 256
    image_height = 256

    print("P3\n" + str(image_width) + " " + str(image_height) + "\n255\n")

    for j in range(image_height - 1, -1, -1):
        for i in range(image_width):
            r = float(i) / (image_width - 1)
            g = float(j) / (image_height - 1)
            b = 0.25

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            print(str(ir) + " " + str(ig) + " " + str(ib))


def main():
    ''' Main entry point of the app '''
    render()


if __name__ == "__main__":
    main()
