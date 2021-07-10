from tkinter import *
import mysql.connector
import tkinter as ttk
import tkinter.ttk as tkrttk
import os
import random
import tkinter.messagebox
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Sarvo@123456",database="ansdep")
mycur=mydb.cursor()
root=Tk()
root.geometry("1366x768")
root.title("ans department")
#creating treeview
tree = tkrttk.Treeview(root,height=17)
#tree.pack(side=ttk.BOTTOM,fill=ttk.X)
tree.place(x=0,y=450)
tree2 = tkrttk.Treeview(root,height=17)
tree2.place(x=600,y=450)



        #creating labeles

heading = Label(root, text="Operation Theatre Inventory Management System", font=("arial 30 bold"),fg='steelblue')
heading.place(x=150,y=0)
heading2 = Label(root, text="Sarvodaya Hospital and Research Centre", font=("arial 30 bold"),fg='steelblue')
heading2.place(x=250,y=60)
cat_l = Label(root, text="GRN No", font=("arial 20 bold"),fg='steelblue')
cat_l.place(x=50,y=150)
name_l = Label(root, text="Name of instrument", font=("arial 20 bold"),fg='steelblue')
name_l.place(x=50,y=200)
date_l = Label(root, text="Date of entry", font=("arial 20 bold"),fg='steelblue')
date_l.place(x=50,y=250)
number_l = Label(root, text="Initial number of units", font=("arial 20 bold"),fg='steelblue')
number_l.place(x=50,y=300)
inven_l = Label(root, text="Inventory table", font=("arial 20 bold"),fg='steelblue')
inven_l.place(x=50,y=400)
inst_l = Label(root, text="Instrument table", font=("arial 20 bold"),fg='steelblue')
inst_l.place(x=650,y=400)
yrmnday_l = Label(root, text="y  y  y  y  m  m  d  d", font=("arial 10 bold"),fg='steelblue')
yrmnday_l.place(x=400,y=230)
datefortab_l = Label(root, text="Date of entry", font=("arial 20 bold"),fg='red')
datefortab_l.place(x=900,y=150)
addedfortab_l = Label(root, text="Issued", font=("arial 20 bold"),fg='red')
addedfortab_l.place(x=900,y=200)
subfortab_l = Label(root, text="Charged off", font=("arial 20 bold"),fg='red')
subfortab_l.place(x=900,y=250)
discfortab_l = Label(root, text="Description", font=("arial 20 bold"),fg='red')
discfortab_l.place(x=900,y=300)
yrmnday2_l = Label(root, text="y  y  y  y  m  m  d  d", font=("arial 10 bold"),fg='steelblue')
yrmnday2_l.place(x=1100,y=130)



        #varibales for entry
cat_var=StringVar()
name_var=StringVar()
date_var=StringVar()
number_var=StringVar()
datefortab_var=StringVar()
addedfortab_var=IntVar()
subfortab_var=IntVar()
discfortab_var=StringVar()
        #creating entries for labels
cat_e = Entry(root,width=25, font=("arial 20 bold"),textvariable=cat_var)
cat_e.place(x=400, y=150)

name_e = Entry(root, width=25, font=("arial 20 bold"),textvariable=name_var)
name_e.place(x=400, y=200)

date_e = Entry(root, width=25, font=("arial 20 bold"),textvariable=date_var)
date_e.place(x=400, y=250)

number_e = Entry(root, width=25, font=("arial 20 bold"),textvariable=number_var)
number_e.place(x=400, y=300)

datefortab_e = Entry(root, width=15, font=("arial 20 bold"),textvariable=datefortab_var)
datefortab_e.place(x=1100, y=150)

addedfortab_e = Entry(root, width=15, font=("arial 20 bold"),textvariable=addedfortab_var)
addedfortab_e.place(x=1100, y=200)

subfortab_e = Entry(root, width=15, font=("arial 20 bold"),textvariable=subfortab_var)
subfortab_e.place(x=1100, y=250)

discfortab_e = Entry(root, width=15, font=("arial 20 bold"),textvariable=discfortab_var)
discfortab_e.place(x=1100, y=300)

        #def buttons
