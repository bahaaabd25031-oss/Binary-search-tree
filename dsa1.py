from collections import deque

class node:
    def __init__(self ,data=None):
        self.__data = data
        self.left = None
        self.right = None


    def insert(self,data):
        if self.__data is None:
            print('  root')
            self.__data = data
            
        elif (data <= self.__data):
            print('  left')
            if self.left is None:
                self.left = node(data)
            else:
                self.left.insert(data)

        else:
            print('  right')
            if self.right is None:
                self.right = node(data)
            else:
                self.right.insert(data)


    def count_left(self):
        if self.left is None:
            return 0
        else:
            left = self.left.count_left()
            right = self.left.count_right()
            total_count = left + right + 1
            return total_count


    def count_right(self):
        if self.right is None:
            return 0
        else:
            left = self.right.count_left()
            right = self.right.count_right()
            total_count = 1 + left + right
            return total_count

    
    def count_total(self):
        if self.__data is None:
            return 0
        return 1 + self.count_left() + self.count_right() 


    def search(self,target):
        if self.__data is None:
            print('not found')
            return
        elif target == self.__data:
            print('found')
            return
        elif target < self.__data:
            if self.left is None:
                print('not found')
                return
            self.left.search(target)
        else:
            if self.right is None:
                print('not found')
                return
            self.right.search(target)


    def display_depth(self,type='dlr'):
        if type == 'dlr':
            print(self.__data)
            
            if self.left is not None:
                self.left.display_depth(type)
                
            if self.right is not None:
                self.right.display_depth(type)
                
        elif type == 'ldr':
            if self.left is not None:
                self.left.display_depth(type) 
                           
            print(self.__data)
            
            if self.right is not None:
                self.right.display_depth(type)
                
        elif type == 'lrd':
            if self.left is not None:
                self.left.display_depth(type)
                
            if self.right is not None:
                self.right.display_depth(type)  
                          
            print(self.__data)
            
        else:
            print('Incorrect type.')
    
    
    def display_breadth(self):
        print('display breadth:')
        if self.__data is None:
            print('The tree is empty.')
            return
        
        queue = deque([self])
        while queue:
            current = queue.popleft()
            print(current.__data)
            if current.left is not None:    
                queue.append(current.left)
            if current.right is not None:    
                queue.append(current.right)

  
tree = node()
print(tree.count_total())
for i in range(7):
    value = float(input('value: '))
    tree.insert(value)
tree.display_depth(type='ldr')
tree.display_breadth()
print('left: ' + str(tree.count_left()))
print('right: ' + str(tree.count_right()))
print('total: ' + str(tree.count_total()))
tree.search(float(input('target: ')))
