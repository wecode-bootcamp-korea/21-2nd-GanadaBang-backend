-- MySQL dump 10.13  Distrib 8.0.25, for macos11.3 (x86_64)
--
-- Host: localhost    Database: ganadabang
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',12,'add_permission'),(2,'Can change permission',12,'change_permission'),(3,'Can delete permission',12,'delete_permission'),(4,'Can view permission',12,'view_permission'),(5,'Can add group',13,'add_group'),(6,'Can change group',13,'change_group'),(7,'Can delete group',13,'delete_group'),(8,'Can view group',13,'view_group'),(9,'Can add user',14,'add_user'),(10,'Can change user',14,'change_user'),(11,'Can delete user',14,'delete_user'),(12,'Can view user',14,'view_user'),(13,'Can add content type',1,'add_contenttype'),(14,'Can change content type',1,'change_contenttype'),(15,'Can delete content type',1,'delete_contenttype'),(16,'Can view content type',1,'view_contenttype'),(17,'Can add session',2,'add_session'),(18,'Can change session',2,'change_session'),(19,'Can delete session',2,'delete_session'),(20,'Can view session',2,'view_session'),(21,'Can add location',3,'add_location'),(22,'Can change location',3,'change_location'),(23,'Can delete location',3,'delete_location'),(24,'Can view location',3,'view_location'),(25,'Can add option',4,'add_option'),(26,'Can change option',4,'change_option'),(27,'Can delete option',4,'delete_option'),(28,'Can view option',4,'view_option'),(29,'Can add room',5,'add_room'),(30,'Can change room',5,'change_room'),(31,'Can delete room',5,'delete_room'),(32,'Can view room',5,'view_room'),(33,'Can add room type',6,'add_roomtype'),(34,'Can change room type',6,'change_roomtype'),(35,'Can delete room type',6,'delete_roomtype'),(36,'Can view room type',6,'view_roomtype'),(37,'Can add trade type',7,'add_tradetype'),(38,'Can change trade type',7,'change_tradetype'),(39,'Can delete trade type',7,'delete_tradetype'),(40,'Can view trade type',7,'view_tradetype'),(41,'Can add room option',8,'add_roomoption'),(42,'Can change room option',8,'change_roomoption'),(43,'Can delete room option',8,'delete_roomoption'),(44,'Can view room option',8,'view_roomoption'),(45,'Can add room image',9,'add_roomimage'),(46,'Can change room image',9,'change_roomimage'),(47,'Can delete room image',9,'delete_roomimage'),(48,'Can view room image',9,'view_roomimage'),(49,'Can add option type',11,'add_optiontype'),(50,'Can change option type',11,'change_optiontype'),(51,'Can delete option type',11,'delete_optiontype'),(52,'Can view option type',11,'view_optiontype'),(53,'Can add user',10,'add_user'),(54,'Can change user',10,'change_user'),(55,'Can delete user',10,'delete_user'),(56,'Can view user',10,'view_user');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (13,'auth','group'),(12,'auth','permission'),(14,'auth','user'),(1,'contenttypes','contenttype'),(3,'rooms','location'),(4,'rooms','option'),(11,'rooms','optiontype'),(5,'rooms','room'),(9,'rooms','roomimage'),(8,'rooms','roomoption'),(6,'rooms','roomtype'),(7,'rooms','tradetype'),(2,'sessions','session'),(10,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-06-22 19:34:56.183530'),(2,'contenttypes','0002_remove_content_type_name','2021-06-22 19:34:56.222285'),(4,'sessions','0001_initial','2021-06-22 19:34:56.439416'),(5,'users','0001_initial','2021-06-22 19:34:56.451945'),(8,'users','0002_user_name','2021-06-23 10:47:09.846990'),(9,'rooms','0001_initial','2021-06-23 13:07:37.181075'),(10,'rooms','0002_auto_20210623_1524','2021-06-23 15:24:56.800217'),(11,'rooms','0003_location_dong_code','2021-06-24 17:27:33.238638'),(12,'rooms','0004_auto_20210630_0955','2021-07-12 17:14:48.652653'),(13,'rooms','0005_alter_room_location','2021-07-12 17:14:48.788375'),(14,'rooms','0006_auto_20210630_2029','2021-07-12 17:14:48.870214'),(15,'users','0003_auto_20210630_1448','2021-07-12 17:14:48.935101'),(16,'auth','0001_initial','2021-07-13 10:26:12.881496'),(17,'auth','0002_alter_permission_name_max_length','2021-07-13 10:26:12.919486'),(18,'auth','0003_alter_user_email_max_length','2021-07-13 10:26:12.937391'),(19,'auth','0004_alter_user_username_opts','2021-07-13 10:26:12.946038'),(20,'auth','0005_alter_user_last_login_null','2021-07-13 10:26:12.968060'),(21,'auth','0006_require_contenttypes_0002','2021-07-13 10:26:12.970190'),(22,'auth','0007_alter_validators_add_error_messages','2021-07-13 10:26:12.977504'),(23,'auth','0008_alter_user_username_max_length','2021-07-13 10:26:13.005979'),(24,'auth','0009_alter_user_last_name_max_length','2021-07-13 10:26:13.032298'),(25,'auth','0010_alter_group_name_max_length','2021-07-13 10:26:13.047102'),(26,'auth','0011_update_proxy_permissions','2021-07-13 10:26:13.059048'),(27,'auth','0012_alter_user_first_name_max_length','2021-07-13 10:26:13.082193');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `detail` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `latitude` decimal(17,14) NOT NULL,
  `longitude` decimal(17,14) NOT NULL,
  `utmk_x` decimal(18,10) NOT NULL,
  `utmk_y` decimal(18,10) NOT NULL,
  `dong_code` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  `city` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  `dong` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  `state` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (1,'테헤란로 427',37.50637292000000,127.05364070000000,1945020.8373940600,960738.9391262820,'1','','',''),(2,'봉은사로 471',37.51273146000000,127.05125270000000,1945727.2837530800,960531.2319793970,'1','','',''),(3,'삼성로111길 8',37.51469337000000,127.05165860000000,1945944.7767557500,960568.1379505720,'1','','',''),(4,'선릉로 668',37.51646636000000,127.04190200000000,1946145.6213185800,959706.8612650630,'1','','',''),(5,'선릉로118길 9',37.51313017000000,127.04361710000000,1945774.7542456500,959856.6383504930,'1','','',''),(6,'남부순환로317길 18-16',37.48030346000000,127.01107000000000,1942147.2170688000,956961.3890727640,'1','','',''),(7,'명달로 150',37.49061546000000,127.00510450000000,1943294.0227712400,956439.9470883800,'1','','',''),(8,'반포대로30길 6',37.49139536000000,127.00894790000000,1943378.7741141000,956780.1640776520,'1','','',''),(9,'서초중앙로12길 35',37.48806205000000,127.01677890000000,1943005.3900195300,957470.5454816430,'1','','',''),(10,'서초대로70길 51',37.49206332000000,127.02494880000000,1943445.6431034100,958195.0444135630,'1','','',''),(11,'대왕판교로644번길 12',37.39942931000000,127.10859790000000,1933134.6088563800,965547.1578738820,'1','','',''),(12,'판교역로 235 에이치스퀘어 엔동',37.40209537000000,127.10864080000000,1933430.3720964100,965552.1776792960,'1','','',''),(13,'대왕판교로606번길 33',37.39694726000000,127.11084870000000,1932858.4233124100,965745.2437338530,'1','','',''),(14,'대왕판교로644번길 62',37.39954384000000,127.11373040000000,1933145.4493281400,966001.4858656650,'1','','',''),(15,'대왕판교로645번길 21',37.39952995000000,127.10381110000000,1933147.5364496200,965123.5261933390,'1','','',''),(16,'대왕판교로712번길 22 판교테크노밸리 글로벌 R&D센터',37.40617684000000,127.10209350000000,1933885.5960126600,964974.6018591420,'1','','',''),(17,'올림픽로 240',37.51148180000000,127.09822410000000,1945569.9404441600,964681.8055729680,'1','','',''),(18,'테헤란로19길 46',37.50295512000000,127.03313450000000,1944650.4183130800,958924.6436273810,'1','','',''),(19,'강남대로 324',37.49214635000000,127.03095290000000,1943452.2011003900,958725.8581350810,'1','','',''),(20,'강남대로 370',37.49586247000000,127.02922270000000,1943865.2450567000,958574.9628829340,'1','','',''),(21,'',37.50600000000000,127.05000000000000,1945020.8200000001,950333.0000000000,'1','서울','녹번동','서울특별시'),(22,'',31.50600000000000,227.05000000000001,1925020.8200000001,950332.0000000000,'1','서울','녹8번1동','서울특별시');
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `option_types`
--

