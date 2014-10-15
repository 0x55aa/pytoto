-- MySQL dump 10.13  Distrib 5.5.38, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: pytoto
-- ------------------------------------------------------
-- Server version	5.5.38-0ubuntu0.12.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_profile`
--

DROP TABLE IF EXISTS `accounts_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `level` int(11) NOT NULL,
  `topic_count` int(11) NOT NULL,
  `post_count` int(11) NOT NULL,
  `avatar_url` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `user_id_refs_id_76babe75` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_profile`
--

/*!40000 ALTER TABLE `accounts_profile` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_profile` ENABLE KEYS */;

--
-- Table structure for table `accounts_userlog`
--

DROP TABLE IF EXISTS `accounts_userlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_userlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `des` varchar(200) NOT NULL,
  `c_time` datetime NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `object_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_userlog_6340c63c` (`user_id`),
  KEY `accounts_userlog_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_16db6531` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_31da63fd` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_userlog`
--

/*!40000 ALTER TABLE `accounts_userlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_userlog` ENABLE KEYS */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add profile',7,'add_profile'),(20,'Can change profile',7,'change_profile'),(21,'Can delete profile',7,'delete_profile'),(22,'Can add user log',8,'add_userlog'),(23,'Can change user log',8,'change_userlog'),(24,'Can delete user log',8,'delete_userlog'),(25,'Can add site',9,'add_site'),(26,'Can change site',9,'change_site'),(27,'Can delete site',9,'delete_site'),(28,'Can add category',10,'add_category'),(29,'Can change category',10,'change_category'),(30,'Can delete category',10,'delete_category'),(31,'Can add forum',11,'add_forum'),(32,'Can change forum',11,'change_forum'),(33,'Can delete forum',11,'delete_forum'),(34,'Can add topic type',12,'add_topictype'),(35,'Can change topic type',12,'change_topictype'),(36,'Can delete topic type',12,'delete_topictype'),(37,'Can add tag',13,'add_tag'),(38,'Can change tag',13,'change_tag'),(39,'Can delete tag',13,'delete_tag'),(40,'Can add topic',14,'add_topic'),(41,'Can change topic',14,'change_topic'),(42,'Can delete topic',14,'delete_topic'),(43,'Can add post',15,'add_post'),(44,'Can change post',15,'change_post'),(45,'Can delete post',15,'delete_post'),(46,'Can add attachment',16,'add_attachment'),(47,'Can change attachment',16,'change_attachment'),(48,'Can delete attachment',16,'delete_attachment');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$a3n8T761pOoI$ZcOlJsVEGFuC0YTnGVbZF2dQB7unCNS941TNiFBcWSY=','2014-08-12 08:40:29',1,'admin','','','a0x55aa@foxmail.com',1,1,'2014-08-12 08:40:29');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'profile','accounts','profile'),(8,'user log','accounts','userlog'),(9,'site','forum','site'),(10,'category','forum','category'),(11,'forum','forum','forum'),(12,'topic type','topic','topictype'),(13,'tag','topic','tag'),(14,'topic','topic','topic'),(15,'post','topic','post'),(16,'attachment','topic','attachment');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

--
-- Table structure for table `forum_category`
--

DROP TABLE IF EXISTS `forum_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forum_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `slug` varchar(32) DEFAULT NULL,
  `ordering` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_category`
--

/*!40000 ALTER TABLE `forum_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `forum_category` ENABLE KEYS */;

--
-- Table structure for table `forum_forum`
--

