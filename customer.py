from flask import * 
from database import*

from datetime import date



customer=Blueprint('customer',__name__)

@customer.route('/customer_home')
def customer_home():

	return render_template('customer_home.html')


@customer.route('/customer_viewproduct',methods=['post','get'])
def customer_viewproduct():
	data={}
	if "search" in request.form:
		p=request.form['product']+'%'

		q="select * FROM product  INNER JOIN `category` USING (`category_id`) INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN `color` USING (`color_id`) INNER JOIN `brand` USING (brand_id) where category_name like '%s' or subcategory_name like '%s' or product_name like '%s'"%(p,p,p)
		res=select(q)
		data['productsearch']=res
		
		

	else:

		q="select * FROM product  INNER JOIN `category` USING (`category_id`) INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN `color` USING (`color_id`) INNER JOIN `brand` USING (brand_id)"
	res=select(q)
	data['productsearch']=res
	
	return render_template('customer_viewproduct.html',data=data)


@customer.route('/customer_addtocart',methods=['post','get'])
def customer_addtocart():
	data={}
	st=request.args['stock']
	pname=request.args['pname']
	data['pname']=pname

	pdis=request.args['pdis']
	data['pdis']=pdis

	pimg=request.args['pimg']
	data['pimg']=pimg

	pamo=request.args['pamo']
	data['pamo']=pamo


	if "cart" in request.form:
		tot=request.form['total']	
		pid=request.args['pid']
		cid=session['customer_id']

		qty=request.form['quantity']	
		


		if int(st)< int(qty):
			flash('enter less quantity')
		else:


			q="select * from order_master where customer_id='%s' and order_status='pending'"%(cid)
			res=select(q)
			if res:
				omid=res[0]['order_master_id']

			else:

				q="insert into order_master values(null,'%s','0',curdate(),'pending')"%(cid)
				omid=insert(q)


			q="select * from order_details where product_id='%s' and order_master_id='%s'"%(pid,omid)
			res=select(q)
			if res:
				odid=res[0]['order_details_id']

				a=res[0]['quantity']
				qty=request.form['quantity']




				c=int(a)+int(qty)
				print(c)

				if int(c) > int(st):
					
					flash('Out Of Stock')
					return redirect(url_for('customer.customer_viewcart'))
					

				else:

		
					q="update order_details set quantity=quantity+'%s' , total_price=total_price+'%s' where order_details_id='%s'"%(qty,tot,odid)
					update(q)

			else:

				q="insert into order_details values(null,'%s','%s','%s','%s')"%(omid,pid,qty,tot)
				insert(q)

			q="update order_master set total_amount=total_amount+'%s' where order_master_id='%s'"%(tot,omid)
			update(q)

			flash('successfully')

			return redirect(url_for('customer.customer_viewcart'))

	return render_template('customer_addtocart.html',data=data)


@customer.route('/customer_viewcart',methods=['get','post'])
def customer_viewcart():
	data={}
	cid=session['customer_id']



	q="SELECT * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (customer_id) INNER JOIN `category` USING (`category_id`) INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (color_id)INNER JOIN brand USING (brand_id) where order_status='pending' and customer_id='%s'"%(cid)
	res=select(q)
	data['len']=len(res)
	data['cart']=res

	for i in range(1,len(res)+1):
		if 'btn'+str(i) in request.form:
			oid=request.form['oid'+str(i)]
			pid=request.form['pid'+str(i)]

			q="update order_master set total_amount=total_amount-(select total_price from order_details where product_id='%s' and order_master_id='%s') where order_master_id='%s'"%(pid,oid,oid)
			print(q)
			update(q)
			q="delete from order_details where order_master_id='%s' and product_id='%s'"%(oid,pid)
			delete(q)
			q=" select * from order_master where order_master_id='%s' and total_amount='0'"%(oid)
			ves=select(q)
			if ves:
				q="delete from order_master where order_master_id='%s'"%(oid)
				delete(q)


			flash('successfully')
			
			return redirect(url_for("customer.customer_viewcart"))

	return render_template('customer_viewcart.html',data=data)

@customer.route('/customer_makepayment',methods=['post','get'])	
def customer_makepayment():
	data={}
	cid=session['customer_id']

	amt=request.args['amt']
	data['amt']=amt

	q="select * from card where customer_id='%s'"%(cid)
	res=select(q)
	data['carddrop']=res
			

	if "payment" in request.form:
		ca=request.form['card']
		omid=request.args['omid']
		amt=request.args['amt']


		q="insert into payment values(null,'%s','%s','%s',curdate())"%(ca,omid,amt)
		insert(q)
		q="update order_master set order_status='Paid' where order_master_id='%s'"%(omid)
		update(q)

		q="select * from order_details where order_master_id='%s'"%(omid)
		res=select(q)

		for i in res:

			quantity=i['quantity']
			item_id=i['product_id']
			q="update product set stock=stock-'%s' where product_id='%s'"%(quantity,item_id)
			update(q)

			flash('successfully')

		return redirect(url_for('customer.customer_viewmyorder'))

	return render_template('customer_makepayment.html',data=data,amt=amt)

@customer.route('/customer_addcard',methods=['post','get'])
def customer_addcard():


	if "card" in request.form:

		cid=session['customer_id']
		num=request.form['num']
		name=request.form['name']

		d=request.form['date']

		q="select * from card where customer_id='%s' and card_no='%s'"%(cid,num)
		res=select(q)
		if res:
			flash('already exist')

		else:


			from datetime import date,datetime

			d1=datetime.strptime(d,'%Y-%m')
			print(type(d1))


			today = datetime.today()
			print("Today's date:", type(today))

			print(d,")))))))))))")

			print(today)
			if d1 < today:
				flash('expired')
			else:
				q="insert into card values(null,'%s','%s','%s','%s') "%(cid,num,name,d)
				insert(q)
				flash('successfully')
				return redirect(url_for('customer.customer_viewcart'))
	return render_template('customer_addcard.html')	

@customer.route('/customer_viewmyorder')
def customer_viewmyorder():
	data={}
	cid=session['customer_id']

	q="SELECT * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (customer_id) INNER JOIN `category` USING (`category_id`) INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (color_id)INNER JOIN brand USING (brand_id) where ( customer_id='%s' and order_status='paid')  or (customer_id='%s'  and order_status='Picked') or (customer_id='%s'  and order_status='Delivered')"%(cid,cid,cid)
	res=select(q)
	data['myorder']=res
	return render_template('customer_viewmyorder.html',data=data)


@customer.route('/customer_sendcomplaint',methods=['post','get'])	
def customer_sendcomplaint():
	data={}
	cid=session['customer_id']
	q="select * from complaint inner join customer using (customer_id) where customer_id='%s'"%(cid)
	res=select(q)
	data['complaint']=res

	if "complaints" in request.form:
		c=request.form['comp']
		q="insert into complaint values(null,'%s','%s','pending',curdate())"%(cid,c)
		insert(q)
		return redirect(url_for('customer.customer_sendcomplaint'))

	return render_template('customer_sendcomplaint.html',data=data)	
			
			
