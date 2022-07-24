#en2 is the second entry, at the very top
#en is the first and main entry
from tkinter import *
from tkinter import ttk
import math
import pyperclip

main_font=("times new roman",18)
normal="SystemButtonFace"
found_dot=False
found_expression=False
operation_count=False
def main():
	global root,style
	root=Tk()
	root.title("Calculator")
	root.resizable(0,0)
	style=ttk.Style()
	style.configure("TButton",font=main_font,background=normal)

	root.bind("1",lambda event:appear2(1))
	root.bind("2",lambda event:appear2(2))
	root.bind("3",lambda event:appear2(3))
	root.bind("4",lambda event:appear2(4))
	root.bind("5",lambda event:appear2(5))
	root.bind("6",lambda event:appear2(6))
	root.bind("7",lambda event:appear2(7))
	root.bind("8",lambda event:appear2(8))
	root.bind("9",lambda event:appear2(9))
	root.bind("0",lambda event:appear2(0))
	root.bind(".",lambda event:appear2("."))
	root.bind("<*>",lambda event:operate("*"))
	root.bind("</>",lambda event:operate("/"))
	root.bind("<+>",lambda event:operate("+"))
	root.bind("-",lambda event:operate("-"))
	root.bind("<s>",lambda event:other_funcs("square"))
	root.bind("<i>",lambda event:other_funcs("inverse"))
	root.bind("<BackSpace>",lambda event:del_one())
	root.bind("<Control-w>",lambda event:root.destroy())
	root.bind("<Return>",lambda event:equal())
	root.bind("<Delete>",lambda event:c())
	root.bind("<(>",lambda event:left_pa())
	root.bind("<)>",lambda event:right_pa())
	root.bind("<Control-n>",lambda event:loga("log"))
	root.bind("<Control-l>",lambda event:loga("log10"))
	root.bind("<Control-e>",lambda event:others())
	root.bind("<Control-v>",lambda event:paste_number())
	lala()
	root.mainloop()
def paste_number(event=0):
	enable(en)
	# get clipboard data
	the_val=pyperclip.paste()
	en.delete(0,END)
	en.insert(0,the_val)
	disable(en)	
def left_pa():
	enable(en)
	en.insert(END,"(")
	disable(en)
def right_pa():
	enable(en)
	en.insert(END,")")
	disable(en)	
def lala():
	global frame,en,mama,mama2,en2
	mama=StringVar()
	mama2=StringVar()
	frame=Frame(root)
	frame.configure(bg=normal)
	frame.grid()
	root.attributes("-topmost", True)


	main_menu=Menu(frame)
	root.configure(menu=main_menu)
	operations_menu=Menu(main_menu,tearoff=0)
	main_menu.add_cascade(menu=operations_menu,label="Other Operations")
	operations_menu.add_command(label="Log (base 10)",command=lambda:loga("log10"),accelerator="Ctrl+L")
	operations_menu.add_command(label="Ln",command=lambda:loga("log"),accelerator="Ctrl+N")
	operations_menu.add_command(label="e",command=lambda:others(),accelerator="Ctrl+E")

#--------------------------Row 0 ---------------------------------------------
	en2=Entry(frame,width=67,justify="right",font=(main_font[0],11))
	en2.grid(row=0,column=0,columnspan=5,sticky=EW)
	disable(en2)

#--------------------------Row 1 ---------------------------------------------	

	en=Entry(frame,width=50,textvariable=mama,justify="right",font=(main_font))
	en.insert(0,0)
	en.grid(row=1,column=0,columnspan=5,sticky=EW)
	disable(en)


#---------------------------Row 2 --------------------------------------------	
	square_but=ttk.Button(frame,text="√",command=lambda:other_funcs("square"))
	square_but.grid(row=2,column=0)

	c_but=ttk.Button(frame,text="C",command=c)
	c_but.grid(row=2,column=1)

	del_one_but=ttk.Button(frame,text="←",command=del_one)
	del_one_but.grid(row=2,column=2)

	divide_but=ttk.Button(frame,text="÷",command=lambda:operate("/"))
	divide_but.grid(row=2,column=3)



