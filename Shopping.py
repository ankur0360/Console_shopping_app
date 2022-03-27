#user id    = Ankur
#user pass  = 1234
#admin id   = Ankur
#admin pass = 4321

print('\t\t\t****************DEVELOPED BY ANKUR***************\n\n')
print('\t\t\t****************WELCOME TO APNA SHOP*************\n\n')
print("WELCOME TO DASHBOARD\n\n")
def dash():
	print('If you want to close the app type [Ctrl+c]\n\n')
	inpt=input("If you are a Admin type [Admin].\nIf you are a User type [User].\n")
	inpt=inpt.lower()
	if (inpt=='admin'):
		ad_pass()
	elif (inpt=='user'):
		user()
	else:
		print("Select Correctly.")
		dash()
		
#
def logout():
	print('Rdirecting to Dashboard.')
	dash()

def p_log():
	print('\n\n**********If you want to logout type [logout]**********\n\n')
	
def back():
	print('\n\n****If you want to go back menu type [exit]******\n\n')
#
a='Ankur'
b='1234'
def user():
	p_log()
	usrid=input("Enter your USER ID : ")
	pwd=input("Enter your PASS : ")
	if (usrid==a and pwd==b):
		catagory()
	elif (usrid=='logout' or pwd=='logout'):
		logout()
	else:
		print("Enter correct user id and password.")
		user()
#		
elec_rs=[50,999,200,15,300,30]
elec_name=['fan','mobile','t.v','light','ipad','earphone']
elec_stock=[20,20,20,20,20,20]
qua_elec=0
def browse():
	print('\n\n\nThere are some Recommendation : ',elec_name,sep="\n")
	p_log()
	back()
	br=input('Please type Which you want to buy : ')
	br=br.lower()
	if (br=='logout' or br=='log out'):
			logout()
	elif (br=='exit'):
			catagory()
	if br not in elec_name:
		print('There is no item like',br,'As soon As possible we will get this stock','\n\nRedirecting to Main menu.')
		browse()
	qua_elec=int(input('Enter your quantity : '))
	for x in range(0,len(elec_name)):
		if elec_name[x]==br and elec_stock[x]>=qua_elec:
			for x in range(0,len(elec_name)):
				if (br==elec_name[x]):
					print('The',elec_name[x],' price is',elec_rs[x],'$ for qantity 1.')
					conform()
					elec_stock[x]-=qua_elec
					print("Subtotal =",elec_rs[x]*qua_elec,'$')
					thank()
	for x in range(0,len(elec_name)):
		if elec_name[x]==br and elec_stock[x]<qua_elec:
			print('OUT OF STOCK !, we have only',elec_stock[x],'stocks')
			browse()
#		
def conform():
	cnf=input('\n\nAre you sure to CONFIRM your order then type [Yes] or Cancel your order type [No] : ')
	cnf=cnf.lower()
	if (cnf=='yes'):
		print('Your order is SUCCESSFULLY placed .')
		bill()
	elif (cnf=='no'):
		print('Redirecting to Menu.')
		catagory()
	else:
		print('Please type correctly')
		conform()
#
def bill():
	print('\n\n*****Your bill is here*****\n')
#
def thank():
	print('Thank you for buy our product Sir',a,'\n\nContinue shoping\n')
	cp=input('Type [yes] or [no] : ' )
	cp=cp.lower()
	if (cp=='yes'):
		catagory()
	elif (cp=='no'):
		print('Have a Good day Sir.')
		dash()
	else: 
		print('Please type correctly')
#	
def catagory():
	p_log()
	print('Press [1] for ELECTRONICS Press [2] for GROCERY Press [3] for CLOTHING \n\n')
	cho=input('Please type which catagory is your favourite :')
	if cho=='1':
		browse()
	elif cho=='2':
		grocery()
	elif cho=='3':
		cloth()
	elif cho=='logout' or cho=='log out':
		logout()
	else:
		print('please type correctly')
		catagory()
