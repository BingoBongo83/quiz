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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `config`
--

LOCK TABLES `config` WRITE;
/*!40000 ALTER TABLE `config` DISABLE KEYS */;
INSERT INTO `config` VALUES
(1,'monitor_round','0'),
(2,'buzzer_blocked','0'),
(10,'final_date','Sep 28 2024  19:00:00'),
(11,'player_correct','0'),
(12,'play_mode','1');
/*!40000 ALTER TABLE `config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `last_song`
--

DROP TABLE IF EXISTS `last_song`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `last_song` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `artist` varchar(255) DEFAULT NULL,
  `year` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `last_song`
--

LOCK TABLES `last_song` WRITE;
/*!40000 ALTER TABLE `last_song` DISABLE KEYS */;
INSERT INTO `last_song` VALUES
(1,'','','');
/*!40000 ALTER TABLE `last_song` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `max_songs`
--

DROP TABLE IF EXISTS `max_songs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `max_songs` (
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

LOCK TABLES `max_songs` WRITE;
/*!40000 ALTER TABLE `max_songs` DISABLE KEYS */;
INSERT INTO `max_songs` VALUES
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
(1,2,6),
(2,1,4),
(3,6,4),
(4,5,2),
(5,9,12),
(6,12,6);
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
  `name` varchar(13) DEFAULT NULL,
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
(1,'Kevin'),
(2,'Micha'),
(3,'Collin'),
(4,'Alexandra'),
(5,'Sabine'),
(6,'Thomas'),
(7,'Ron'),
(8,'Simone'),
(9,'Schorch'),
(10,'Biggi'),
(11,'Patrick'),
(12,'Elke'),
(13,'Jörg'),
(14,'Basti'),
(15,'Torsten'),
(16,'Dieter');
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
(13,1,13,4,0,1,NULL),
(14,2,14,4,0,1,NULL),
(15,3,15,4,0,1,NULL),
(16,4,16,4,0,1,NULL),
(17,1,NULL,5,0,1,NULL),
(18,2,NULL,5,0,1,NULL),
(19,3,NULL,5,0,1,NULL),
(20,4,NULL,5,0,1,NULL),
(21,1,NULL,6,0,1,NULL),
(22,2,NULL,6,0,1,NULL),
(23,3,NULL,6,0,1,NULL),
(24,4,NULL,6,0,1,NULL),
(25,1,NULL,7,0,1,NULL),
(26,2,NULL,7,0,1,NULL),
(27,3,NULL,7,0,1,NULL),
(28,4,NULL,7,0,1,NULL),
(29,1,5,8,0,1,NULL);
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
(4,'Vorrunde 4'),
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

DROP TABLE IF EXISTS `songs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `songs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `artist` varchar(255) DEFAULT NULL,
  `round` bigint(20) unsigned DEFAULT NULL,
  `seq` bigint(20) unsigned DEFAULT NULL,
  `played` bigint(20) unsigned DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL,
  `year` bigint(20) unsigned DEFAULT NULL,
  `deadline` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `ux_title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=218 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songs`
--

