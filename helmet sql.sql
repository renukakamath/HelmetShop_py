/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - helmet
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`helmet` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `helmet`;

/*Table structure for table `brand` */

DROP TABLE IF EXISTS `brand`;

CREATE TABLE `brand` (
  `brand_id` int(11) NOT NULL AUTO_INCREMENT,
  `brand_name` varchar(100) DEFAULT NULL,
  `brand_desc` varchar(100) DEFAULT NULL,
  `brand_status` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`brand_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `brand` */

insert  into `brand`(`brand_id`,`brand_name`,`brand_desc`,`brand_status`) values 
(1,'brand','fefew','0');

/*Table structure for table `card` */

DROP TABLE IF EXISTS `card`;

CREATE TABLE `card` (
  `card_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `card_no` varchar(100) DEFAULT NULL,
  `card_name` varchar(100) DEFAULT NULL,
  `expiry_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`card_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `card` */

insert  into `card`(`card_id`,`customer_id`,`card_no`,`card_name`,`expiry_date`) values 
(1,1,'1234567890123456','qwertyuio','2023-01-13'),
(2,1,'1234567890123456','67o','2023-01-21'),
(3,1,'1234567890123456','123','2023-06'),
(4,3,'1234567890345678','renu','2023-12');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) DEFAULT NULL,
  `category_description` varchar(100) DEFAULT NULL,
  `status` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category_name`,`category_description`,`status`) values 
(1,'cart1','vfdgf11','1'),
(2,'fsfs','ffdgfs','1');

/*Table structure for table `color` */

DROP TABLE IF EXISTS `color`;

CREATE TABLE `color` (
  `color_id` int(11) NOT NULL AUTO_INCREMENT,
  `color_name` varchar(100) DEFAULT NULL,
  `color_desc` varchar(100) DEFAULT NULL,
  `color_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`color_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `color` */

insert  into `color`(`color_id`,`color_name`,`color_desc`,`color_status`) values 
(1,'blue','sfsfsgs1','1'),
(2,'red','wded','1'),
(3,'#198665','sfsfsgs1','1'),
(4,'#0f8ef0','gfdg','1'),
(5,'green','hukhlo','0'),
(6,'red','bhdafkdjaf','1');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`customer_id`,`complaint`,`reply`,`date`) values 
(1,1,'good','ok','2023-01-01');

/*Table structure for table `courier` */

DROP TABLE IF EXISTS `courier`;

CREATE TABLE `courier` (
  `courier_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `courier_name` varchar(100) DEFAULT NULL,
  `courier_street` varchar(100) DEFAULT NULL,
  `courier_dist` varchar(100) DEFAULT NULL,
  `courier_state` varchar(100) DEFAULT NULL,
  `courier_pincode` varchar(100) DEFAULT NULL,
  `courier_phone` varchar(100) DEFAULT NULL,
  `courier_email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`courier_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `courier` */

insert  into `courier`(`courier_id`,`staff_id`,`username`,`courier_name`,`courier_street`,`courier_dist`,`courier_state`,`courier_pincode`,`courier_phone`,`courier_email`) values 
(1,0,'courier@gmail.com','user1','dgsdyhtyswt1','ekm1','Kerala1','682032','2345678907','rddgt1@gmail.com');

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `customer_fname` varchar(100) DEFAULT NULL,
  `customer_lname` varchar(100) DEFAULT NULL,
  `customer_houser_name` varchar(100) DEFAULT NULL,
  `customer_street` varchar(100) DEFAULT NULL,
  `customer_dist` varchar(100) DEFAULT NULL,
  `customer_state` varchar(100) DEFAULT NULL,
  `customer_pincode` varchar(100) DEFAULT NULL,
  `customer_dob` varchar(100) DEFAULT NULL,
  `customer_gender` varchar(100) DEFAULT NULL,
  `customer_phone` varchar(100) DEFAULT NULL,
  `customer_email` varchar(100) DEFAULT NULL,
  `customer_status` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`username`,`customer_fname`,`customer_lname`,`customer_houser_name`,`customer_street`,`customer_dist`,`customer_state`,`customer_pincode`,`customer_dob`,`customer_gender`,`customer_phone`,`customer_email`,`customer_status`) values 
