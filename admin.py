from flask import * 
from database import*
import uuid



admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():

	return render_template('admin_home.html')
@admin.route('/admin_managestaff',methods=['post','get'])
def admin_managestaff():
	data={}
	q="select * from staff inner join login using (username)"
	res=select(q)
	
	data['staffview']=res

	if "action" in request.args:
		action=request.args['action']
		uid=request.args['uid']

		if action=='active':
			q="update login set `status`='1' where username='%s'"%(uid)
			update(q)
			q="update staff set `staff_status`='1' where username='%s'"%(uid)
			update(q)
			flash('successfully')
			return redirect(url_for('admin.admin_managestaff'))
		
		if action=='inactive':
			q="update login set `status`='0' where username='%s'"%(uid)
			update(q)
			q="update staff set `staff_status`='0' where username='%s'"%(uid)
			update(q)
			flash('successfully')
			return redirect(url_for('admin.admin_managestaff'))


		if action=='update':
			q="select * from staff where username='%s'"%(uid)
			res=select(q)
			data['staffupdate']=res

		if "update" in request.form:
			f=request.form['fname']
			l=request.form['lname']
			g=request.form['gen']
			d=request.form['date']
			h=request.form['hno']
			s=request.form['street']
			di=request.form['district']
			st=request.form['state']
			p=request.form['pin']
			n=request.form['num']
			e=request.form['email']
			q="update staff set staff_fname='%s',staff_lname='%s',staff_gender='%s',staff_dob='%s',staff_house_name='%s',staff_street='%s',staff_dist='%s',staff_state='%s',staff_pincode='%s',staff_phone='%s',staff_email='%s' where username='%s'"%(f,l,g,d,h,s,di,st,p,n,e,uid)
			update(q)
			flash('successfully')
			print(q)

			return redirect(url_for('admin.admin_managestaff'))
	

	if "staffreg" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		g=request.form['gen']
		d=request.form['date']
		h=request.form['hno']
		s=request.form['street']
		di=request.form['district']
		st=request.form['state']
		p=request.form['pin']
		n=request.form['num']
		e=request.form['email']
		u=request.form['uname']
		pa=request.form['pwd']
		q="insert into login values('%s','%s','staff','1')"%(u,pa)
		insert(q)
		q="insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','1')"%(u,f,l,g,d,h,s,di,st,p,n,e)
		insert(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managestaff'))


	return render_template('admin_managestaff.html',data=data)


@admin.route('/admin_managevendor',methods=['post','get'])	
def admin_managevendor():
	data={}
	q="select * from vendor"
	res=select(q)
	data['vendorview']=res


	if "action" in request.args:
		action=request.args['action']
		vid=request.args['vid']

	else:
		action=None

	if action=='inactive':
		q="update vendor set vendor_status='0' where vendor_id='%s'"%(vid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managevendor'))

	if action=='active':
		q="update vendor set vendor_status='1' where vendor_id='%s'"%(vid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managevendor'))

	if action=='update':
		q="select * from vendor where vendor_id='%s'"%(vid)
		res=select(q)
	
		data['vendorupdate']=res

	if "up" in request.form:
		f=request.form['fname']
		n=request.form['num']
		e=request.form['email']
		h=request.form['hno']
		s=request.form['street']
		di=request.form['district']
		p=request.form['pin']
		d=request.form['date']
		q="update vendor set vendor_name='%s',vendor_phone='%s',vendor_email='%s',vendor_hno='%s',vendor_street='%s',vendor_dist='%s',vendor_pin='%s',vendor_date='%s' where vendor_id='%s'"%(f,n,e,h,s,di,p,d,vid)
		update(q)
		flash('successfully')
		print(q)
		return redirect(url_for('admin.admin_managevendor'))
		
			

	if "vendor" in request.form:
	
		f=request.form['fname']
		n=request.form['num']
		e=request.form['email']
		h=request.form['hno']
		s=request.form['street']
		di=request.form['district']
		p=request.form['pin']
		d=request.form['date']
		q="insert into vendor values(null,'0','%s','%s','%s','%s','%s','%s','%s','%s','1')"%(f,n,e,h,s,di,p,d)
		insert(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managevendor'))
	return render_template('/admin_managevendor.html',data=data)

@admin.route('/admin_managecourier',methods=['post','get'])
def admin_managecourier():
	data={}
	q="select * from courier inner join login using (username)"
	res=select(q)
	data['courierview']=res

	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']

	else:
		action=None

	if action=='update':
		q="select * from courier where username='%s'"%(cid)
		res=select(q)

		data['courierupdate']=res



	if "update" in request.form:
		f=request.form['fname']
		s=request.form['street']
		d=request.form['district']
		st=request.form['state']
		p=request.form['pin']
		n=request.form['num']
		e=request.form['email']
		q="update  courier set courier_name='%s', courier_street='%s',courier_dist='%s',courier_state='%s',courier_pincode='%s',courier_phone='%s',courier_email='%s',username='%s'"%(f,s,d,st,p,n,e,cid)
		update(q)
		flash('successfully')
		print(q)
		return redirect(url_for('admin.admin_managecourier'))


	if action=='inactive':
		q="update login set `status`='0' where username='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managecourier'))

	if action=='active':
		q="update login set `status`='1' where username='%s'"%(cid)
		update(q)
		return redirect(url_for('admin.admin_managecourier'))
		

	if "courier" in request.form:
		f=request.form['fname']
		s=request.form['street']
		d=request.form['district']
		st=request.form['state']
		p=request.form['pin']
		n=request.form['num']
		e=request.form['email']
		u=request.form['uname']
		pa=request.form['pwd']
		q="insert into login values('%s','%s','courier',1)"%(u,pa)
		insert(q)
		q="insert into courier values(null,'0','%s','%s','%s','%s','%s','%s','%s','%s')"%(u,f,s,d,st,p,n,e)
		insert(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managecourier'))		

	return render_template('admin_managecourier.html',data=data)


@admin.route('/admin_managecategory',methods=['post','get'])	
def admin_managecategory():
	data={}
	q="select * from category"
	res=select(q)
	data['categoryview']=res

	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']

	else:
		action=None

	if action=='active':
		q="update category set status='1' where category_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managecategory'))
	if action=='inactive':
		q="update category set status='0' where category_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managecategory'))

	if action=='update':
		q="select * from category where category_id='%s'"%(cid)
		res=select(q)
		data['categoryupdate']=res

	if "update" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="update category set category_name='%s', category_description='%s' where category_id='%s'"%(f,d,cid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managecategory'))
	if "category" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="insert into category values(null,'%s','%s','1')"%(f,d)
		insert(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managecategory'))
		
	return render_template('admin_managecategory.html',data=data)

@admin.route('/admin_managesubcategory',methods=['post','get'])
def admin_managesubcategory():
	data={}
	q="select * from subcategory"
	res=select(q)
	data['subview']=res

	if "action" in request.args:
		action=request.args['action']
		sid=request.args['sid']

	else:
		action=None


	if action=='active':
		q="update subcategory set sub_status='1' where subcategory_id='%s'"%(sid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managesubcategory'))

	if action=='inactive':
		q="update subcategory set sub_status='0' where subcategory_id='%s'"%(sid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managesubcategory'))

	if action=='update':
		q="select * from subcategory where subcategory_id='%s'"%(sid)
		res=select(q)
		data['subcategoryupdate']=res


	if "update" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="update subcategory set subcategory_name='%s',subcategory_description='%s' where subcategory_id='%s'"%(f,d,sid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managesubcategory'))

			
			
			

	if "subcategory" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="insert into subcategory values(null,'%s','%s','1')"%(f,d)
		insert(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managesubcategory'))

	return render_template('admin_managesubcategory.html',data=data)

@admin.route('/admin_managecolor',methods=['post','get'])	
def admin_managecolor():
	data={}
	q="select * from color"
	res=select(q)
	data['colorview']=res


	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None
	if action=='active':
		q="update color set color_status='1' where color_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managecolor'))

	if action=='inactive':
		q="update color set color_status='0' where color_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managecolor'))

	if action=='update':
		q="select * from color where color_id='%s'"%(cid)
		res=select(q)
		data['colorupdate']=res

	if "update" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="update color set color_name='%s',color_desc='%s' where color_id='%s'"%(f,d,cid)
		update(q)
		return redirect(url_for('admin.admin_managecolor'))

	if "color" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="insert into color values(null,'%s','%s','1')"%(f,d)
		insert(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managecolor'))
		
	
	return render_template('admin_managecolor.html',data=data)


@admin.route('/admin_managebrand',methods=['post','get'])	
def admin_managebrand():
	data={}
	q="select * from brand"
	res=select(q)
	data['brandview']=res

	if "action" in request.args:
		action=request.args['action']
		bid=request.args['bid']

	else:
		action=None

	if action=='active':
		q="update brand set brand_status='1' where brand_id='%s'"%(bid)
		update(q)

		flash('successfully')
		return redirect(url_for('admin.admin_managebrand'))

	if action=='inactive':
		q="update brand set brand_status='0' where brand_id='%s'"%(bid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managebrand'))

	if action=='update':
		q="select * from brand where brand_id='%s'"%(bid)
		res=select(q)
		data['brandupdate']=res

	if "update" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="update brand set brand_name='%s',brand_desc='%s' where brand_id='%s'"%(f,d,bid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managebrand'))
								

	if "brand" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="insert into brand values(null,'%s','%s','1')"%(f,d)
		insert(q)
		flash('successfully')
		return redirect(url_for('admin.admin_managebrand'))
	return render_template('admin_managebrand.html',data=data)


@admin.route('/admin_manageitem',methods=['post','get'])	
def admin_manageitem():
	data={}

	q="select * from category where status='1'"
	res=select(q)
	data['categorydrop']=res

	q="select * from subcategory where sub_status='1'"
	res=select(q)
	data['subcategorydrop']=res

	q="select * from color where color_status='1' "
	res=select(q)
	data['colordrop']=res

	q="select * from brand where brand_status='1'"
	res=select(q)
	data['branddrop']=res


	q="SELECT * FROM product INNER JOIN category USING (`category_id`) INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (`color_id`) INNER JOIN brand USING (brand_id)"
	res=select(q)
	data['productview']=res



	if "action" in request.args:
		action=request.args['action']
		pid=request.args['pid']

	else:
		action=None

	if action=='available':
		q="update product set product_status='1' where product_id='%s'"%(pid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_manageitem'))

	if action=='notavailable':
		q="update product set product_status='0' where product_id='%s'"%(pid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_manageitem'))	

	if action=='update':
		q="SELECT * FROM product INNER JOIN category USING (`category_id`) INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (`color_id`) INNER JOIN brand USING (brand_id) where product_id='%s'"%(pid)
		res=select(q)
		
		data['productupdate']=res


	if "update" in request.form:
		cat=request.form['cat']
		sub=request.form['subcategory']
		col=request.form['color']
		b=request.form['brand']
		f=request.form['fname']
		d=request.form['dis']
		i=request.files['imgg']
		path="static/image"+str(uuid.uuid4())+i.filename
		i.save(path)
		r=request.form['rate']
		s=request.form['stock']
		q="update product set category_id='%s',subcategory_id='%s',color_id='%s',brand_id='%s',product_name='%s',product_description='%s',product_image='%s' ,product_rate='%s',stock='%s' where product_id='%s'"%(cat,sub,col,b,f,d,path,r,s,pid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_manageitem'))


	if "product" in request.form:
		cat=request.form['cat']
		sub=request.form['subcategory']
		col=request.form['color']
		b=request.form['brand']
		f=request.form['fname']
		d=request.form['dis']
		i=request.files['imgg']
		path="static/image"+str(uuid.uuid4())+i.filename
		i.save(path)
		r=request.form['rate']
		s=request.form['stock']
		q="insert into product values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','1')"%(cat,sub,col,b,f,d,path,r,s)
		insert(q)
		flash('successfully')
		return redirect(url_for('admin.admin_manageitem'))		


	return render_template('admin_manageitem.html',data=data)



@admin.route('/admin_managepurchase',methods=['post','get'])	
def admin_managepurchase():
	data={}

	q="select * from vendor where vendor_status='1'"
	res=select(q)
	data['vendordrop']=res


	q="select * from product where product_status='1'"
	res=select(q)
	data['productdrop']=res



	q="SELECT * FROM `purchase_child` INNER JOIN `purchase_master` USING (`purchase_master_id`) INNER JOIN `vendor` USING (`vendor_id`) INNER JOIN `product` USING (`product_id`) where status='pending'"
	res=select(q)
	data['purchaseview']=res


	if "action" in request.args:
		action=request.args['action']
		pid=request.args['pid']
	else:
		action=None

	if  action=='conform':
		q="update purchase_master set status='purchased' where purchase_master_id='%s'"%(pid)
		update(q)

		q="select * from purchase_child where purchase_master_id='%s'"%(pid)
		res=select(q)

		for i in res:

			item_id=i['product_id']
			qty=i['quantity']
			q="update product set stock=stock+'%s' where product_id='%s'"%(qty,item_id)
			update(q)

			flash('successfully')




		
		return redirect(url_for('admin.admin_managepurchase'))



	if "purchase" in request.form:
		ve=request.form['ven']
		p=request.form['pro']
		f=request.form['fname']
		d=request.form['dis']
		i=request.files['imgg']
		path="static/image"+str(uuid.uuid4())+i.filename
		i.save(path)
		c=int(request.form['cost_price'])
	
		qu=request.form['quantity']
		t=request.form['total']

		sellp=(20/100)*int(c)
		new=int(sellp)+int(c)


		q="select * from purchase_master where vendor_id='%s' and status='pending'"%(ve)
		res=select(q)
		if res:
			pmid=res[0]['purchase_master_id']

		else:
			
			q="insert into purchase_master values(null,'%s','0','0','pending')"%(ve)
			pmid=insert(q)

		q="select * from purchase_child where product_id='%s' and purchase_master_id='%s' "%(p,pmid)
		res=select(q)
		print(q)
		if res:

			pcid=res[0]['purchase_child_id']


			q="update purchase_child set quantity=quantity+'%s',cost_price=cost_price+'%s' where purchase_child_id='%s'"%(qu,t,pcid)
			update(q)
			print(q)

		else:


					
			q="insert into purchase_child values(null,'%s','%s','%s','%s','%s')"%(pmid,p,t,new,qu)
			insert(q)
			print(q)

		q="update purchase_master set total=total+'%s' where purchase_master_id='%s'"%(t,pmid)
		update(q)
		flash('successfully')

		return redirect(url_for('admin.admin_managepurchase'))


		
	
	return render_template('admin_managepurchase.html',data=data)

@admin.route('/admin_viewbooking')
def admin_viewbooking():
	data={}
	q="SELECT * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (customer_id) INNER JOIN `category` USING (`category_id`) INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (color_id)INNER JOIN brand USING (brand_id)"
	res=select(q)
	data['bookingview']=res
	return render_template('admin_viewbooking.html',data=data)

@admin.route('/admin_viewpayment')
def admin_viewpayment():
	data={}
	oid=request.args['oid']
	q="SELECT * FROM `payment` INNER JOIN `card` USING (card_id) INNER JOIN `customer` USING (`customer_id`) INNER JOIN `order_master` USING (`order_master_id`) where order_master_id='%s'"%(oid)
	res=select(q)
	data['paymentview']=res
	return render_template('admin_viewpayment.html',data=data)	


@admin.route('/admin_viewcomplaint')	
def admin_viewcomplaint():
	data={}
	q="select * from complaint inner join customer using (customer_id)"
	res=select(q)
	data['complaintview']=res
	return render_template('admin_viewcomplaint.html',data=data)


@admin.route('/admin_sendreply',methods=['post','get'])
def admin_sendreply():

	
	if "reply" in request.form:
		rep=request.form['rep']
		cid=request.args['cid']
		q="update complaint set reply='%s' where complaint_id='%s'"%(rep,cid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_viewcomplaint'))

	
	return render_template('admin_sendreply.html')	



@admin.route('/admin_viewcustomer')	
def admin_viewcustomer():
	data={}

	if "action" in request.args:
		action=request.args['action']
		lid=request.args['lid']

	else:
		action=None

	if action=='accept':
		q="update login set status='1' where username='%s'"%(lid)
		update(q)
		q="update customer set customer_status='1' where username='%s'"%(lid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_viewcustomer'))

	if action=='reject':
		q="update login set status='0' where username='%s'"%(lid)
		update(q)
		q="update customer set customer_status='0' where username='%s'"%(lid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_viewcustomer'))
			
	q="select * from customer inner join login using (username)"
	res=select(q)
	data['customerview']=res

	return render_template('admin_viewcustomer.html',data=data)

@admin.route('/admin_managereport',methods=['post','get'])	
def admin_managereport():
	data={}
	if "sale" in request.form:
		daily=request.form['daily']
		if request.form['monthly']=="":
			monthly=""
		else:
			monthly=request.form['monthly']+'%'
		print(monthly)
		customer=request.form['customer']	
		q="SELECT * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (customer_id) INNER JOIN `category` USING (`category_id`) INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (color_id)INNER JOIN brand USING (brand_id) where (`customer_fname` like '%s') or (`date` like '%s'  ) or (`date` like '%s' ) "%(customer,daily,monthly)
		res=select(q)
		print(q)
		data['report']=res
		session['res']=res
		r=session['res']
	else:
		q="SELECT * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (customer_id) INNER JOIN `category` USING (`category_id`) INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (color_id)INNER JOIN brand USING (brand_id)"
		res=select(q)
		data['report']=res
	
	return render_template('admin_managereport.html',data=data)

@admin.route('/admin_salesreport')
def admin_salesreport():
	data={}

	r=session['res']
	data['r']=r


	return render_template('admin_salesreport.html',data=data)	



	


	
	
