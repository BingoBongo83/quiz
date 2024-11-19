-- -------------------------------------------------------------
-- -------------------------------------------------------------
-- TablePlus 1.2.2
--
-- https://tableplus.com/
--
-- Database: mariadb
-- Generation Time: 2024-11-18 14:15:27.184042
-- -------------------------------------------------------------
SEt FOREIGN_KEY_CHECKS=0;

CREATE TABLE `config` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `value` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `last_question` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `question` varchar(255) DEFAULT NULL,
  `answer` varchar(255) DEFAULT NULL,
  `image` varchar(64) DEFAULT NULL,
  `comment` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `max_questions` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `round` varchar(64) DEFAULT NULL,
  `maximum` bigint(20) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `play_off` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `player` bigint(20) unsigned DEFAULT NULL,
  `points` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `name_idx` (`player`),
  CONSTRAINT `fk_name_2` FOREIGN KEY (`player`) REFERENCES `player` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `player` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB AUTO_INCREMENT=204 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `round` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `round` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `config` (`id`, `name`, `value`) VALUES
(1, 'monitor_round', '0'),
(2, 'buzzer_blocked', '4'),
(10, 'final_date', 'Dec 19 2024  18:00:00'),
(11, 'player_correct', '0'),
(12, 'play_mode', '1'),
(13, 'play_round', '1'),
(14, 'buzzer_pressed', '4'),
(15, 'version', '0.9');

INSERT INTO `last_question` (`id`,`question`,`answer`,`image`,`comment`) VALUES (1,'','','standard.jpg','');

INSERT INTO `max_questions` (`id`, `round`, `maximum`) VALUES
(1, '1', 15),
(2, '2', 15),
(3, '3', 15),
(4, '4', 15),
(5, '5', 20),
(6, '6', 20),
(7, '7', 25);

INSERT INTO `play_off` (`id`, `player`, `points`) VALUES
(1, 4, 6),
(2, 5, 10),
(3, 11, 4),
(4, 1, 4),
(5, 6, 4),
(6, 12, 2);

INSERT INTO `player` (`id`, `name`) VALUES
(1, 'Alena'),
(2, 'Michelle'),
(3, 'Leni'),
(4, 'Ilja'),
(5, 'Lara'),
(6, 'Renato'),
(7, 'Kordula'),
(8, 'Fredi'),
(9, 'Ann'),
(10, 'Harri'),
(11, 'Philippe'),
(12, 'Nicole'),
(13, 'Franjo'),
(14, 'Stilla'),
(15, 'Hans-Herbert'),
(16, 'Eleonore');

INSERT INTO `player_round` (`id`, `player_round_id`, `player`, `round`, `points`, `is_active`, `color`) VALUES
(1, 1, 1, 1, 0, 1, NULL),
(2, 2, 2, 1, 0, 1, NULL),
(3, 3, 3, 1, 0, 1, NULL),
(4, 4, 4, 1, 0, 1, NULL),
(5, 1, 5, 2, 0, 1, NULL),
(6, 2, 6, 2, 0, 1, NULL),
(7, 3, 7, 2, 0, 1, NULL),
(8, 4, 8, 2, 0, 1, NULL),
(9, 1, 9, 3, 0, 1, NULL),
(10, 2, 10, 3, 0, 1, NULL),
(11, 3, 11, 3, 0, 1, NULL),
(12, 4, 12, 3, 0, 1, NULL),
(13, 1, 13, 4, 0, 1, NULL),
(14, 2, 14, 4, 0, 1, NULL),
(15, 3, 15, 4, 0, 1, NULL),
(16, 4, 16, 4, 0, 1, NULL),
(17, 1, 1, 5, 0, 1, NULL),
(18, 2, 5, 5, 0, 1, NULL),
(19, 3, 10, 5, 0, 1, NULL),
(20, 4, 14, 5, 0, 1, NULL),
(21, 1, 9, 6, 0, 1, NULL),
(22, 2, 13, 6, 0, 1, NULL),
(23, 3, 2, 6, 0, 1, NULL),
(24, 4, 6, 6, 0, 1, NULL),
(25, 1, 1, 7, 0, 1, NULL),
(26, 2, 9, 7, 0, 1, NULL),
(27, 3, 5, 7, 0, 1, NULL),
(28, 4, 13, 7, 0, 1, NULL),
(29, 1, 1, 8, 0, 1, NULL);

