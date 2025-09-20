


import turtle as tu
from PIL import Image, ImageGrab
# import winsound

class ascii_art:
    def __init__(
        self,
        x_len=5,
        y_len=7,
        chars=["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."],
        color_set={
            "*": "white",
            "S": "green",
            "#": "green",
            "&": "white",
            "@": "black",
            "$": "white",
            "%": "white",
            "!": "blue",
            ":": "darkgreen",
            ".": "grey",
        },
        save=True,
    ):
        """example usage:
        from sketchpy import canvas
        obj = cavnas.ascii_art()
        res = obj.load_data(img_path="image.png")
        obj.draw()

        paramerter:
        x_len = pixel movement in x direction
        y_lenn = pixel movement in y direction
        chars = list of characters to be used from convertion of image to ASCII art
        color_set = dictionary map for specific character to a specific color
        save = takes a screen shot of the entire screen and saves it

        """
        self.x_len = x_len
        self.y_len = y_len
        self.chars = chars
        self.colo_set = color_set
        self.save = save

    def convert_to_acsii(self, img_path, file_name=None) -> str:
        """Converts the given image to ascii art and save it to output_file, returns string
        img_path = path of the image
        file_name = name of the output text file"""

        # pass the image as command line argument
        img = Image.open(img_path)

        # resize the image
        width, height = img.size
        aspect_ratio = height / width
        new_width = 80
        new_height = aspect_ratio * new_width * 0.55
        img = img.resize((new_width, int(new_height)))
        # new size of image
        # print(img.size)

        # convert image to greyscale format
        img = img.convert("L")

        pixels = img.getdata()

        # replace each pixel with a character from array
        chars = self.chars
        new_pixels = [chars[pixel // 25] for pixel in pixels]
        new_pixels = "".join(new_pixels)

        # split string of chars into multiple strings of length equal to the new width and create a list
        new_pixels_count = len(new_pixels)
        ascii_image = [
            new_pixels[index : index + new_width]
            for index in range(0, new_pixels_count, new_width)
        ]
        n_chars = len(ascii_image[0])

        self.half_width = n_chars * self.x_len * -1

        ascii_image = "\n".join(ascii_image)

        # write to a text file.
        if file_name != None:
            with open(f"{file_name}.txt", "w") as f:
                f.write(ascii_image)
        print(ascii_image)
        return ascii_image

    def load_data(self, file_path=None, img_path=None, raw_data=None):
        """used to load a previously processed image,
        file_path = path of the ascii art txt file
        img_path = path of the image
        raw_data = sting containing the ascii art"""

        if img_path != None:
            self.data = self.convert_to_acsii(img_path)
        elif file_path != None:
            re = open(file_path, "r")
            self.data = re.readlines()
        elif raw_data != None:
            self.data = raw_data
            print("sepcify the correct data")
            return
        return self.data

    def draw(self, data=None):
        # setting the x and y coordinates
        s_x = self.half_width
        s_y = 250

        if data != None:
            self.data = data

        p = tu.Pen()
        p.speed(0)
        tu.bgcolor("black")
        p.up()
        p.width(2)
        p.goto(s_x, s_y)
        p.down()

        # function to select the color
        def set_col(c):
            chars = self.colo_set
            col = chars[c]
            p.pencolor(col)
            return col

        for i in self.data:

            if i == "\n":
                p.up()
                p.goto(self.half_width, s_y - self.y_len)
                s_y -= self.y_len
                s_x = self.half_width
                p.down()
                continue
            else:
                col = set_col(i)
                if col == "black":
                    s_x += 2 * self.x_len
                    p.up()
                    p.goto(s_x, s_y)
                    continue
                else:
                    p.down()
                    s_x += self.x_len
                    p.goto(s_x, s_y)

                    s_x += self.x_len
                    p.up()
                    p.goto(s_x, s_y)
                    p.down()
        if self.save:
            image = ImageGrab.grab()
            image.save("sketch.png")
            print("your sketch is saved as sketch.png!!")
        # winsound.PlaySound("SystemDefault", winsound.SND_ALIAS) # Commented out for cross-platform compatibility
        tu.done()

    def print_to_terminal(self):
        for i in self.data:
            print(i, end="")

