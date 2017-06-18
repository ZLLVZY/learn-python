class Screen(object):
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        if value<0:
            raise ValueError('width must bigger than 0')
        else:
            self._width=value
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        if value<0:
            raise ValueError('height must bigger than 0')
        else:    
            self._height=value
        
    @property
    def resolution(self):
        self._resolution=self._width*self._height
        return self._resolution
        
s=Screen()
s.width=1024
s.height=768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution