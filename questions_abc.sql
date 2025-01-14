-- -------------------------------------------------------------
-- -------------------------------------------------------------
-- TablePlus 1.2.2
--
-- https://tableplus.com/
--
-- Database: quizduell
-- Generation Time: 2025-01-14 15:49:11.283139
-- -------------------------------------------------------------

DROP TABLE `questions`;


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
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `questions` (`id`, `question`, `answer`, `round`, `seq`, `played`, `comment`, `image`) VALUES 
(1, 'In welchem Gerätefach finden wir Edelstahltrichter?', 'G2', 1, 1, 1, 'Kommentar', 'standard.jpg'),
(2, 'Wie viele Atemanschlüsse halten wir vor?', '9', 5, 1, 1, 'Kommentar', 'standard.jpg'),
(3, 'Wo finden wir Material zur Stromerzeugung/Verteilung?', 'G3', 1, 3, 1, 'Kommentar', 'standard.jpg'),
(4, 'Welche Farben hat das Absperrband ("Flatterband") auf dem AB-G?', 'Rot/Weiß & Schwarz/Gelb', 1, 4, 1, 'Kommentar', 'standard.jpg'),
(5, 'Von welchem Hersteller ist der Dosisleistungsmesser "Teletektor"?', 'Graetz', 1, 6, 1, 'Kommentar', 'standard.jpg'),
(6, 'Wie viele Warnschilder "Radioaktiv" halten wir auf dem AB-G vor?', '4', 7, 6, 1, 'Kommentar', 'standard.jpg'),
(7, 'Wo finden wir alle verfügbaren Geräte zur Messung im A-Einsatz?', 'GR', 1, 7, 1, 'Kommentar', 'standard.jpg'),
(8, 'Was bin ich? Wir haben mich 4mal auf dem AB-G, ich habe einen Griff, ich habe 50m Einsatzreichweite, ich habe eine Kurbel, ich befinde mich in G1', 'Leitungsroller 50m', 1, 8, 1, 'Kommentar', 'standard.jpg'),
(9, 'Wo finden wir den Klapptisch?', 'G6', 1, 9, 1, 'Kommentar', 'standard.jpg'),
(10, 'Holt mir 1 Warnschild "Radioaktiv" und 1 Edelstahleimer vom AB-G', 'AKTION', 3, 10, 1, 'Kommentar', 'standard.jpg'),
(11, 'Wo befindet sich die AÜ Tafel?', 'GR', 1, 11, 1, 'Kommentar', 'standard.jpg'),
(12, 'Wie viele Gerätefächer hat der AB-G?', '7', 1, 12, 1, 'Kommentar', 'standard.jpg'),
(13, 'Wo finden wir die Kontaminationsschutzanzüge?', 'GR', 6, 3, 1, 'Kommentar', 'standard.jpg'),
(14, 'Was finden wir sowohl in G2 als auch in G1?', 'Handmembranpumpe (Saug- Druckschlauch DN50 (jedoch unterschiedliche Längen)', 5, 4, 1, 'Kommentar', 'standard.jpg'),
(15, 'Nenne 3 Teile aus G1!', 'Siehe Beladeliste', 1, 5, 1, 'Kommentar', 'standard.jpg'),
(16, 'Welches Gerätefach befindet sich gegenüber G3', 'G4', 2, 1, 1, 'Kommentar', 'standard.jpg'),
(17, 'Wo finden wir die Trittleitern ?', 'G6 und G5', 2, 2, 1, 'Kommentar', 'standard.jpg'),
(18, 'Nenne drei Teile aus G4', 'siehe Beladeliste', 2, 3, 1, 'Kommentar', 'standard.jpg'),
(19, 'In welchen Gerätefächern finden wir Materialien zum abdichten?', 'G2/G5', 2, 4, 1, 'Kommentar', 'standard.jpg'),
(20, 'Wie viele Filter vom Typ ABEK2P3 halten wir auf dem AB-G vor?', '9', 2, 5, 1, 'Kommentar', 'standard.jpg'),
(21, 'Wie viele Alarmdosimeter finden wir auf dem AB-G?', '6', 7, 4, 1, 'Kommentar', 'standard.jpg'),
(22, 'In welchen Gerätefächern finden wir Erdungsmaterialien?', 'G3/G1', 2, 6, 1, 'Kommentar', 'standard.jpg'),
(23, 'Wie viel Paar Gummistiefel haben wir auf dem AB-G?', '5', 2, 7, 1, 'Kommentar', 'standard.jpg'),
(24, 'Holt mir eine Schöpfkelle und eine Löschdecke aus dem AB-G!', 'AKTION', 2, 8, 1, ' (G2 G4 G3)', 'standard.jpg'),
(25, 'Wie viele Handlampen bevorratet der AB-G?', '5', 2, 9, 1, '4x GR, 1x G1', 'standard.jpg'),
(26, 'Wo befinden sich die Kontaminationsschutzhandschuhe?', 'GR', 2, 11, 1, 'Kommentar', 'standard.jpg'),
(27, 'in welchem GF befinden sich die Kabelbinder?', 'G2', 5, 3, 1, 'Kommentar', 'standard.jpg'),
(28, 'Wieviel Volumen hat der Reservekanister für den Stromerzeuger?', '10 liter', 2, 12, 1, 'Kommentar', 'standard.jpg'),
(29, 'Von welchem Hersteller ist der Hochdruckreiniger, der auf dem AB-G verlastet ist?', 'Kärcher', 6, 4, 1, 'Kommentar', 'standard.jpg'),
(30, 'Wie lang ist die Förderlänge aller DN50 Saug- und Druckschläuche, blau-weiß-ring, die verlastet sind?', '30m (4*5 , 1*10)', 2, 13, 1, 'Schätzfrage', 'standard.jpg'),
(31, 'Wie viele Fasspumpen sind verlastet?', '1', 3, 1, 1, 'Kommentar', 'standard.jpg'),
(32, 'Wie viele Pumpwerke sind verlastet?', '2', 3, 2, 1, 'Kommentar', 'standard.jpg'),
(33, 'Wie viele CSA bevorraten wir insgesamt?', '6', 3, 3, 1, 'Kommentar', 'standard.jpg'),
(34, 'Wie viele Wathosen haben wir auf dem AB-G?', 'keine', 3, 4, 1, 'Kommentar', 'standard.jpg'),
(35, 'Auf welcher Fahrzeugseite (Fahrtrichtung) befindet sich G6?', 'Rechts', 3, 5, 1, 'Kommentar', 'standard.jpg'),
(36, 'Nenne mir 3 Dinge aus G2', 'Siehe Beladeliste', 3, 6, 1, 'Kommentar', 'standard.jpg'),
(37, 'In welchen Farben halten wir Abfallsäcke vor?', 'blau / gelb / rot', 3, 7, 1, 'G5 und G2', 'standard.jpg'),
(38, 'Auf welchen Schlauchdurchmesser zum ab- und umpumpen ist unser AB-G ausgelegt?', '50mm (DN50)', 3, 8, 1, 'Kommentar', 'standard.jpg'),
(39, 'Geht zum AB-G, zieht euch ein Paar Gummistiefel und eine warnweste an und kommt in diesen zurück', 'AKTION', 1, 10, 1, 'Kommentar', 'standard.jpg'),
(40, 'Wie hoch ist das Gesamtvolumen beider Falttanks?', '4000l', 5, 2, 1, 'Kommentar', 'standard.jpg'),
(41, 'Welche Leistung hat der Stromerzeuger?', '8kVA', 3, 9, 1, 'Kommentar', 'standard.jpg'),
(42, 'Wir wollen Mineralölhaltige Chemikalien umpumpen. Welchen Schlauch nehmen wir?', 'blau-weiß', 3, 12, 1, 'Kommentar', 'standard.jpg'),
(43, 'Aus welchem Material ist der DN50 Schlauch mit Lilaring?', 'EPDM (Ethlylen-Propylen-Dien-Kautschuk)', 7, 7, 1, 'Kommentar', 'standard.jpg'),
(44, 'Wie viele Verkehrsleitkegel sind auf dem AB-G?', '8', 5, 5, 1, 'Kommentar', 'standard.jpg'),
(45, 'Welche Pumpwerke für die Fasspumpe befinden sich auf dem AB-G?', 'PP/NIRO(VA)', 6, 5, 1, 'Kommentar', 'standard.jpg'),
(46, 'Welches GF ist gegenüber G5?', 'G6', 4, 1, 1, 'Kommentar', 'standard.jpg'),
(47, 'Wie lang ist die gesamte Förderlänge aller verlasteten Chemikaliensaug- und Druckschläuche Lilaring?', '40m (4*5,2*10)', 4, 13, 1, 'Schätzfrage', 'standard.jpg'),
(48, 'Aus welchem Material ist der Dn50 Schlauch mit Blauweiß-Ring?', 'UPE (Ultrahochmolekulares PE)', 4, 2, 1, 'Kommentar', 'standard.jpg'),
(49, 'In welchem GF finden wir das nicht funkenreißende Werkzeug?', 'G6', 4, 3, 1, 'Kommentar', 'standard.jpg'),
(50, 'Auf welcher Fahrzeugseite (Fahrtrichtung) befindet sich G3?', 'Links', 4, 4, 1, 'Kommentar', 'standard.jpg'),
(51, 'Wir müssen Ammoniak umpumpen, welcher DN50 Saug- und Druckschlauch kommt in Frage?', 'lilaring / blau-weiß-ring', 7, 5, 1, 'Kommentar', 'standard.jpg'),
(52, 'Wie viele PE Wannen a 220l befinden sich auf dem AB-G?', '3', 4, 5, 1, 'Kommentar', 'standard.jpg'),
(53, 'In Welchem GF befindet sich der Abgasschlauch?', 'G1', 4, 6, 1, 'Kommentar', 'standard.jpg'),
(54, 'Was bin ich? Ich bin klein, ich kann mit einer Hand bedient werden, ich stehe unter Druck, ich helfe dir bei der Suche, ich befinde mich in G5', 'Lecksuchspray', 4, 7, 1, 'Kommentar', 'standard.jpg'),
(55, 'Geht zum AB-G, zieht euch einen Feuerwehrhelm an, holt euch einen Verkehrsleitkegel und kommt zurück', 'AKTION', 4, 8, 1, 'Kommentar', 'standard.jpg'),
(56, 'Wie viele edelstahlkanister mit 20l Volumen befinden sich auf dem AB-G?', '2', 4, 9, 1, 'Kommentar', 'standard.jpg'),
(57, 'Wo befindet sich der Hochdruckreiniger?', 'G5', 4, 10, 1, 'Kommentar', 'standard.jpg'),
(58, 'Wo befindet sich die Fasspumpe?', 'G2', 4, 11, 1, 'Kommentar', 'standard.jpg'),
(59, 'Nenne mir 5 Dinge aus GR', 'Siehe Beladeliste', 5, 6, 1, 'Kommentar', 'standard.jpg'),
(60, 'Wieviele Erdnägel sind auf dem ABG verlastet?', '6', 4, 12, 1, 'Kommentar', 'standard.jpg'),
(61, 'Wo finden wir die Atemanschlüsse?', 'GR', 1, 2, 1, 'Kommentar', 'standard.jpg'),
(62, 'Wo befinden sich die Handmembranpumpen?', 'G1 und G2', 6, 6, 1, 'Kommentar', 'standard.jpg'),
(63, 'Gegen welche relevanten Gase schützt unser ABEK2P3 Filter nicht?', 'Kohlenmonoxid, Nitrose Gase, Quecksilberdampf', 7, 1, 1, 'Kommentar', 'standard.jpg'),
(64, 'Wie viel Volumen haben die Edelstahl Kanister für Gefahrgut?', 'je 20l', 6, 1, 1, 'Kommentar', 'standard.jpg'),
(65, 'Wo befinden sich eben jene Kanister?', 'G5', 6, 2, 1, 'Kommentar', 'standard.jpg'),
(66, 'Was bin ich? Ich bin dicht, ich bin schwer, ich bin genormt in DIN EN 943-2, ich werde bei Benutzung von innen feucht, keiner mag mich ...', 'CSA', 3, 11, 1, 'Kommentar', 'standard.jpg'),
(67, 'Was bin ich? Ich bin 1/2 m groß, ich wiege ca. 3 kg, ich trage untenrum schwarz, ich bin ansonsten orange', 'Verkehrsleitkegel', 2, 10, 1, 'Kommentar', 'standard.jpg'),
(68, 'Wie hoch sind die Verkehrsleitkegel? (mm)', '500mm', 1, 13, 1, 'Schätzfrage', 'standard.jpg'),
(69, 'Wie viel Volumen haben die Edelstahleimer?', 'je 14l', 3, 13, 1, 'Kommentar', 'standard.jpg'),
(70, 'Geht zum AB-G und zieht ein Paar gelbe Gummihandschuhe an und bringt einen ErsteHilfeKasten mit', 'AKTION', 5, 7, 1, 'Kommentar', 'standard.jpg'),
(71, 'Was bin ich? Es gibt mich in folgenden Größen(zoll): 1/2, 3/4, 1, 1 1/4, 1 1/2, 2, 2 1/2, 3, 4', 'Rohrdichtmanschetten', 5, 8, 1, 'Kommentar', 'standard.jpg'),
(72, 'Wie viele der Handlampen sind Ex-geschützt?', '1', 5, 9, 1, 'die in G1', 'standard.jpg'),
(73, 'Wie viele Besen sind verlastet?', '3', 5, 10, 1, '2 Besen, 1 Handfeger', 'standard.jpg'),
(74, 'Wie viele Schaufeln sind verlastet?', '5', 7, 3, 1, '2 Schaufel, 2 Spaten, 1 Kehrblech', 'standard.jpg'),
(75, 'In welchem GF befindet sich die Putzwolle?', 'G5', 5, 11, 1, 'G5.9', 'standard.jpg'),
(76, 'Welche Farbe hat der Koffer mit den Filmplaketten?', 'blau', 5, 12, 1, 'Kommentar', 'standard.jpg'),
(77, 'Was befindet sich in der Pappröhre in GR?', 'Nuklidkarte', 7, 2, 1, 'Kommentar', 'standard.jpg'),
(78, 'Wo finde ich das Gurtmesser?', 'G5', 7, 8, 1, 'G5.8', 'standard.jpg'),
(79, 'Wie viele Filmplaketten sind verlastet?', '34', 5, 13, 1, 'Kommentar', 'standard.jpg'),
(80, 'Was ist das Baujahr des AB-G?', '1991', 7, 21, 1, 'Kommentar', 'standard.jpg'),
(81, 'Wo sind die Warnwesten verlastet?', 'G1', 6, 7, 1, 'Kommentar', 'standard.jpg'),
(82, 'Welche Grundfläche hat das aufblasbare Zelt?', '16m2 (4x4)', 6, 8, 1, 'Kommentar', 'standard.jpg'),
(83, 'Von Welchem Hersteller ist die Fasspumpe?', 'LUTZ', 6, 9, 1, 'Kommentar', 'standard.jpg'),
(84, 'Geht zum AB-G, zieht Feuerwehrhelm und Lederhandschuhe an und kommt mit einem Besen zurück.', 'AKTION', 6, 10, 1, 'Kommentar', 'standard.jpg'),
(85, 'Für welche 2 Spannungsarten haben wir Leitungsroller?', '230V/400V', 6, 11, 1, 'Kommentar', 'standard.jpg'),
(86, 'Für welche Spannung ist der Ex-Verteiler geeignet?', '230V/400V', 6, 12, 1, 'Kommentar', 'standard.jpg'),
(87, 'Wie ist die Gesamtlänge aller Saug oder Druckschläuche?', '166,4m', 6, 13, 1, 'nur Förderschläuche', 'standard.jpg'),
(88, 'Wie viel bar Druck hat die Pressluftflasche für Arbeitsluft?', '200', 7, 9, 1, 'Kommentar', 'standard.jpg'),
(89, 'Geht zum AB-G, holt eine Rolle Flatterband und einen PA und führt hier im Raum die Einsatzkurzprüfung durch.', 'AKTION', 7, 10, 1, 'Kommentar', 'standard.jpg'),
(90, 'Welchen Wasseranschluss hat der Hochdruckreiniger?', 'D-Storz', 7, 11, 1, 'Kommentar', 'standard.jpg'),
(91, 'Wie viele Funksprechgarnituren sind vorhanden?', '8', 7, 12, 1, 'Kommentar', 'standard.jpg'),
(92, 'Wo ist der Klapptisch verlastet?', 'G6', 7, 13, 1, 'Kommentar', 'standard.jpg'),
(93, 'Welche Gegenstände auf dem AB-G bestehen aus einer Kupfer-Beryllium Legierung?', 'Nicht-funkenreißende Werkzeuge und Armaturen', 7, 14, 1, 'Kommentar', 'standard.jpg'),
(94, 'Wie viel Chemikalienbinder wird vorgehalten?', '5kg', 7, 15, 1, 'Kommentar', 'standard.jpg'),
(95, 'Welche Gegenstände aus Feinripp sind auf dem AB-G verlastet?', 'Unterhemden (11 Stück)', 7, 16, 1, 'Kommentar', 'standard.jpg'),
(96, 'Was bin ich? Mein Erfinder hieß Alfred, ich werde elektrisch betrieben, ich unterliege Sicherheitsüberprüfungen nach BGV-A3, ich bin gelb und in G5', 'Hochdruckreiniger', 7, 17, 1, 'Alfred Kärcher baute aus Dampfstrahlreinigern der US Armee den ersten Hochdruckreiniger', 'standard.jpg'),
(97, 'Wann darf ich die verlasteten Atemschutzfilter nicht einsetzen?', 'siehe Kommentar', 7, 18, 1, 'unbekannte Art und Eigenschaften der Atemgifte
zu Hohe Konzentration der Atemgifte
starke Flockenbildung/Staubbildung
< 17% Luftsauerstoff
Funkenflug
Kohlenmonoxid', 'standard.jpg'),
(98, 'Welche Farben haben die Ringe auf dem ABEK2P3 Filter?', 'Braun, Grau, Gelb, Grün, Weiß', 7, 19, 1, 'Braun: org. Dämpfe
Grau: Anorg. Gase/Dämpfe
Gelb: Schwefeldioxid, Chlorwasserstoff
Grün: Ammoniak
Weiß: Partikel', 'standard.jpg'),
(99, 'Welche RAL Nummer hat die Rote Farbe des AB-G?', 'RAL3000 (Feuerrot)', 7, 20, 1, 'Kommentar', 'standard.jpg'),
(100, 'Wie hoch ist das Behältervolumen des elektr. Saugers?', '48l', 7, 23, 1, 'Kommentar', 'standard.jpg'),
(101, 'Wie ist die angegebene Aufrüstzeit des aufblasbaren Zeltes?', '40 Sekunden', 7, 22, 1, 'Kommentar', 'standard.jpg');