#----------------------------Row 3 -------------------------------------------	
	seven_but=ttk.Button(frame,text="7",command=lambda:appear2(7))
	seven_but.grid(row=3,column=0)

	eight_but=ttk.Button(frame,text="8",command=lambda:appear2(8))
	eight_but.grid(row=3,column=1)

	nine_but=ttk.Button(frame,text="9",command=lambda:appear2(9))
	nine_but.grid(row=3,column=2)

	times_but=ttk.Button(frame,text="✕",command=lambda:operate("*"))
	times_but.grid(row=3,column=3)


#-----------------------------Row 4 ------------------------------------------	
	four_but=ttk.Button(frame,text="4",command=lambda:appear2(4))
	four_but.grid(row=4,column=0)

	five_but=ttk.Button(frame,text="5",command=lambda:appear2(5))
	five_but.grid(row=4,column=1)

	six_but=ttk.Button(frame,text="6",command=lambda:appear2(6))
	six_but.grid(row=4,column=2)

	minus_but=ttk.Button(frame,text="-",command=lambda:operate("-"))
	minus_but.grid(row=4,column=3)


#-----------------------------Row 5 ------------------------------------------------
	one_but=ttk.Button(frame,text="1",command=lambda:appear2(1))
	one_but.grid(row=5,column=0)

	two_but=ttk.Button(frame,text="2",command=lambda:appear2(2))
	two_but.grid(row=5,column=1)

	three_but=ttk.Button(frame,text="3",command=lambda:appear2(3))
	three_but.grid(row=5,column=2)

	plus_but=ttk.Button(frame,text="+",command=lambda:operate("+"))
	plus_but.grid(row=5,column=3)
	

#-----------------------------Row 6 ---------------------------------------------
	inv_but=ttk.Button(frame,text="1/x",command=lambda:other_funcs("inverse"))
	inv_but.grid(row=6,column=0)	

	zero_but=ttk.Button(frame,text="0",command=lambda:appear2(0))
	zero_but.grid(row=6,column=1)

	dot_but=ttk.Button(frame,text=".",command=lambda:appear2("."))
	dot_but.grid(row=6,column=2)

	ala_but=ttk.Button(frame,text="x^y",command=lambda:operate("^"))
	ala_but.grid(row=6,column=3)

	equal_but=ttk.Button(frame,text="=",command=equal)
	equal_but.grid(row=6,column=4)


#---------------------------------Newly Added Buttons------------------------------
	plus_minus_but=ttk.Button(frame,text="±",command=lambda:other_funcs("plus_minus"))
	plus_minus_but.grid(row=2,column=4)

	x_squared_but=ttk.Button(frame,text="x²",command=lambda:other_funcs("power"))
	x_squared_but.grid(row=3,column=4)

	ce_but=ttk.Button(frame,text="CE",command=lambda:other_funcs("CE"))
	ce_but.grid(row=4,column=4)

	pi_but=ttk.Button(frame,text="π",command=lambda:other_funcs("PI"))
	pi_but.grid(row=5,column=4)
#------------------------------Functions------------------------------------------	
def other_funcs(op):
	try:
		global found_expression,res
		if en.get()=="Error" and op=="CE":
			enable(en)
			en.delete(0,END)
			en.insert(0,0)
			disable(en)
			return
		elif en.get()=="Error":
			return	
		if op=="square":
			if float(en.get())<0:
				err()
			else:	
				res=float(en.get())**0.5
		elif op=="inverse":
			res=1/float(en.get())
		elif op=="PI":
			enable(en)
			en.delete(0,END)
			en.insert(END,"π")
			disable(en)
			return	
		elif op=="CE":
			if en.get()=="0":
				return
			enable(en)
			en.delete(0,END)
			en.insert(0,0)
			disable(en)
			return
		elif op=="power":
			res=float(en.get())**2
			enable(en)
			en.delete(0,END)
			en.insert(0,res)
			disable(en)	
		elif op=="plus_minus":
			first_char=en.get()[:1]
			if first_char!="-":
				enable(en)
				en.insert(0,"-")
				disable(en)
				return
			else:
				newy=en.get()[1:]
				enable(en)
				en.delete(0,END)
				en.insert(0,newy)
				disable(en)
				return	
		found_expression=True
		check_zero(res)
	except Exception as e:
		err()
		return		