def show_inventory():
            #global mycur
            #display.delete(0, display.size())
            #display.insert(END, "date         name     cno  amt1")
            #mycur.execute("select * from inven")
            #result2 = mycur.fetchall()
            #c = len(result2)
            #for i in range(c):
                #display.insert(END, result2[i])

            #tree = tkrttk.Treeview(root,height=17)
            #tree.pack(side=ttk.BOTTOM,fill=ttk.X)

            mycur.execute("select * from inven")
            result1 = mycur.fetchall()
            c = len(result1)
            for j in tree.get_children():
                tree.delete(j)
            for i in range(c):

                tree.insert("",i,text=f"{i+1}",values =(f"{result1[i][0]}",f"{result1[i][1]}",f"{result1[i][2]}",f"{result1[i][3]}"))



def add_to_invent1():
            global mycur
            catpatno1=cat_var.get()
            dateentry1=date_var.get()
            nameenntry1=name_var.get()
            numentry1=number_var.get()
            if catpatno1=="":
                tkinter.messagebox.showerror("error","GRN number entry box can not be empty")
            else:
            #mycur.execute(f"create table {self.cat_var.get()}(date_of_entry date,amt_added int,amt_decresed int,reason varchar(20),total int")
                try:
                    mycur.execute(f"insert into inven value({dateentry1},'{nameenntry1}','{catpatno1}',{numentry1})")
                    mydb.commit()
                    mycur.execute(f"create table c{catpatno1} ( dateofentry date  , amount_added int , amount_sub int ,reason varchar(200), total int)")
                    mydb.commit()
                    mycur.execute(f"insert into c{catpatno1} values({dateentry1},{numentry1},0,'first_entry',{numentry1})")
                    mydb.commit()
                #display.delete(0, display.size())
                #display.insert(END, "date         name     cno  amt")
                    mycur.execute("select * from inven")
                    result2 = mycur.fetchall()
                    c = len(result2)
                    for j in tree.get_children():
                        tree.delete(j)
                    for i in range(c):
                        tree.insert("", i, text=f"{i + 1}",values=(f"{result2[i][0]}", f"{result2[i][1]}", f"{result2[i][2]}", f"{result2[i][3]}"))
                    mydb.commit()
                    #saveing in backup
                    catpat7 = cat_var.get()
                    mycur.execute(f"select name_of_instrument from inven where cat_pat_no = '{catpat7}'")
                    nameofinst = mycur.fetchall()
                    t = nameofinst[0][0]
                    mycur.execute(f"select * from c{catpat7}")
                    result9 = mycur.fetchall()
                    c = len(result9)
                    docs1 = "D:/ans management software/database/backup/" + f"{catpat7}" + "/"
                    if not os.path.exists(docs1):
                        os.makedirs(docs1)
                    # template for saved docs
                    name = "\t\t\t\t\tSarvodaya Hospital and Research Center\n"
                    pur = "\t\t\t\t\tOperation Theatre Inventory Management \n"
                    tabel = f"\t\t{catpat7}\t{nameofinst[0][0]}\n"
                    header = "\n\n\n\t\t\n\t\tDate\tIssued\tCharged off\tDescription\tBalance\n"
                    final = name + pur + tabel + header
                    # writing into file
                    file_name = str(docs1) + f"{nameofinst[0][0]}" + ".xls"
                    f = open(file_name, 'w')
                    f.write(final)
                    for x in range(c):
                        f.write("\t\t" + str(result9[x][0]))
                        f.write("\t" + str(result9[x][1]))
                        f.write("\t" + str(result9[x][2]))
                        f.write("\t" + str(result9[x][3]))
                        f.write("\t" + str(result9[x][4]) + "\n")
                    f.close()

                except Exception as e:
                    error=str(e)
                    if error==f"1062 (23000): Duplicate entry '{catpatno1}' for key 'inven.PRIMARY'":
                        tkinter.messagebox.showerror("error","this GRN number already exists")
                    elif error==f"1292 (22007): Incorrect date value: '{dateentry1}' for column 'date_of_entry' at row 1":
                        tkinter.messagebox.showerror("error", "Invalid Date format\nCorrect format eg: 19 July 2000 =20000719")
                    else:
                        print(e)
                        tkinter.messagebox.showerror("error", f"Initial number of units entry box can not be empty ")
def show_table():
    catpatno2 = cat_var.get()
    dateentry2 = date_var.get()
    nameenntry2 = name_var.get()
    numentry2 = number_var.get()
    #display.delete(0, display.size())
    #display.insert(1,"date          add sub reason  total ")
    try:
        mycur.execute(f"select * from c{catpatno2}")
        result3 = mycur.fetchall()
        c = len(result3)
        for j in tree2.get_children():
            tree2.delete(j)
        for i in range(c):
            tree2.insert("", i, text=f"{i + 1}",values=(f"{result3[i][0]}", f"{result3[i][1]}", f"{result3[i][2]}", f"{result3[i][3]}",f"{result3[i][4]}"))
    except Exception:
        tkinter.messagebox.showerror("error", "Invalid GRN no")
