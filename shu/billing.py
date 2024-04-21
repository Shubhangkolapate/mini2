from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class BillClass:
 def __init__(self,root):
        self.root=root
        self.root.geometry("1800x1500+0+0")
        self.root.title("Storiso")
        self.root.config(bg="white")

#===title=====
        self.icon_title=PhotoImage(file="image/logo img.png")
        title=Label(self.root,text="Storiso",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),background="#d3d3d3",fg="black",anchor="w",padx=1).place(x=0,y=0,relwidth=1,height=70)

#==========================================
         #==btn logout===
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="sky blue").place(x=1350,y=10,height=50,width=150)
        #==clock===
        self.lbl_clock=Label(self.root,text="Welcome To Storiso\t\t Date:1-03-2024\t\t\ Time:hh:mm:ss",font=("times new roman",15,"bold"),background="#ADD8E6",fg="black")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
#===============prduct frame=========================
        self.var_search=StringVar()
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTtile=Label(ProductFrame1,text="All Products",font=("times new roman",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
#============product search frame==============
        self.var_search=StringVar()
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(ProductFrame2,text="Search Product| by name",font=("times new roman",15,"bold"),bg="#FFFFFF",fg="Black").place(x=2,y=5)

        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=5,y=45)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,text="Product Name",font=("times new roman",15),bg="lightblue").place(x=135,y=47,width=150,height=22)
        
        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("times new roman",15),bg="#2196f3",fg="white",cursor="hand2").place(x=290,y=45,width=100,height=25)

        btn_show_all=Button(ProductFrame2,text="Show All",font=("times new roman",15),bg="blue",fg="white",cursor="hand2").place(x=290,y=10,width=100,height=25)

#============product  details==============================
        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=388)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(ProductFrame3,columns=("pid","Name","price","qty","status"),xscrollcommand=scrollx.set) 
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        self.productTable.heading("pid",text="PID")
        self.productTable.heading("Name",text="Name")
        self.productTable.heading("price",text="price")
        self.productTable.heading("qty",text="QTY")
        self.productTable.heading("status",text="Status")
        
        self.productTable["show"]="headings"
        self.productTable.column("pid",width=40)
        self.productTable.column("Name",width=100)
        self.productTable.column("price",width=100)
        self.productTable.column("qty",width=40)
        self.productTable.column("status",width=90)
        self.productTable.pack(fill=BOTH,expand=1)
        #self.productTable.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(ProductFrame1,text="Note:'Enter 0 qty to remove the product from cart'",font=("times new roman",10),anchor="w",bg="white",fg="black").pack(side=BOTTOM,fill=X)


#==============student(customer frame)===============================
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        self.var_search=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)
        cTitle=Label(CustomerFrame,text="Student Details",font=("times new roman",15,"bold"),bg="lightgray",fg="white").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name:",font=("times new roman",15),bg="#FFFFFF").place(x=5,y=35)
        txt_nme=Entry(CustomerFrame,textvariable=self.var_cname,text="Name",font=("times new roman",15),bg="lightblue").place(x=70,y=35,width=180)

        lbl_name=Label(CustomerFrame,text="Contact No.",font=("times new roman",15),bg="#FFFFFF").place(x=260,y=35)
        txt_nme=Entry(CustomerFrame,textvariable=self.var_contact,text="Contact",font=("times new roman",15),bg="lightblue").place(x=360,y=35,width=160)

#==============cal_art framme=============================
        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)
