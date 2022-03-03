#Exercise 13

class Attendee(object):
    
    def __init__(self,people=0):
        self.people = people
        
    def join(self):
        self.people +=  1
        return "Welcome to meeting \nNumber of people in the meeting is: {}".format(self.people)
    
    def leave(self):
        self.people -=  1
        

meet = Attendee()

print(meet.join())  #1
print(meet.join())  #2
print(meet.join())  #3
print(meet.leave()) #2
print(meet.join())  #3
print(meet.join())  #4
print(meet.join())  #5
print(meet.leave()) #4
print(meet.leave()) #3
print(meet.join())  #4