def search_cat():
    #display.delete(0, display.size())
    #display.insert(END, "date         name     cno  amt")
    catpatno3 = cat_var.get()
    try:
        mycur.execute(f"select * from inven where cat_pat_no like '{catpatno3}%'")
        result4 = mycur.fetchall()
        c = len(result4)
        for j in tree.get_children():
            tree.delete(j)
        for i in range(c):
            tree.insert("", i, text=f"{i + 1}",values=(f"{result4[i][0]}", f"{result4[i][1]}", f"{result4[i][2]}", f"{result4[i][3]}"))
    except Exception:
        tkinter.messagebox.showerror("error", "invalid cat pat no")
def search_name():
    #display.delete(0, display.size())
    #display.insert(END, "date         name     cno  amt")
    catpatno4 = cat_var.get()
    nameenntry4 = name_var.get()
    mycur.execute(f"select * from inven where name_of_instrument like '{nameenntry4}%'")
    result5 = mycur.fetchall()
    c = len(result5)
    for j in tree.get_children():
        tree.delete(j)
    for i in range(c):
        tree.insert("", i, text=f"{i + 1}",values=(f"{result5[i][0]}", f"{result5[i][1]}", f"{result5[i][2]}", f"{result5[i][3]}"))
def del_tab():
    #display.delete(0, display.size())
    #display.insert(END, "date         name     cno  amt")
    try:
        catpatno5 = cat_var.get()
        nameenntry5 = name_var.get()
        mycur.execute(f"delete from inven where cat_pat_no='{catpatno5}'")
        mydb.commit()
        mycur.execute(f"drop table c{catpatno5}")
        mydb.commit()
        mycur.execute("select * from inven")
        result6 = mycur.fetchall()
        c = len(result6)
        for j in tree.get_children():
            tree.delete(j)
        for i in range(c):
            tree.insert("", i, text=f"{i + 1}",values=(f"{result6[i][0]}", f"{result6[i][1]}", f"{result6[i][2]}", f"{result6[i][3]}"))
        mydb.commit()
    except Exception:
        tkinter.messagebox.showerror("error", "Invalid GRN no")


def update():
    datefortable=datefortab_var.get()
    added=addedfortab_var.get()
    sub=subfortab_var.get()
    disc=discfortab_var.get()
    catpat6=cat_var.get()
    #importing the number of inst before updation
    try:
        mycur.execute(f"select number_of_units from inven where cat_pat_no ='{catpat6}'")
        pretotal=mycur.fetchall()
        total=pretotal[0][0]
        ntotal=total+added-sub
        print(ntotal)
        mycur.execute(f"insert into c{catpat6} values ({datefortable},{added},{sub},'{disc}',{ntotal})")
        mydb.commit()
        mycur.execute(f"update inven set number_of_units={ntotal} where cat_pat_no={catpat6}")
        mydb.commit()
        #setting values in tree
        mycur.execute(f"select * from c{catpat6}")
        result7 = mycur.fetchall()
        c = len(result7)
        for j in tree2.get_children():
            tree2.delete(j)
        for i in range(c):
            tree2.insert("", i, text=f"{i + 1}",values=(f"{result7[i][0]}", f"{result7[i][1]}", f"{result7[i][2]}", f"{result7[i][3]}",f"{result7[i][4]}"))
        mycur.execute("select * from inven")
        result8 = mycur.fetchall()
        c = len(result8)
        for j in tree.get_children():
            tree.delete(j)
        for i in range(c):
            tree.insert("", i, text=f"{i + 1}",values=(f"{result8[i][0]}", f"{result8[i][1]}", f"{result8[i][2]}", f"{result8[i][3]}"))
        mydb.commit()
        #saving in backup
        catpat7 = cat_var.get()
        mycur.execute(f"select name_of_instrument from inven where cat_pat_no = '{catpat7}'")
        nameofinst = mycur.fetchall()
        t = nameofinst[0][0]
        mycur.execute(f"select * from c{catpat7}")
        result9 = mycur.fetchall()
        c = len(result9)
        docs = "D:/ans management software/database/backup/" + f"{catpat7}" + "/"
        if not os.path.exists(docs):
            os.makedirs(docs)
        # template for saved docs
        name = "\t\t\t\t\tSarvodaya Hospital and Reasearch Center\n"
        pur = "\t\t\t\t\tOperation Theatre Inventory Management\n"
        tabel = f"\t\t{catpat7}\t{nameofinst[0][0]}\n"
        header = "\n\n\n\t\t\n\t\tDate\tIssued\tCharged off\tDescription\tBalance\n"
        final = name + pur + tabel + header
        # writing into file
        file_name = str(docs) + f"{nameofinst[0][0]}" + ".xls"
        f = open(file_name, 'w')
        f.write(final)
        for x in range(c):
            f.write("\t\t" + str(result9[x][0]))
            f.write("\t" + str(result9[x][1]))
            f.write("\t" + str(result9[x][2]))
            f.write("\t" + str(result9[x][3]))
            f.write("\t" + str(result9[x][4]) + "\n")
        f.close()
    except Exception as e1:
        error1 = str(e1)
        if error1 == f"1292 (22007): Incorrect date value: '{datefortable}' for column 'dateofentry' at row 1":
            tkinter.messagebox.showerror("error", "Invalid Date format\nCorrect format eg: 19 July 2000 =20000719")
        else:
            tkinter.messagebox.showerror("error", "invalid entries,check GRN no")
            print(e1)

