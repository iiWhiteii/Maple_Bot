import numpy as np 
import win32gui, win32ui, win32con

class window_capture: 
    #properties
    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    def __init__(self,window_name = None): 

        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else: 
            '''window handle : win32gui.FindWindow(None, window_name) allows us to interact and manuipate the identified window
             interact and manuipate allows screenshots, sending input events, etc'''
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception('Window Not found {}'.format(window_name))



        # get the Window Size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        # Account for the window border and titlebar and cut them off
        border_pixels = 8 
        titlebar_pixels = 30 
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels 

        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels 

        self.offset_x = window_rect[0] + self.cropped_x 
        self.offset_y = window_rect[1] + self.cropped_y


        
    #Method
    def screenshot(self): 
        #Creating handle 
        wDC = win32gui.GetWindowDC(self.hwnd)
        'creating device context OBJECT allows us manipulate various operation like coordinate location'
        dcObj = win32ui.CreateDCFromHandle(wDC)
        'creating a compatible device context tells youre creating oringal dc obj with same attribute and setting'
        cDC = dcObj.CreateCompatibleDC() 
        # This create Bitmap Obj
        dataBitMap = win32ui.CreateBitmap()
        #CreateCompatibileBitmap method alows a compatible bitmap with specified device context 'dcObj' and has dimensions with w and heights a
        #allows us to perform graphical operation
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        #any drawing or painting operations perform on cDc will impact databitMap
        cDC.SelectObject(dataBitMap) 
        '''Is like taking a snapshot of an image (dcObj) pasting it onto a canvas (cDC) at the position (0,0).'''
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (self.cropped_x,self.cropped_y), win32con.SRCCOPY) 

        signedIntsArray = dataBitMap.GetBitmapBits(True)
       

        img = np.fromstring(signedIntsArray, dtype= 'uint8')
        img.shape = (self.h,self.w,4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())  

        img = img[...,:3]


        return img  
    

    ### For now these two code in the bottom not important

    '''@staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)


    def get_screen_position(self,pos): 
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)'''
    