(1,'anu@gmail.com','user','qwerty','shjdbjskaf','msdnsa','slkmdlkw','ksmdlkas','123456','2022-12-31','female','1234560987','anu@gmail.com',1),
(2,'renuka@gmail.com','renuka','qwerty','Thusiprambil house Karanakodam Thammanam','vfg','dfwsgr','Kerala','682032','2023-01-01','female','1234567890','renuka@gmail.com',0),
(3,'hai@gmail.com','user','fegrwg','feww','rtwrt','rtrw','rtet','123456','2023-01-21','female','1234567890','tewt@gmail.com',1),
(4,'hai1@gmail.com','user','qwerty','xfdsgdsg','gsdgdsg','Ernakulam','dgdsgd','123456','2023-01-19','female','02345678907','student@gmail.com',1);

/*Table structure for table `delivery` */

DROP TABLE IF EXISTS `delivery`;

CREATE TABLE `delivery` (
  `delivery_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_master_id` int(11) DEFAULT NULL,
  `courier_id` int(11) DEFAULT NULL,
  `delivery_date` varchar(100) DEFAULT NULL,
  `status` varchar(41) DEFAULT NULL,
  PRIMARY KEY (`delivery_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `delivery` */

insert  into `delivery`(`delivery_id`,`order_master_id`,`courier_id`,`delivery_date`,`status`) values 
(1,1,1,'2023-01-01','Delivered');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  `status` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`user_type`,`status`) values 
('admin@gmail.com','admin','admin','1'),
('anu@gmail.com','anu','customer','1'),
('a@gmail.com','a','staff','0'),
('staff@gmail.com','staff','staff','1'),
('r@gmail.com','r','staff','1'),
('courier@gmail.com','cou','courier','0'),
('renuka@gmail.com','renu','customer','0'),
('hai@gmail.com','hai','customer','1'),
('hai1@gmail.com','helolo','customer','1');

/*Table structure for table `order_details` */

DROP TABLE IF EXISTS `order_details`;

CREATE TABLE `order_details` (
  `order_details_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_master_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `total_price` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`order_details_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `order_details` */

insert  into `order_details`(`order_details_id`,`order_master_id`,`product_id`,`quantity`,`total_price`) values 
(4,2,1,'100','50000'),
(3,2,2,'100','500100');

/*Table structure for table `order_master` */

DROP TABLE IF EXISTS `order_master`;

CREATE TABLE `order_master` (
  `order_master_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `total_amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `order_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`order_master_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `order_master` */

insert  into `order_master`(`order_master_id`,`customer_id`,`total_amount`,`date`,`order_status`) values 
(2,1,'550100','2023-01-04','pending');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `card_id` int(11) DEFAULT NULL,
  `order_master_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`card_id`,`order_master_id`,`amount`,`date`) values 
(1,1,1,'6501','2023-01-01'),
(2,1,1,'6501','2023-01-01'),
(3,1,1,'6501','2023-01-01'),
(4,1,1,'6501','2023-01-01'),
(5,1,2,'5001','2023-01-02'),
(6,1,3,'5501','2023-01-02'),
(7,2,4,'21504','2023-01-02'),
(8,1,8,'20000','2023-01-03'),
(9,1,11,'430000','2023-01-03');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `subcategory_id` int(11) DEFAULT NULL,
  `color_id` int(11) DEFAULT NULL,
  `brand_id` int(11) DEFAULT NULL,
  `product_name` varchar(100) DEFAULT NULL,
  `product_description` varchar(100) DEFAULT NULL,
  `product_image` varchar(1000) DEFAULT NULL,
  `product_rate` varchar(100) DEFAULT NULL,
  `stock` varchar(100) DEFAULT NULL,
  `product_status` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`category_id`,`subcategory_id`,`color_id`,`brand_id`,`product_name`,`product_description`,`product_image`,`product_rate`,`stock`,`product_status`) values 
(1,1,1,1,1,'shop','sfgdshrsh','static/image1e11bc3f-d15b-4c15-9a01-9f0e8bffa6b7download (1) - Copy.jfif','500','100','1'),
(2,1,2,2,1,'podwer','sfgdshrsh1','static/image84e75c26-0e23-4af7-8b47-c954e3632956HD-wallpaper-laptop-red-sunset-background-laptop.jpg','5001','100','1');

/*Table structure for table `purchase_child` */

DROP TABLE IF EXISTS `purchase_child`;