#===========calculator frame=====================
        self.var_cal_input=StringVar()

        Cal_Frame=Frame(Cal_Cart_Frame,bd=18,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)


        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=("times new roman",15,"bold"),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(Cal_Frame,text='7',font=("times new roman",14,"bold"),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text='8',font=("times new roman",14,"bold"),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text='9',font=("times new roman",14,"bold"),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text='+',font=("times new roman",14,"bold"),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)
        
        btn_4=Button(Cal_Frame,text='4',font=("times new roman",14,"bold"),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text='5',font=("times new roman",14,"bold"),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text='6',font=("times new roman",14,"bold"),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text='-',font=("times new roman",14,"bold"),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)
        
        btn_1=Button(Cal_Frame,text='1',font=("times new roman",14,"bold"),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text='2',font=("times new roman",14,"bold"),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text='3',font=("times new roman",14,"bold"),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_multiply=Button(Cal_Frame,text='*',font=("times new roman",12,"bold"),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)
 
        btn_0=Button(Cal_Frame,text='0',font=("times new roman",14,"bold"),command=lambda:self.get_input(0),bd=5,width=4,pady=10,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text='c',font=("times new roman",14,"bold"),command=self.clear_cal,bd=5,width=4,pady=10,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text='=',font=("times new roman",14,"bold"),command=self.perform_cal,bd=5,width=4,pady=10,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text='/',font=("times new roman",14,"bold"),command=lambda:self.get_input('/'),bd=5,width=4,pady=10,cursor="hand2").grid(row=4,column=3)

      #=====cart frame===========================
        Cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        Cart_Frame.place(x=280,y=8,width=245,height=342)
        cartTitle=Label(Cart_Frame,text="Cart \t Total Product:[0]",font=("times new roman",15,"bold"),bg="lightgray",fg="black").pack(side=TOP,fill=X)


        scrolly=Scrollbar(Cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Cart_Frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(Cart_Frame,columns=("pid","Name","price","qty","status"),xscrollcommand=scrollx.set) 
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("Name",text="Name")
        self.CartTable.heading("price",text="price")
        self.CartTable.heading("qty",text="QTY")
        self.CartTable.heading("status",text="Status")
        
        self.CartTable["show"]="headings"
        self.CartTable.column("pid",width=40)
        self.CartTable.column("Name",width=100)
        self.CartTable.column("price",width=90)
        self.CartTable.column("qty",width=40)
        self.CartTable.column("status",width=100)
        self.CartTable.pack(fill=BOTH,expand=1)
        #self.CartTable.bind("<ButtonRelease-1>",self.get_data)
        
        #===========ADD cart widgets frame============================
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
       
        Add_CartWidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=420,y=550,width=530,height=110)

        lbl_p_name=Label(Add_CartWidgetsFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_name=Label(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),bg="lightblue").place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Add_CartWidgetsFrame,text="Price per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Label(Add_CartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),bg="lightblue").place(x=230,y=35,width=150,height=22)

        lbl_p_qty=Label(Add_CartWidgetsFrame,text="Qantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg="lightblue").place(x=390,y=35,width=130,height=22)

        self.lbl_inStock=Label(Add_CartWidgetsFrame,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)
       
        btn_clear_cart=Button(Add_CartWidgetsFrame,text="Clear",font=("time new roman",12,"bold"),bg="lightblue",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Add_CartWidgetsFrame,text="Add | update Cart",font=("time new roman",12,"bold"),bg="blue",cursor="hand2").place(x=340,y=70,width=180,height=30)

#================Billing frame=========================
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billFrame.place(x=953,y=110,width=550,height=410)

        bTtile=Label(billFrame,text="Customer Bill Area",font=("times new roman",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

#================billing buttons=======================
        billMenu=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billMenu.place(x=953,y=520,width=550,height=140)

        self.lbl_amnt=Label(billMenu,text="Bill Amount\n[0]",font=("times new roman\n[0]",14,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=120,height=70)

        self.lbl_netpay=Label(billMenu,text="NetPay\n[0]",font=("times new roman\n[0]",14,"bold"),bg="blue",fg="white")
        self.lbl_netpay.place(x=130,y=5,width=160,height=70)

        btn_print=Button(billMenu,text="Print",font=("times new roman\n[0]",14,"bold"),bg="#3f51b5",fg="white")
        btn_print.place(x=300,y=5,width=120,height=70)

        btn_clear_all=Button(billMenu,text="Clear All",cursor="hand2",font=("times new roman\n[0]",14,"bold"),bg="blue",fg="white")
        btn_clear_all.place(x=425,y=5,width=120,height=70)

        btn_generate=Button(billMenu,text="Generate/Save Bill",cursor="hand2",font=("times new roman\n[0]",13,"bold"),bg="#008B8B",fg="white")
        btn_generate.place(x=2,y=76,width=160,height=70)

        self.show()
#=============================All Functions=============
 def get_input(self,num):
    xnum=self.var_cal_input.get()+str(num)
    self.var_cal_input.set(xnum)
 def clear_cal(self):
    self.var_cal_input.set('')
 def perform_cal(self):
    result=self.var_cal_input.get()
    self.var_cal_input.set(eval(result))
 def show(self):
         con=sqlite3.connect(database=r'shu.db')
         cur=con.cursor()
         try:
             cur.execute("select ID,Name,price,qty,status from product")
             rows=cur.fetchall()
             self.productTable.delete(*self.productTable.get_children())
             for row in rows:
                 self.productTable.insert('',END,values=row)
         except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
 def search(self):
        con=sqlite3.connect(database=r'shu.db')
        cur=con.cursor()
        try:
             if self.var_search.get()=="":
               messagebox.showerror("error","select search input should be required",parent=self.root)
             else:
                 cur.execute("select * from product where name LIKE '%"+self.var_search.get()+"%'")
                 rows=cur.fetchall()
                 if len(rows)!=0:
                  self.productTable.delete(*self.productTable.get_children())
                  for row in rows:
                   self.productTable.insert('',END,values=row)
                 else:
                     messagebox.showerror("Error","No record found!!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


 
if __name__=="__main__":
  root=Tk()
  obj=BillClass(root)
  root.mainloop()