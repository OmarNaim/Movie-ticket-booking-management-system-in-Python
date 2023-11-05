class Hall:
    def __init__(self,rows,cols,hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self,id,movie_name,time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        self.seats[id] = [[0] * self.cols for _ in range(self.rows)]


    def book_seats(self,id,l):
        if id in self.seats:
            for i in l:
                if 1<=row<=self.rows and 1<=col<=self.cols:
                    if self.seats[id][i[0]][i[1]] == 0:
                        self.seats[id][i[0]][i[1]]= 1
                        print(f"You have booked row {row}, col {col} seat.")
                        print()
                    else:
                        print(f"Seat at row {row}, col {col} is already booked.")
                        print()
                else:
                    print("Invalid row and column number.")
                    print()
        else:
            print("Invalid Show ID.")
            print()

    def view_show_list(self):
        for i in self.show_list:
            print(i)
            print()


    def view_available_seats(self,id):
        for i in self.seats[id]:
            print(i)
        



class Star_Cinema(Hall):
    def __init__(self):
        self.hall_list = []
    def add_to_list(self,value):
        self.hall_list.append(value)


obj1 = Star_Cinema()
obj1.add_to_list(Hall(5,5,1))

obj1.hall_list[0].entry_show("111","PK","10:00")
obj1.hall_list[0].entry_show("222","DUNKI","1:00")


while(True):
    print("1.VIEW ALL SHOW TODAY")
    print("2.VIEW AVAILABLE SEATS")
    print("3.BOOK TICKET")
    print("4.EXIT")

    n = int(input())
    if(n==1):
        obj1.hall_list[0].view_show_list()
    elif(n==2):
        id = input("SHOW ID: ")
        obj1.hall_list[0].view_available_seats(id)
    elif(n==3):
        id = input("SHOW ID: ")
        row = int(input("ENTER SEAT ROW: "))
        col = int(input("ENTER SEAT COL: "))
        obj1.hall_list[0].book_seats(id,[(row,col)])
    elif(n==4):
        break
