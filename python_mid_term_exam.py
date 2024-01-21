class Star_Cinema:
    hall_list=[]
    def entry_hall(self,hall):
        self.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__ (self,rows:list,cols:list,hall_no:int):
        self.seats={}
        self.Show_list=[]
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no
        super().entry_hall(self)

    def entry_show(self,id:str,movie_name:str,time:str):
        Tuple=(id,movie_name,time)
        self.Show_list.append(Tuple)
        self.seats[id]=[[0]*self.__cols for _ in range(self.__rows)]

    def book_seats(self,id:str,row:int,col:int):
        if id not in self.seats:
            print("\n_____________________________")  
            print(f'{id} not found')
            print("______________________________\n")  
            return
        elif row>self.__rows:
            print("\n______________________________")
            print(f"invalid row{row}")
            print('_________________________________')
            return           
        elif col>self.__cols:
            print("\n______________________________")
            print(f"invalid cols{col}")
            print('_________________________________')
            return 
        elif self.seats[id][row][col] ==1:
            print("\n________________________________")
            print('seat already booked')   
            print('____________________________________\n')    
        self.seats[id][row][col] =1
    def view_show_list (self):
        for id,name ,time in self.Show_list:
            print(f'id:{id},movie_name:{name},time:{time}')

    def view_avilable_seat(self,id):
        if id not in self.seats:
            return print(f"{id}not found")
        for s in self.seats[id]:
            print(s)
        print()

hall1=Hall(5,5,1)
hall2=Hall(6,6,2)
hall1.entry_show('111','spider man','1/2/3')
hall2.entry_show('222','bat man','4/5/6')

def view_all_show_today():
    print('\n________________________')
    for hall in Star_Cinema.hall_list:
        hall.view_show_list()
    print('___________________________\n')
def view_avilable_seat():
    found=False
    show_id=input('enter show id :')
    for hall in Star_Cinema.hall_list:
        for show in hall.Show_list:
            if show[0]==show_id:
                print('\n______________________________\n')
                hall.view_avilable_seat(show_id)
                print('___________________________________\n')
                found=True
    if found==False:
        print('\n_______________________________________')
        print('show not found')
        print('_________________________________________\n')
def book_ticket():
    show_id=input('enter show id: ')
    inHall=None
    for hall in Star_Cinema.hall_list:
        for show in hall.Show_list:
            if show[0]==show_id:
                inHall=hall
    if inHall==None:
        print('\n___________________________________________')
        print(f'show not found')
        print('_______________________________________________\n')
        return
    tickets=int(input('Number of tickets: '))

    for _ in range(tickets):
        row=int(input('Enter seat row : '))
        col=int(input('Enter seat col: '))
        inHall.book_seats(show_id,row,col)
while True:
    txt='_____________________________\n1. view all show today \n2. view avilable seat\n3. Book Ticket\n4. Exit\nEnter Option below line\n'
    op=int(input(txt))
    if op==1:
        view_all_show_today()
    elif op==2:
        view_avilable_seat()
    elif op==3:
        book_ticket()
    elif op==4:
        break