DROP TABLE IF EXISTS `option_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `option_types` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `option_types`
--

LOCK TABLES `option_types` WRITE;
/*!40000 ALTER TABLE `option_types` DISABLE KEYS */;
INSERT INTO `option_types` VALUES (1,'NORMAL'),(2,'SECURITY');
/*!40000 ALTER TABLE `option_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `options`
--

DROP TABLE IF EXISTS `options`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `options` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  `image_url` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `option_type_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `options_option_type_id_e6b4e375` (`option_type_id`),
  CONSTRAINT `options_option_type_id_e6b4e375_fk_option_types_id` FOREIGN KEY (`option_type_id`) REFERENCES `option_types` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `options`
--

LOCK TABLES `options` WRITE;
/*!40000 ALTER TABLE `options` DISABLE KEYS */;
INSERT INTO `options` VALUES (1,'에어컨','https://www.dabangapp.com/static/media/aircondition.e635232d.svg',1),(2,'세탁기','https://www.dabangapp.com/static/media/laundry.030d913d.svg',1),(3,'신발장','https://www.dabangapp.com/static/media/shoes.9a00f9bc.svg',1),(4,'냉장고','https://www.dabangapp.com/static/media/refrigerator.1d986b2c.svg',1),(5,'가스레인지','https://www.dabangapp.com/static/media/gas.5823444e.svg',1),(6,'옷장','https://www.dabangapp.com/static/media/closet.61cb1751.svg',1),(7,'인덕션','https://www.dabangapp.com/static/media/induction.e57b4890.svg',1),(8,'비데','https://m.dabangapp.com/static/media/bidet.581ee9a3.svg',1),(9,'TV','https://www.dabangapp.com/static/media/tv.545c9579.svg',1),(10,'침대','https://www.dabangapp.com/static/media/bed.26f43a52.svg',1),(11,'전자레인지','https://www.dabangapp.com/static/media/microoven.6bf503f5.svg',1),(12,'책상','https://www.dabangapp.com/static/media/desk.10fc27f5.svg',1),(13,'전자도어락','https://www.dabangapp.com/static/media/doorlock.1b4ae1e7.svg',2),(14,'CCTV','https://www.dabangapp.com/static/media/cctv.82eb8ea7.svg',2),(15,'방범창','https://www.dabangapp.com/static/media/windowguard.9763544a.svg',2),(16,'인터폰','https://www.dabangapp.com/static/media/intercom.a85eac33.svg',2),(17,'비디오폰','https://www.dabangapp.com/static/media/videophone.953e2f08.svg',2),(18,'공동현관','https://www.dabangapp.com/static/media/entrance.f47bfd88.svg',2),(19,'경비원','https://www.dabangapp.com/static/media/guard.51cdd2fe.svg',2),(20,'화재경보기','https://www.dabangapp.com/static/media/firealarm.1539d50d.svg',2);
/*!40000 ALTER TABLE `options` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room_images`
--

