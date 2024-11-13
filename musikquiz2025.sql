/*!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.8-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: musikquiz
-- ------------------------------------------------------
-- Server version	10.11.8-MariaDB-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `config`
--

DROP TABLE IF EXISTS `config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `config` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `value` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `config`
--

LOCK TABLES `config` WRITE;
/*!40000 ALTER TABLE `config` DISABLE KEYS */;
INSERT INTO `config` VALUES
(1,'monitor_round','0'),
(2,'buzzer_blocked','4'),
(10,'final_date','Mar 8 2025  19:30:00'),
(11,'player_correct','0'),
(12,'play_mode','2'),
(13,'play_round','1'),
(14,'buzzer_pressed','4'),
(15,'version','0.9');
/*!40000 ALTER TABLE `config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `last_song`
--

DROP TABLE IF EXISTS `last_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `last_question` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `question` varchar(255) DEFAULT NULL,
  `answer` varchar(255) DEFAULT NULL,
  `image` varchar(64) DEFAULT NULL,
  `comment` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `last_song`
--

LOCK TABLES `last_question` WRITE;
/*!40000 ALTER TABLE `last_song` DISABLE KEYS */;
INSERT INTO `last_question` VALUES
(1,'','','standard.jpg','');
/*!40000 ALTER TABLE `last_song` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `max_songs`
--

DROP TABLE IF EXISTS `max_questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `max_questions` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `round` varchar(64) DEFAULT NULL,
  `maximum` bigint(20) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `max_songs`
--

LOCK TABLES `max_questions` WRITE;
/*!40000 ALTER TABLE `max_songs` DISABLE KEYS */;
INSERT INTO `max_questions` VALUES
(1,'1',20),
(2,'2',20),
(3,'3',20),
(4,'4',20),
(5,'5',25),
(6,'6',25),
(7,'7',30);
/*!40000 ALTER TABLE `max_songs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `play_off`
--

DROP TABLE IF EXISTS `play_off`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `play_off` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `player` bigint(20) unsigned DEFAULT NULL,
  `points` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `name_idx` (`player`),
  CONSTRAINT `fk_name_2` FOREIGN KEY (`player`) REFERENCES `player` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `play_off`
--

LOCK TABLES `play_off` WRITE;
/*!40000 ALTER TABLE `play_off` DISABLE KEYS */;
INSERT INTO `play_off` VALUES
(1,3,0),
(2,7,0),
(3,11,0),
(4,4,0),
(5,8,0),
(6,12,0);
/*!40000 ALTER TABLE `play_off` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `player` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
INSERT INTO `player` VALUES
(1,'Robin'),
(2,'Sahin'),
(3,'Gernot'),
(4,'Cäcilia'),
(5,'Alex'),
(6,'Jessika'),
(7,'Henning'),
(8,'Albertine'),
(9,'Thies'),
(10,'Anatol'),
(11,'Alexander'),
(12,'Karlfried'),
(13,'Yvette'),
(14,'Roselinde'),
(15,'Karl-Heinrich'),
(16,'Xaver');
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player_round`
--

DROP TABLE IF EXISTS `player_round`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `player_round` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `player_round_id` bigint(20) unsigned DEFAULT NULL,
  `player` bigint(20) unsigned DEFAULT NULL,
  `round` bigint(20) unsigned DEFAULT NULL,
  `points` int(11) unsigned DEFAULT NULL,
  `is_active` tinyint(1) unsigned DEFAULT NULL,
  `color` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `name_idx` (`player`),
  KEY `round_idx` (`round`),
  CONSTRAINT `fk_name` FOREIGN KEY (`player`) REFERENCES `player` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_round` FOREIGN KEY (`round`) REFERENCES `round` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_round`
--

LOCK TABLES `player_round` WRITE;
/*!40000 ALTER TABLE `player_round` DISABLE KEYS */;
INSERT INTO `player_round` VALUES
(1,1,1,1,0,1,NULL),
(2,2,2,1,0,1,NULL),
(3,3,3,1,0,1,NULL),
(4,4,4,1,0,1,NULL),
(5,1,5,2,0,1,NULL),
(6,2,6,2,0,1,NULL),
(7,3,7,2,0,1,NULL),
(8,4,8,2,0,1,NULL),
(9,1,9,3,0,1,NULL),
(10,2,10,3,0,1,NULL),
(11,3,11,3,0,1,NULL),
(12,4,12,3,0,1,NULL),
(13,1,3,4,0,1,NULL),
(14,2,7,4,0,1,NULL),
(15,3,11,4,0,1,NULL),
(16,4,4,4,0,1,NULL),
(17,1,1,5,0,1,NULL),
(18,2,5,5,0,1,NULL),
(19,3,10,5,0,1,NULL),
(20,4,7,5,0,1,NULL),
(21,1,9,6,0,1,NULL),
(22,2,3,6,0,1,NULL),
(23,3,2,6,0,1,NULL),
(24,4,6,6,0,1,NULL),
(25,1,1,7,0,1,NULL),
(26,2,9,7,0,1,NULL),
(27,3,5,7,0,1,NULL),
(28,4,13,7,0,1,NULL),
(29,1,1,8,0,1,NULL);
/*!40000 ALTER TABLE `player_round` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `round`
--

DROP TABLE IF EXISTS `round`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `round` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `round` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `round`
--

LOCK TABLES `round` WRITE;
/*!40000 ALTER TABLE `round` DISABLE KEYS */;
INSERT INTO `round` VALUES
(1,'Vorrunde 1'),
(2,'Vorrunde 2'),
(3,'Vorrunde 3'),
(4,'Playoff'),
(5,'Halbfinale 1'),
(6,'Halbfinale 2'),
(7,'Finale'),
(8,'Gewinner'),
(9,'Pause');
/*!40000 ALTER TABLE `round` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `songs`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `questions` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `question` varchar(255) DEFAULT NULL,
  `answer` varchar(255) DEFAULT NULL,
  `round` bigint(20) unsigned DEFAULT NULL,
  `seq` bigint(20) unsigned DEFAULT NULL,
  `played` bigint(20) unsigned DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL,
  `image` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songs`
--

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-13 14:24:40