def save():
    try:
        catpat7 = cat_var.get()
        mycur.execute(f"select name_of_instrument from inven where cat_pat_no = '{catpat7}'")
        nameofinst=mycur.fetchall()
        t=nameofinst[0][0]
        mycur.execute(f"select * from c{catpat7}")
        result9 = mycur.fetchall()
        c=len(result9)
        docs="D:/ans management software/database/" + f"{catpat7}" +"/"
        if not os.path.exists(docs):
            os.makedirs(docs)
        #template for saved docs
        name="\t\t\t\t\tSarvodaya Hospital and Research Center\n"
        pur="\t\t\t\t\tOperation Theatre Inventory Management \n"
        tabel=f"\t\t{catpat7}\t{nameofinst[0][0]}\n"
        header="\n\n\n\t\t\n\t\tDate\tIssued\tCharged off\tDescription\tBalance\n"
        final=name+pur+tabel+header
        #writing into file
        file_name=str(docs)+ f"{nameofinst[0][0]}"+".xls"
        f=open(file_name,'w')
        f.write(final)
        for x in range(c):

            f.write("\t\t" + str(result9[x][0]))
            f.write("\t" + str(result9[x][1]))
            f.write("\t" + str(result9[x][2]))
            f.write("\t" + str(result9[x][3]))
            f.write("\t" + str(result9[x][4])+"\n")
        f.close()
    except Exception:
        tkinter.messagebox.showerror("error","Invalid Catpat no")

def save2():

    mycur.execute(f"select * from inven")
    result9 = mycur.fetchall()
    c = len(result9)
    docs = "D:/ans management software/database/" + f"Inventory" + "/"
    if not os.path.exists(docs):
        os.makedirs(docs)
    # template for saved docs
    name = "\t\t\t\t\tSarvodaya Hospital and Research Center\n"
    pur = "\t\t\t\t\tOperation Theatre Inventory Management \n"
    tabel = f"\t\t\t\t\tInventory\n"
    header = "\n\n\n\t\t\n\t\tDate\tName\tGRN NO\tBalance\n"
    final = name + pur + tabel + header
    # writing into file
    file_name = str(docs) + f" Latest" + ".xls"
    f = open(file_name, 'w')
    f.write(final)
    for x in range(c):
        f.write("\t\t" + str(result9[x][0]))
        f.write("\t" + str(result9[x][1]))
        f.write("\t" + str(result9[x][2]))

        f.write("\t" + str(result9[x][3]) + "\n")
    f.close()


        #creating buttons

search_b=Button(root,text="Search",padx=10,pady=5,font=("arial 10 bold"),bg='white',command=search_cat)
search_b.place(x=800,y=150)

search2_b=Button(root,text="Search",padx=10,pady=5,font=("arial 10 bold"),bg='white',command=search_name)
search2_b.place(x=800,y=200)

show_b = Button(root, text="Show table", padx=10, pady=5, font=("arial 10 bold"), bg='white',command=show_table)
show_b.place(x=200, y=350)

show_inven_b = Button(root, text="Show inventory", padx=10, pady=5, font=("arial 10 bold"), bg='white',command=show_inventory)
show_inven_b.place(x=400, y=350)

