from vec3 import Vec3


Color = Vec3


def write_color(color):
    print(int(255.999 * color.x),
          int(255.999 * color.y),
          int(255.999 * color.z))
