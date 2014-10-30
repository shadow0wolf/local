import copy

class Grid:
    grid = []
    
    def constructGrid2(self):
        self.constructGrid(self.x,self.y)
            
    def __init__(self , x ,y ):
        self.x = x;
        self.y = y;
        self.grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#        self.constructGrid(x,y)
            
    def constructGrid(self,x,y):                   
            grid_y = []        
            for y_ in range (0 , y) :
                grid_x = []
                for x_ in range (0,x):
                    val = input('enter element ('+str(x_) +' , '+ str(y_) +') : ')
                    grid_x.append(int(val))
                
                grid_y.append(copy.deepcopy(grid_x))
            self.grid = copy.deepcopy(grid_y)        
            
    def displayGrid(self):
        #for y in range (0 , self.y ):
        print(self.grid)

    def getAdjecentIndexForElement(self,x,y):
        lst = []
        lst2 =[]
        lst.append((x-1,y-1))
        lst.append((x,y-1))
        lst.append((x+1,y-1))
        lst.append((x-1,y))
        lst.append((x+1,y))
        lst.append((x-1,y+1))
        lst.append((x,y+1))
        lst.append((x+1,y+1))

        for l in lst:
            if(((l[0] >= 0) and (l[0] < self.x) and (l[1]>=0) and (l[1]<self.y))):
                lst2.append(l)
        return lst2

    def getAdjecentElementsForIndex(self,x,y):
        lst1 = self.getAdjecentIndexForElement(x,y)
        lst2 = []
        for i in lst1:
            x = i[0]
            y = i[1]
            element =  self.grid[y][x]
            lst2.append(element)
        return lst2
                
#x = input('enter x size : ')
#y = input('enter y size : ')
#grid = Grid(int(x),int(y))
grid = Grid(3,3)
#grid.constructGrid2()
grid.displayGrid()
k1 = 0
while(k1 != 99):
    k1 = int(input('k1:'))
    k2 = int(input('k2:'))
    print(grid.getAdjecentIndexForElement(k1,k2))
    print(grid.getAdjecentElementsForIndex(k1,k2))
    
        

    
