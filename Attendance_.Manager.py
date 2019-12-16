import mysql.connector
from tkinter import *
from tkinter import messagebox
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="ashutosh",
  database="mydatabase"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")
#mycursor.execute("CREATE TABLE subject (name VARCHAR(255), total INT, remaining INT)")
'''mycursor.execute("Delete from subject where name='AXC'")
mydb.commit()'''
def det():
    root4=Tk()
    root4.title("Credits")
    root4['bg']='black'
    l=Label(root4,text="Information",fg='white',bg='black')
    l.place(x=60,y=0)
    t = Text(root4,font=["Times",10],bg='black',fg='white')
    t.insert(END,"This Project is a combined effort of:\n1.Sumit Bhardwaj \t N212\n"
                 "2.Ashutosh Choubey \t N217\n"
                 "3.Nitya Darshanil \t N219\n"
                 "4.Yash Gandhi \t N221\n\n"
                 "Under the guidance of:\n\n"
                 "\tProf. Dhananjay Joshi"
             )
    t.place(x=0,y=20)
    root4.mainloop()

def change(e1,e2,m,root):
    for i in range(m):
        str=(e2[i].cget("text"),e1[i].cget("text"))
        sql=f'update subject set remaining=(%s) where name=(%s)'
        mycursor.execute(sql,str)
        mydb.commit()
    root.destroy()
    home(2)
def update(a,b,c,root3):
    # update in sql and remove pass
    x = b-((c / 100) * b)
    sql = "INSERT INTO subject (name, total, remaining) VALUES (%s, %s, %s)"
    val = (a, b, x)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.execute("SELECT * FROM subject")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    root3.destroy()
    home(1)

def subject(root):
    root2 = Tk()
    root2.title('Details')
    e1=Entry(root2,width=25)
    e1.insert(0,"enter subject name")
    e1.place(x=0,y=0)
    e2=Entry(root2,width=25)
    e2.insert(0, "enter total no. of hrs")
    e3=Entry(root2,width=25)
    e3.insert(0,"enter % req.")
    b2=Button(root2,text="submit",width=10,command=lambda:update(e1.get(),int(e2.get()),int(e3.get()),root2))
    e2.place(x=0, y=50)
    e3.place(x=0, y=100)
    b2.place(x=0,y=150)
    root.destroy()
    root2.mainloop()
def home(a=0):
    def inc(j):
        val = int(e2[j].cget("text"))
        e2[j]["text"] = val + 1
    def dec(j):
        val = int(e2[j].cget("text"))
        if val>0:
            e2[j]["text"] = val - 1
    root=Tk()
    root.geometry("250x350")
    root.title("BUNK MANAGER")
    root['bg']='black'
    if(a==1):
        messagebox.showinfo(root,"Subject Added successfully")
    if (a == 2):
        messagebox.showinfo(root, "Record updated successfully")

    l1 = Label(root, width=15, text="BUNK MANAGER", bg='black', fg='white', font=['bold'])
    l1.place(x=50, y=0)
    b=Button(root,text="i",fg="blue",bg='white',font=["Times",9,'bold italic'],height=1,command=det)
    b.place(x=230,y=0)
    a=30
    b1=Button(root,width=10,text="Add subject",command=lambda:subject(root))
#fetch  info from sql
    mycursor.execute("select name from subject")
    myresult2=mycursor.fetchall()
    mycursor.execute("select remaining from subject")
    myresult3=mycursor.fetchall()
    e1=[]
    e2=[]
    b3=[]
    b4=[]
    if(len(myresult2)>0):
        l2 = Label(root, width=10, text="SUBJECT", bg='black', fg='white')
        l2.place(x=0, y=30)
        l3 = Label(root, width=10, text="CAN LEAVE", bg='black', fg='white')
        l3.place(x=90, y=30)
        l4 = Label(root, width=10, text="INC/DEC", bg='black', fg='white')
        l4.place(x=170, y=30)
        a=(len(myresult2)+3)*25
        for i in range(len(myresult2)):
            e1.append(Label(root, width=10, bg='pink', fg='blue',text=myresult2[i]))
            e1[i].place(x=0, y=(i+3)*20)
            e2.append(Label(root, width=10, bg='purple', fg='black',text=myresult3[i]))
            e2[i].place(x=90, y=(i + 3) * 20)
            b3.append(Button(root,width=1,text="-",bg='red',fg='blue',font=['arial',13],command=lambda c=i:dec(c)))
            b3[i].place(x=180,y=(i+3)*20)
            b4.append(Button(root, width=1, text="+", bg='green',fg='blue', font=['arial', 13], command=lambda c=i: inc(c)))
            b4[i].place(x=200, y=(i + 3) * 20)
        b2=Button(root,width=5,text="Update",fg='blue')
        b2['command']=lambda:change(e1,e2,len(myresult2),root)
        b2.place(x=200,y=a)
    b1.place(x=0,y=a)
    root.mainloop()
home()