INSERT INTO `questions` (`id`, `question`, `answer`, `round`, `seq`, `played`, `comment`, `image`) VALUES
(111, 'Wer war der erste Bundeskanzler der BRD?', 'Konrad Adenauer', 1, 1, 0, 'Kommentar', 'adenauer.jpg'),
(112, 'Wie hoch ist der Kölner Dom?', '157 Meter', 1, 2, 0, 'Kommentar', 'koelnerdom.jpg'),
(113, 'der wievielte Monat ist der September?', 'der 9.', 1, 18, 0, 'Kommentar', 'september.jpg'),
(114, 'Welcher Berg ist der höchste Berg der Welt?', 'Mount Everest', 1, 3, 0, '8849 meter', 'mounteverest.jpg'),
(115, 'Wer war der erste Präsident der Vereinigten Staaten von Amerika?', 'George Washington', 2, 1, 0, '1789 - 1797 Präsident der USA', 'washington.jpg'),
(116, 'In welcher Stadt lebte der Detektiv Sherlock Holmes?', 'London', 1, 4, 0, 'Baker Street 221b', 'sherlockholmes.jpg'),
(117, 'Wie heißt die Hauptstadt von Ungarn?', 'Budapest', 1, 5, 0, 'Kommentar', 'budapest.jpg'),
(118, 'Welcher Planet unseres Sonnensystems ist der Sonne am nächsten?', 'Merkur', 1, 6, 0, 'Merkur, Venus, Erde, Mars, Jupiter, Saturn, Uranus, Neptun', 'merkur.jpg'),
(119, 'An welchem Tag fiel die Berliner Mauer?', '9. November 1989', 2, 2, 0, 'Kommentar', 'mauerfall.jpg'),
(120, 'Wie viele Beine hat eine Spinne?', '8', 2, 3, 0, 'Kommentar', 'spinne.jpg'),
(121, 'Wie viele Sekunden hateine Stunde?', '3600', 2, 17, 0, 'Kommentar', 'uhr.jpg'),
(122, 'Wie viele Punkte hat ein standard Würfel?', '21', 2, 6, 0, '', 'wuerfel.jpg'),
(123, 'Auf welchem Kontinent liegt die größte Wüste der Welt?', 'Antarktis', 7, 1, 0, 'Kommentar', 'antarktis.jpg'),
(124, 'Wie heißt die Hauptstadt von Irland?', 'Dublin', 3, 1, 0, 'Kommentar', 'dublin.jpg'),
(125, 'Welcher Fluss durchfließt den Grand Canyon?', 'Colorado River', 5, 1, 0, 'Kommentar', 'colorado.jpg'),
(126, 'Welche Staatsflagge hat als einzige keine 4 Seiten?', 'Nepal', 7, 2, 0, 'Kommentar', 'nepal.jpg'),
(127, 'In welchem Land wird am meisten Kaffee getrunken?', 'Finnland', 5, 2, 0, '12 Kg pro Person
Deutschland: 5Kg', 'finnland.jpg'),
(128, 'Von wann bis wann dauerte der 1. Weltkrieg?', '1914-1918', 3, 2, 0, 'Kommentar', 'weltkrieg1.jpg'),
(129, 'In welchem Jahr landete Christoph Kolumbus in Amerika?', '1492', 5, 3, 0, 'Kommentar', 'christopherkolumbus.jpg'),
(130, 'Was ist eine Primzahl?', 'Eine Zahl, die nur durch 1 und sich selbst teilbar ist.', 1, 8, 0, '2,3,5,7,11,13,17,19,23,29,31,37,41', 'primzahlen.jpg'),
(131, 'Wie viele Planeten gehören zu unserem Sonnensystem?', '8', 3, 3, 0, 'Merkur, Venus, Erde, Mars, Jupiter, Saturn, Uranus, Neptun', 'sonnensystem.jpg'),
(132, 'Aus was besteht ein Diamant?', 'Kohlenstoff', 2, 7, 0, 'Kommentar', 'diamant.jpg'),
(133, 'Wie oft finden die Wahlen zum Europäischen Parlament statt?', 'alle 5 Jahre', 6, 1, 0, 'Kommentar', 'europaparlament.jpg'),
(134, 'Wie heißt der freche Kobold von Meister Eder? ', 'Pumuckl', 1, 9, 0, 'Kommentar', 'pumuckl.jpg'),
(135, 'Welcher ist der längste Fluss der Welt?', 'Der Nil', 5, 4, 0, '6671 km', 'nil.jpg'),
(136, 'Welche Farbe hat die Null beim Roulette?', 'Grün', 5, 5, 0, 'Kommentar', 'roulettenull.jpg'),
(137, 'Aus welchem Land kommt die Band AC DC?', 'Aus Australien', 2, 9, 0, '1973 gegründet', 'acdc.jpg'),
(138, 'In welchem Jahr starb John F. Kennedy', '1963', 3, 4, 0, '22. November 1963 in Dallas', 'kennedy.jpg'),
(139, 'Welches menschliche Organ verbraucht die meiste Energie?', 'Das Gehirn', 1, 10, 0, 'circa 500 KiliKalorien per Tag', 'gehirn.jpg'),
(140, 'In welchem Jahr landete der erste Mensch auf dem Mond?', '1969', 4, 1, 0, '20. Juli 1969 Apollo 11', 'apollo11.jpg'),
(141, 'In welchem Jahr fand die Katastrophe von Tschernobyl statt?', '1986', 6, 2, 0, '26. April 1986 Prypjat', 'tschernobyl.jpg'),
(142, 'Welche Farben hat die mexikanische Flagge?', 'Grün, Weiß, Rot', 1, 11, 0, 'Grün: Hoffnung
Weiß: Einheit
Rot: Blut der Helden', 'mexico.jpg'),
(143, 'Wer war während des WW2 Premierminister des UK?', 'Winston Churchill', 5, 6, 0, 'Kommentar', 'churchill.jpg'),
(144, 'Wie lautet das Chemische Symbol für Gold?', 'Au', 5, 7, 0, 'aurum', 'aurum.jpg'),
(145, 'Wie heißt die Hauptstadt von Island?', 'Reykjavik', 2, 10, 0, 'Kommentar', 'reykjavik.jpg'),
(146, 'Welche Entdeckung machte Marie Curie', 'Radioaktivität', 3, 5, 0, 'Kommentar', 'radioaktivitaet.jpg'),
(147, 'Welches ist da flächenmäßig größte Land der Welt?', 'Russland', 4, 2, 0, '17.098.242 km2', 'russia.jpg'),
(148, 'Wo wird im menschlichen Körper Insulin produziert?', 'in der Bauchspeicheldrüse', 4, 3, 0, 'Kommentar', 'pankreas.jpg'),
(149, 'Welche Schauspielerin spielte Prinzessin Leia in der Star Wars saga?', 'Carrie Fisher', 6, 3, 0, 'Kommentar', 'carriefisher.jpg'),
(150, 'Wie lange dauert ein Fußballspiel?', '90 Minuten (2x45)', 2, 12, 0, 'Kommentar', 'fussball.jpg'),
(151, 'Wie heißt der zweithöchste Berg der Erde?', 'K2', 4, 4, 0, '8611 m', 'k2.jpg'),
(152, 'Wie hieß Marylin Monroe wirklich?', 'Norma Jeane Baker', 7, 3, 0, 'Kommentar', 'marylinmonroe.jpg'),
(153, 'Welches Säugetier kann fliegen?', 'Fledermaus / Flughund', 3, 6, 0, 'beide gehören zu den Fledertieren', 'fledermaus.jpg'),
(154, 'Wie viele Elemente enthält das Periodensystem?', '118', 5, 8, 0, 'Kommentar', 'periodensystem.jpg'),
(155, 'Welcher roman von Stephen King spielt im Overlook Hotel?', 'Shining', 7, 4, 0, 'Mit Jack Nicholson in der Hauptrolle (1980)', 'shining.jpg'),
(156, 'Wer war der erste Mensch auf dem Mond?', 'Neil Armstrong', 7, 5, 0, '20. Juli 1969', 'armstrong.jpg'),
(157, 'Wie heißt das am meisten verkaufte Musikalbum aller Zeiten?', 'Thriller - Michael Jackson', 5, 9, 0, 'Kommentar', 'thriller.jpg'),
(158, 'Was ist das größte menschliche Organ?', 'Die Haut', 2, 13, 0, 'Kommentar', 'haut.jpg'),
(159, 'Welches ist die weltweit größte Stadt?', 'Tokio', 3, 7, 0, '38 mio Einwohner', 'tokio.jpg'),
(160, 'Welcher Film erhielt die bisher meisten Oskars?', 'Titanic (1997)', 4, 5, 0, '11 Oscars', 'standard.jpg'),
(161, 'Wer hat die Mona Lisa gemalt?', 'Leonardo DaVinci', 2, 14, 0, 'Kommentar', 'monalisa.jpg'),
(162, 'Wie viele Tage hat ein Jahr?', '365', 1, 12, 0, 'Schaltjahr 366', 'kalender.jpg'),
(163, 'Wie lautet die chemische Formel für Wasser?', 'H20', 1, 13, 0, 'Kommentar', 'wetfloor.jpg'),
(164, 'Was ist die Quadratwurzel von 64?', '8', 1, 14, 0, 'Kommentar', 'mathe.jpg'),
(165, 'Welcher Schauspieler gewann den Oscar für Philadelphia und Forest Gump?', 'Tom Hanks', 1, 15, 0, 'Kommentar', 'hanks.jpg'),
(166, 'Wie heißt die Band mit folgenden Mitgliedern: John Deacon, Roger Taylor, Brian May, Freddie Mercury?', 'Antwort', 2, 15, 0, 'Kommentar', 'queen.jpg'),
(167, 'Welcher amerikanische Popstar hatte 2015 mit den Singles „Sorry“ und „Love Yourself“ zwei aufeinanderfolgende Chart-Erfolge?', 'Justin Bieber', 3, 8, 0, 'Kommentar', 'justinbieber.jpg'),
(168, 'Wer wählt den Bundespräsidenten?', 'Die Bundesversammlung', 7, 6, 0, 'Kommentar', 'bundesversammlung.jpg'),
(169, 'Wie heißt die Landeshauptstadt von Thüringen?', 'Erfurt', 2, 16, 0, 'Kommentar', 'thueringen.jpg'),
(170, 'In welcher Einheit wird der elektrische Widerstand gemessen?', 'Ohm', 3, 9, 0, 'U = R*I', 'ohm.jpg'),
(171, 'Wofür steht das L in RTL?', 'Luxembourg', 4, 6, 0, 'Radio Television Luxembourg', 'rtl.jpg'),
(172, 'Wie beginnt Artikel 1 des Grundgesetzes?', 'Die Würde des Menschen ist unantastbar.', 1, 7, 0, 'Kommentar', 'grundgesetz.jpg'),
(173, 'Wie lautet das chemische Symbol für Blei?', 'Pb', 2, 8, 0, 'plumbum', 'blei.jpg'),
(174, 'Wer verbreitete das heliozentrische Weltbild?', 'Nikolaus Kopernikus', 5, 10, 0, 'Kommentar', 'kopernikus.jpg'),
(175, 'Wie lautet der Satz des Pythagoras?', 'a²+a²=c²', 3, 10, 0, 'a+b=katheten
c=Hypotenuse', 'pytagoras.jpg'),
(176, 'Welche 3 Staatsgewalten gibt es in Deutschland?', 'Legislative, Exekutive, Judikative', 6, 4, 0, 'Legislative=gesetzgebend
Exekutive=vollziehend
Judikative=richterliche', 'gewalten.jpg'),
(177, 'Was bedeutet LCD?', 'liquid crystal display', 4, 7, 0, 'Kommentar', 'lcd.jpg'),
(178, 'Was bedeutet LED?', 'light emitting diod', 2, 4, 0, 'LIchtemittierende Diode', 'led.jpg'),
(179, 'Wer war der 2. Bundeskanzler der BRD?', 'Ludwig Erhard', 6, 5, 0, 'Bereits Wirtschaftsminister unter Adenauer', 'erhard.jpg'),
(180, 'Wie viele Bundesländer hat die BRD?', '16', 3, 11, 0, 'Schleswig-Holstein, Meck-Pom,HH,HB,Brandenburd,Berlin,Niedersachsen,Sachsen-Anhalt,NRW,Sachsen,Thüringen,Hessen,RLP,Saarland,Bayern,BW', 'bundeslaender.jpg'),
(181, 'Wie viele Länder grenzen an die BRD?', '9', 2, 5, 0, 'FR,BE,NL,LUX,DEN,PL,CZ,AUT,CHE', 'brd.jpg'),
(182, 'Wie heißt die Hauptstadt von Australien?', 'Canberra', 3, 12, 0, 'Kommentar', 'canberra.jpg'),
(183, 'Wofür steht die Abkürzung IT?', 'Informationstechnik', 4, 8, 0, 'Kommentar', 'it.jpg'),
(184, 'Welches ist flächenmäßig das größte Bundesland der BRD?', 'Bayern', 4, 9, 0, '70550km²', 'bayern.jpg'),
(185, 'In welcher Einheit wird die elektrische Spannung gemessen?', 'Volt', 4, 10, 0, 'Kommentar', 'volt.jpg'),
(186, 'Wie heißt die Hauptstadt von Äthiopien?', 'Addis Abeba', 5, 11, 0, 'Kommentar', 'addisabeba.jpg'),
(187, 'Wer wohnt in der Downing Street 10 in  London?', 'Der englische Premierminister', 6, 6, 0, 'Kommentar', 'downingstreet.jpg'),
(188, 'Wie lautet das Chemische Symbol für Eisen?', 'Fe', 3, 13, 0, 'ferrum', 'ferrum.jpg'),
(189, 'Wie lautet das chemische Symbol für Stickstoff?', 'N', 4, 11, 0, 'nitrogenium', 'nitrogenium.jpg'),
(190, 'Wie lautet das chemische Symbol für Uran?', 'U', 7, 7, 0, 'Nach dem Planeten Uranus', 'uran.jpg'),
(191, 'Wie heißt der kleinste Staat der Welt?', 'Vatikan', 1, 16, 0, 'ca 770 Einwohner', 'vatikan.jpg'),
(192, 'Wo liegen die Langerhans Inseln?', 'in der Bauchspeicheldrüse', 7, 8, 0, 'Für die Hormbildung zuständig', 'langerhans.jpg'),
(193, 'Wie viele Kontinente gibt es auf der Erde?', '7', 1, 17, 0, 'Nordamerika, Südamerika, Europa, Afrika, Asien, Australien, Antarktika', 'kontinente.jpg'),
(194, 'Welches ist die viertgrößte Stadt der BRD?', 'Köln', 2, 11, 0, 'Nach Berlin, HH, München', 'koeln.jpg'),
(195, 'Welches Ereignis war der Auslöser des 30-jährigen Krieges?', 'Prager Fenstersturz', 7, 9, 0, 'Kommentar', 'pragerfenstersturz.jpg'),
(196, 'Wie lang ist ein Marathon?', '42,195km', 6, 7, 0, 'Kommentar', 'marathon.jpg'),
(197, 'Wie heißt die Hauptstadt von Indonesien?', 'Jakarta', 4, 12, 0, 'Kommentar', 'jakarta.jpg'),
(198, 'Zu welchem Land gehört Grönland?', 'Königreich Dänemark', 1, 19, 0, 'Eigene Regierung , eigenes Parlament', 'groenland.jpg'),
(199, 'Welcher Partei gehörte Adenauer an?', 'CDU', 1, 20, 0, 'Kommentar', 'adenauer.jpg'),
(200, 'Wie groß ist die Summer aller Winkel in einem Dreieck?', '180°', 3, 14, 0, 'Kommentar', 'winkelsummedreieck.jpg'),
(201, 'Mit welchen 3 Ziffern beginnt die Kreiszahl Pi?', '3,14', 4, 13, 0, '3,141592653589793', 'pi.jpg'),
(202, 'Wer schrieb den Erlkönig?', 'Johann Wolfgang von Goethe', 3, 15, 0, 'Kommentar', 'erlkoenig.jpg'),
(203, 'Wer schrieb Krieg und Frieden?', 'Leo Tolstoi', 6, 8, 0, 'Kommentar', 'kriegundfrieden.jpg');

INSERT INTO `round` (`id`, `round`) VALUES
(1, 'Vorrunde 1'),
(2, 'Vorrunde 2'),
(3, 'Vorrunde 3'),
(4, 'Vorrunde 4'),
(5, 'Halbfinale 1'),
(6, 'Halbfinale 2'),
(7, 'Finale'),
(8, 'Gewinner'),
(9, 'Pause');

SET FOREIGN_KEY_CHECKS = 1;
