#!/usr/bin/env python3

''' Raytracer - A simple raytracer written in Python '''


from color import Color, write_color


def render():
    ''' Renders the scene '''
    image_width = 256
    image_height = 256

    print("P3\n" + str(image_width) + " " + str(image_height) + "\n255\n")

    for j in range(image_height - 1, -1, -1):
        for i in range(image_width):
            pixel_color = Color(float(i) / (image_width - 1),
                                float(j) / (image_height - 1),
                                0.25)
            write_color(pixel_color)


def main():
    ''' Main entry point of the app '''
    render()


if __name__ == "__main__":
    main()
