import numpy as np 
import win32gui, win32ui, win32con
import cv2

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
        self.w = 1920
        self.h = 1080 
        

    def screenshot(self): 
        #Creating handle 
        wDC = win32gui.GetWindowDC(self.hwnd)
        'creating device context obj allows us manipulate various operation like coordinate location'
        dcObj = win32ui.CreateDCFromHandle(wDC)


        #[white]}
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
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
    