DROP TABLE IF EXISTS `room_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room_images` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `url` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `room_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `room_images_room_id_7ee1491d_fk_rooms_id` (`room_id`),
  CONSTRAINT `room_images_room_id_7ee1491d_fk_rooms_id` FOREIGN KEY (`room_id`) REFERENCES `rooms` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room_images`
--

LOCK TABLES `room_images` WRITE;
/*!40000 ALTER TABLE `room_images` DISABLE KEYS */;
INSERT INTO `room_images` VALUES (1,'https://i.imgur.com/SwiHvRG.png',1),(2,'https://i.imgur.com/vUamptR.png',2),(3,'https://i.imgur.com/vBUgV3s.png',3),(4,'https://i.imgur.com/j5cEMAh.png',4),(5,'https://i.imgur.com/Zxsa3aZ.png',5),(6,'https://i.imgur.com/e6TqL7X.png',6),(7,'https://i.imgur.com/mjVjiL5.png',7),(8,'https://i.imgur.com/Dh0muvn.png',8),(9,'https://i.imgur.com/75bneLO.png',9),(10,'https://i.imgur.com/lgc9RHI.png',10),(11,'https://i.imgur.com/iHRnG60.png',11),(12,'https://i.imgur.com/AcA2rsH.png',12),(13,'https://i.imgur.com/z21goCh.png',13),(14,'https://i.imgur.com/aylXNh7.png',14),(15,'https://i.imgur.com/YjbCdHX.png',15),(16,'https://i.imgur.com/FYd89Dx.png',16),(17,'https://i.imgur.com/dXrDNLl.png',17),(18,'https://i.imgur.com/Yqi5OQt.png',18),(19,'https://i.imgur.com/wgzS1mp.png',19),(20,'https://i.imgur.com/TPCQT4h.png',20);
/*!40000 ALTER TABLE `room_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room_options`
--

DROP TABLE IF EXISTS `room_options`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room_options` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `option_id` bigint NOT NULL,
  `room_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `room_options_option_id_fbaf7499_fk_options_id` (`option_id`),
  KEY `room_options_room_id_52e1ad4e_fk_rooms_id` (`room_id`),
  CONSTRAINT `room_options_option_id_fbaf7499_fk_options_id` FOREIGN KEY (`option_id`) REFERENCES `options` (`id`),
  CONSTRAINT `room_options_room_id_52e1ad4e_fk_rooms_id` FOREIGN KEY (`room_id`) REFERENCES `rooms` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room_options`
--

LOCK TABLES `room_options` WRITE;
/*!40000 ALTER TABLE `room_options` DISABLE KEYS */;
INSERT INTO `room_options` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,5,1),(6,6,1),(7,7,1),(8,8,1),(9,9,1),(10,13,1),(11,14,1),(12,15,1),(13,16,1),(14,1,2),(15,2,2),(16,3,2),(17,4,2),(18,5,2),(19,7,2),(20,8,2),(21,9,2),(22,15,2),(23,16,2),(24,17,2),(25,2,3),(26,3,3),(27,4,3),(28,5,3),(29,7,3),(30,13,3),(31,14,3),(32,15,3),(33,16,3),(34,17,3),(35,18,3),(36,19,3),(37,1,4),(38,16,4),(39,1,5),(40,16,5),(41,1,6),(42,16,6),(43,2,7),(44,13,7),(45,3,8),(46,17,8),(47,8,9),(48,20,9),(49,3,10),(50,11,10),(51,4,11),(52,5,11),(53,7,12),(54,8,12),(55,3,13),(56,19,13),(57,2,14),(58,14,14),(59,1,15),(60,16,15),(61,8,16),(62,17,16),(63,7,17),(64,8,17),(65,3,18),(66,19,18),(67,2,19),(68,14,19),(69,1,20),(70,16,20);
/*!40000 ALTER TABLE `room_options` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room_types`
--

DROP TABLE IF EXISTS `room_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room_types` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room_types`
--

LOCK TABLES `room_types` WRITE;
/*!40000 ALTER TABLE `room_types` DISABLE KEYS */;
INSERT INTO `room_types` VALUES (1,'ONE_ROOM'),(2,'MULTI_ROOM'),(3,'OFFICETEL');
/*!40000 ALTER TABLE `room_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rooms`
--

DROP TABLE IF EXISTS `rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rooms` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `content` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `monthly_rent` int DEFAULT NULL,
  `deposit` int DEFAULT NULL,
  `sale` int DEFAULT NULL,
  `agent` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  `floor` int NOT NULL,
  `room_area` double NOT NULL,
  `room_count` int NOT NULL,
  `bathroom_count` int NOT NULL,
  `heating_type` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  `elevator` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `location_id` bigint NOT NULL,
  `room_type_id` bigint NOT NULL,
  `trade_type_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rooms_location_id_5e8b93b4_uniq` (`location_id`),
  KEY `rooms_room_type_id_c94e486c_fk_room_types_id` (`room_type_id`),
  KEY `rooms_trade_type_id_01de1d62_fk_trade_types_id` (`trade_type_id`),
  CONSTRAINT `rooms_location_id_5e8b93b4_fk_locations_id` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`),
  CONSTRAINT `rooms_room_type_id_c94e486c_fk_room_types_id` FOREIGN KEY (`room_type_id`) REFERENCES `room_types` (`id`),
  CONSTRAINT `rooms_trade_type_id_01de1d62_fk_trade_types_id` FOREIGN KEY (`trade_type_id`) REFERENCES `trade_types` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rooms`
--

LOCK TABLES `rooms` WRITE;
/*!40000 ALTER TABLE `rooms` DISABLE KEYS */;
INSERT INTO `rooms` VALUES (1,'원룸1','매물정보 원룸 1 풀옵션 ',30,100,0,'성규부동산',1,10.12,1,1,'개별','유','2021-06-23 18:35:49.952570',1,1,1),(2,'쓰리룸3','매물정보 쓰리룸 1 풀옵션',105,3000,0,'건우부동산',11,51.96,3,1,'개별','유','2021-06-23 18:35:49.958915',2,2,1),(3,'원룸3','매물정보 원룸 3 풀옵션',50,1000,0,'아름매니저부동산',3,30.14,1,1,'개별','유','2021-06-23 18:35:49.959763',3,1,1),(4,'원룸4','매물정보 원룸 4 풀옵션',0,10000,0,'성훈멘토부동산',4,15.06,1,1,'지역','무','2021-06-23 18:35:49.960628',4,1,2),(5,'원룸5','매물정보 원룸 5 풀옵션',0,12000,0,'병민멘토부동산',5,31.75,1,1,'개별','유','2021-06-23 18:35:49.961367',5,1,2),(6,'투룸1','매물정보 투룸 1 풀옵션',65,2000,0,'아란부동산',6,32.89,2,1,'지역','무','2021-06-23 18:35:49.962108',6,2,1),(7,'투룸2','매물정보 투룸 2 풀옵션',75,2500,0,'태우부동산',7,36.7,2,1,'개별','유','2021-06-23 18:35:49.963174',7,2,1),(8,'투룸3','매물정보 투룸 3 풀옵션',70,3000,0,'도윤부동산',8,40.52,2,1,'지역','무','2021-06-23 18:35:49.964204',8,2,1),(9,'투룸4','매물정보 투룸 4 풀옵션',0,15000,0,'민규부동산',9,44.33,2,1,'개별','유','2021-06-23 18:35:49.965067',9,2,2),(10,'투룸5','매물정보 투룸 5 풀옵션',0,18000,0,'민기부동산',10,48.14,2,1,'지역','무','2021-06-23 18:35:49.965918',10,2,2),(11,'쓰리룸1','매물정보 쓰리룸 1 풀옵션',105,3000,0,'건우부동산',11,51.96,3,1,'개별','유','2021-06-23 18:35:49.966864',11,2,1),(12,'쓰리룸2','매물정보 쓰리룸 2 풀옵션',110,3200,0,'유정부동산',12,55.77,3,1,'지역','무','2021-06-23 18:35:49.967998',12,2,1),(13,'쓰리룸3','매물정보 쓰리룸 3 풀옵션',0,23000,0,'선주부동산',13,59.58,3,1,'개별','유','2021-06-23 18:35:49.968865',13,2,2),(14,'쓰리룸4','매물정보 쓰리룸 4 풀옵션',0,27000,0,'경철부동산',14,63.4,3,1,'지역','무','2021-06-23 18:35:49.969735',14,2,2),(15,'쓰리룸5','매물정보 쓰리룸 5 풀옵션',0,0,50000,'지우부동산',15,67.21,3,1,'개별','유','2021-06-23 18:35:49.970767',15,2,3),(16,'오피스텔1','매물정보 오피스텔 1 풀옵션',120,5000,0,'윤성부동산',16,71.02,1,1,'지역','무','2021-06-23 18:35:49.971919',16,3,1),(17,'오피스텔2','매물정보 오피스텔 2 풀옵션',0,29000,0,'송준부동산',17,74.83,2,1,'개별','유','2021-06-23 18:35:49.972682',17,3,2),(18,'오피스텔3','매물정보 오피스텔 3 풀옵션',0,0,34000,'연우멘토님부동산',18,78.65,3,1,'지역','무','2021-06-23 18:35:49.973497',18,3,3),(19,'오피스텔4','매물정보 오피스텔 4 풀옵션',0,0,41000,'정연부동산',19,82.46,1,1,'개별','유','2021-06-23 18:35:49.974231',19,3,3),(20,'오피스텔5','매물정보 오피스텔 5 풀옵션',0,0,19000,'준희부동산',20,86.27,2,1,'지역','무','2021-06-23 18:35:49.975547',20,3,3),(21,'원룸ee1','매물정보ee 원룸 1 풀옵션',30,100,0,'성규부동산',1,10.12,1,1,'개별','유','2021-07-13 13:24:26.869175',21,1,1),(22,'오피스텔3','매물정보 오피스텔 3 풀옵션',0,0,34000,'연우멘토님부동산',18,78.65,3,1,'지역','무','2021-07-14 17:06:42.920205',22,3,3);
/*!40000 ALTER TABLE `rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trade_types`
--

DROP TABLE IF EXISTS `trade_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trade_types` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trade_types`
--

LOCK TABLES `trade_types` WRITE;
/*!40000 ALTER TABLE `trade_types` DISABLE KEYS */;
INSERT INTO `trade_types` VALUES (1,'MONTHLY_RENT'),(2,'DEPOSIT'),(3,'SALE');
/*!40000 ALTER TABLE `trade_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `nick_name` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  `kakao_pk` bigint NOT NULL,
  `profile_url` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-15 13:16:56
