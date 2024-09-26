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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `config`
--

LOCK TABLES `config` WRITE;
/*!40000 ALTER TABLE `config` DISABLE KEYS */;
INSERT INTO `config` VALUES
(1,'monitor_round','1'),
(2,'buzzer_blocked','0'),
(10,'final_date','Sep 26 2024  18:15:00'),
(11,'player_correct','0'),
(12,'play_mode','1');
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
(1,'Welche 4 Taktischen Einheiten gibt es bei der Feuerwehr?','Selbstständiger Trupp, Staffel, Gruppe, Zug');
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
(1,'1',10),
(2,'2',10),
(3,'3',10),
(4,'4',10),
(5,'5',15),
(6,'6',15),
(7,'7',20);
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
(1,'Lukas B'),
(2,'Ben'),
(3,'Max'),
(4,'Sascha H'),
(5,'Lukas H'),
(6,'Hans'),
(7,'Yannick'),
(8,'Daniel'),
(9,'Dominik'),
(10,'Jessi'),
(11,'Tobias'),
(12,'Dirk'),
(13,'Jason'),
(14,'Nico'),
(15,'Alex'),
(16,'Tim');
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
(1,1,1,1,2,1,NULL),
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
(18,2,2,5,0,1,NULL),
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `ux_question` (`question`)
) ENGINE=InnoDB AUTO_INCREMENT=175 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES
(1,'Was bedeutet der FMS Status 1?','einsatzbereit über Funk (auch Einbuchen)',1,1,1,NULL),
(2,'Durch eine lose Rolle wird die Kraft…','…halbiert.',1,2,1,NULL),
(3,'Welche 4 Taktischen Einheiten gibt es bei der Feuerwehr?','Selbstständiger Trupp, Staffel, Gruppe, Zug',1,3,1,NULL),
(4,'In welchem Bereich liegt die Verschäumungszahl von Mittelschaum?','21 - 200',1,4,0,NULL),
(5,'Um als Atemschutzgeräteträger eingesetzt werden zu dürfen, muss der Feuerwehrangehörige gemäß FwDV 7….','… das 18. Lebensjahr vollendet haben, einer Untersuchung nach G26.3 genügen, Ausbildung zum AGT erfolgreich absolviert haben.',1,5,0,NULL),
(6,'Was unfasst Gefahrgutklasse 8?','Ätzende Stoffe',1,6,0,NULL),
(7,'Welche Brände werden der Brandklasse C zugeordnet? Nenne auch 2 Beispiele.','Brände von Gasen z.B. Methan, Propan, Wasserstoff, Acetylen, Erdgas, Stadtgas',1,7,0,NULL),
(8,'Wie viele Atemschutztrupps müssen für die Durchführung eines Innenangriffs mindestens an der Einsatzstelle vorhanden sein?','2 Trupps',1,8,0,NULL),
(9,'Wie viel Liter Löschwasser muss ein LF20 mindestens bevorraten?','2000 liter',1,9,0,NULL),
(10,'Welche(s) Löschmittel sind (ist) bei einem Magnesiumbrand geeignet?','D-Pulver',1,10,0,NULL),
(11,'Welcher (welchen) Brandklasse(n) werden Brände Speiseölen und Speisefetten zugeordnet?','Brandklasse F',1,11,0,NULL),
(12,'In welchem Bereich liegt die Verschäumungszahl von Schwerschaum?','4 - 20',1,12,0,NULL),
(13,'Nenne die Luftverzleichszahl von Schwefeldioxid','64',1,13,0,NULL),
(14,'Aus welchen Bestandteilen besteht Löschschaum?','Schaummittel, Wasser, Umgebungsluft',1,14,0,NULL),
(15,'Wann kann auf einen Sicherheitstrupp verzichtet werden?','Bei Brandeinsätzen im Freien, bei der eine Rettung des Trupps auch ohne Atemschutz möglich wäre',1,15,0,NULL),
(16,'Wie ist die Rettungshöhe der 3-teiligen Steckleiter?','12m',2,1,0,NULL),
(17,'Wie viel Wasser fasst ein 15 m D-Druckschlauch?','7,5 Liter',2,2,0,NULL),
(18,'Was ist der Hauptbestandteil unserer Atemluft?','N (Stickstoff)',2,3,0,NULL),
(19,'Wie viele Gerätefächer hat das Spicher LF20?','7',2,4,0,NULL),
(20,'Welchen FMS Status setze ich , wenn sich das Fahrzeug in einer Notlage befindet?','Status 0',2,5,0,NULL),
(21,'Welche für uns relevanten Gase sind leichter als Luft? Nenne 3 Stück','Wasserstoff, Helium, Methan, Ammoniak, Fluorwasserstoff, Acetylen, Kohlenmonoxid CO,  Stickstoff, Ethen',2,6,0,NULL),
(22,'Welche Brände werden der Brandklasse F zugeordnet?','Brände von Speiseölen und Speisefetten',2,7,0,NULL),
(23,'Was bedeutet die Verschäumungszahl?','das Verhältnis zwischen dem Volumen des Wasserschaummittelgemisches und dem Schaummittelvolumen. ',2,8,0,NULL),
(24,'Welche 3 relevanten Gesetze und Verordnungen werden durch §35 StVO NICHT ausser Kraft gesetzt? ','StVG, StVZO, StGB, ',2,9,0,NULL),
(25,'Welchen FMS Status setze ich , wenn das Fahrzeug nicht (mehr) einsatzbereit ist?','Status 6',2,10,0,NULL),
(26,'Welche Nachteile treffen auf Unterflurhydranten zu?','Schwer aufzufinden bei Dunkelheit/Schnee, kann zugeparkt sein, Kann verunreinigt sein',2,11,0,NULL),
(27,'Welche Schaumart erzeugt man bei einer Verschäumungszahl von 48?','Mittelschaum',2,12,0,NULL),
(28,'Welcher Brandklasse werden Brände von Metallen zugeordnet?','Brandklasse D',2,13,0,NULL),
(29,'Was müssen Atemschutzgeräteträger jährlich nachweisen?','Belastungsübung, Einsatzübung oder Einsatz',2,14,0,NULL),
(30,'Was bedeutet FPN 10-2000?','Fire Pump Norm Pressure / 2000 l/m bei 10 Bar',2,15,0,NULL),
(31,'Wo sind Atemschutzgeräte an- und abzulegen?','Außerhalb des Gefahrenbereichs',3,1,0,NULL),
(32,'Nenne die Luftverzleichszahl von Ammoniak','17',3,2,0,NULL),
(33,'Was unfasst Gefahrgutklasse 6?','Giftige Stoffe',3,3,0,NULL),
(34,'Unter Normaldruck entsteht beim Verdampfen von einem Liter Wasser wie viel Wasserdampf?','1700 (1673)',3,4,0,NULL),
(35,'Wie viel Liter Löschwasser bevorratet unser Spicher LF?','3000 liter',3,5,0,NULL),
(36,'In welche Bereiche wird eine Einsatzstelle im ABC-Einsatz geordnet?','Gefahrenbereich und Absperrbereich',3,6,0,NULL),
(37,'Was bedeutet der FMS Status 6?','nicht einsatzbereit',3,7,0,NULL),
(38,'Was bedeutet 3% Zumischung im Bezug auf Löschschaum?','Anteil des Schaummittels vor dem Schaumrohr: 97% Wasser, 3% Schaummittel',3,8,0,NULL),
(39,'Was regelt §38 StVO?','Blaues Blinklicht und gelbes Blinklicht',3,9,0,NULL),
(40,'Wo werden die sogenannten Sonderrechte geregelt?','§35 StVO',3,10,0,NULL),
(41,'Was bedeutet DMO?','„Direct Mode Operation“ netzunabhängiger Betrieb',3,11,0,NULL),
(42,'Welcher Anstellwinkel von tragbaren Leitern ist zu beachten?','65-75°',3,12,0,NULL),
(43,'Was regelt §35 StVO?','Sonderrechte',3,13,0,NULL),
(44,'Wie gliedert sich die Mannschaftsstärke der Gruppe?','1/8/9',3,14,0,NULL),
(45,'Ab wann spricht man bei Gleichstrom von Hochspannung in einer Anlage?','1500V',3,15,0,NULL),
(46,'Was bedeutet PFPN 10-1000?','Portable Fire Pump Norm Pressure / 1000 l/m bei 10 Bar',4,1,0,NULL),
(47,'Was bedeutet der FMS Status 3?','Einsatzauftrag übernommen',4,2,0,NULL),
(48,'Welche Löschwirkung(en) werden beim Löschen mit Schwerschaumgenutzt?','Kühlen, Ersticken',4,3,0,NULL),
(49,'Nenne die Luftverzleichszahl von Methan','16',4,4,0,NULL),
(50,'Woraus besteht eine taktische Einheit nach FwDV 3?','Einsatzmittel, Mannschaft',4,5,0,NULL),
(51,'Wofür steht die Abkürzung UEG?','Untere Explosionsgrenze',4,6,0,NULL),
(52,'In welchem Bereich liegt die Verschäumungszahl von Leichtschaum?','201 - 1000',4,7,0,NULL),
(53,'Nenne die Luftverzleichszahl von Kohlenstoffdioxid','44',4,8,0,NULL),
(54,'Was unfasst Gefahrgutklasse 2?','Gase und gasförmige Stoffe',4,9,0,NULL),
(55,'Was bedeutet BOS?','Behörden und Organisationen mit Sicherheitsaufgaben',4,10,0,NULL),
(56,'Was bedeutet TMO?','„Trunked Mode Operation“ netzabhängiger Betrieb ',4,11,0,NULL),
(57,'Wie setzt sich normalerweise die Ausatemluft zusammen?','N 78%, O 16%, Edelgase < 1%, CO2 4,03 %',4,12,0,NULL),
(58,'Welche Bestandteile muss ein Befehl im Löscheinsatz ohne Bereitstellung enthalten (Reihenfolge!)? (8)','Lageschilderung, Lage Verteiler, Wasserentnahmestelle, Einheit, Auftrag, Mittel, Ziel, Weg',4,13,0,NULL),
(59,'Wie groß ist die so genannte Luftvergleichszahl?','29',4,14,0,NULL),
(60,'Wie viel Wasser fasst ein 15 m C52-Druckschlauch?','32 Liter',4,15,0,NULL),
(61,'Welche Schaumart erzeugt man bei einer VZ 160?','Mittelschaum',5,1,0,NULL),
(62,'Welche Schaumart erzeugt man bei einer VZ 16?','Schwerschaum',5,2,0,NULL),
(63,'Wie viel Wasser fasst ein 5 m B-Druckschlauch?','22 Liter',5,3,0,NULL),
(64,'Wie ist die Transportlänge der 3-teiligen Schiebleiter?','5,6m',5,4,0,NULL),
(65,'Was unfasst Gefahrgutklasse 3?','Flüssige Stoffe',5,5,0,NULL),
(66,'Wie viele Einsatzkräfte müssen zur Vornahme einer 4-teiligen Steckleiter mindestens eingesetzt werden?','3',5,6,0,NULL),
(67,'Als unerschöpfliche Löschwasserentnahmestelle(n) gelten ?','Natürliche/Künstliche offene Gewässer, Löschwasserbrunnen (DIN 14220)',5,7,0,NULL),
(68,'Welche Schaumart erzeugt man bei einer VZ 25?','Mittelschaum',5,8,0,NULL),
(69,'Was versteht man unter Körperschutz Form 1?','Feuerwehrkleidung zur Brandbekämpfung, Atemschutzgerät, Kontaminationsschutzhaube',5,9,0,NULL),
(70,'Welche Arten der Wärmeübertragung gibt es?','Wärmeleitung, Wärmeströmung, Wärmestrahlung',5,10,0,NULL),
(71,'Unter welchem Namen ist Chlorwasserstoff auch bekannt?','Salzsäure',5,11,0,NULL),
(72,'Was unfasst Gefahrgutklasse 4?','Feste Stoffe und Gegenstände',5,12,0,NULL),
(73,'Welcher (welchen) Brandklasse(n) werden Brände flüssiger oder flüssigwerdender Stoffe zugeordnet?','Brandklasse B',5,13,0,NULL),
(74,'Welche Brände werden der Brandklasse D zugeordnet?','Brände von Metallen z.B. Aluminium, Magnesium, Lithium, Natrium, Kalium und deren Legierungen',5,14,0,NULL),
(75,'Wer gibt beim Herstellen einer Saugleitung die Kommandos?','Wassertruppführer',5,15,0,NULL),
(76,'Wie wird die Inanspruchnahme der Wegerechte kenntlich gemacht?','mit Blaulicht und Einsatzhorn',5,16,0,NULL),
(77,'Was bedeutet der FMS Status 0?','Notruf / priorisierter Sprechwunsch',5,17,0,NULL),
(78,'Was beschreibt die FwDV 3?','Einheiten im Lösch- und Hilfeleistungseinsatz',5,18,0,NULL),
(79,'Welche Einsatzart(en) unterscheidet die FwDV 3?','Mit und ohne Bereitstellung',5,19,0,NULL),
(80,'Welche Schaumart erzeugt man bei einer VZ 400?','Leichtschaum',5,20,0,NULL),
(81,'Welche Gefahrengruppen werden gemäß FwDV 500 unterschieden?','Gefahrengruppe I, II und III',6,1,0,NULL),
(82,'Wie muss der Sicherheitstrupp mindestens ausgerüstet sein?','Gleich- oder höherwertig dem vorgehenden Trupp',6,2,0,NULL),
(83,'Nenne die Luftverzleichszahl von Acetylen','26',6,3,0,NULL),
(84,'Was bedeutet DLK 23-12?','Drehleiter mit Korb, Nennausladung 12m bei Nennrettungshöhe 23m',6,4,0,NULL),
(85,'Was heißt BHKG?','Gesetz über den Brandschutz, die Hilfeleistung und den Katastrophenschutz',6,5,0,NULL),
(86,'Welche für uns relevanten Gase sind schwerer als Luft? Nenne 3 Stück','Chlor, Chlorwasserstoff (Salzsäure), Benzol, Brom, Butan, Kohlenstoffdioxid CO2, Schwefeldioxid, Schwefelkohlenstoff',6,6,0,NULL),
(87,'Wie ist die Rettungshöhe der 4-teiligen Steckleiter bei 2 Teilen?','3,7m / 1.OG',6,7,0,NULL),
(88,'Woraus besteht ein selbsständiger Trupp?','Truppführer, Truppmann und Maschinist',6,8,0,NULL),
(89,'Welche Brände werden der Brandklasse B zugeordnet?','Brände von flüssigen oder flüssig werdenden Stoffen z.B. Benzin, Benzol, Öle, Lacke, Teer, Äther, Alkohol, Stearin, Paraffin',6,9,0,NULL),
(90,'Welche Dienstvorschrift regelt den Sprechfunkverkehr?','FwDV / PDV 810',6,10,0,NULL),
(91,'Wie viel Wasser fasst ein 20 m B-Druckschlauch?','88 Liter',6,11,0,NULL),
(92,'Wer stellt beim Einsatz einer offenen Wasserentnahmestelle die Saugleitung her?','Wassertrupp und Schlauchtrupp',6,12,0,NULL),
(93,'Was unfasst Gefahrgutklasse 5?','5.1: Entzündend wirkende Stoffe / 5.2: organische peroxide',6,13,0,NULL),
(94,'Welche Brände werden der Brandklasse A zugeordnet?','Brände fester Stoffe, die normalerweise unter Glutbildung verbrennen z.B. Holz, Papier, Stroh, Textilien, Kohle\n',6,14,0,NULL),
(95,'Was unfasst Gefahrgutklasse 9?','Verschiedene gefährliche Stoffe',6,15,0,NULL),
(96,'Durch eine feste Rolle wird die Kraft…','…des Seils umgelenkt.',6,16,0,NULL),
(97,'Welche technischen Merkmale hat ein Zumischer Z2?','200l/min Wasserleistung, C-Kupplung',6,17,0,NULL),
(98,'Wie kann Löschwasser bei einer geodätischen Saughöhe von 11 m mit einer Feuerlöschkreiselpumpe gefördert werden?','gar nicht',6,18,0,NULL),
(99,'Welchen FMS Status setze ich beim eintreffen an der Einsatzstelle?','Status 4',6,19,0,NULL),
(100,'Das wievielte Gerätehaus (damals noch Spritzenhaus) ist das aktuelle Haus?','3. (vormals Niederkasseler Str, Fliersbachstr )',6,20,0,NULL),
(101,'Welche 3 Betriebsarten gibt es im Digitalfunk?','TMO, DMO, RMO',7,1,0,NULL),
(102,'Welchen Wasserdurchfluss weist ein C-Mehrzweckstrahlrohr bei 5 bar Strahlrohrdruck auf?','100/200 l/m (mit und ohne Mundstück)',7,2,0,NULL),
(103,'Wie ist die Rettungshöhe der 4-teiligen Steckleiter?','7,2m / 2.OG',7,3,0,NULL),
(104,'Durch eine Lose Rolle wird die mögliche Last…','…verdoppelt.',7,4,0,NULL),
(105,'Wie setzt sich normalerweise die Ungebungsluft zusammen?','N 78%, O 21%, Edelgase < 1%, CO2 0,04 %',7,5,0,NULL),
(106,'Was unfasst Gefahrgutklasse 7?','Radioaktive Stoffe',7,6,0,NULL),
(107,'Welche Schaumart erzeugt man bei einer VZ 10?','Schwerschaum',7,7,0,NULL),
(108,'Was bedeutet der FMS Status 2?','einsatzbereit auf Wache',7,8,0,NULL),
(109,'Welche Aufgabe(n) hat der Melder bei Einsätzen nach FwDV 3?','Er übernimmt befohlene Aufgaben.',7,9,0,NULL),
(110,'Was ist in der FwDV7 geregelt?','Ausbildung, die Fortbildung und den Einsatz unter und mit Atemschutz',7,10,0,NULL),
(111,'Welcher (welches) Stoff (Stoffgemisch) ist durch ein ovales Handrad an der Gasflasche zu erkennen?','Acetylen',7,11,0,NULL),
(112,'Mit welchem Kennwort(en) wird durch den Atemschutztrupp eine Notfallmeldung abgesetzt?','„MAYDAY; MAYDAY; MAYDAY“',7,12,0,NULL),
(113,'Welcher (welchen) Brandklasse(n) werden Brände fester Stoffe zugeordnet?','Brandklasse A',7,13,0,NULL),
(114,'Welchen FMS Status setze ich beim verlassen der Einsatzstelle nach Ende des Einsatzes?','Status 1',7,14,0,NULL),
(115,'Welche technischen Merkmale hat ein Zumischer Z8?','800l/min Wasserleistung, B-Kupplung',7,15,0,NULL),
(116,'Mit welchem Knoten wird gemäß FwDV10 das Zugseil einer Schiebleiter befestigt?','Mastwurf',7,16,0,NULL),
(117,'Welchen FMS Status setze ich beim übernehmen des Einsatzauftrages bzw. verlassen des Gerätehauses mit Einsatzauftrag?','Status 3',7,17,0,NULL),
(118,'Wie viele Straßen sind in Spich anch ehemaligen Löschgruppenführern benannt?','2 (Fliersbachstr, Franz-Bergen-Str)',7,18,0,NULL),
(119,'Wie viele Steckleiterteile dürfen maximal zusammen verwendet werden?','4',7,19,0,NULL),
(120,'Welche Aufgabe(n) hat der Angriffstrupp bei Brandeinsätzen ohne Bereitstellung nach FwDV 3?','Er nimmt das erste einzusetzende Strahlrohr vor und setzt den Verteiler',7,20,0,NULL),
(121,'Welche Löscheffekte gibt es?','Stickeffekt, Kühleffekt, Inhibition',7,21,0,NULL),
(122,'Welche Vorteile haben Oberflurhydranten?','Gut Sichtbar, Schnell einsatzbereit',7,22,0,NULL),
(123,'Nenne die Luftverzleichszahl von Chlor','71',7,23,0,NULL),
(124,'Wann wurde die LG Spich gegründet?','06.02.1911',7,24,0,NULL),
(125,'Wie lang ist die 3-teilige Schiebleiter?','14m',7,25,0,NULL),
(126,'In welcher(n) Maßeinheit(en) werden Förderströme von Feuerwehrpumpen üblicherweise angegeben?','liter pro Minute',7,26,0,NULL),
(127,'Wie lang ist die 4-teilige Steckleiter komplett?','8,4m',7,27,0,NULL),
(128,'Als was können tragbare Leitern der Feuerwehr grundsätzlich eingesetzt werden?','Rettungsweg, Angriffsweg, Hilfsgerät',7,28,0,NULL),
(129,'Welcher (welchen) Brandklasse(n) werden Brände gasförmiger Stoffe zugeordnet?','Brandklasse C',7,29,0,NULL),
(130,'Welches Löschmittel ist bei brennendem Holz am besten geeignet?','Wasser',7,30,0,NULL),
(131,'In Welcher Norm ist das Spicher LF genormt?','DIN 14530',NULL,NULL,0,NULL),
(132,'Welche(s) Löschmittel sind (ist) bei brennendem Dieselkraftstoff auf der Straße geeignet?','Mittelschaum, ABC-Pulver',NULL,NULL,0,NULL),
(133,'Was ist ist nicht auf unserem Spicher LF verlastet, gehört aber nach aktueller Norm zur Ausrüctung eines LF20?','Sprungrettungsgerät (& 4 CSA)',NULL,NULL,0,NULL),
(134,'Ab wann spricht man bei Wechselspannung von Hochspannung in einer Anlage?','1000V',NULL,NULL,0,NULL),
(135,'Wofür steht im ABC-Einsatz die Abkürzung GAMS?','Gefahr erkennen, Absperren des Gefahrenbereichs, Menschenrettung einleiten, Spezialkräfte nachfordern.',NULL,NULL,0,NULL),
(136,'Wofür steht die Abkürzung OEG?','Obere Explosionsgrenze',NULL,NULL,0,NULL),
(137,'Wo wird das Wegerecht geregelt?','§38 StVO',NULL,NULL,0,NULL),
(138,'Was unfasst Gefahrgutklasse 1?','explosive Stoffe',NULL,NULL,0,NULL),
(139,'In Welcher FwDV werden Leitern beschrieben?','FwDV10',NULL,NULL,0,NULL),
(140,'Welchen FMS Status setze ich beim ankommen am Gerätehaus nach Ende des Einsatzes?','Status 2',NULL,NULL,0,NULL),
(141,'Wann dürfen Atemfilter nicht eingesetzt werden?','Art der Atemgifte unbekannt, starke Rußbildung, unzureichend Luftsauerstoff',NULL,NULL,0,NULL),
(142,'Was bedeutet der FMS Status 4?','Ankunft am Einsatzort ',NULL,NULL,0,NULL),
(143,'Was versteht man unter Körperschutz Form 3?','Gasdichter Chemikalienschutzanzug',NULL,NULL,0,NULL),
(144,'Gegen welche(n) Stoff(e) schützt der ABEK2-P3 Filter nicht?','Kohlenstoffmonoxid',NULL,NULL,0,NULL),
(145,'Was bedeutet der FMS Status 5?','Sprechwunsch',NULL,NULL,0,NULL),
(146,'Wer darf Wegerechte in Anspruch nehmen? Nenne 5!','Feuerwehr, Polizei, Rettungsdienst, Notfallmanager der DB, Bundeswehr, Stadtwerke, Zoll, THW',NULL,NULL,0,NULL),
(147,'Wie viel Wasser fasst ein 15 m C42-Druckschlauch?','21 Liter',NULL,NULL,0,NULL),
(148,'Welchen FMS Status setze ich bei Großschadenslagen oder Großeinsatzlagen, bei viel Funkverkehr, wenn ich einen Sprechwunsch habe?','Status 5',NULL,NULL,0,NULL),
(149,'Wie viel % des Nennfülldrucks müssen Atemschutzgeräte beinhalten, damit Sie eingesetzt werden dürfen?','> 90%',NULL,NULL,0,NULL),
(150,'Der wievielte LG Führer ist Alexander Ossendorf?','14.',NULL,NULL,0,NULL),
(151,'Welche technischen Merkmale hat ein Zumischer Z4?','400l/min Wasserleistung, C-Kupplung',NULL,NULL,0,NULL),
(152,'Wer ist für die Rückstellung einer ausgelösten Brandmeldeanlage zuständig?','Der Einsatzleiter',NULL,NULL,0,NULL),
(153,'Wer darf, unter gebührender Berücksichtigung der öffentlichen Sicherheit und Ordnung, Sonderrechten nach §35 StVO ausüben? Nenne 5!','Feuerwehr, Polizei, Rettungsdienst, Notfallmanager der DB, Bundeswehr, Stadtwerke, Zoll, THW, Stadtreinigung, Müllabfuhr',NULL,NULL,0,NULL),
(154,'Welchen Wasserdurchfluss weist ein B-Mehrzweckstrahlrohr bei 5 bar Strahlrohrdruck auf?','400/800 l/m (mit und ohne Mundstück)',NULL,NULL,0,NULL),
(155,'Welche Hydranten werden für Feuerlöschzwecke genutzt?','Unterflurhyranten, Oberflurhydranten, Wandhydranten',NULL,NULL,0,NULL),
(156,'Welchen Wasserdurchfluss weist ein D-Mehrzweckstrahlrohr bei 5 bar Strahlrohrdruck auf?','25/50 l/m (mit und ohne Mundstück)',NULL,NULL,0,NULL),
(157,'Welche Information(en) kann man Hinweisschildern für Hydranten entnehmen?','Nennweite der Versorgungsleitung, Lage des Hydranten (evtl Nummer)',NULL,NULL,0,NULL),
(158,'Welche taktische Einheit ist die Grundeinheit der Feuerwehr?','Die Gruppe',NULL,NULL,0,NULL),
(159,'Womit kann der pH-Wert von Flüssigkeiten im Einsatz ermittelt werden?','Indikatorpapier?',NULL,NULL,0,NULL),
(160,'Wofür steht die Abkürzung UVV?','Unfallverhütungsvorschriften',NULL,NULL,0,NULL),
(161,'Eine 6 Liter Pressluftflasche ist mit Atemluft und einem Fülldruck von 300 bar gefüllt. Wie viel Liter Atemluft entspricht dies bei 1 bar Umgebungsdruck (Faustwert)?','1600 Liter',NULL,NULL,0,NULL),
(162,'Welche Schaumart erzeugt man bei einer VZ 201?','Leichtschaum',NULL,NULL,0,NULL),
(163,'Wie hieß der erste Löschgruppenführer der LG Spich?','Conrad Fliersbach',NULL,NULL,0,NULL),
(164,'Aus welchen Materialien darf die Steckleiter nach FwDV10 sein?','Holz, Aluminium',NULL,NULL,0,NULL),
(165,'Nenne die Luftverzleichszahl von Kohlenstoffmonoxid','28',NULL,NULL,0,NULL),
(166,'Welche Einsatzkraft (Einsatzkräfte) darf (dürfen) per Gesetz bei einem Feuerwehreinsatz einen Platzverweis aussprechen?','Polizei, Einsatzleiter',NULL,NULL,0,NULL),
(167,'Wie rufen wir per TMO die Leitstelle an?','Leitstelle Rhein Sieg von Spich LF20, kommen!',NULL,NULL,0,NULL),
(168,'Was ist (sind) zulässige Sicherung(en) für den Rückweg im Atemschutzeinsatz?','Feuerwehrleine, Schlauchleitung',NULL,NULL,0,NULL),
(169,'Wo wird das 1. Rohr am Verteiler (in Flussrichtung) angeschlossen?','Links',NULL,NULL,0,NULL),
(170,'Bis zu welchem Obergeschoss kann die 3-teilige Schiebleiter üblicherweise eingesetzt werden?','3. OG',NULL,NULL,0,NULL),
(171,'Wie viel Wasser fasst ein 20 m A-Druckschlauch?','190 Liter',NULL,NULL,0,NULL),
(172,'Was bedeutet ein X auf der orangenen Gefahrgut-Warntafel','Stoff reagiert gefährlich mit Wasser',NULL,NULL,0,NULL),
(173,'Aus welchen Trupps und Personen besteht eine Staffel?','Staffelführer, Maschinist, Angriffstrupp, Wassertrupp',NULL,NULL,0,NULL),
(174,'Welche Pumpe ist bei einem LF20 verbaut?','FPN 10-2000',NULL,NULL,0,NULL);
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

-- Dump completed on 2024-09-26 16:29:15