def check_zero(the_thing):						
	determi=str(the_thing)
	determining=determi[-2:]
	if determining==".0":
		enable(en)
		en.delete(0,END)
		en.insert(0,int(the_thing))
		disable(en)
	else:
		enable(en)
		en.delete(0,END)
		en.insert(0,the_thing)
		disable(en)		
def c():
	enable(en)
	enable(en2)
	en.delete(0,END)
	en2.delete(0,END)
	en.insert(0,0)
	disable(en)
	disable(en2)
def del_one():
	if en.get()=="0" or en.get()=="Error":
		return
	if len(en.get())==1:
		enable(en)
		en.delete(0,END)
		en.insert(0,0)
		disable(en)
		return		
	enable(en)
	en.delete(len(en.get())-1)
	disable(en)
def operate(exp):
	try:
		global found_dot,found_expression,operation_count
		found_dot=False
		value=mama.get()

		last=en2.get()[-1:]
		ac_num=en2.get()[:-1]
		if en.get()==ac_num:
			if last in("-","/","+","*","^"):
				enable(en2)
				en2.delete(len(en2.get())-1)
				en2.insert(END,exp)
				disable(en2)
				return
			else:
				err()
				return
		if value!=0:
			equal()
			found_expression=True
			enable(en2)
			en2.insert(END,str(res)+str(exp))
			disable(en2)
		else:
			found_expression=True
			enable(en2)
			en2.insert(END,value+exp)
			disable(en2)
	except NameError:
		err()
		return		
def equal():
	global found_dot,res,found_expression
	found_dot=False
	found_expression=True
	true_one=en2.get()
	sh=[]
	sh2=[]
	for i in true_one:
		if i=="^":
			i="**"	
		sh.append(i)	
	blabla="".join(sh)	
	for i in en.get():
		if i=="π":
			i=math.pi
		sh2.append(str(i))	
	bloblo="".join(sh2)		
	try:
		res=eval(str(blabla)+str(bloblo))
		print("Result: {0}".format(res))
	except:
		err()
		return
	enable(en2)
	enable(en)
	en2.delete(0,END)
	en.delete(0,END)		
	two_chara=str(res)
	two_act=two_chara[-2:]
	if two_act==".0":	
		en.insert(0,int(res))
	else:
		en.insert(0,res)	
	disable(en)	
	disable(en2)
def loga(tipo,event=0):
	global found_expression
	enable(en2)
	enable(en)
	ola=en.get()
	print(ola)
	try:
		if tipo=="log":
			gal=math.log(float(en.get())) #ln
		elif tipo=="log10":	
			gal=math.log10(float(en.get())) #log base 10
		check_zero(gal)	
	except:	
		err()
		return
	en2.delete(0,END)
	en.delete(0,END)	
	en.insert(0,gal)	
	disable(en2)
	disable(en)
	found_expression=True
def others():
	enable(en)
	en.delete(0,END)
	en.insert(0,math.e)
	disable(en)	


def err():
	enable(en)
	enable(en2)
	en.delete(0,END)
	en2.delete(0,END)
	en.insert(0,"Error")
	disable(en)
	disable(en2)
	return
def enable(a):
	a.configure(state=NORMAL)
def disable(b):
	b.configure(state="readonly")	
def appear2(y):
	global found_expression,found_dot
			
	for i in en.get():
		if i==".":
			found_dot=True		
	if found_dot:
		if y==".":
			return	
	if en.get()=="Error" or en.get()=="0":
		if not y==".":	
			enable(en)
			en.delete(0,END)
			disable(en)	


	#Here begins the nightmare :(
	if found_expression:
		enable(en)
		en.delete(0,END)
		en.insert(END,y)
		disable(en)
		found_expression=False
		found_dot=False
	else:
		enable(en)
		en.insert(END,y)
		disable(en)

if __name__=="__main__":
	main()