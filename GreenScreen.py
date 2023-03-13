import PySimpleGUI as sg
import cv2
from ImageEditing import ChangeBrightness,ChangeSaturation,ImageSharpen,ImageFlip
from ImageFilters import OilPainting, Water , BlackAndWhite,GrayScale
'''
Requirements
    - PySimpleGUI
    - OpenCV (specifically pip install opencv-contrib-python, if error persists uninstall both opencv-contrib-python  and opencv-python(if installed) and "pip install --no-cache-dir opencv-contrib-python")

'''


def main():

    # sg.theme("Reddit")
    sg.theme("DarkBrown2")
    column = [
        sg.Column([
            [
            sg.Radio("Mask", "Radio", size=(10, 1), key="-MASK-",font=("Cascadia Code SemiBold", 12)),
            ],
            [sg.Text("Lower Threshold",font=("Cascadia Code SemiBold", 12))],
            [sg.Slider(
                (0, 255),
                # add 50 ticks to the slider
                tick_interval=0.1,                
                orientation="h",
                size=(20, 15),
                key="-RLOWER-",
            ),
            sg.Slider(
                (0, 255),
                # add 50 ticks to the slider
                tick_interval=0.1,                
                orientation="h",
                size=(20, 15),
                key="-GLOWER-",
            ),
            sg.Slider(
                (0, 255),
                tick_interval=0.1,
                orientation="h",
                size=(20, 15),
                key="-BLOWER-",
            )
            ],
            [sg.Text("Upper Threshold",font=("Cascadia Code SemiBold", 12))],
            [sg.Slider(
                (0, 255),
                # add 50 ticks to the slider
                tick_interval=0.1,                
                orientation="h",
                size=(20, 15),
                key="-RUPPER-",
            ),
            sg.Slider(
                (0, 255),
                # add 50 ticks to the slider
                tick_interval=0.1,                
                orientation="h",
                size=(20, 15),
                key="-GUPPER-",
            ),
            sg.Slider(
                (0, 255),
                tick_interval=0.1,
                orientation="h",
                size=(20, 15),
                key="-BUPPER-",
            )
            ],
            
            [sg.Button("Exit", size=(10, 1), font=("Cascadia Code SemiBold", 12))],
    ],scrollable=True,vertical_scroll_only=True,expand_y=True,expand_x=True)
]

    # Define the window layout
    layout = [
        [
        sg.Column(
            [
                [sg.Text("Image Editing", font=("Cascadia Code SemiBold", 25))],
                [sg.Image(filename="", key="-IMAGE-", size=(800, 800))]],element_justification='center')
            ]
            ,
            column
        ]

    # Create the window and show it without the plot
    
    window = sg.Window("OpenCV Integration", layout, location=(400, 0),grab_anywhere=True,resizable=True,size=(600, 1000) )

    cap = cv2.VideoCapture(0)
    # q: why is videocaptue have (0)
    # a: 0 is the default camera, if you have more than one camera you can use 1,2,3,4,5,6,7,8,9

    while True:
        event, values = window.read(timeout=20)

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        ret, frame = cap.read()

        if values["-MASK-"]:
            lower = (values["-RLOWER-"], values["-GLOWER-"], values["-BLOWER-"])
            upper = (values["-RUPPER-"], values["-GUPPER-"], values["-BUPPER-"])
            mask = cv2.inRange(frame, lower, upper)
            frame = cv2.bitwise_and(frame, frame, mask=mask)

        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)
        
    window.close()

if __name__ == "__main__":
    main()


