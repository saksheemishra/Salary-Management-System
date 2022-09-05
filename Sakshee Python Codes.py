import time
import datetime
from tkinter import *
import tkinter.messagebox 

borderr = 8

root=Tk()
root.title("Employee payroll system")
root.geometry('1300x600+0+0')
root.configure(background="blue")

Tops=Frame(root,width=1000,height=10,bd=8,bg="blue")
Tops.pack(side=TOP)

f1=Frame(root,width=600,height=400,bd=8,bg="blue")
f1.pack(side=LEFT)
f2=Frame(root,width=300,height=400,bd=8,bg="blue")
f2.pack(side=RIGHT)

fla=Frame(f1,width=600,height=160,bd=8,bg="blue")
fla.pack(side=TOP)
flb=Frame(f1,width=300,height=400,bd=8,bg="blue")
flb.pack(side=TOP)

lblinfo=Label(Tops,font=('arial',20,'bold'),text="Employee Management system ",bd=10,fg="white",bg="blue")
lblinfo.grid(row=0,column=0)

def exit():
  exit=tkinter.messagebox.askyesno("Employee system","Do you want to exit the system")
  if exit>0:
    root.destroy()
    return

def reset():
  Name.set("")
  Address.set("")
  HoursWorked.set("")
  wageshour.set("")
  Payable.set("")
  Taxable.set("")
  NetPayable.set("")
  GrossPayable.set("")
  OverTimeBonus.set("")
  Employer.set("")
  NINumber.set("")
  txtpayslip.delete("1.0",END)
def enterinfo():
  txtpayslip.delete("1.0",END)
  txtpayslip.insert(END,"\t\tPay Slip\n\n")
  txtpayslip.insert(END,"Name :\t\t"+Name.get()+"\n\n")
  txtpayslip.insert(END,"Address :\t\t"+Address.get()+"\n\n")
  txtpayslip.insert(END,"Employer :\t\t"+Employer.get()+"\n\n")
  txtpayslip.insert(END,"Number :\t\t"+NINumber.get()+"\n\n")
  txtpayslip.insert(END,"Designation :\t\t"+something4.get()+"\n\n")
  txtpayslip.insert(END,"Date of Joining :\t\t"+something3.get()+"\n\n")
  txtpayslip.insert(END,"Company ID :\t\t"+something5.get()+"\n\n")
  txtpayslip.insert(END,"Company Tel :\t\t"+something6.get()+"\n\n")
  txtpayslip.insert(END,"Miscellaneous :\t\t"+something1.get()+"\n\n")
  txtpayslip.insert(END,"Travel Allowance :\t\t"+something2.get()+"\n\n")
  txtpayslip.insert(END,"Hours Worked :\t\t"+HoursWorked.get()+"\n\n")
  txtpayslip.insert(END,"Net Payable :\t\t"+NetPayable.get()+"\n\n")
  txtpayslip.insert(END,"Wages per hour :\t\t"+wageshour.get()+"\n\n")
  txtpayslip.insert(END,"Tax Paid :\t\t"+Taxable.get()+"\n\n")
  txtpayslip.insert(END,"Payable :\t\t"+Payable.get()+"\n\n") 
def weeklywages():
  txtpayslip.delete("1.0",END)
  hoursworkedperweek=float(HoursWorked.get())
  wagesperhours=float(wageshour.get())
  
  paydue=wagesperhours*hoursworkedperweek
  paymentdue="INR",str('%.2f'%(paydue))
  Payable.set(paymentdue)
  
  tax=paydue*0.2
  taxable="INR",str('%.2f'%(tax))
  Taxable.set(taxable)
  
  netpay=paydue-tax
  netpays="INR",str('%.2f'%(netpay))
  NetPayable.set(netpays)
  
  if hoursworkedperweek > 40:
    overtimehours=(hoursworkedperweek-40)+wagesperhours*1.5
    overtime="INR",str('%.2f'%(overtimehours))
    OverTimeBonus.set(overtime)
  elif hoursworkedperweek<=40:
    overtimepay=(hoursworkedperweek-40)+wagesperhours*1.5
    overtimehrs="INR",str('%.2f'%(overtimepay))
    OverTimeBonus.set(overtimehrs)  
  return  
    
#=============================== Variables ========================================================
Name=StringVar()
Address=StringVar()
HoursWorked=StringVar()
wageshour=StringVar()
Payable=StringVar()
Taxable=StringVar()
NetPayable=StringVar()
GrossPayable=StringVar()
OverTimeBonus=StringVar()
Employer=StringVar()
NINumber=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()
something1=StringVar()
something2=StringVar()
something3=StringVar()
something4=StringVar()
something5=StringVar()
something6=StringVar()

DateOfOrder.set(time.strftime("%d/%m/%Y"))

#================================ Label Widget =================================================

