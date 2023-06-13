import numpy as np 
import win32gui, win32ui, win32con
import cv2 as cv 

class window_capture: 
    w = 0 
    h = 0 
    #Constructor
    def __init__(self,window_name): 


        '''window handle : win32gui.FindWindow(None, window_name) allows us to interact and manuipate the identified window
        interact and manuipate allows screenshots, sending input events, etc'''
        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window Not found {}'.format(window_name))
       
        rect = win32gui.GetClientRect(self.hwnd)
        self.w = rect[2]
        self.h = rect[3]
        
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
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (0,0), win32con.SRCCOPY) 

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
    