#		
grcy=['banana','apple','kiwi','orange','lemon']
rupees=[30,5,10,25,70]
grcy_stock=[20,20,20,20,20]
qua_groc=0
def grocery():
	print('\n\n\nThere are some Recommendation : ',grcy,sep="\n")	
	p_log()
	back()
	gro=input('Please type Which you want to buy : ')
	gro=gro.lower()
	if (gro=='logout' or gro=='log out'):
			logout()
	elif (gro=='exit'):
			catagory()
	if gro not in grcy:
		for i in range(0,len(grcy)):
			print('There is no item like',gro,'As soon As possible we will get this stock','\n\nRedirecting to Main menu.')
			grocery()	
	qua_groc=int(input('Enter your qyantity : '))
	for i in range(0,len(grcy)):
		if grcy[i]==gro and grcy_stock[i]>=qua_groc:
			for i in range(0,len(grcy)):
				if (gro==grcy[i]):
					print('The',grcy[i],' price is',rupees[i],'$ for 1kg.')
					conform()
					grcy_stock[i]-=qua_groc
					print('Subtotal =',rupees[i]*qua_groc,'$')
					thank()
	for i in range(0,len(grcy)):
		if grcy[i]==gro and grcy_stock[i]<qua_groc:
			print('OUT OF STOCK !, we have only',grcy_stock[i],'stocks')
			grocery()
#
cloth_rs=[20,15,50,40,99]
cloth_name=['lowers','boxer','shirt','t-shirt','jeans']
cloth_stock=[20,20,20,20,20]
qua_cloth=0
def cloth():
	print('\n\n\nThere are some Recommendation : ',cloth_name,sep="\n")	
	p_log()
	back()
	clo=input('Please type Which you want to buy : ')
	clo=clo.lower()
	if (clo=='logout' or clo=='log out'):
			logout()
	elif (clo=='exit'):
			catagory()
	if clo not in cloth_name:
		print('There is no item like',clo,'As soon As possible we will get this stock','\n\nRedirecting to Main menu.')
		cloth()
	qua_cloth=int(input('Enter your quantity : '))
	for z in range(0,len(cloth_name)):
		if cloth_name[z]==clo and cloth_stock[z]>=qua_cloth:
			for z in range(0,len(cloth_name)):
				if (clo==cloth_name[z]):
					print('The',cloth_name[z],'price is =',cloth_rs[z],'$ for quantity 1')
					conform()
					cloth_stock[z]-=qua_cloth
					print('Subtotal =',cloth_rs[z]*qua_cloth,'$')
					thank()
	for z in range(0,len(cloth_name)):
		if cloth_name[z]==clo and cloth_stock[z]<qua_cloth:
			print('OUT OF STOCK !, we have only',cloth_stock[z],'stocks')
			cloth()
#
c='Ankur'
d='4321'
def ad_pass():
	p_log()
	adid=input("Enter your ADMIN ID : ")
	pas=input("Enter your PASS : ")
	if (adid==c and pas==d):
		doit()
	elif (adid=='logout' or pas=='logout'):
		logout()
	else:
		print("Enter correct ADMIN ID and PASSWORD.")
		ad_pass()
#
def doit():
	p_log()
	desi=input('If you want to REMOVE press[1] or for ADDITION press[2] or for MANAGE STOCK press[3] : ')
	if desi=='1':
		rmvb()
	elif desi=='2':
		admin()
	elif desi=='3':
		showstc()
	elif desi=='logout':
		logout()
	else:
		print('Please type correctly')
		doit()
#	
def admin():
	p_log()
	back()
	mng=input('If you want to manage type [Grocery] or [Clothing] or [Electronics]: ')
	mng=mng.lower()
	if (mng=='grocery'):
		grcymng=int(input('How many items you want to add : '))
		for i in range(len(grcy),grcymng+len(grcy)):
			count=input('Enter Name : ')
			count=count.lower()
			pr_grc=int(input('Enter price : '))
			stc_grc=int(input('Enter Stock : '))
			grcy.append(count)
			rupees.append(pr_grc)
			grcy_stock.append(stc_grc)
		print('SUCCESSFUL')
	elif (mng=='clothing'):
		clthmng=int(input('How many items you want to add : '))
		for i in range(len(cloth_name),clthmng+len(cloth_name)):
			inpt=input('Enter Name : ')
			inpt=inpt.lower()
			pr_clth=int(input('Enter price : '))
			stc_cloth=int(input('Enter Stock : '))
			cloth_name.append(inpt)
			cloth_rs.append(pr_clth)
			cloth_stock.append(stc_cloth)
		print('SUCCESSFUL')
	elif (mng=='electronics'):
		elecmng=int(input('How many items you want to add : '))
		for i in range(len(elec_name),elecmng+len(elec_name)):
			inpelec=input('Enter Name : ')
			inpelec=inpelec.lower()
			pr_elec=int(input('Enter price : '))
			stc_elec=int(input('Enter Stock : '))
			elec_name.append(inpelec)
			elec_rs.append(pr_elec)
			elec_stock.append(stc_elec)
		print('SUCCESSFUL')
	elif mng=='exit':
		doit()
	elif (mng=='logout'):
		logout()
	admin()