lblName=Label(fla,text="Full Name",font=('arial',12,'bold'),bd=16,fg="white",bg="blue").grid(row=0,column=0)
lblAddress=Label(fla,text="Address",font=('arial',12,'bold'),bd=16,fg="white",bg="blue").grid(row=0,column=2)
lblEmployer=Label(fla,text="Employer ID",font=('arial',12,'bold'),bd=16,fg="white",bg="blue").grid(row=1,column=0)
lblNINumber=Label(fla,text="Contact Number",font=('arial',12,'bold'),bd=16,fg="white",bg="blue").grid(row=1,column=2)
lblHoursWorked=Label(fla,text="Hours Worked",font=('arial',12,'bold'),bd=16,fg="white",bg="blue").grid(row=2,column=0)
lblHourlyRate=Label(fla,text="Hourly Rate",font=('arial',12,'bold'),bd=16,fg="white",bg="blue").grid(row=2,column=2)
lblTax=Label(fla,text="Tax",font=('arial',12,'bold'),bd=16,anchor='w',fg="white",bg="blue").grid(row=3,column=0)
lblOverTime=Label(fla,text="Over Time",font=('arial',12,'bold'),bd=16,fg="white",bg="blue").grid(row=3,column=2)
lblGrossPay=Label(fla,text="Gross Pay",font=('arial',12,'bold'),bd=16,fg="white",bg="blue").grid(row=4,column=0)
lblNetPay=Label(fla,text="Net Pay",font=('arial',12,'bold'),bd=16,fg="white",bg="blue").grid(row=4,column=2)

lblNetPay=Label(fla,text="Travel Allowance",font=('arial',12,'bold'),bd=16,fg="white",bg="blue").grid(row=5,column=0)
lblNetPay=Label(fla,text="Miscellaneous",font=('arial',12,'bold'),bd=16,fg="white",bg="blue").grid(row=5,column=2)
lblNetPay=Label(fla,text="Date of Joining",font=('arial',12,'bold'),bd=16,fg="white",bg="blue").grid(row=6,column=0)
lblNetPay=Label(fla,text="Designation",font=('arial',12,'bold'),bd=16,fg="white",bg="blue").grid(row=6,column=2)
lblNetPay=Label(fla,text="Company ID",font=('arial',12,'bold'),bd=16,fg="white",bg="blue").grid(row=7,column=0)
lblNetPay=Label(fla,text="Company Tel.",font=('arial',12,'bold'),bd=16,fg="white",bg="blue").grid(row=7,column=2)

#=============================== Entry Widget =================================================


etxname=Entry(fla,textvariable=Name,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxname.grid(row=0,column=1)

etxaddress=Entry(fla,textvariable=Address,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxaddress.grid(row=0,column=3)

etxemployer=Entry(fla,textvariable=Employer,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxemployer.grid(row=1,column=1)

etxhoursworked=Entry(fla,textvariable=HoursWorked,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxhoursworked.grid(row=2,column=1)

etxwagesperhours=Entry(fla,textvariable=wageshour,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxwagesperhours.grid(row=2,column=3)

etxnin=Entry(fla,textvariable=NINumber,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxnin.grid(row=1,column=3)

etxgrosspay=Entry(fla,textvariable=Payable,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxgrosspay.grid(row=4,column=1)

etxnetpay=Entry(fla,textvariable=NetPayable,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxnetpay.grid(row=4,column=3)

etxtax=Entry(fla,textvariable=Taxable,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxtax.grid(row=3,column=1)

etxovertime=Entry(fla,textvariable=OverTimeBonus,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxovertime.grid(row=3,column=3)

etxsomething1=Entry(fla,textvariable=something1,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxsomething1.grid(row=5,column=1)

etxsomething2=Entry(fla,textvariable=something2,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxsomething2.grid(row=5,column=3)


etxsomething3=Entry(fla,textvariable=something3,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxsomething3.grid(row=6,column=1)

etxsomething4=Entry(fla,textvariable=something4,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxsomething4.grid(row=6,column=3)

etxsomething5=Entry(fla,textvariable=something5,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxsomething5.grid(row=7,column=1)

etxsomething6=Entry(fla,textvariable=something6,font=('arial',12,'bold'),bd=borderr,width=22,justify='left')
etxsomething6.grid(row=7,column=3)
#=============================== Text Widget ============================================================

payslip=Label(f2,textvariable=DateOfOrder,font=('arial',15,'bold'),fg="white",bg="blue").grid(row=0,column=0)
txtpayslip=Text(f2,height=35,width=50,bd=borderr,font=('arial',8,'bold'),fg="white",bg="blue")
txtpayslip.grid(row=1,column=0)

#=============================== buttons ===============================================================

btnsalary=Button(flb,text='Weekly Salary',padx=16,pady=16,bd=8,font=('arial',12,'bold'),width=14,fg="white",bg="blue",command=weeklywages).grid(row=0,column=0)

btnreset=Button(flb,text='Reset',padx=16,pady=16,bd=8,font=('arial',12,'bold'),width=14,command=reset,fg="white",bg="blue").grid(row=0,column=1)

btnpayslip=Button(flb,text='View Payslip',padx=16,pady=16,bd=8,font=('arial',12,'bold'),width=14,command=enterinfo,fg="white",bg="blue").grid(row=0,column=2)

btnexit=Button(flb,text='Exit System',padx=16,pady=16,bd=8,font=('arial',12,'bold'),width=14,command=exit,fg="white",bg="blue").grid(row=0,column=3)

root.mainloop()