add_b = Button(root, text="Add to inventory", padx=10, pady=5, font=("arial 10 bold"), bg='white',command=add_to_invent1)
add_b.place(x=600, y=350)

delete_b = Button(root, text="Delete table", padx=10, pady=5, font=("arial 10 bold"), bg='white',command=del_tab)
delete_b.place(x=800, y=350)

update_b = Button(root, text="Update table", padx=10, pady=5, font=("arial 10 bold"), bg='red',command=update)
update_b.place(x=1000, y=350)

save_b=Button(root, text="Save table", padx=10, pady=5, font=("arial 10 bold"), bg='red',command=save)
save_b.place(x=1000, y=400)

save2_b=Button(root, text="Save Inventory", padx=10, pady=5, font=("arial 10 bold"), bg='white',command=save2)
save2_b.place(x=400, y=400)

        #making the display area
#display=Listbox(root,width=100,height=10,font=("arial 15 bold"),bg='white')
#display.place(x=75,y=400)
        #display config
#display.insert(END,"date         name     cno  amt")
#mycur.execute("select * from inven")
#result = mycur.fetchall()
#c=len(result)
#for i in range(c):
            #display.insert(END, result[i])
tree["columns"]=("c2","c3","c4","c5")

tree.column("#0",width=110,minwidth=25)
tree.column("c2", width=110, minwidth=25)
tree.column("c3", width=110, minwidth=25)
tree.column("c4", width=110, minwidth=25)
tree.column("c5", width=110, minwidth=25)

tree.heading("#0", text="Sno", anchor=ttk.CENTER)
tree.heading("c2", text="Date", anchor=ttk.CENTER)
tree.heading("c3", text="Name", anchor=ttk.CENTER)
tree.heading("c4", text="GRN", anchor=ttk.CENTER)
tree.heading("c5", text="Amount", anchor=ttk.CENTER)
mycur.execute("select * from inven")
result = mycur.fetchall()
c = len(result)
for j in tree.get_children():
    tree.delete(j)
for i in range(c):

    tree.insert("",i,text=f"{i+1}",values =(f"{result[i][0]}",f"{result[i][1]}",f"{result[i][2]}",f"{result[i][3]}"))
tree2["columns"]=("c2","c3","c4","c5","c6")

tree2.column("#0",width=90,minwidth=25)
tree2.column("c2", width=90, minwidth=25)
tree2.column("c3", width=100, minwidth=25)
tree2.column("c4", width=130, minwidth=25)
tree2.column("c5", width=150, minwidth=25)
tree2.column("c6", width=90, minwidth=25)


tree2.heading("#0", text="Sno", anchor=ttk.CENTER)
tree2.heading("c2", text="Date", anchor=ttk.CENTER)
tree2.heading("c3", text="Issued", anchor=ttk.CENTER)
tree2.heading("c4", text="Charged off", anchor=ttk.CENTER)
tree2.heading("c5", text="Description", anchor=ttk.CENTER)
tree2.heading("c6", text="Total", anchor=ttk.CENTER)









#l=StringVar()
#label=Label(root,text="Anesthesia departmen inventory management system",font=("arial 40 bold"),fg='steelblue').pack()
#label1=Label(root,text="cat").pack()
#e=Entry(root,width=5,textvar=l).pack()
#label2=Label(root,text="name").pack()
#e2=Entry(root,width=8,textvar=m).pack()
#lbx = Listbox(root)
#lbx.pack()
#mycur.execute("show tables")
#result = mycur.fetchall()
#c=len(result)
#for i in range(c):
    #lbx.insert(END, result[i])
def bitti():
    entry1=l.get()
    entry2=m.get()
    mycur.execute(f"create table {entry1}_{entry2}(sno int , dateofentry date  , amount_added int , amount_sub int , total int)")
    lbx.insert(END, f"{entry1}_{entry2}")

def deletebt():
    entry1 = l.get()
    entry2 = m.get()
    lbx.delete(0,lbx.size())

    mycur.execute(f"drop table {entry1}_{entry2}")
    mycur.execute("show tables")
    result2 = mycur.fetchall()
    lol = len(result2)
    for i in range(0,lol):
        lbx.insert(END, result2[i])


#em=Button(root,text="delete",command=deletebt).pack()
#el=Button(root,text="add",command=bitti).pack()
#display1 = Listbox(root).pack()
#display1.insert(END,"lol")
mydb.commit()
root.mainloop()
mydb.close()
