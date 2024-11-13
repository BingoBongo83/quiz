-- -------------------------------------------------------------
-- -------------------------------------------------------------
-- TablePlus 1.2.2
--
-- https://tableplus.com/
--
-- Database: musikquiz
-- Generation Time: 2024-11-13 12:08:20.871187
-- -------------------------------------------------------------

DROP TABLE `musikquiz`.`songs`;


CREATE TABLE `songs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `artist` varchar(255) DEFAULT NULL,
  `round` bigint(20) unsigned DEFAULT NULL,
  `seq` bigint(20) unsigned DEFAULT NULL,
  `played` bigint(20) unsigned DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL,
  `year` bigint(20) unsigned DEFAULT NULL,
  `cover` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `musikquiz`.`songs` (`id`, `title`, `artist`, `round`, `seq`, `played`, `comment`, `year`, `cover`) VALUES 
(1, 'Ordinary World ', 'Duran Duran', 1, 3, 0, 'Benannt nach dem Bösewicht Durand Durand,
aus den SciFiFilm Barbarella
', 1993, 'R-854954-1165753222.jpg'),
(2, 'Love Will Tear Us Apart', 'Joy Division ', 1, 2, 0, 'Kurz vor dem Suizid von Sänger Ian Curtis veröffentlich, Love will tear us apart steht auf seinem Grabstein ', 1980, 'R-28027-1163963079.jpg'),
(4, ' Boom, Boom, Boom, Boom!! ', 'Vengaboys ', 1, 4, 0, 'Erste Strophe aus `Lay all your love on me - ABBA` ', 1998, 'R-371317-1466283790-1815.jpg'),
(5, 'Bitter Sweet Symphony', 'The Verve ', 1, 5, 0, 'Streicher aus einer Orchester-Version von `the last time - rolling stones`', 1997, 'R-881598-1230071652.jpg'),
(6, 'Come As You Are ', 'Nirvana ', 1, 6, 0, 'Come as you are steht auf den Ortseingangschilder der Stadt Aberdeen
(Geburtort Kurt Cobain)', 1991, 'R-783216-1416890641-7794.jpg'),
(7, 'Don`t Speak ', 'No Doubt ', 1, 7, 0, '', 1995, 'R-678365-1594718493-2561.jpg'),
(8, 'Hyper Hyper ', 'Scooter ', 1, 8, 0, 'Feinste Lyric von Hans Peter Gerdes', 1994, 'R-125910-1395612429-9704.jpg'),
(9, 'Ein bisschen Aroma', 'Roger Whittaker ', 1, 9, 0, '', 1986, 'R-3048914-1709500460-5114.jpg'),
(10, 'Only You ', 'Yazoo ', 1, 10, 0, 'Vince clark schrieb den Song mit Depeche Mode

erst mit Yazoo (mit Alyson Moyet) aufgenommen
', 1982, 'R-4824598-1426733035-2407.jpg'),
(11, 'Eins Zwei Polizei ', 'Mo-Do ', 1, 11, 0, 'Eurodance des italienischen Dance-Projects Mo-Do', 1995, 'R-193925-1262119140.jpg'),
(12, 'Suspicious Minds ', 'Elvis Presley ', 1, 14, 0, 'Im Original von Mark James (1968), der lediglich 12 Platten davon verkaufte', 1969, 'R-5243431-1388570549-1457.jpg'),
(14, 'Mrs. Robinson', 'Simon & Garfunkel ', 1, 15, 0, 'Veröffentlichung:
1967 im Film die Reifeprüfung
1968 als Single', 1968, 'R-1695140-1589733272-2457.jpg'),
(15, 'Shout ', 'Tears For Fears ', 1, 21, 0, '15 Coverversionen von TfF selbst', 1985, 'R-148862-1165181725.jpg'),
(16, 'Thank You ', 'Dido ', 1, 18, 0, 'Dido nach Faithless Solo,
2000 durch `Stan` von Eminem erfolgreicher als zuvor
Dido ist die Gründerin Karthagos', 1999, 'R-654897-1462033082-6624.jpg'),
(17, 'Paranoid ', 'Black Sabbath ', 1, 19, 0, 'Die Begründer des Heavy Metal,
Paranoid ist ihre Debutsingle ', 1970, 'R-10509769-1518886177-5588.jpg'),
(18, 'I`m a Believer', 'The Monkees ', 1, 20, 0, 'Erfolgreichste Single, geschrieben von Neil Diamond
Bekanntestes Cover: Neil Diamond 1967', 1967, 'R-1181460-1449650967-3295.jpg'),
(19, 'You Give Love A Bad Name ', 'Bon Jovi ', 1, 17, 0, 'Platz 1 USA
Österreich Platz 25
in Deutschland nie in den Charts', 1994, 'R-1052784-1248623822.jpg'),
(20, 'Flat Beat ', 'Mr. Oizo ', 1, 22, 0, 'Mr. Oizo ist Quentin Dupieux (Regisseur)
Europaweit in den Top Ten
', 1999, 'R-11699-1167567049.jpg'),
(21, 'Eifel - Radio Edit ', 'Brings ', 1, 23, 0, '', 2007, 'R-11873040-1714982974-4591.jpg'),
(22, 'Don`t Stop Believin` ', 'Journey ', 1, 13, 0, '', 1981, 'R-419741-1454675353-7372.jpg'),
(23, 'Son Of A Preacher Man ', 'Dusty Springfield ', 1, 24, 0, '', 1969, 'R-556921-1273994950.jpg'),
(24, 'König von Deutschland ', 'Rio Reiser ', 1, 16, 0, '', 1986, 'R-1010856-1539874254-7239.jpg'),
(25, 'Invisible Touch', 'Genesis ', 1, 25, 0, '', 1986, 'R-512282-1275630548.jpg'),
(26, 'Friday I`m In Love ', 'The Cure ', 2, 1, 0, '', 1992, ''),
(27, 'Fast Car ', 'Tracy Chapman ', 2, 2, 0, '', 1988, ''),
(28, '7 Seconds', 'Youssou N`Dour, Neneh Cherry ', 2, 3, 0, '', 1994, ''),
(29, 'Hedonism (Just Because You Feel Good) ', 'Skunk Anansie ', 2, 4, 0, '', 1996, ''),
(30, 'It`s My Life', 'Talk Talk ', 2, 5, 0, '', 1984, ''),
(31, 'Bette Davis Eyes ', 'Kim Carnes ', 2, 6, 0, '', 1981, ''),
(32, 'Because the Night ', 'Patti Smith ', 2, 7, 0, '', 1978, ''),
(33, 'Time After Time ', 'Cyndi Lauper ', 2, 8, 0, '', 1983, ''),
(34, 'Luka ', 'Suzanne Vega ', 2, 9, 0, '', 1987, ''),
(35, 'Let`s Dance', 'David Bowie ', 2, 10, 0, '', 1983, ''),
(36, 'Song 2', 'Blur ', 2, 11, 0, '', 1997, ''),
(37, 'Thunderstruck ', 'AC/DC ', 2, 12, 0, '', 1990, ''),
(38, 'Nessaja ', 'Peter Maffay, Tabaluga ', 2, 13, 0, '', 1983, ''),
(39, 'To Be With You', 'Mr. Big ', 2, 14, 0, '', 1991, ''),
(40, 'Breakfast At Tiffany`s ', 'Deep Blue Something ', 2, 15, 0, '', 1995, ''),
(41, 'Wellenreiter ', 'BAP ', 2, 16, 0, '', 1982, ''),
(42, 'I`ve Been Thinking About You ', 'Londonbeat ', 2, 17, 0, '', 1995, ''),
(43, 'Don`t Look Back In Anger', 'Oasis ', 2, 18, 0, '', 1995, ''),
(44, 'Miami ', 'Will Smith ', 2, 19, 0, '', 1997, ''),
(45, 'Vienna ', 'Ultravox ', 2, 20, 0, '', 1980, ''),
(46, 'Love Shine a Light ', 'Katrina And The Waves ', 2, 21, 0, '', 1997, ''),
(47, 'Albany - German Version ', 'Roger Whittaker ', 2, 22, 0, '', 1981, ''),
(48, 'Hard to Say I`m Sorry ', 'Chicago ', 2, 23, 0, '', 1982, ''),
(49, 'Talkin` Bout a Revolution ', 'Tracy Chapman ', 2, 24, 0, '', 1988, ''),
(50, 'Whatever You Want ', 'Status Quo ', 2, 25, 0, '', 1979, ''),
(51, 'Give A Little Bit ', 'Supertramp ', 3, 1, 0, 'Das ist 
Ein 

Text', 1977, ''),
(52, 'Drive', 'The Cars ', 3, 2, 0, '', 1984, ''),
(53, 'My Sweet Lord', 'George Harrison ', 3, 3, 0, '', 1970, ''),
(54, 'Wild World ', 'Yusuf / Cat Stevens ', 3, 4, 0, '', 1970, ''),
(55, 'How Bizarre ', 'OMC ', 3, 5, 0, '', 1996, ''),
(56, 'It Must Have Been Love', 'Roxette ', 3, 6, 0, '', 1990, ''),
(57, 'The Boxer ', 'Simon & Garfunkel ', 3, 7, 0, '', 1970, ''),
(58, 'Californication ', 'Red Hot Chili Peppers ', 3, 8, 0, '', 1999, ''),
(59, 'Drink doch eine met ', 'Bläck Fööss ', 3, 9, 0, '', 1990, ''),
(60, 'Message In A Bottle ', 'The Police ', 3, 10, 0, '', 1979, ''),
(61, 'Basket Case ', 'Green Day ', 3, 11, 0, '', 1994, ''),
(62, 'A Whiter Shade of Pale', 'Procul Harum ', 3, 12, 0, '', 1985, ''),
(63, 'You Can`t Always Get What You Want ', 'The Rolling Stones ', 3, 13, 0, '', 1969, ''),
(64, 'Komet ', 'Udo Lindenberg, Apache 207 ', 3, 14, 0, '', 2023, ''),
(65, 'Wir sagen danke schön', 'Die Flippers ', 3, 15, 0, '', 2022, ''),
(66, 'Cold as Ice ', 'Foreigner ', 3, 16, 0, '', 1977, ''),
(67, 'Hells Bells ', 'AC/DC ', 3, 17, 0, '', 1980, ''),
(68, 'Celebration ', 'Fun Factory ', 3, 18, 0, '', 2016, ''),
(69, ' Another Brick In The Wall, Pt. 2', 'Pink Floyd ', 3, 19, 0, '', 1979, ''),
(70, 'Horny', 'Mousse T., Hot `N` Juicy ', 3, 20, 0, '', 2019, ''),
(71, 'A Horse with No Name ', 'America, George Martin ', 3, 21, 0, '', 1972, ''),
(72, 'Tell Me When ', 'The Human League ', 3, 22, 0, '', 1995, ''),
(73, 'True', 'Spandau Ballet ', 3, 23, 0, '', 1983, ''),
(74, 'Walking in Memphis ', 'Marc Cohn ', 3, 24, 0, '', 1991, ''),
(75, 'One ', 'U2 ', 3, 25, 0, '', 1991, ''),
(76, 'Mmm Mmm Mmm Mmm ', 'Crash Test Dummies ', 4, 1, 0, '', 1993, ''),
(77, 'The Logical Song', 'Supertramp ', 4, 2, 0, '', 1979, ''),
(78, 'Every Breath You Take ', 'The Police ', 4, 3, 0, '', 1983, ''),
(79, 'Do Wah Diddy Diddy', 'Manfred Mann ', 4, 4, 0, '', 1963, ''),
(80, 'San Francisco (Be Sure to Wear Some Flowers In Your Hair) ', 'Scott McKenzie ', 4, 5, 0, '', 1967, ''),
(81, 'Cats In The Cradle ', 'Ugly Kid Joe ', 4, 6, 0, '', 1992, ''),
(82, 'Mambo No. 5 (a Little Bit of...) ', 'Lou Bega ', 4, 7, 0, '', 1999, ''),
(83, 'I Don`t Like Mondays ', 'The Boomtown Rats ', 4, 8, 0, '', 1979, ''),
(84, 'Old Pop in an Oak ', 'Rednex ', 4, 9, 0, '', 1994, ''),
(85, 'Lück wie ich un du ', 'Bläck Fööss ', 4, 10, 0, '', 1988, ''),
(86, 'Lullaby ', 'The Cure ', 4, 11, 0, '', 1989, ''),
(87, 'Start Me Up', 'The Rolling Stones ', 4, 12, 0, '', 1981, ''),
(88, 'Friesenjung ', 'Ski Aggu, Joost, Otto Waalkes ', 4, 13, 0, '', 2023, ''),
(89, 'All Right Now ', 'Free ', 4, 14, 0, '', 1970, ''),
(90, 'Hotel California', 'Eagles ', 4, 15, 0, '', 1976, ''),
(91, 'All The Small Things ', 'blink-182 ', 4, 16, 0, '', 1999, ''),
(92, 'Go Your Own Way', 'Fleetwood Mac ', 4, 17, 0, '', 1977, ''),
(93, 'Amoi seg` ma uns wieder', 'Andreas Gabalier ', 4, 18, 0, '', 2014, ''),
(94, ' Take Me Home, Country Roads', 'John Denver ', 4, 19, 0, '', 1973, ''),
(95, 'Heroes', 'David Bowie ', 4, 20, 0, '', 1977, ''),
(96, 'Our House ', 'Madness ', 4, 21, 0, '', 1982, ''),
(97, 'The Safety Dance ', 'Men Without Hats ', 4, 22, 0, '', 1982, ''),
(98, 'Karma Chameleon', 'Culture Club ', 4, 23, 0, '', 1983, ''),
(99, 'I Walk The Line', 'Johnny Cash', 4, 24, 0, '', 1958, ''),
(100, 'She Drives Me Crazy ', 'Fine Young Cannibals ', 4, 25, 0, '', 1988, ''),
(101, 'Hungry like the Wolf', 'Duran Duran', 5, 1, 0, '', 1982, 'standard.jpg'),
(102, 'Infinity', 'Guru Josh', 5, 2, 0, '', 1990, 'standard.jpg'),
(103, 'Let The Beat Control Your Body', '2 Unlimited', 5, 3, 0, 'Kommentar', 1993, 'standard.jpg'),
(105, 'Just Can´t Get Enough', 'Depeche Mode', 1, 1, 0, 'Kommentar', 1981, 'standard.jpg'),
(106, 'Two Princes', 'Spin Doctors', 1, 12, 0, 'Kommentar', 1991, 'standard.jpg'),
(110, 'All Night Long', 'Lionel Richie', 5, 4, 0, 'Kommentar', 1983, 'standard.jpg');

