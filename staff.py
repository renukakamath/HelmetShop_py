from flask import * 
from database import*
import uuid



staff=Blueprint('staff',__name__)

@staff.route('/staff_home')
def staff_home():

	return render_template('staff_home.html')



@staff.route('/staff_managevendor',methods=['post','get'])	
def staff_managevendor():
	data={}
	sid=session['staff_id']
	q="select * from vendor where staff_id='%s'"%(sid)
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
		return redirect(url_for('staff.staff_managevendor'))

	if action=='active':
		q="update vendor set vendor_status='1' where vendor_id='%s'"%(vid)
		update(q)
		return redirect(url_for('staff.staff_managevendor'))

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
		print(q)
		return redirect(url_for('staff.staff_managevendor'))
		
			

	if "vendor" in request.form:
		sid=session['staff_id']
	
		f=request.form['fname']
		n=request.form['num']
		e=request.form['email']
		h=request.form['hno']
		s=request.form['street']
		di=request.form['district']
		p=request.form['pin']
		d=request.form['date']
		q="insert into vendor values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','1')"%(sid,f,n,e,h,s,di,p,d)
		insert(q)
		return redirect(url_for('staff.staff_managevendor'))
	return render_template('/staff_managevendor.html',data=data)

@staff.route('/staff_managecourier',methods=['post','get'])
def staff_managecourier():
	data={}
	sid=session['staff_id']
	q="select * from courier where staff_id='%s'"%(sid)
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
		print(q)
		return redirect(url_for('staff.staff_managecourier'))
	if action=='inactive':
		q="update login set `status`='0' where username='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managecourier'))

	if action=='active':
		q="update login set `status`='1' where username='%s'"%(cid)
		update(q)
		return redirect(url_for('staff.staff_managecourier'))
		

	if "courier" in request.form:
		sid=session['staff_id']
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
		q="insert into courier values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(sid,u,f,s,d,st,p,n,e)
		insert(q)
		return redirect(url_for('staff.staff_managecourier'))		

	return render_template('staff_managecourier.html',data=data)


@staff.route('/staff_managecategory',methods=['post','get'])	
def staff_managecategory():
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
		return redirect(url_for('staff.staff_managecategory'))
	if action=='inactive':
		q="update category set status='0' where category_id='%s'"%(cid)
		update(q)
		return redirect(url_for('staff.staff_managecategory'))

	if action=='update':
		q="select * from category where category_id='%s'"%(cid)
		res=select(q)
		data['categoryupdate']=res

	if "update" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="update category set category_name='%s', category_description='%s' where category_id='%s'"%(f,d,cid)
		update(q)
		return redirect(url_for('staff.staff_managecategory'))
	if "category" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="insert into category values(null,'%s','%s','1')"%(f,d)
		insert(q)
		return redirect(url_for('staff.staff_managecategory'))
		
	return render_template('staff_managecategory.html',data=data)

@staff.route('/staff_managesubcategory',methods=['post','get'])
def staff_managesubcategory():
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
		return redirect(url_for('staff.staff_managesubcategory'))

	if action=='inactive':
		q="update subcategory set sub_status='0' where subcategory_id='%s'"%(sid)
		update(q)
		return redirect(url_for('staff.staff_managesubcategory'))

	if action=='update':
		q="select * from subcategory where subcategory_id='%s'"%(sid)
		res=select(q)
		data['subcategoryupdate']=res


	if "update" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="update subcategory set subcategory_name='%s',subcategory_description='%s' where subcategory_id='%s'"%(f,d,sid)
		update(q)
		return redirect(url_for('staff.staff_managesubcategory'))

			
			
			

	if "subcategory" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="insert into subcategory values(null,'%s','%s','1')"%(f,d)
		insert(q)
		return redirect(url_for('staff.staff_managesubcategory'))

	return render_template('staff_managesubcategory.html',data=data)

@staff.route('/staff_managecolor',methods=['post','get'])	
def staff_managecolor():
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
		return redirect(url_for('staff.staff_managecolor'))

	if action=='inactive':
		q="update color set color_status='0' where color_id='%s'"%(cid)
		update(q)
		return redirect(url_for('staff.staff_managecolor'))

	if action=='update':
		q="select * from color where color_id='%s'"%(cid)
		res=select(q)
		data['colorupdate']=res

	if "update" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="update color set color_name='%s',color_desc='%s' where color_id='%s'"%(f,d,cid)
		update(q)
		return redirect(url_for('staff.staff_managecolor'))

	if "color" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="insert into color values(null,'%s','%s','1')"%(f,d)
		insert(q)
		return redirect(url_for('staff.staff_managecolor'))
		
	
	return render_template('staff_managecolor.html',data=data)


