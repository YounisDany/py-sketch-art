
import turtle as tu
from PIL import ImageGrab

class sketch:

    def __init__(self, x_offset=300, y_offset=300, save=False):
        """Draw the traced image with help of this sketch function\n
        x-offset - postion of the image in x axis\n
        y-offset - postion of the image in y axis\n
        call the draw_fn() to draw the traced image"""
        self.pen = tu.Turtle()
        self.pen.speed(0)
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.save = save

    def get_coord(self, data):
        tu = []
        for i in data.readlines():
            i = (i.strip("\n")).strip("(").strip(")")
            tu.append(tuple(map(int, i.split(","))))

        return tu

    def go(self, x, y):
        self.pen.penup()
        self.pen.goto(x - self.x_offset, (y * -1) + self.y_offset)
        self.pen.pendown()

    def paint(self, coord, co=(0, 0, 0)):
        self.pen.color(co)
        t_x, t_y = coord[0]
        self.go(t_x, t_y)
        self.pen.fillcolor(co)
        self.pen.begin_fill()
        t = 0
        for i in coord[1:]:
            print(i)
            x, y = i
            if t:
                self.go(x, y)
                t = 0
                self.pen.begin_fill()
                continue
            if x == -1 and y == -1:
                t = 1
                self.pen.end_fill()
                continue
            else:
                self.pen.goto(x - self.x_offset, (y * -1) + self.y_offset)
        self.pen.end_fill()

    def draw_fn(self, file, mode=1, co=(0, 0, 0), thickness=1, retain=False):
        """file - path of the file which contains the coordinates\n
        mode - mode of drawing (1 - sketch with line, 0 - fill with color)\n
        co - color of the line or fill\n
        thickness - thickness of the line\n
        retain - retain the image drawn after executing"""

        co = (co[0] / 255, co[1] / 255, co[2] / 255)

        self.pen.color(co)
        data = open(f"{file}.txt", "r")
        coord = self.get_coord(data)

        self.pen.width(thickness)
        if mode:
            t_x, t_y = coord[0]
            self.go(t_x, t_y)
            t = 0
            for i in coord[1:]:
                print(i)
                x, y = i
                if t:
                    self.go(x, y)
                    t = 0
                    continue
                if x == -1 and y == -1:
                    t = 1
                    continue
                else:
                    self.pen.goto(x - self.x_offset, (y * -1) + self.y_offset)
        else:
            self.paint(coord=coord, co=co)

        if self.save:
            image = ImageGrab.grab()
            image.save("sketch.png")
            print("your sketch is saved as sketch.png!!")


        if retain:
            tu.done()



import cv2
import subprocess
import pkg_resources

