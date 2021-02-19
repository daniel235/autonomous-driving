'''

Send inputs to dqn and model.  
create view object


'''

class carView():
    def __init__(self):
        self.left_view = None
        self.right_view = None
        self.front_view = None


    def set_car_view(self, left, front, right):
        self.left_view = left
        self.front_view = front
        self.right_view = right


    def get_car_view(self):
        return self.left_view, self.right_view, self.front_view

    
    
    
 


    