DROP TABLE IF EXISTS `forum_forum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forum_forum` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `slug` varchar(32) DEFAULT NULL,
  `ordering` int(11) NOT NULL,
  `description` varchar(100) NOT NULL,
  `created_on` datetime NOT NULL,
  `topic_count` int(11) NOT NULL,
  `post_count` int(11) NOT NULL,
  `today_post_count` int(11) NOT NULL,
  `post_count_day` date NOT NULL,
  `last_replay_on` datetime DEFAULT NULL,
  `last_post_user_id` int(11) DEFAULT NULL,
  `last_post_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`),
  KEY `forum_forum_6f33f001` (`category_id`),
  KEY `forum_forum_8e07095b` (`last_post_user_id`),
  KEY `forum_forum_9e222a3a` (`last_post_id`),
  CONSTRAINT `last_post_id_refs_id_9cdda98a` FOREIGN KEY (`last_post_id`) REFERENCES `topic_post` (`id`),
  CONSTRAINT `category_id_refs_id_e1edd574` FOREIGN KEY (`category_id`) REFERENCES `forum_category` (`id`),
  CONSTRAINT `last_post_user_id_refs_id_b00bcc23` FOREIGN KEY (`last_post_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_forum`
--

/*!40000 ALTER TABLE `forum_forum` DISABLE KEYS */;
/*!40000 ALTER TABLE `forum_forum` ENABLE KEYS */;

--
-- Table structure for table `forum_site`
--

DROP TABLE IF EXISTS `forum_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forum_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `value` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_site`
--

/*!40000 ALTER TABLE `forum_site` DISABLE KEYS */;
/*!40000 ALTER TABLE `forum_site` ENABLE KEYS */;

--
-- Table structure for table `topic_attachment`
--

DROP TABLE IF EXISTS `topic_attachment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topic_attachment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slug` varchar(32) NOT NULL,
  `name` varchar(32) NOT NULL,
  `display_name` varchar(32) NOT NULL,
  `created_on` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topic_attachment`
--

/*!40000 ALTER TABLE `topic_attachment` DISABLE KEYS */;
/*!40000 ALTER TABLE `topic_attachment` ENABLE KEYS */;

--
-- Table structure for table `topic_post`
--

DROP TABLE IF EXISTS `topic_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topic_post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic_id` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `update_user_id` int(11) DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  `floor` int(11) NOT NULL,
  `content` longtext NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `deleted_by_id` int(11) DEFAULT NULL,
  `deleted_on` datetime DEFAULT NULL,
  `reply_email` tinyint(1) NOT NULL,
  `sort_order` int(11) NOT NULL,
  `reply_count` int(11) NOT NULL,
  `spam_count` int(11) NOT NULL,
  `like_count` int(11) NOT NULL,
  `reply_user_count` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `topic_post_76f18ad3` (`topic_id`),
  KEY `topic_post_410d0aac` (`parent_id`),
  KEY `topic_post_6340c63c` (`user_id`),
  KEY `topic_post_94f2480a` (`update_user_id`),
  KEY `topic_post_7fc0c793` (`deleted_by_id`),
  CONSTRAINT `topic_id_refs_id_625d347d` FOREIGN KEY (`topic_id`) REFERENCES `topic_topic` (`id`),
  CONSTRAINT `deleted_by_id_refs_id_05b28250` FOREIGN KEY (`deleted_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `parent_id_refs_id_ea9b2090` FOREIGN KEY (`parent_id`) REFERENCES `topic_post` (`id`),
  CONSTRAINT `update_user_id_refs_id_05b28250` FOREIGN KEY (`update_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `user_id_refs_id_05b28250` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topic_post`
--

/*!40000 ALTER TABLE `topic_post` DISABLE KEYS */;
/*!40000 ALTER TABLE `topic_post` ENABLE KEYS */;

--
-- Table structure for table `topic_tag`
--

DROP TABLE IF EXISTS `topic_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topic_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `topic_count` int(11) NOT NULL,
  `slug` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topic_tag`
--

/*!40000 ALTER TABLE `topic_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `topic_tag` ENABLE KEYS */;

--
-- Table structure for table `topic_topic`
--

DROP TABLE IF EXISTS `topic_topic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topic_topic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `forum_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  `update_user_id` int(11) DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  `topic_type_id` int(11) DEFAULT NULL,
  `subject` varchar(100) NOT NULL,
  `slug` varchar(32) DEFAULT NULL,
  `last_reply_on` datetime DEFAULT NULL,
  `last_reply_user_id` int(11) NOT NULL,
  `sort_order` int(11) NOT NULL,
  `reply_count` int(11) NOT NULL,
  `view_count` int(11) NOT NULL,
  `spam_count` int(11) NOT NULL,
  `like_count` int(11) NOT NULL,
  `reply_user_count` int(11) NOT NULL,
  `closed` tinyint(1) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `essence` tinyint(1) NOT NULL,
  `sticky` tinyint(1) NOT NULL,
  `homepage` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `topic_topic_f979685d` (`forum_id`),
  KEY `topic_topic_6340c63c` (`user_id`),
  KEY `topic_topic_94f2480a` (`update_user_id`),
  KEY `topic_topic_ba636318` (`topic_type_id`),
  KEY `topic_topic_23951b80` (`last_reply_user_id`),
  CONSTRAINT `forum_id_refs_id_195c33c3` FOREIGN KEY (`forum_id`) REFERENCES `forum_forum` (`id`),
  CONSTRAINT `last_reply_user_id_refs_id_23e185c7` FOREIGN KEY (`last_reply_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `topic_type_id_refs_id_f3bcd02d` FOREIGN KEY (`topic_type_id`) REFERENCES `topic_topictype` (`id`),
  CONSTRAINT `update_user_id_refs_id_23e185c7` FOREIGN KEY (`update_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `user_id_refs_id_23e185c7` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topic_topic`
--

/*!40000 ALTER TABLE `topic_topic` DISABLE KEYS */;
/*!40000 ALTER TABLE `topic_topic` ENABLE KEYS */;

--
-- Table structure for table `topic_topic_tag`
--

DROP TABLE IF EXISTS `topic_topic_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topic_topic_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `topic_id` (`topic_id`,`tag_id`),
  KEY `topic_topic_tag_76f18ad3` (`topic_id`),
  KEY `topic_topic_tag_5659cca2` (`tag_id`),
  CONSTRAINT `topic_id_refs_id_043f2844` FOREIGN KEY (`topic_id`) REFERENCES `topic_topic` (`id`),
  CONSTRAINT `tag_id_refs_id_3b602662` FOREIGN KEY (`tag_id`) REFERENCES `topic_tag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topic_topic_tag`
--

/*!40000 ALTER TABLE `topic_topic_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `topic_topic_tag` ENABLE KEYS */;

--
-- Table structure for table `topic_topictype`
--

DROP TABLE IF EXISTS `topic_topictype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topic_topictype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `forum_id` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `slug` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`),
  KEY `topic_topictype_f979685d` (`forum_id`),
  CONSTRAINT `forum_id_refs_id_be484e18` FOREIGN KEY (`forum_id`) REFERENCES `forum_forum` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topic_topictype`
--

/*!40000 ALTER TABLE `topic_topictype` DISABLE KEYS */;
/*!40000 ALTER TABLE `topic_topictype` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-08-12 16:42:06