@staff.route('/staff_managebrand',methods=['post','get'])	
def staff_managebrand():
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
		q="update brand set brand_status='1'  where brand_id='%s'"%(bid)
		update(q)
		return redirect(url_for('staff.staff_managebrand'))

	if action=='inactive':
		q="update brand set brand_status='0' where brand_id='%s'"%(bid)
		update(q)
		return redirect(url_for('staff.staff_managebrand'))

	if action=='update':
		q="select * from brand where brand_id='%s'"%(cid)
		res=select(q)
		data['brandview']=res

	if "update" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="update brand set brand_name='%s',brand_desc='%s' where brand_id='%s'"%(f,d,bid)
		update(q)
		return redirect(url_for('staff.staff_managebrand'))
								

	if "brand" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="insert into brand values(null,'%s','%s','1')"%(f,d)
		insert(q)
		return redirect(url_for('staff.staff_managebrand'))
	return render_template('staff_managebrand.html',data=data)


@staff.route('/staff_manageitem',methods=['post','get'])	
def staff_manageitem():
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

	if action=='active':
		q="update product set product_status='1' where product_id='%s'"%(pid)
		update(q)
		return redirect(url_for('staff.staff_manageitem'))

	if action=='inactive':
		q="update product set product_status='1' where product_id='%s'"%(pid)
		update(q)
		return redirect(url_for('staff.staff_manageitem'))	

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
		return redirect(url_for('staff.staff_manageitem'))


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
		return redirect(url_for('staff.staff_manageitem'))		


	return render_template('staff_manageitem.html',data=data)



@staff.route('/staff_managepurchase',methods=['post','get'])	
def staff_managepurchase():
	data={}
	sid=session['staff_id']

	q="select * from vendor where vendor_status='1'"
	res=select(q)
	data['vendordrop']=res


	q="select * from product where product_status='1'"
	res=select(q)
	data['productdrop']=res



	q="SELECT * FROM `purchase_child` INNER JOIN `purchase_master` USING (`purchase_master_id`) INNER JOIN `vendor` USING (`vendor_id`) INNER JOIN `product` USING (`product_id`) where status='pending' and purchase_master.staff_id='%s'"%(sid)
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


		
		return redirect(url_for('staff.staff_managepurchase'))



	if "purchase" in request.form:
		sid=session['staff_id']
		

		ve=request.form['ven']
		p=request.form['pro']
		f=request.form['fname']
		d=request.form['dis']
		i=request.files['imgg']
		path="static/image"+str(uuid.uuid4())+i.filename
		i.save(path)
		c=request.form['cost_price']
		s=request.form['selling_price']
		qu=request.form['quantity']
		t=request.form['total']

		sellp=(20/100)*int(c)
		new=int(sellp)+int(c)

		q="select * from purchase_master where vendor_id='%s' and status='pending'"%(ve)
		res=select(q)
		if res:
			pmid=res[0]['purchase_master_id']

		else:
			
			q="insert into purchase_master values(null,'%s','%s','0','pending')"%(ve,sid)
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


					
			q="insert into purchase_child values(null,'%s','%s','%s','%s','%s')"%(pmid,p,t,s,qu)
			insert(q)
			print(q)

		q="update purchase_master set total=total+'%s' where purchase_master_id='%s'"%(t,pmid)
		update(q)

		return redirect(url_for('staff.staff_managepurchase'))


		
	
	return render_template('staff_managepurchase.html',data=data)

@staff.route('/staff_viewbooking')
def staff_viewbooking():
	data={}
	q="SELECT * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (customer_id) INNER JOIN `category` USING (`category_id`) INNER JOIN `subcategory` USING (`subcategory_id`) INNER JOIN color USING (color_id)INNER JOIN brand USING (brand_id)"
	res=select(q)
	data['bookingview']=res
	return render_template('staff_viewbooking.html',data=data)

@staff.route('/staff_viewpayment')
def staff_viewpayment():
	data={}
	q="SELECT * FROM `payment` INNER JOIN `card` USING (card_id) INNER JOIN `customer` USING (`customer_id`) INNER JOIN `order_master` USING (`order_master_id`) where order_master.order_status='paid'"
	res=select(q)
	data['pay']=res
	return render_template('staff_viewpayment.html',data=data)	


@staff.route('/staff_viewcomplaint')	
def staff_viewcomplaint():
	data={}
	q="select * from complaint inner join customer using (customer_id)"
	res=select(q)
	data['complaintview']=res
	return render_template('staff_viewcomplaint.html',data=data)


@staff.route('/staff_managereport',methods=['post','get'])	
def staff_managereport():
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
	
	return render_template('staff_managereport.html',data=data)

@staff.route('/staff_salesreport')
def staff_salesreport():
	data={}

	r=session['res']
	data['r']=r


	return render_template('staff_salesreport.html',data=data)	




	


	
	
