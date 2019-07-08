# B_R_R
# M_S_A_W



"""
Coding Problem using Magic Method:
We can use magic methods to define how operators like +, -, *, /, ==, >, <, etc. will work with our
custom objects
"""



class MyTime:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour=hour
        self.minute=minute
        self.second=second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute,self.second)

    def __add__(self, other_time):
        new_time=MyTime()

        if (self.second+other_time.second)>=60:
            self.minute+=1
            new_time.second=(self.second+other_time.second)-60
        else:
            new_time.second=self.second-other_time.second


        if (self.minute+other_time.minute)>=60:
            self.hour+=1
            new_time.minute=(self.minute+other_time.minute)-60
        else:
            new_time.minute=self.minute-other_time.minute


        if (self.hour+other_time.hour)>24:

            new_time.hour=(self.hour+other_time.hour)-24
        else:
            new_time.hour=self.hour+other_time.hour

        return new_time


def main():
    time1=MyTime(1, 20, 45)
    print(time1)
    time2=MyTime(24,41,15)
    print(time2)
    print(time1+time2)

main()
