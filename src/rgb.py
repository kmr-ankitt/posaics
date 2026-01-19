from PIL import Image

def find_average(pixels: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    r_sum = 0
    g_sum = 0
    b_sum = 0
    num_pixels = len(pixels)
    for r, g, b in pixels:
        r_sum += r
        g_sum += g
        b_sum += b
    return (r_sum // num_pixels, g_sum // num_pixels, b_sum // num_pixels)

def get_avg(input_image: Image.Image):
    rgb_img = input_image.convert("RGB")
    all_pixels = list(rgb_img.getdata())
    print(find_average(all_pixels))