CREATE TABLE `purchase_child` (
  `purchase_child_id` int(11) NOT NULL AUTO_INCREMENT,
  `purchase_master_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `cost_price` varchar(100) DEFAULT NULL,
  `selling_price` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`purchase_child_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `purchase_child` */

insert  into `purchase_child`(`purchase_child_id`,`purchase_master_id`,`product_id`,`cost_price`,`selling_price`,`quantity`) values 
(1,1,1,'512','200','4'),
(2,2,2,'100','1','1'),
(3,3,2,'80000','1000','20'),
(4,3,1,'9696','21','3'),
(5,4,2,'2000','120','20'),
(6,5,1,'150','180','1');

/*Table structure for table `purchase_master` */

DROP TABLE IF EXISTS `purchase_master`;

CREATE TABLE `purchase_master` (
  `purchase_master_id` int(11) NOT NULL AUTO_INCREMENT,
  `vendor_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`purchase_master_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `purchase_master` */

insert  into `purchase_master`(`purchase_master_id`,`vendor_id`,`staff_id`,`total`,`status`) values 
(1,1,0,'512','purchased'),
(2,2,0,'100','purchased'),
(3,2,0,'89696','purchased'),
(4,1,0,'2000','purchased'),
(5,1,0,'150','purchased');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `staff_fname` varchar(100) DEFAULT NULL,
  `staff_lname` varchar(100) DEFAULT NULL,
  `staff_gender` varchar(100) DEFAULT NULL,
  `staff_dob` varchar(100) DEFAULT NULL,
  `staff_house_name` varchar(100) DEFAULT NULL,
  `staff_street` varchar(100) DEFAULT NULL,
  `staff_dist` varchar(100) DEFAULT NULL,
  `staff_state` varchar(100) DEFAULT NULL,
  `staff_pincode` varchar(100) DEFAULT NULL,
  `staff_phone` varchar(100) DEFAULT NULL,
  `staff_email` varchar(100) DEFAULT NULL,
  `staff_status` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`username`,`staff_fname`,`staff_lname`,`staff_gender`,`staff_dob`,`staff_house_name`,`staff_street`,`staff_dist`,`staff_state`,`staff_pincode`,`staff_phone`,`staff_email`,`staff_status`) values 
(1,'staff@gmail.com','a@gmail.com','user1','qwerty1','male','2022-12-29','Thammanam','fghjkl11','dfghj11','1','682032','1234560987',0),
(2,'a@gmail.com','a123@gmail.com','user','female','2022-12-24','dafdafda','Thammanamsa','fghjkl11sda','fghjkl11','112312','6820321231','renuka@gmail.com',0),
(3,'r@gmail.com','a@gmail.com','user1','qwerty1','male','2022-12-29','Thammanam','fghjkl11','dfghj11','1','682032','1234560987',1);

/*Table structure for table `subcategory` */

DROP TABLE IF EXISTS `subcategory`;

CREATE TABLE `subcategory` (
  `subcategory_id` int(11) NOT NULL AUTO_INCREMENT,
  `subcategory_name` varchar(100) DEFAULT NULL,
  `subcategory_description` varchar(100) DEFAULT NULL,
  `sub_status` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`subcategory_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `subcategory` */

insert  into `subcategory`(`subcategory_id`,`subcategory_name`,`subcategory_description`,`sub_status`) values 
(1,'staff11','gcsfryt11','1'),
(2,'user1','zhfjg','1');

/*Table structure for table `vendor` */

DROP TABLE IF EXISTS `vendor`;

CREATE TABLE `vendor` (
  `vendor_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `vendor_name` varchar(100) DEFAULT NULL,
  `vendor_phone` varchar(100) DEFAULT NULL,
  `vendor_email` varchar(100) DEFAULT NULL,
  `vendor_hno` varchar(100) DEFAULT NULL,
  `vendor_street` varchar(100) DEFAULT NULL,
  `vendor_dist` varchar(100) DEFAULT NULL,
  `vendor_pin` varchar(100) DEFAULT NULL,
  `vendor_date` varchar(100) DEFAULT NULL,
  `vendor_status` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`vendor_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `vendor` */

insert  into `vendor`(`vendor_id`,`staff_id`,`vendor_name`,`vendor_phone`,`vendor_email`,`vendor_hno`,`vendor_street`,`vendor_dist`,`vendor_pin`,`vendor_date`,`vendor_status`) values 
(1,0,'ammu','2345678907','studen1t@gmail.com','asdfghj1','rtyjjg1','fdfsf1','234566','2022-12-24','1'),
(2,0,'minnu','2345678907','studen1t@gmail.com','asdfghj1','rtyjjg1','fdfsf1','234566','2022-12-24','1');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
