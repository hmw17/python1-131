class Base:
    def init(self, x, y, size):
# TODO: will need to fill this in
        self.x = x
        self.y = y
        self.size = size
#
    def draw(self):
        return ""
class Circle(Base):
    def init(self,x, y, size):
        super().init(x,y,size)
    def draw(self):
        return f"""
({self.x}, {self.y})
{self.size}
        , - ~ ~ ~ - ,
    , '               ' ,
  ,                      ,
 ,                        ,
,                          ,
,                          ,
,                          ,
 ,                        ,
  ,                      ,
    ,                 , '
      ' - ,   _ , '
"""
class Square(Base):
    def init(self, x, y, size):
        super().init(x,y,size)
    def draw(self):
        return f"""
({self.x}, {self.y})
{self.size}
--------------------
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
--------------------
"""
# All of the code below is correct
def draw_any_shape(myShape):
    print(myShape.draw())
def main():
    s = Square(1,2,3)
    draw_any_shape(s)
    c = Circle(2,2,1)
    draw_any_shape(c)
main()