class trace:
    def __init__(self, img_path, zoom=5, scale=0.25):
        """trace any image you want, with the help of this trace class\n
        USE RIGHT CLICK TO CREATE A TRACE POINT \n
        USE LEFT CLICK TO REMOVE A TRACE POINT\n
        ONCE FINISHED PRESS ANY BUTTON TO SAVE YOUR DATA\n \n
        img_path - path of the image to be traced\n
        zoom - zoom of the image\n
        scale - scale of the original image"""
        self.coordinates = []
        self.scale_x, self.scale_y = scale, scale
        self.zoom_scale_x, self.zoom_scale_y = zoom, zoom
        self.cx, self.cy = (self.zoom_scale_x * 100) // 2, (
            self.zoom_scale_y * 100
        ) // 2
        print(
            "----- USE RIGHT CLICK TO CREATE A TRACE POINT -----\n----- USE LEFT CLICK TO REMOVE A TRACE POINT -----\n----- ONCE FINISHED PRESS ANY BUTTON TO SAVE YOUR DATA -----"
        )

        img = cv2.imread(img_path)
        self.img = cv2.resize(img, (0, 0), None, self.scale_x, self.scale_y)
        self.color_li = []

    def click_event(self, event, x, y, flag, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(x, " ", y)
            self.coordinates.append((x, y))
            print(self.img[x][y])
            self.color_li.append(tuple(self.img[x][y]))
            temp = cv2.circle(
                self.img, (x, y), radius=1, color=(0, 255, 255), thickness=-1
            )
        if event == cv2.EVENT_RBUTTONDOWN:
            print(f"poping {x} and {y}")
            print(
                f"coord : {self.coordinates[-1]}\n color : {tuple(self.color_li[-1])}"
            )
            temp = cv2.circle(
                self.img,
                tuple(self.coordinates[-1]),
                radius=0,
                color=(
                    int(self.color_li[-1][0]),
                    int(self.color_li[-1][1]),
                    int(self.color_li[-1][2]),
                ),
                thickness=-1,
            )
            print(
                f"actual col {self.img[x][y]} : changed img {int(self.color_li[-1][0]),int(self.color_li[-1][1]),int(self.color_li[-1][2])}"
            )
            # print("img:",img[y,x,:])

            self.coordinates.pop()
            self.color_li.pop()
        if event == cv2.EVENT_MBUTTONDOWN:
            print("mouse wheel pressed")
            print("creating break point")
            self.coordinates.append((-1, -1))
        try:
            zoom = cv2.resize(
                self.img[y - 50 : y + 50, x - 50 : x + 50, :],
                (0, 0),
                None,
                self.zoom_scale_x,
                self.zoom_scale_y,
            )
            zoom[self.cx - 3 : self.cx + 3, self.cx - 3 : self.cx + 3, :] = 175
            cv2.imshow("zoom", zoom)
        except:
            print("out of range!!")

    def trace(self):
        cv2.imshow("Main image", self.img)
        cv2.setMouseCallback("Main image", self.click_event)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(self.coordinates)

        if len(self.coordinates) > 0:
            from os.path import exists

            file = input("enter the name the file: ")

            path_exists = exists(f"./{file}.txt")

            if path_exists:
                print(f"the file {file} already exists!!!")
                des = input("do you what to append the data: (y/n) ")
                if des == "y" or des == "Y":
                    data = open(f"{file}.txt", "a")
                    print("creating a break point and appending....")
                    data.write(str((-1, -1)) + "\n")
                    for i in self.coordinates:
                        # x,y = i
                        data.write(str(i) + "\n")
                    print(f"all the coordinates are save in {file}")
                    data.close()
                else:
                    print("deleting all the data and writing.....")
                    data = open(f"{file}.txt", "w")
                    for i in self.coordinates:
                        x, y = i
                        data.write(str(i) + "\n")
                    print(f"all the coordinates are save in {file}")
                    data.close()

            else:
                data = open(f"{file}.txt", "w")
                for i in self.coordinates:
                    x, y = i
                    data.write(str(i) + "\n")
                print(f"all the coordinates are save in {file}")
                data.close()

        else:
            print("no coordinates are detected to be saved...")

def get_svg(image_path, output_path=None):
    """Usage: \n
    from sketchpy import canvas
    canvas.get_svg()
    
    opens a local window from converting image files to svg files\n
    requires internet connection!!!"""

   

    exe_path = pkg_resources.resource_filename('sketchpy3', 'files/trace.exe')
    try:
        if output_path != None:
            subprocess.run([exe_path, image_path, output_path], shell=True)
        else:
            subprocess.run([exe_path, image_path], shell=True)

    except Exception as e:
        print("An error occurred:", e)



import multiprocessing as mp
from tqdm import tqdm
from svgpathtools import svg2paths2
from svg.path import parse_path

class color_sketch_from_svg:

    def __init__(
        self,
        path=None,
        no_of_processes = 4,
        scale=500,
        x_offset=0,
        y_offset=0,
        save=True,
    ):
        """
        path -> path of the svg file\n
        no_of_processes -> on of simultanious threads to process the SVG file faster(set it to the no of cores in the system, default value: 4)\n
        scale -> zoom value\n
        x_offset -> amount of movemnt in x direction\n
        y_offset -> amount of movemnt in y direction\n
        save -> True = take a screenshot and save it\n

        used to sketch an colored image from a svg file,  reffer my youtube channel to know more about it
        """
        self.path = path
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.scale = scale
        self.save = save
        self.no_of_processes =  no_of_processes


    def hex_to_rgb(self, string):
        strlen = len(string)
        # print(string)
        if string.startswith("#"):
            if strlen == 7:
                r = string[1:3]
                g = string[3:5]
                b = string[5:7]
            elif strlen == 4:
                r = string[1:2] * 2
                g = string[2:3] * 2
                b = string[3:4] * 2
        elif strlen == 3:
            r = string[0:1] * 2
            g = string[1:2] * 2
            b = string[2:3] * 2
        else:
            r = string[0:2]
            g = string[2:4]
            b = string[4:6]

        return int(r, 16) / 255, int(g, 16) / 255, int(b, 16) / 255

    def process(self,data, id, queue):
        try:
            for i in tqdm(data):
                path = parse_path(i["d"])
                # co = i["style"].replace("fill: ", "").replace(")", "")
                co = i["fill"]

                col = self.hex_to_rgb(co)
                transform = i["transform"].replace("translate(", "").replace(")", "")
                transform = list(map(float, transform.split(",")))
                transform = list(map(int, transform))
                n = str(path).split(" ")
                n = len(n) // 5 - 10
                if n <= 20:
                    n = 20
                pts = [
                    (
                        (int(((p.real + transform[0]) / self.width) * self.scale))
                        - self.x_offset,
                        (int(((p.imag + transform[1]) / self.height) * self.scale))
                        - self.y_offset,
                    )
                    for p in (path.point(i / n) for i in range(1, n + 1))
                ]

                queue.put((pts, col))
        except Exception as e:
            print(f"Error : {e}")  



from PIL import Image
import numpy as np

def auto_trace(image_path, output_file='auto_traced_coords.txt', threshold=100, simplify_factor=5):
    """Automatically traces an image and saves coordinates to a file.

    :param image_path: Path to the input image.
    :param output_file: Path to save the generated coordinate file.
    :param threshold: Threshold for edge detection (0-255).
    :param simplify_factor: Factor to simplify the number of points in the trace.
    """
    try:
        img = Image.open(image_path).convert('L')  # Convert to grayscale
        img_np = np.array(img)

        # Simple edge detection (e.g., Canny or just thresholding)
        # For simplicity, let's use a basic thresholding approach for now.
        # A more advanced edge detection like Canny from OpenCV would be better.
        edges = (img_np < threshold).astype(np.uint8) * 255

        # Find contours (simplified approach without OpenCV for now)
        # This part is a placeholder and needs a proper contour finding algorithm.
        # For a real implementation, OpenCV's findContours would be ideal.
        # Since OpenCV is already imported, let's use it.
        
        # Using OpenCV for edge detection and contour finding
        img_cv = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img_cv is None:
            print(f"خطأ: لا يمكن قراءة الصورة من المسار {image_path}")
            return
        
        blurred = cv2.GaussianBlur(img_cv, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150) # Canny edge detector

        contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        coordinates = []
        for contour in contours:
            if len(contour) > 1:
                # Simplify contour points
                simplified_contour = contour[::simplify_factor]
                for point in simplified_contour:
                    x, y = point[0]
                    coordinates.append((x, y))
                coordinates.append((-1, -1)) # Break point for turtle
        
        if coordinates:
            with open(output_file, 'w') as f:
                for coord in coordinates:
                    f.write(str(coord) + '\n')
            print(f"تم حفظ الإحداثيات التي تم تتبعها تلقائيًا في: {output_file}")
            return output_file
        else:
            print("لم يتم العثور على أي إحداثيات لتتبعها.")
            return None

    except Exception as e:
        print(f"حدث خطأ أثناء التتبع التلقائي: {e}")
        return None

