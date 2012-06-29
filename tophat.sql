-- MySQL dump 10.13  Distrib 5.5.24, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: tophat
-- ------------------------------------------------------
-- Server version	5.5.24-0ubuntu0.12.04.1

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
-- Table structure for table `api_keys`
--

DROP TABLE IF EXISTS `api_keys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `api_keys` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `key` char(64) NOT NULL,
  `group_id` smallint(5) unsigned NOT NULL,
  `user_id` mediumint(8) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_keys`
--

LOCK TABLES `api_keys` WRITE;
/*!40000 ALTER TABLE `api_keys` DISABLE KEYS */;
INSERT INTO `api_keys` VALUES (1,'73640de25b7d656733ce2f808a330f18cfc26385c2003a3674b57cab555aa1b2',1,1);
/*!40000 ALTER TABLE `api_keys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_types`
--

DROP TABLE IF EXISTS `game_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `game_types` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `name` char(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_types`
--

LOCK TABLES `game_types` WRITE;
/*!40000 ALTER TABLE `game_types` DISABLE KEYS */;
INSERT INTO `game_types` VALUES (1,'Assassin'),(2,'QRZar'),(3,'Random Game 3');
/*!40000 ALTER TABLE `game_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `games` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `name` char(255) NOT NULL,
  `game_type_id` smallint(5) unsigned NOT NULL,
  `creator` mediumint(8) unsigned NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `creator` (`creator`),
  FULLTEXT KEY `name_ft` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES (1,'Testing Assasin',1,1,'2012-06-05 12:12:30'),(2,'Testing QRZar',2,1,'2012-06-05 12:12:30'),(3,'CS2015 Assassin',1,2,'2012-06-05 12:12:30'),(4,'CS2014 Assassin',1,1,'2012-06-05 12:12:30'),(5,'RAG Week',1,3,'2012-06-05 12:12:30');
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `games_meta`
--

DROP TABLE IF EXISTS `games_meta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `games_meta` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `game_id` mediumint(8) unsigned NOT NULL,
  `key` char(30) NOT NULL,
  `value` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key_game_id` (`key`,`game_id`),
  KEY `game_id` (`game_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games_meta`
--

LOCK TABLES `games_meta` WRITE;
/*!40000 ALTER TABLE `games_meta` DISABLE KEYS */;
/*!40000 ALTER TABLE `games_meta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group_perms`
--

DROP TABLE IF EXISTS `group_perms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `group_perms` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `group_id` smallint(5) unsigned NOT NULL,
  `perm_id` mediumint(8) unsigned NOT NULL,
  `value` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `group_id` (`group_id`),
  KEY `perm_id` (`perm_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group_perms`
--

LOCK TABLES `group_perms` WRITE;
/*!40000 ALTER TABLE `group_perms` DISABLE KEYS */;
/*!40000 ALTER TABLE `group_perms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groups`
--

DROP TABLE IF EXISTS `groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `groups` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `name` char(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups`
--

LOCK TABLES `groups` WRITE;
/*!40000 ALTER TABLE `groups` DISABLE KEYS */;
INSERT INTO `groups` VALUES (1,'Standard');
/*!40000 ALTER TABLE `groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kills`
--

DROP TABLE IF EXISTS `kills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kills` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `killer_player_id` mediumint(8) NOT NULL,
  `victim_player_id` mediumint(8) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `verified` tinyint(1) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `killer_user_id` (`killer_player_id`),
  KEY `victim_usr_id` (`victim_player_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kills`
--

LOCK TABLES `kills` WRITE;
/*!40000 ALTER TABLE `kills` DISABLE KEYS */;
INSERT INTO `kills` VALUES (1,1,2,'2012-05-22 16:09:02',1),(2,1,5,'2012-05-22 16:09:29',0),(3,1,5,'2012-05-22 16:09:34',1),(4,2,5,'2012-05-22 16:09:40',1),(5,1,2,'2012-05-22 16:09:48',1),(6,2,5,'2012-05-22 16:09:56',0),(7,2,1,'2012-05-22 16:10:05',1),(8,3,4,'2012-05-22 16:10:20',1),(9,3,6,'2012-05-22 16:10:23',1),(10,6,3,'2012-05-22 16:10:31',1),(11,3,4,'2012-05-22 16:10:47',0),(12,4,3,'2012-05-22 16:10:57',1);
/*!40000 ALTER TABLE `kills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perms`
--

DROP TABLE IF EXISTS `perms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `perms` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `key` char(25) NOT NULL,
  `name` char(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `key` (`key`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perms`
--

LOCK TABLES `perms` WRITE;
/*!40000 ALTER TABLE `perms` DISABLE KEYS */;
/*!40000 ALTER TABLE `perms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `players` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `name` char(60) DEFAULT NULL,
  `photo` char(32) DEFAULT NULL,
  `game_id` mediumint(8) unsigned NOT NULL,
  `user_id` mediumint(8) unsigned NOT NULL,
  `lat` float(10,6) DEFAULT NULL,
  `lon` float(10,6) DEFAULT NULL,
  `score` smallint(5) DEFAULT '0',
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `game_id` (`game_id`),
  KEY `user_id` (`user_id`),
  KEY `lat` (`lat`),
  KEY `lon` (`lon`),
  FULLTEXT KEY `name_ft` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES (1,'specialk',NULL,1,1,NULL,NULL,6438,'2012-05-22 15:56:49'),(2,'arboroia',NULL,1,2,NULL,NULL,3456,'2012-05-22 16:00:12'),(3,'specialk [IRL]',NULL,3,1,NULL,NULL,123,'2012-05-22 16:02:31'),(4,'arboroia is god',NULL,3,2,NULL,NULL,2345,'2012-05-22 16:03:42'),(5,'tester',NULL,1,3,NULL,NULL,2845,'2012-05-22 16:07:32'),(6,'tester',NULL,3,3,NULL,NULL,1745,'2012-05-22 16:07:49'),(7,'Meme','357843259b856611ebf03f17dfee2d77',1,4,NULL,NULL,32767,'2012-05-22 16:54:10');
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `players_meta`
--

DROP TABLE IF EXISTS `players_meta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `players_meta` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `player_id` mediumint(8) unsigned NOT NULL,
  `key` char(30) NOT NULL,
  `value` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key_player_id` (`player_id`,`key`),
  KEY `player_id` (`player_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players_meta`
--

LOCK TABLES `players_meta` WRITE;
/*!40000 ALTER TABLE `players_meta` DISABLE KEYS */;
/*!40000 ALTER TABLE `players_meta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_games`
--

DROP TABLE IF EXISTS `user_games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_games` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` mediumint(8) unsigned NOT NULL,
  `game_id` mediumint(8) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `game_id` (`game_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_games`
--

LOCK TABLES `user_games` WRITE;
/*!40000 ALTER TABLE `user_games` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `name` char(60) NOT NULL,
  `photo` char(32) DEFAULT NULL,
  `email` char(255) NOT NULL,
  `password` char(69) DEFAULT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `password` (`password`),
  FULLTEXT KEY `name_ft` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Kevin Baker','354d7eff555998e420c54226cb4dc494','banana@tophat.ie','PBKDF2$sha256$10000$tsj+apzeZCr6yxZ/$aBCcCOilE2+m9ao50PmbxFiPNZ0OWzgs','2012-06-05 10:52:57'),(2,'Kevin Bluett','hfdkjfhakj55998e420c54226cb4dc49','kevin@tophat.ie',NULL,'2012-06-05 10:52:57'),(3,'Test Subject 1','4aa499b089dff5d89ba44c5281ac883c','ts1@tophat.ie',NULL,'2012-06-05 10:52:57'),(4,'Testing Subject 2','357843259b856611ebf03f17dfee2d77','ts2@tophat.ie',NULL,'2012-06-05 10:52:57');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_meta`
--

DROP TABLE IF EXISTS `users_meta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_meta` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` mediumint(8) unsigned NOT NULL,
  `key` char(30) NOT NULL,
  `value` text NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key_user_id` (`key`,`user_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_meta`
--

LOCK TABLES `users_meta` WRITE;
/*!40000 ALTER TABLE `users_meta` DISABLE KEYS */;
INSERT INTO `users_meta` VALUES (1,1,'alternate','other'),(2,1,'upgrades','[\'lolnade\', \'bomb\', \'claymore\']');
/*!40000 ALTER TABLE `users_meta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-06-29 15:53:54
