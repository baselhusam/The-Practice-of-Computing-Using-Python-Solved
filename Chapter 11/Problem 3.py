#Exercise 3

class TableFan(object):
    def __init__(self,speed_level, side_to_side_movement, movement_degree,manufacturer_name,cost,used):
        self.speed_level = speed_level
        self.side_to_side_movement = side_to_side_movement
        self.movement_degree = movement_degree
        self.manufacturer_name = manufacturer_name
        self.cost = cost
        self.used = used
        
    def __str__(self):
        return """The speed level: {}
                  side to side movement: {}
                  movement degree: {}
                  manufacturer name: {}
                  cost: {}
                  used: {}
                  """.format(self.speed_level,self.side_to_side_movement,self.movement_degree,self.manufacturer_name,self.cost,self.used)
                  
                  
        