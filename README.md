# Posaics

Posaics is a fun project that creates big pictures
built out of thousands of other tiny pictures.

## Roadmap

- [ ] Use an image processing library to load an input image into your code
- [ ] Divide the input image into squares, and calculate the average color of each square
- [ ] A quick diversion - create an output image out of squares of these average colors.
- [ ] Find an initial set of 100 source images. Write a script that crops them all to squares and saves the cropped versions
- [ ] Calculate the average color of each source image

<img src="https://robertheaton.com/images/mosaic-plan.png" alt="Mosaic Plan" style="max-width:100%;height:auto;">

## Building

To clone the repository, and `cd` into it:

```bash
git clone https://github.com/kmr-ankitt/posaics
```

## Running

To run the project, use the following command:

```bash
uv run src/main.py example/jonsnow.jpg
```