#
def rmvb():
	p_log()
	back()
	enter=input('Press [1] for ELECTRONICS Press [2] for GROCERY Press [3] for CLOTHING : ')
	if enter=='1':
		for p in range(0,len(elec_name)):
			print(p+1,elec_name[p])
		rmv=int(input('Please type the SERIAL NUMBER to repalce the item : '))
		if (rmv<=len(elec_name)):
			elec_name.pop(rmv-1)	
			elec_rs.pop(rmv-1)
			print('SUCCESSFULLY REMOVED')
			rmvb()
		else:
			print('Number out of BOUNDARY .')
			rmvb()
	elif enter=='2':
		for p in range(0,len(grcy)):
			print(p+1,grcy[p])
		rmv_grc=int(input('Please type the SERIAL NUMBER to repalce the item : '))
		if (rmv_grc<=len(elec_name)):
			grcy.pop(rmv_grc-1)	
			rupees.pop(rmv_grc-1)
			print('SUCCESSFULLY REMOVED')
			rmvb()
		else:
			print('Number out of BOUNDARY .')
			rmvb()
	elif enter=='3':
		for p in range(0,len(cloth_name)):
			print(p+1,cloth_name[p])
		rmv_clt=int(input('Please type the SERIAL NUMBER to repalce the item : '))
		if (rmv_clt<=len(cloth_name)):
			cloth_name.pop(rmv_clt-1)	
			cloth_rs.pop(rmv_clt-1)
			print('SUCCESSFULLY REMOVED')
			rmvb()
		else:
			print('Number out of BOUNDARY .')
			rmvb()
	elif enter=='logout':
		logout()
	elif enter=='exit':
		doit()
	else:
		print('Please select proper number')
		rmvb()
#
def showstc():
	p_log()
	back()
	print('Please press which stock you want to manage.\n\n')
	shw=input('Press [1] for ELECTRONICS Press [2] for GROCERY Press [3] for CLOTHING : ')
	if shw=='1':
		for p in range(0,len(elec_name)):
			print(p+1,'Stock = ',elec_stock[p],'Items = ',elec_name[p])
		stc_mng=int(input('Please the SERIAL NUMBER to manage the stock : '))
		if stc_mng<=len(elec_stock):
			stc_value=int(input('Enter the stock : '))	
			elec_stock[stc_mng-1]=stc_value
			print('\nSUCCESSFULLY MANAGED\n')
			showstc()
		else:
			print('You type out of BOUNDARY')
			showstc()
	elif shw=='2':
		for p in range(0,len(grcy)):
			print(p+1,'Stock =',grcy_stock[p],'Items =',grcy[p])
		stc_mngry=int(input('Please enter the SERIAL NUMBER to manage the stock : '))
		if stc_mngry<=len(grcy_stock):
			stc_valgry=int(input('Enter the stock : '))
			grcy_stock[stc_mngry-1]=stc_valgry
			print('\nSUCCESSFULLY MANAGED\n')
			showstc()
		else:
			print('You type out of BOUNDARY')
			showstc()
	elif shw=='3':
		for p in range(0,len(cloth_name)):
			print(p+1,'Stock =',cloth_stock[p],'Items =',cloth_name[p])
		stc_mngcl=int(input('Please enter the SERIAL NUMBER to manage the stock : '))
		if stc_mngcl<=len(cloth_stock):
			stc_valcl=int(input('Enter the stock : '))
			cloth_stock[stc_mngcl-1]=stc_valcl
			print('\nSUCCESSFULLY MANAGED\n')
			showstc()
		else:
			print('You type out of BOUNDARY')
			showstc()
		
	elif shw=='exit':
		doit()
	elif shw=='logout':
		logout()
	else:
		print('Please type CORRECTLY')
#
dash()
print('*************** THANK YOU TO USE OUR APPLICATION ***************')
