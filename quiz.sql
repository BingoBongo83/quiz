/*!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.8-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: quiz
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
(10,'final_date','Dec 19 2024  18:00:00'),
(11,'player_correct','0'),
(12,'play_mode','1'),
(13,'play_round','1'),
(14,'buzzer_pressed','4'),
(15,'version','0.9');
/*!40000 ALTER TABLE `config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `last_question`
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
-- Dumping data for table `last_question`
--

LOCK TABLES `last_question` WRITE;
/*!40000 ALTER TABLE `last_question` DISABLE KEYS */;
INSERT INTO `last_question` VALUES
(1,'','','standard.jpg','');
/*!40000 ALTER TABLE `last_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `max_questions`
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
-- Dumping data for table `max_questions`
--

LOCK TABLES `max_questions` WRITE;
/*!40000 ALTER TABLE `max_questions` DISABLE KEYS */;
INSERT INTO `max_questions` VALUES
(1,'1',15),
(2,'2',15),
(3,'3',15),
(4,'4',15),
(5,'5',20),
(6,'6',20),
(7,'7',25);
/*!40000 ALTER TABLE `max_questions` ENABLE KEYS */;
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
(1,4,6),
(2,5,10),
(3,11,4),
(4,1,4),
(5,6,4),
(6,12,2);
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
(1,'Yannick'),
(2,'Alex V'),
(3,'Hans'),
(4,'Ben'),
(5,'Max'),
(6,'Sascha H'),
(7,'Daniel'),
(8,'Dominik'),
(9,'Ricco'),
(10,'Gerri'),
(11,'Dirk'),
(12,'Sarah'),
(13,'Nico'),
(14,'Tim'),
(15,'Pascal'),
(16,'Franzi');
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
(17,1,1,5,0,1,NULL),
(18,2,5,5,0,1,NULL),
(19,3,10,5,0,1,NULL),
(20,4,14,5,0,1,NULL),
(21,1,9,6,0,1,NULL),
(22,2,13,6,0,1,NULL),
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
-- Table structure for table `questions`
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
) ENGINE=InnoDB AUTO_INCREMENT=275 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES
(111,'Wer war der erste Bundeskanzler der BRD?','Konrad Adenauer',1,16,0,'Kommentar','adenauer.jpg'),
(112,'Wie hoch ist der Kölner Dom?','157 Meter',1,21,0,'Kommentar','koelnerdom.jpg'),
(113,'der wievielte Monat ist der September?','der 9.',1,17,0,'Kommentar','september.jpg'),
(114,'Welcher Berg ist der höchste Berg der Welt?','Mount Everest',1,1,0,'8849 meter','mounteverest.jpg'),
(115,'Wer war der erste Präsident der Vereinigten Staaten von Amerika?','George Washington',2,16,0,'1789 - 1797 Präsident der USA','washington.jpg'),
(116,'In welcher Stadt lebte der Detektiv Sherlock Holmes?','London',1,2,0,'Baker Street 221b','sherlockholmes.jpg'),
(117,'Wie heißt die Hauptstadt von Ungarn?','Budapest',1,3,0,'Kommentar','budapest.jpg'),
(118,'Welcher Planet unseres Sonnensystems ist der Sonne am nächsten?','Merkur',1,4,0,'Merkur, Venus, Erde, Mars, Jupiter, Saturn, Uranus, Neptun','merkur.jpg'),
(119,'An welchem Tag fiel die Berliner Mauer?','9. November 1989',2,13,0,'Kommentar','mauerfall.jpg'),
(120,'Wie viele Beine hat eine Spinne?','8',2,1,0,'Kommentar','spinne.jpg'),
(121,'Wie viele Sekunden hateine Stunde?','3600',2,18,0,'Kommentar','uhr.jpg'),
(122,'Wie viele Punkte hat ein standard Würfel?','21',2,8,0,'','wuerfel.jpg'),
(123,'Auf welchem Kontinent liegt die größte Wüste der Welt?','Antarktis',7,25,0,'Kommentar','antarktis.jpg'),
(124,'Wie heißt die Hauptstadt von Irland?','Dublin',3,1,0,'Kommentar','dublin.jpg'),
(125,'Welcher Fluss durchfließt den Grand Canyon?','Colorado River',5,1,0,'Kommentar','colorado.jpg'),
(126,'Welche Staatsflagge hat als einzige keine 4 Seiten?','Nepal',7,20,0,'Kommentar','nepal.jpg'),
(127,'In welchem Land wird am meisten Kaffee getrunken?','Finnland',5,2,0,'12 Kg pro Person\nDeutschland: 5Kg','finnland.jpg'),
(128,'Von wann bis wann dauerte der 1. Weltkrieg?','1914-1918',3,17,0,'Kommentar','weltkrieg1.jpg'),
(129,'In welchem Jahr landete Christoph Kolumbus in Amerika?','1492',5,19,0,'Kommentar','christopherkolumbus.jpg'),
(130,'Was ist eine Primzahl?','Eine Zahl, die nur durch 1 und sich selbst teilbar ist.',1,8,0,'2,3,5,7,11,13,17,19,23,29,31,37,41','primzahlen.jpg'),
(131,'Wie viele Planeten gehören zu unserem Sonnensystem?','8',3,2,0,'Merkur, Venus, Erde, Mars, Jupiter, Saturn, Uranus, Neptun','sonnensystem.jpg'),
(132,'Aus was besteht ein Diamant?','Kohlenstoff',2,9,0,'Kommentar','diamant.jpg'),
(133,'Wie oft finden die Wahlen zum Europäischen Parlament statt?','alle 5 Jahre',6,18,0,'Kommentar','europaparlament.jpg'),
(134,'Wie heißt der freche Kobold von Meister Eder? ','Pumuckl',1,9,0,'Kommentar','pumuckl.jpg'),
(135,'Welcher ist der längste Fluss der Welt?','Der Nil',5,3,0,'6671 km','nil.jpg'),
(136,'Welche Farbe hat die Null beim Roulette?','Grün',5,4,0,'Kommentar','roulettenull.jpg'),
(137,'Aus welchem Land kommt die Band AC DC?','Aus Australien',2,2,0,'1973 gegründet','acdc.jpg'),
(138,'In welchem Jahr starb John F. Kennedy','1963',3,21,0,'22. November 1963 in Dallas','kennedy.jpg'),
(139,'Welches menschliche Organ verbraucht die meiste Energie?','Das Gehirn',1,18,0,'circa 500 KiliKalorien per Tag','gehirn.jpg'),
(140,'In welchem Jahr landete der erste Mensch auf dem Mond?','1969',4,20,0,'20. Juli 1969 Apollo 11','apollo11.jpg'),
(141,'In welchem Jahr fand die Katastrophe von Tschernobyl statt?','1986',6,2,0,'26. April 1986 Prypjat','tschernobyl.jpg'),
(142,'Welche Farben hat die mexikanische Flagge?','Grün, Weiß, Rot',1,11,0,'Grün: Hoffnung\nWeiß: Einheit\nRot: Blut der Helden','mexico.jpg'),
(143,'Wer war während des WW2 Premierminister des UK?','Winston Churchill',5,23,0,'Kommentar','churchill.jpg'),
(144,'Wie lautet das Chemische Symbol für Gold?','Au',5,6,0,'aurum','aurum.jpg'),
(145,'Wie heißt die Hauptstadt von Island?','Reykjavik',2,11,0,'Kommentar','reykjavik.jpg'),
(146,'Welche Entdeckung machte Marie Curie','Radioaktivität',3,3,0,'Kommentar','radioaktivitaet.jpg'),
(147,'Welches ist da flächenmäßig größte Land der Welt?','Russland',4,1,0,'17.098.242 km2','russia.jpg'),
(148,'Wo wird im menschlichen Körper Insulin produziert?','in der Bauchspeicheldrüse',4,2,0,'Kommentar','pankreas.jpg'),
(149,'Welche Schauspielerin spielte Prinzessin Leia in der Star Wars saga?','Carrie Fisher',6,5,0,'Kommentar','carriefisher.jpg'),
(150,'Wie lange dauert ein Fußballspiel?','90 Minuten (2x45)',2,6,0,'Kommentar','fussball.jpg'),
(151,'Wie heißt der zweithöchste Berg der Erde?','K2',4,3,0,'8611 m','k2.jpg'),
(152,'Wie hieß Marylin Monroe wirklich?','Norma Jeane Baker',7,26,0,'Kommentar','marylinmonroe.jpg'),
(153,'Welches Säugetier kann fliegen?','Fledermaus / Flughund',3,4,0,'beide gehören zu den Fledertieren','fledermaus.jpg'),
(154,'Wie viele Elemente enthält das Periodensystem?','118',5,7,0,'Kommentar','periodensystem.jpg'),
(155,'Welcher Roman von Stephen King spielt im Overlook Hotel?','Shining',7,1,0,'Mit Jack Nicholson in der Hauptrolle (1980)','shining.jpg'),
(156,'Wer war der erste Mensch auf dem Mond?','Neil Armstrong',7,2,0,'20. Juli 1969','armstrong.jpg'),
(157,'Wie heißt das am meisten verkaufte Musikalbum aller Zeiten?','Thriller - Michael Jackson',5,8,0,'Kommentar','thriller.jpg'),
(158,'Was ist das größte menschliche Organ?','Die Haut',2,14,0,'Kommentar','haut.jpg'),
(159,'Welches ist die weltweit größte Stadt?','Tokio',3,5,0,'38 mio Einwohner','tokio.jpg'),
(160,'Welcher Film erhielt die bisher meisten Oskars?','Titanic (1997)',4,6,0,'11 Oscars','51VoG4YuPbL.jpg'),
(161,'Wer hat die Mona Lisa gemalt?','Leonardo DaVinci',2,15,0,'Kommentar','monalisa.jpg'),
(162,'Wie viele Tage hat ein Jahr?','365',1,12,0,'Schaltjahr 366','kalender.jpg'),
(163,'Wie lautet die chemische Formel für Wasser?','H20',1,10,0,'Kommentar','wetfloor.jpg'),
(164,'Was ist die Quadratwurzel von 64?','8',1,13,0,'Kommentar','mathe.jpg'),
(165,'Welcher Schauspieler gewann den Oscar für Philadelphia und Forest Gump?','Tom Hanks',1,14,0,'Kommentar','hanks.jpg'),
(166,'Wie hieß die Band mit folgenden Mitgliedern: John Deacon, Roger Taylor, Brian May, Freddie Mercury?','Antwort',2,12,0,'Kommentar','queen.jpg'),
(167,'Welcher amerikanische Popstar hatte 2015 mit den Singles „Sorry“ und „Love Yourself“ zwei aufeinanderfolgende Chart-Erfolge?','Justin Bieber',3,20,0,'Kommentar','justinbieber.jpg'),
(168,'Wer wählt den Bundespräsidenten?','Die Bundesversammlung',7,23,0,'Kommentar','bundesversammlung.jpg'),
(169,'Wie heißt die Landeshauptstadt von Thüringen?','Erfurt',2,17,0,'Kommentar','thueringen.jpg'),
(170,'In welcher Einheit wird der elektrische Widerstand gemessen?','Ohm',3,7,0,'U = R*I','ohm.jpg'),
(171,'Wofür steht das L in RTL?','Luxembourg',4,7,0,'Radio Television Luxembourg','rtl.jpg'),
(172,'Wie beginnt Artikel 1 des Grundgesetzes?','Die Würde des Menschen ist unantastbar.',1,5,0,'Kommentar','grundgesetz.jpg'),
(173,'Wie lautet das chemische Symbol für Blei?','Pb',2,3,0,'plumbum','blei.jpg'),
(174,'Wer verbreitete das heliozentrische Weltbild?','Nikolaus Kopernikus',5,9,0,'Kommentar','kopernikus.jpg'),
(175,'Wie lautet der Satz des Pythagoras?','a²+a²=c²',3,9,0,'a+b=katheten\nc=Hypotenuse','pytagoras.jpg'),
(176,'Welche 3 Staatsgewalten gibt es in Deutschland?','Legislative, Exekutive, Judikative',6,7,0,'Legislative=gesetzgebend\nExekutive=vollziehend\nJudikative=richterliche','gewalten.jpg'),
(177,'Was bedeutet LCD?','liquid crystal display',4,10,0,'Kommentar','lcd.jpg'),
(178,'Was bedeutet LED?','light emitting diod',2,4,0,'LIchtemittierende Diode','led.jpg'),
(179,'Wer war der 2. Bundeskanzler der BRD?','Ludwig Erhard',6,21,0,'Bereits Wirtschaftsminister unter Adenauer','erhard.jpg'),
(180,'Wie viele Bundesländer hat die BRD?','16',3,10,0,'Schleswig-Holstein, Meck-Pom,HH,HB,Brandenburd,Berlin,Niedersachsen,Sachsen-Anhalt,NRW,Sachsen,Thüringen,Hessen,RLP,Saarland,Bayern,BW','bundeslaender.jpg'),
(181,'Wie viele Länder grenzen an die BRD?','9',2,5,0,'FR,BE,NL,LUX,DEN,PL,CZ,AUT,CHE','brd.jpg'),
(182,'Wie heißt die Hauptstadt von Australien?','Canberra',3,11,0,'Kommentar','canberra.jpg'),
(183,'Wofür steht die Abkürzung IT?','Informationstechnik',4,12,0,'Kommentar','it.jpg'),
(184,'Welches ist flächenmäßig das größte Bundesland der BRD?','Bayern',4,13,0,'70550km²','bayern.jpg'),
(185,'In welcher Einheit wird die elektrische Spannung gemessen?','Volt',4,14,0,'Kommentar','volt.jpg'),
(186,'Wie heißt die Hauptstadt von Äthiopien?','Addis Abeba',5,17,0,'Kommentar','addisabeba.jpg'),
(187,'Wer wohnt in der Downing Street 10 in  London?','Der englische Premierminister',6,8,0,'Kommentar','downingstreet.jpg'),
(188,'Wie lautet das Chemische Symbol für Eisen?','Fe',3,12,0,'ferrum','ferrum.jpg'),
(189,'Wie lautet das chemische Symbol für Stickstoff?','N',4,9,0,'nitrogenium','nitrogenium.jpg'),
(190,'Wie lautet das chemische Symbol für Uran?','U',7,16,0,'Nach dem Planeten Uranus','uran.jpg'),
(191,'Wie heißt der kleinste Staat der Welt?','Vatikan',1,15,0,'ca 770 Einwohner','vatikan.jpg'),
(192,'Wo liegen die Langerhans Inseln?','in der Bauchspeicheldrüse',7,17,0,'Für die Hormbildung zuständig','langerhans.jpg'),
(193,'Wie viele Kontinente gibt es auf der Erde?','7',1,7,0,'Nordamerika, Südamerika, Europa, Afrika, Asien, Australien, Antarktika','kontinente.jpg'),
(194,'Welches ist die viertgrößte Stadt der BRD?','Köln',2,7,0,'Nach Berlin, HH, München','koeln.jpg'),
(195,'Welches Ereignis war der Auslöser des 30-jährigen Krieges?','Prager Fenstersturz',7,22,0,'Kommentar','pragerfenstersturz.jpg'),
(196,'Wie lang ist ein Marathon?','42,195km',6,9,0,'Kommentar','marathon.jpg'),
(197,'Wie heißt die Hauptstadt von Indonesien?','Jakarta',4,15,0,'Kommentar','jakarta.jpg'),
(198,'Zu welchem Land gehört Grönland ?','Königreich Dänemark',1,19,0,'Eigene Regierung , eigenes Parlament','groenland.jpg'),
(199,'Welcher Partei gehörte Adenauer an?','CDU',1,20,0,'Kommentar','adenauer.jpg'),
(200,'Wie groß ist die Summer aller Winkel in einem Dreieck?','180°',3,13,0,'Kommentar','winkelsummedreieck.jpg'),
(201,'Mit welchen 3 Ziffern beginnt die Kreiszahl Pi?','3,14',4,5,0,'3,141592653589793','pi.jpg'),
(202,'Wer schrieb den Erlkönig?','Johann Wolfgang von Goethe',3,14,0,'Kommentar','erlkoenig.jpg'),
(203,'Wer schrieb Krieg und Frieden?','Leo Tolstoi',6,22,0,'Kommentar','kriegundfrieden.jpg'),
(204,'Wie viele Streifen hat die US Flagge?','13',2,19,0,'13 Gründungsstaaten','starspangledbanner.jpg'),
(205,'Welche ist die am meisten verkaufte Buchreihe des 21. Jhd.?','Harry Potter',3,15,0,'Kommentar','harrypotter.jpg'),
(206,'Welcher Künstler malte die Decke der Sixtinischen Kapelle in Rom?','Michelangelo',2,20,0,'Kommentar','sistinische.jpg'),
(207,'Wann wurde die Londoner UBahn eröffnet?','1863',2,21,0,'London Underground','underground.jpg'),
(208,'Aus welcher Stadt kommen die Beatles?','Liverpool',4,4,0,'Kommentar','beatles.jpg'),
(209,'Welches ist das meistgespielte Lied auf Spotify?','Ed Sheeran - Shape of You',3,16,0,'Kommentar','sheeran.jpg'),
(212,'Wie viele Formel 1Weltmeister Titel gewann Michael Schumacher?','7',4,11,0,'1994,1995,2000,2001,2002,2003,2004','Schumacher_1993_European_GP.jpg'),
(213,'Welches war der erste Pixar Film?','Toy Story (1995)',4,17,0,'Kommentar','toystory.jpg'),
(214,'In welchem Land befindet sich die Hauptstadt Ankara?','Türkei',3,18,0,'Kommentar','turkey.jpg'),
(215,'Wie heißt der amtierende König des British Empire?','König Charles III.',7,3,0,'Früher auch König Karl','charles.jpg'),
(216,'Welche politische Organisation verbirgt sich hinter der Abkürzung UNO?','Vereinten Nationen',5,10,0,'United Nations Organisation','uno.jpg'),
(217,'Wozu gehören die folgenden Tiere? Krebs, Skorpion, Löwe, Stier, Widder, Fische?','Tierkreiszeichen (Sternzeichen)',5,11,0,'Kommentar','00_All-Zodiacs.jpg'),
(218,'Wie heißt die Frau die Tarzan im Dschungel zur Seite steht?','Jane',3,19,0,'Kommentar','jane.jpg'),
(219,'Wie heißt das Gebäude des amerikanischen Parlaments?','Kapitol',4,8,0,'Kommentar','kapitol.jpg'),
(220,'Welches Tier hat 8 Arme?','Oktopuss (Kraken)',7,6,0,'Kraken haben einen Lieblingsarm','Octopus3.jpg'),
(221,'Welche Denkmäler ließen sich die aägyptischen Pharaonen bauen?','Die Pyramiden',3,6,0,'Kommentar','pyramidengizeh.jpg'),
(222,'Wie viel Gramm sind 7,5 Kg?','7500',5,12,0,'Kommentar','7500.jpg'),
(223,'Wie heißt die kleine schwarze Spielscheibe beim Eishockey?','Puck',5,13,0,'1 Zoll hoch, 3 Zoll durchmesser, 156-170gr','puck.jpg'),
(224,'Wie heißt das berühmte Schloss in Potsdam?','Schloß Sanssouci',7,14,0,'1745 erbaut durch Friedrich den Großen','sanssouci.jpg'),
(225,'Welche Farbe hat das Kreuz der schwedischen Nationalflagge?','Gelb',5,14,0,'Kommentar','schweden.jpg'),
(226,'Welche Vornamen trug der Dichter von Goethe?','Johann Wolfgang',5,22,0,'Kommentar','goethe.jpg'),
(227,'Welche Säugetiere singen unter Wasser?','Wale',4,18,0,'Kommentar','wale.jpg'),
(228,'Was für ein Tier ist Donald Duck?','Ente (Erpel)',4,16,0,'Kommentar','donald.jpg'),
(229,'Wie heißt der bekannte Vampir aus Transsylvanien?','Graf Dracula',4,19,0,'Kommentar','dracula.jpg'),
(230,'Wie heißt der berühmte Freizeitpark in Wien?','Prater (Wurstelprater)',5,25,0,'Prater ist eigentlich das Gebiet und Wurstelprater der Freizeitpark','prater.jpg'),
(231,'Welcher Fluß mündet bei Koblenz in den Rhein?','Die Mosel',5,15,0,'Kommentar','model.jpg'),
(232,'Auf welchem Spielbrett sind 3 verschieden Große Quadrate aufgezeichnet?','Mühle',5,16,0,'Kommentar','muehle.jpg'),
(233,'Wer kommandiert im Dschungelbuch die Elefanten?','Colonel Hathi',6,10,0,'Kommentar','hathi.jpg'),
(234,'Was erfanden Ladislaus und Georg Biro 1938?','Kugelschreiber',7,11,0,'auf englisch biro','biro.jpg'),
(235,'Unter welchem Namen ist die Republik China umgangssprachlich bekannt?','Taiwan',6,11,0,'Kommentar','taiwan.jpg'),
(236,'Wer baute 1876 den ersten 4Takt-Motor?','Nikolaus August Otto',6,12,0,'Kommentar','nikolausaugustotto.jpg'),
(237,'Was sind die beiden Amtssprachen in Kanada?','Französich, Englisch',6,13,0,'Kommentar','kanada.jpg'),
(238,'Welchen Zahlenwert haben König, Dame und Bube beim Blackjack?','10',6,4,0,'Kommentar','Blackjack.jpg'),
(239,'Wie hieß der erste Bundespräsident der BRD?','Theodor Heuss',5,18,0,'1949-1959','heuss.jpg'),
(240,'In welchem Land liegt das Kap Verde?','Senegal',5,20,0,'Kommentar','kapverde.jpg'),
(241,'Welches Gerät wurde während der franz. Revolution zur Enthauptung benutzt?','Guillotine',6,3,0,'Kommentar','guillotine.jpg'),
(242,'Wie lange lebt eine Stubenfliege maximal?','70 Tage',5,26,0,'Kommentar','fliege.jpg'),
(243,'Welche Staatsbürgerschaft nahm Albert Einstein 1901 an?','Die Schweizer Staatsbürgerschaft',6,14,0,'Schweizer Bürgerrecht','einstein.jpg'),
(244,'Welcher Kaiser brannte angeblich Rom nieder?','Nero (Claudius Caesar Augustus Germanicus)',6,1,0,'Kommentar','nero.jpg'),
(245,'Welcher Buchstabe symbolisiert die Menge natürlicher Zahlen?','n',7,7,0,'Kommentar','nmengezahlen.jpg'),
(246,'Welche beiden Bundesländer grenzen an Luxembourg?','Rheinland Pfalz und Saarland',5,21,0,'Kommentar','laenderbrd.jpg'),
(247,'Welches DIN Format ergibt sich aus 14,8 x 21 cm?','DIN A5',7,19,0,'Kommentar','din-formate.jpg'),
(248,'Wie viele Hörner besitzt das afrikanische Nashorn?','2',5,24,0,'Kommentar','nashorn.jpg'),
(249,'Welche Farbe hat meistens die Blackbox einen Flugzeuges?','Orange',6,6,0,'Kommentar','blackbox.jpg'),
(250,'Wo hat jeder Mensch eine Schnecke?','Im Ohr',6,23,0,'Kommentar','ohr.jpg'),
(251,'Welches ist die Grundzahl des Dezimalsystems?','10',6,15,0,'Kommentar','10.jpg'),
(252,'Welche Disziplinen müssen beim Ironman bewältigt werden?','Schwimmen, Radfahren, Marathonlauf',7,21,0,'3,8km Schwimmen, 180km Radfahren, 42,195km Marathon','ironman.jpg'),
(253,'Welches Säugetier kann 7 mal im Jahr Junge bekommen?','Die Feldmaus',7,24,0,'Kommentar','feldmaus.jpg'),
(254,'Wie viel Sauerstoff befindet sich normalerweise in unserer Atemluft?','21 % ',7,5,0,'Kommentar','atemluft.jpg'),
(255,'Welchen Namen erhielt der Grand Prix D´Eurovision de la Chanson ab 2004?','Eurovision Song Contest',7,8,0,'Kommentar','waddehadde.jpg'),
(256,'Welcher deutsche Entertainer startete 2024 nach 10 Jahren Pause eine neue Show im deutschen Fernsehen?','Stefan Raab',6,16,0,'Kommentar','raab.jpg'),
(257,'Mit welchem Song trat Stefan Raab 2000 beim Grand Prix d´Eurovision de la Chanson an?','Wadde Hadde Dudde Da?',7,18,0,'Belegte den 5. Platz','Wadde_hadde_dudde_da.jpg'),
(258,'Wie lautet der gemeinsame Name für Protonen und Neutronen?','Nukleonen',7,12,0,'Kommentar','atom.jpg'),
(259,'Welches ist die berühmteste und älteste Levis Hose?','501',7,10,0,'Kommentar','levis.jpg'),
(260,'Welche Stadt hat das KFZ Kennzeichen HH?','Hansestadt Hamburg',7,4,0,'Kommentar','Hamburger-Nummernschild.jpg'),
(261,'Welches ist die größte deutsche Nicht-Milllionenstadt?','Frankfurt am Main',7,27,0,'775790 Einwohner','Frankfurt_Skyline_2022.jpg'),
(262,'Welches ist die kleinste deutsche Großstadt?','Cottbus',6,17,0,'100010 Einwohner','960px-Stadtmuseum-Cottbus.jpg'),
(263,'Wie viele Einwohner (gerundet auf tsd.) hatte Troisdorf im Jahr 2023 ?','77000',1,6,0,'76503','DEU_Troisdorf_COA.svg.jpg'),
(264,'Die wievieltgrößte Stadtteil Troisdorfs ist Spich?','Zweitgrößte',2,10,0,'13000 Einwohner (Troisdorf Mitte 17000, Sieglar 8800)','Haus_broich_spich.jpg'),
(265,'Welche 2 Fachwerkhäuser in Spich stehen unter Denkmalschutz?','Haus Heep und Et Hüsje',5,5,0,'Kommentar','Et_Huesje_Troisdorf_NRW_D.jpg'),
(266,'Wie heißt der amtierende Bürgermeister der Stadt Troisdorf und welcher Partei gehört er an?','Alexander Biber, CDU',3,8,0,'Kommentar','dsc00227.jpg'),
(267,'Welche Nadelbäume tragen die längsten Nadeln?','Die Kiefern',7,15,0,'Kommentar','kiefer.jpg'),
(268,'Worauf trommelt ein Gorilla wenn er einen Rivalen einschüchtern möchte?','Auf der Brust',7,28,0,'Kommentar','gorilla.jpg'),
(269,'Was ist als der 90. Teil eines rechten Winkels definiert?','Der Grad',6,20,0,'Kommentar','rechter.jpg'),
(270,'Welche beiden Zahlen entsprechen den Schaltzuständen beim Computer?','1 & 0',6,19,0,'Kommentar','binaer.jpg'),
(271,'Womit befasst sich ein Mediziner mit dem Titel Dr. Med. Vet ?','Mit Tieren',7,9,0,'Kommentar','tierarzt.jpg'),
(272,'Was gibt es in Kurzhaar, Langhaar und Rauhaar?','Dackel',7,29,0,'Kommentar','Kurzhaardackel.jpg'),
(273,'Was bedeutet kurativ?','heilend',7,30,0,'Kommentar','kurativ.jpg'),
(274,'Welche Farbe hat der Hintergrund der olympischen Ringe?','Weiß',7,13,0,'Kommentar','Olympic_flag.jpg');
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-19  9:48:52