LOCK TABLES `songs` WRITE;
/*!40000 ALTER TABLE `songs` DISABLE KEYS */;
INSERT INTO `songs` VALUES
(1,'kids in america','kim wilde',1,1,0,'Von ihrem Vater Marty und jüngeren Bruder Ricky produziert',1981,'00:45'),
(3,'moonlight shadow','mike oldfield',1,2,0,'Enya lehnte abe es zu singen, so kam Maggy Reilly',1988,'-'),
(4,'flowers','miley cyrus',1,3,0,'platz 2, 2023',2023,'00:32'),
(5,'knockin´ on heavens door','guns n’ roses',1,4,0,'Original Bob Dylan, gecovert von Eric Clapton, Brian Ferry, Mark Knopfler',1991,'00:52'),
(6,'talkin´ bout a revolution','tracy chapman',1,5,0,'2011 im arabischen Frühling viel gespielt',1988,'-'),
(8,'whatever you want','status quo',1,7,0,'',1979,'01:11'),
(9,'wunder gibt es immer wieder','katja ebstein',1,8,0,'ESC 1970 3. Platz',1970,'01:04'),
(11,'wind of change','scorpions',1,11,0,'LIEDTEXT VORLESEN',1990,'-'),
(12,'basket case','green day',1,23,0,'',1994,'00:54'),
(13,'don´t stop believin´','journey',1,10,0,'beste stück mit Steve Perry',1981,'01:20'),
(14,'cotton eye joe','rednex',1,12,0,'',1994,'01:25'),
(15,'the logical song','supertramp',1,16,0,'Rodger Hodgsons geniale Stimme',1979,'-'),
(17,'ein kompliment','sportfreunde stiller',1,15,0,'2024 3faches Gold erhalten',2002,'00:59'),
(19,'africa','toto',1,14,0,'der einzige No1 Hit von Toto in US',1982,'-'),
(20,'forever young','alphaville',1,17,0,'Alphaville hieß zuerst Forever young',1984,'00:56'),
(21,'the look','roxette',2,1,0,'nach Abba und Rednex die besten Schweden',1988,'-'),
(22,'dancing with tears in my eyes','ultravox',2,2,0,'',1984,'-'),
(23,'love yourself','justin bieber',2,3,0,'geschrieben von Ed Sheeran',2015,'00:57'),
(24,'bobby brown (goes down)','frank zappa',2,4,0,'Boykott der US Radios verhinderte Charteintritt',1979,'02:03'),
(25,'wonderwall','oasis',2,5,0,'Brüder Noel und Liam Gallagher',1995,'-'),
(26,'what is love','haddaway',2,6,0,'Nestor Alexander Haddaway, Dr. Phil (USA/Washington), Ab 1989 in Köln, spielte bis 1993 bei den Cologne Crocodiles',1993,'-'),
(28,'far far away','slade',2,7,0,'gute coverversion von den Toten Hosen',1974,'00:43'),
(29,'safety dance','men without hats',2,9,0,'Kanadier',1983,'-'),
(30,'hotel california','eagles',2,10,0,'geniale performance des Schlagzeugers Don Henley',1976,'-'),
(31,'venus','shocking blue',2,11,0,'LIEDTEXT VORLESEN',1969,'-'),
(32,'sweet caroline','neil diamond',2,13,0,'angeblich für caroline kennedy geschrieben',1969,'02:00'),
(33,'coco jamboo','mr. president',2,12,0,'als Panflöten noch in die deutschen Charts einziehen durften',1996,'-'),
(34,'purple rain','prince',2,24,0,'',1984,'00:44'),
(35,'total eclipse of the heart','bonny tyler',2,18,0,'Von Jim Steinman, wurde zuerst Meat Loaf angeboten',1982,'01:44'),
(37,'99 luftballons','nena',2,19,0,'',1983,'-'),
(38,'our house','madness',2,20,0,'letzter song',1982,'00:43'),
(39,'waterloo','abba',2,16,0,'ESC 1974 Platz1, erster Abba Song auf No1 in Norwegen',1974,'00:31'),
(40,'video killed the radio star','the buggles',2,17,0,'Im Musikvideo ist Hans Zimmer zu sehen',1979,'00:49'),
(41,'personal jesus','depeche mode',3,1,0,'2002 von Johnny Cash gecovert',1990,'-'),
(42,'in the army now','status quo',3,2,0,'original von bolland & bolland (1981)',1986,'-'),
(43,'don´t you','simple minds',3,3,0,'nie auf einem Studioalbum erschienen',1985,'-'),
(44,'out of the dark','falco',3,4,0,'+6.2.98, Album 3 Wochen postum veröffentlicht (27.02), Single 6 wochen (20.03.)',1998,'00:55'),
(45,'nothing compares to u','sinnead o’connor',3,5,0,'im original von Prince geschrieben und der Band „The Family“ 1985 veröffentlicht',1990,'01:11'),
(46,'blue (da ba dee)','Eiffel 65',3,6,0,'29 Wochen PLatz 1 in Deutschland',1999,'00:32'),
(48,'sweet dreams (are made of this)','eurythmics',3,7,0,'von dave steward produziert, handelt von deren Trennung',1983,'-'),
(49,'bayern','die toten hosen',3,15,0,'',1999,'-'),
(50,'handy, schlüssel , portemonnaie','ikke hüftgold',3,13,0,'',2024,'-'),
(51,'rivers of babylon','boney m.',3,10,0,'Original: The Melodians (1970)',1979,'01:38'),
(52,'74-75','the connells',3,25,0,'',1993,'00:45'),
(53,'sexbomb','tom jones, mousse t',3,14,0,'',1999,'00:46'),
(54,'i love rock´n´roll','joan jett',3,11,0,'LIEDTEXT VORLESEN',1986,'01:26'),
(55,'wouldn´t it be good','nik kershaw',3,9,0,'',1984,'01:14'),
(56,'streets of philadelphia','bruce springsteen',3,17,0,'bekanntes drum intro',1993,'-'),
(57,'the best','tina turner',3,18,0,'zuerst von bonnie tyler veröffentlicht',1989,'01:03'),
(58,'feel','robbie williams',3,19,0,'',2002,'00:46'),
(59,'all that she wants','ace of base',3,16,0,'',1992,'00:50'),
(60,'texas hold´em','beyonce',3,20,0,'',2024,'-'),
(61,'just can´t get enough','depeche mode',4,1,0,'nie in den deutschen charts platziert gewesen',1981,'-'),
(62,'i promised myself','nick kamen',4,2,0,'Das Levis Modell Nick Kamen',1990,'-'),
(63,'i’m too sexy','right said fred',4,3,0,'Bandname basiert auf dem Hi von Bernhard Cribbins (1962)',1991,'-'),
(64,'you win again','bee gees',4,4,0,'',1987,'00:56'),
(65,'save tonight','eagle eye cherry',4,5,0,'Eagle-Eye Lanoo Cherry, Sohn des Jazz Trompeters Don Cherry',1997,'00:49'),
(66,'angels','robbie williams',4,6,0,'',1997,'01:00'),
(67,'meine liebe, meine stadt, mein verein','domstürmer',4,7,0,'',2008,'-'),
(68,'live is life','opus',4,8,0,'',1984,'00:50'),
(69,'bad guy','billie eilish',4,9,0,'',2019,'00:56'),
(70,'komet','udo lindenberg, apache 207',4,10,0,'',2023,'00:44'),
(71,'what a feeling','irene cara',4,11,0,'LIEDTEXT',1983,'01:08'),
(72,'everywhere','fleetwood mac',4,12,0,'',1987,'-'),
(73,'westerland','die ärzte',4,14,0,'',1988,'01:21'),
(74,'go west','pet shop boys',4,15,0,'',1993,'01:07'),
(75,'life is for living','barclay james harvest',4,24,0,'',1981,'-'),
(76,'i want to know what love is','foreigner',4,16,0,'',1984,'01:34'),
(77,'whiskey in the jar','thin lizzy',4,18,0,'',1972,'-'),
(78,'großstadtrevier','truck stop',4,19,0,'',1986,'-'),
(80,'stumblin´ in','chris norman, suzi quattro',4,21,0,'stechen',1978,'01:11'),
(81,'back for good','take that',5,1,0,'die ultimative girlband der 90er',1995,'00:57'),
(82,'the boys of summer','don henley',5,2,0,'schlagzeuger der eagles',1984,'01:11'),
(83,'dreams are ten a penny','john kincade',5,3,0,'hat john carter gesungen',1972,'00:41'),
(84,'your love','the outfield',5,4,0,'Tony Lewis geniale stimme',1985,'-'),
(85,'black velvet','alannah myles',5,5,0,'',1989,'00:55'),
(86,'kokomo','the beach boys',5,6,0,'',1988,'-'),
(87,'l´amour toujours','gigi d’agostino',5,7,0,'',1999,'-'),
(88,'saturday night','whigfield',5,8,0,'',1994,'-'),
(89,'der puppenspieler von mexico','roberto blanco',5,9,0,'tom jones – the young new mexican puppeteer',1973,'01:02'),
(90,'blueprint','rainbirds',5,10,0,'',1987,'-'),
(91,'let it be','the beatles',5,16,0,'LIEDTEXT VORLESEN',1970,'-'),
(92,'big in japan','alphaville',5,12,0,'',1984,'01:19'),
(93,'das schönste mädchen vom westerwald','höhner',5,13,0,'',1989,'01:14'),
(94,'valerie','amy winehouse',5,14,0,'',2006,'00:40'),
(95,'whole lotta love','led zeppelin',5,15,0,'',1969,'00:35'),
(96,'runaway','bon jovi',5,11,0,'',1984,'00:56'),
(97,'manchmal möchte ich schon mit dir','roland kaiser',5,17,0,'',1983,'00:57'),
(98,'wellenreiter','bap',5,29,0,'',1982,'-'),
(99,'another one bites the dust','queen',5,29,0,'',1980,'00:41'),
(100,'down under','men at work',5,20,0,'',1981,'00:29'),
(101,'in my mind','dynoro, gigi d’agostino',5,21,0,'',2018,'-'),
(102,'poker face','lady gaga',5,22,0,'',2008,'00:55'),
(103,'dear mr. President','pink, indigo girls',5,25,0,'',2006,'-'),
(104,'piano man','billy joel',5,23,0,'',1973,'01:25'),
(105,'come together','the beatles',5,24,0,'',1969,'01:09'),
(106,'you´re the voice','john farnham',6,1,0,'',1986,'01:08'),
(107,'the free electric band','albert hammond',6,2,0,'',1973,'00:46'),
(108,'smooth criminal','michael jackson',6,3,0,'',1987,'01:34'),
(109,'this flight tonight','nazareth',6,4,0,'',1973,'-'),
(110,'wicked game','chris isaak',6,28,0,'',1989,'01:43'),
(111,'Played-a-live','safri duo',6,6,0,'',2001,'-'),
(112,'ne kölsche jung','willy millowitsch',6,7,0,'',1963,'-'),
(113,'the rhythm of the night','corona',6,8,0,'',1995,'00:27'),
(114,'i´m so excited','the pointer sisters',6,9,0,'',1982,'00:57'),
(116,'let me entertain you','robbie williams',6,10,0,'',1997,'00:39'),
(117,'you sexy thing','hot chocolate',6,11,0,'',1975,'-'),
(118,'sunglasses at night','corey hart',6,16,0,'LIEDTEXT VORLESEN',1984,'00:30'),
(119,'am tag als conny cramer starb','juliane werding',6,13,0,'',1972,'00:57'),
(120,'don´t you want me','the human league',6,15,0,'',1981,'00:52'),
(121,'gloria','laura branigan',6,20,0,'',1982,'00:58'),
(122,'dreamer','ozzy osbourne',6,12,0,'',2001,'00:59'),
(123,'back to black','amy winehouse',6,18,0,'',2006,'-'),
(124,'orinoco flow','enya',6,19,0,'',1988,'-'),
(125,'i still haven´t found what i´m looking for','u2',6,26,0,'',1987,'01:05'),
(126,'blurred lines','robin thicke,pharell williams',6,14,0,'',2013,'01:06'),
(127,'waka waka (this time for africa)','shakira, freshlyground',6,23,0,'',2010,'00:52'),
(128,'driver´s seat','sniff’n’ the tears',6,22,0,'',1978,'-'),
(129,'heroes','david bowie',6,24,0,'',1977,'-'),
(130,'Ob-la-di, ob-la-da','the beatles',6,17,0,'',1968,'00:26'),
(131,'don´t leave me this way','the communards, sarah jane morris',7,1,0,'',1986,'-'),
(132,'love is a shield','camouflage',7,2,0,'',1989,'-'),
(133,'der letztze wage es immer ne kombi','jp weber',7,3,0,'',2018,'-'),
(134,'rhythm is a dancer','snap!',7,4,0,'',1992,'-'),
(135,'the bad touch','bloudhound gang',7,5,0,'',1999,'01:12'),
(136,'the one and only','chesney hawkes',7,6,0,'',1991,'-'),
(137,'tearin´ up my heart','nsync',7,7,0,'',1997,'-'),
(138,'comfortably numb','pink floyd',7,8,0,'',1979,'-'),
(139,'maria magdalena','sandra',7,9,0,'',1985,'01:02'),
(140,'chery chery lady','modern talking',7,10,0,'',1985,'00:42'),
(142,'here comes the rain again','eurythmics, annie lennox, dave stewart',7,13,0,'',1983,'-'),
(143,'nessaja','scooter',7,14,0,'',2002,'-'),
(144,'school','supertramp',7,15,0,'',1974,'-'),
(145,'enola gay','orchestral manoeuvres in the dark (OMD)',7,11,0,'',1980,'-'),
(146,'da da da ich lieb dich nicht du liebst mich nicht aha aha aha','trio',7,17,0,'',1982,'-'),
(147,'how much is the fish','scooter',7,16,0,'LIEDTEXT VORLESEN',1998,'00:41'),
(148,'money','pink floyd',7,18,0,'',1973,'-'),
(149,'sound like a melody','alphaville',7,36,0,'',1984,'01:00'),
(150,'all my loving','the beatles',7,20,0,'',1963,'-'),
(151,'born to be alive','patrick hernandez',7,22,0,'',1978,'-'),
(152,'livin´ on a prayer','bon jovi',7,23,0,'',1986,'01:38'),
(153,'everybody wants to rule the world','tears for fears',7,25,0,'',1985,'00:52'),
(154,'hit the road jack','ray charles',7,27,0,'',1961,'-'),
(155,'i got you babe','Sonny & cher',7,32,0,'',1965,'-'),
(156,'you´ll never walk alone','Gerry & the pacemakers',7,24,0,'Noch 5 songs',1963,'01:29'),
(157,'wenn du denkst du denkst dann denkst du nur du denkst','juliane werding',7,33,0,'',1975,'00:58'),
(158,'zigeunerjunge','alexandra',7,28,0,'klub27',1967,'00:49'),
(159,'back in black','AC/DC',7,21,0,'',1980,'-'),
(160,'lay all your love on me','abba',7,19,0,'letzter song',1980,'01:13'),
(166,'i want to break free','queen',1,20,0,'wie viele andere  gute Songs von Queen von Bassist John Deacon geschrieben ( Another One Bites the Dust, Friends Will Be Friends und Spread Your Wings)',1984,NULL),
(168,'vienna','ultravox',1,25,0,'New Wave',1980,NULL),
(169,'ruby tuesday','scorpions',1,21,0,'ursprünglich rolling stones',2011,NULL),
(170,'got my mind set on you','george harrison',1,22,0,'im original von james ray, 1962',1987,NULL),
(171,'ring of fire','johnny cash',2,8,0,'geschrieben von seiner geliebten June Carter',1963,NULL),
(173,'es gibt kein bier auf hawaii','paul kuhn',2,21,0,'stechen',1963,NULL),
(174,'über sieben brücken musst du gehn','karat',2,14,0,'nicht alles in DDR war schlecht',1979,NULL),
(175,'i don´t like mondays','the boomtown rats',2,23,0,'bob geldof',1979,NULL),
(177,'( i just) died in your arms','cutting crew',3,22,0,'stechen',1986,NULL),
(178,'take on me','a-ha',3,23,0,'1 von 2 offiziellen videos bei youtube mit 1 millarde views (neben sweet child of mine)',1985,NULL),
(179,'believe','cher',3,24,0,'stechen',1998,NULL),
(181,'st elmo´s fire','john parr',4,20,0,'letzter song',1985,NULL),
(182,'sailing','rod stewart',4,22,0,'stechen',1975,NULL),
(183,'it´s a heartache','bonnie tyler',4,23,0,'stechen',1977,NULL),
(186,'ich war noch niemals in new york','udo jürgens',5,26,0,'',1982,NULL),
(187,'santa maria','roland kaiser',5,27,0,'',1980,NULL),
(188,'ab in den süden','buddy',6,21,0,'stechen',2004,NULL),
(189,'leuchtturm','nena',6,25,0,'stechen',1983,NULL),
(190,'here i go again','whitesnake',7,31,0,'stechen',1982,NULL),
(191,'radar love','golden earring',7,34,0,'stechen',1973,NULL),
(192,'the riddle','nick kershaw',7,35,0,'stechen',1984,NULL),
(193,'tainted love','soft cell',7,30,0,'im original von ed cobb',1981,NULL),
(194,'egoist','falco',7,12,0,'stechen',1998,NULL),
(196,'i walk the line','johnny cash',1,6,0,'mit günter loose in landshut auf deutsch aufgenommen',1956,NULL),
(197,'ne besuch em zoo','horst muys',1,13,0,'starb mit 45, wurde auf seiner beerdigung gespielt',1971,NULL),
(198,'amsterdam','cora',1,18,0,'Die adeligen Schwestern Cornelia und Swetlana von dem Bottlenberg',2004,NULL),
(199,'oben unten','räuber',2,15,0,'Song des Spicher Dreigestirns der noch bestehenden Session',2023,NULL),
(200,'alle jläser huh','kasalla',3,8,0,NULL,2015,NULL),
(201,'in the ghetto','elvis presley',4,13,0,'Elvis einziger No1 Hit in Deutschland',1969,NULL),
(203,'walk of life','dire straits',1,9,0,NULL,1985,NULL),
(204,'when i´m sixty four','the beatles',5,28,0,'',1967,NULL),
(205,'you can´t hurry love','phil collins',6,27,0,NULL,1982,NULL),
(206,'i want it that way','backstreet boys',3,12,0,NULL,NULL,NULL),
(207,'boombastic','shaggy',4,17,0,'levis werbespot',1995,NULL),
(208,'love is everywhere','caught in the act',5,18,0,NULL,1995,NULL),
(209,'wellerman','nathan evans',6,5,0,NULL,2021,NULL),
(210,'blinding lights','the weeknd',5,19,0,'Top HIt 2020',2020,NULL),
(211,'am fenster','city',7,26,0,NULL,NULL,NULL),
(212,'leev linda lou','bläck föös',7,29,0,NULL,NULL,NULL),
(213,'fade to grey','visage',1,19,0,'',1980,NULL),
(214,'talk','coldplay',3,21,0,'Hook aus Computerliebe / Kraftwerk',2005,NULL),
(215,'alles aus liebe','die toten hosen',2,22,0,NULL,1993,NULL),
(216,'it´s like that','run d.m.c., jason nevins',2,25,0,NULL,1998,NULL),
(217,'nver ending story','limahl',4,25,0,NULL,1984,NULL);
/*!40000 ALTER TABLE `songs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-24 10:51:47
