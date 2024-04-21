from tkinter import*
from PIL import Image,ImageTk
from student import studentClass
from category import categoryClass
from supplier import supplierClass
from product import  productClass
from login import login_system
from sales import salesClass
class shu:
 def __init__(self,root):
        self.root=root
        self.root.geometry("1800x1500+0+0")
        self.root.title("Storiso")
        self.root.config(bg="white")

#===title=====
        self.icon_title=PhotoImage(file="image/logo img.png")
        title=Label(self.root,text="Storiso",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),background="#d3d3d3",fg="black",anchor="w",padx=1).place(x=0,y=0,relwidth=1,height=70)
        #==btn logout===
        #==clock===
        self.lbl_clock=Label(self.root,text="Welcome To Storiso\t\t Date:1-03-2024\t\t\ Time:12:04:10",font=("times new roman",15,"bold"),background="#ADD8E6",fg="black")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #===left menu=====
        self.Menu_logo=Image.open("image/menu_im.png")
        self.Menu_logo=self.Menu_logo.resize((200,200))
        self.Menu_logo=ImageTk.PhotoImage(self.Menu_logo)
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.Menu_logo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        
        
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#ADD8E6").pack(side=TOP,fill=X)
        btn_student=Button(LeftMenu,text="Student",command=self.student,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_categoryt=Button(LeftMenu,text="Category",command=self.category,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

      #==content======
        self.lbl_Student=Label(self.root,text="Total Student\n[0]",bd=5,relief=RIDGE,bg="#00CDCD",fg="white",font=("cooper black",20))
        self.lbl_Student.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[0]",bd=5,relief=RIDGE,bg="#00B2EE",fg="white",font=("cooper black",20))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[0]",bd=5,relief=RIDGE,bg="#1874CD",fg="white",font=("cooper black",20))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n[0]",bd=5,relief=RIDGE,bg="#1874CD",fg="white",font=("cooper black",20))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[0]",bd=5,relief=RIDGE,bg="#0000EE",fg="white",font=("cooper black",20))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

    #=====footer=====
        lbl_footer=Label(self.root,text="shu-Storiso\nfor any technical issues Contact:900xxxxx13",font=("times new roman",20,"bold"),background="#ADD8E6",fg="black").pack(side=BOTTOM,fill=X)
#========================================================================
 def student(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=studentClass(self.new_win)

 def category(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=categoryClass(self.new_win)

 def supplier(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=supplierClass(self.new_win)

 def product(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=productClass(self.new_win) 
 def login(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=login_system(self.new_win)
 def sales(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=salesClass(self.new_win) 


if __name__=="__main__":
  root=Tk()
  obj=shu(root)
  root.mainloop()

