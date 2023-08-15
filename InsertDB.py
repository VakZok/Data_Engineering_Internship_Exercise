import sqlite3
import os
import sys


#Verbindung zur DB
connection = sqlite3.connect("CustomerSales.db")

#Datensatz-Cursor erzeugen
cursor = connection.cursor()

# Datenbanktabellen
insertquery = [
    """INSERT INTO kunde(kundenID, vorname, nachname, geburtstag, familienstand, geschlecht, 
        jahreseinkommen, bildungsstand, beruf, hausbesitzer, anzahl_autos, adresse)
        VALUES
        (11000,	'Jon', 'Yang',      '1966-04-08', 'V', 'M', 90000, 'Bachelor', 'Fachmann', 1, 0, '3761 N. 14th St.'),
        (11001,	'Eugene', 'Huang',  '1964-05-14', 'L',	'M', 60000, 'Bachelor', 'Profi', 0, 1, '2243 W St.'),	
        (11002,	'Ruben', 'Torres',  '1965-08-12', 'V',	'M', 60000, 'unvollstaendiger Abschluss', 'Fachmann', 1, 1,
         '5844 Linden Land'),	
        (11003,	'Christy', 'Zhu',   '1968-02-15', 'L', 'W', 70000, 'Bachelor', 'Profi', 0, 1, '1825 Village Pl.'),	
        (11004, 'Elizabeth', 'Johnson', '1968-08-08', 'L', 'W', 80000, 'Bachelor', 'Profi', 1, 4, '7553 Harness'), 
        (11005,	'Julio', 'Ruiz',    '1965-08-05', 'L', 'M', 70000, 'Bachelor', 'Profi', 1, 1, '7305 Humphrey Drive'),	
        (11006,	'Janet', 'Alvarez', '1965-12-06', 'L', 'W', 70000, 'Oberschule', 'Profi', 1, 1, '2612 Berry Dr'),	
        (11007, 'Marco', 'Mehta',   '1964-05-09', 'V', 'M', 60000, 'Bachelor', 'Profi', 1, 2, '942 Brook Street'),	
        (11008, 'Rob', 'Verhoff',   '1964-07-07', 'L', 'W', 60000, 'Bachelor', 'Profi', 1, 3, '624 Peabody Road'),	
        (11009, 'Shannon', 'Carlson', '1964-04-01', 'L', 'M', 70000, 'Oberschule', 'Profi', 0, 1,
         '3839 Northgate Road'),	
        (11010,	'Jacquelyn', 'Suarez', '1964-02-06', 'L', 'W', 70000, 'unvollstaendige Oberschule', 'Sachbearbeiter',
         0, 1, '7800 Corrinne Court'),
        (11011,	'Curtis', 'Lu',     '1963-11-04', 'V', 'M', 60000, 'Oberschule', 'Profi', 1, 4, '1224 Shoenic'),	
        (11012,	'Lauren', 'Walker', '1968-01-18', 'V', 'W', 100000, 'unvollstaendige Oberschule', 'Fachmann', 1, 2,
         '4785 Scott Street'),
        (11013, 'Ian', 'Jenkins', '1968-08-06', 'V', 'M', 100000, 'Bachelor', 'Management', 1, 3, '7902 Hudson Ave.'),	
        (11014, 'Sydney', 'Bennett','1968-05-09', 'L', 'W', 100000, 'Bachelor', 'Management', 0, 3,
         '9011 Tank Drive'),
        (11015, 'Chloe', 'Young', '1979-02-27', 'L', 'W', 30000, 'unvollstaendige Oberschule', 'Fachmann', 0, 1,
         '244 Willow Pass Road');""",

        """
        INSERT INTO produkt(produktID, produktname, farbe, produktbeschreibung, herstellungszeit, listenpreis)
        VALUES
        (2, 'Bearing Ball', 'NA', ' ', 0, NULL),
        (214, 'Sport-100 Helmet, Red', 'Red', 'Universal fit, well-vented, lightweight , snap-on visor.', 0, 
        34.99),
        (217, 'Sport-100 Helmet, Black', 'Black', 'Universal fit, well-vented, lightweight , snap-on visor.', 0, 
        34.99),
        (222, 'Sport-100 Helmet, Blue', 'Blue', 'Universal fit, well-vented, lightweight , snap-on visor.', 0, 
        34.99),
        (225, 'AWC Logo Cap', 'Multi', 'Traditional style with a flip-up brim; one-size fits all.', 0, 
        8.99),
        (394, 'LL Headset', 'NA', 'Threadless headset provides quality at an economical price.', 1, 
        34.20),
        (344, 'Mountain-100 Silver, 38', 'Silver', 'Top-of-the-line competition mountain bike. Performance-enhancing 
        options include the innovative HL Frame, super-smooth front suspension, and traction for all terrain.', 4, 
        3399.99),
        (345, 'Mountain-100 Silver, 42', 'Silver', 'Top-of-the-line competition mountain bike. Performance-enhancing 
        options include the innovative HL Frame, super-smooth front suspension, and traction for all terrain.', 4, 
        3399.99),
        (346, 'Mountain-100 Silver, 44', 'Silver', 'Top-of-the-line competition mountain bike. Performance-enhancing 
        options include the innovative HL Frame, super-smooth front suspension, and traction for all terrain.', 4, 
        3399.99),
        (347, 'Mountain-100 Silver, 48', 'Silver', 'Top-of-the-line competition mountain bike. Performance-enhancing 
        options include the innovative HL Frame, super-smooth front suspension, and traction for all terrain.', 4, 
        3399.99),
        (348, 'Mountain-100 Black, 38', 'Black', 'Top-of-the-line competition mountain bike. Performance-enhancing 
        options include the innovative HL Frame, super-smooth front suspension, and traction for all terrain.', 4, 
        3374.99),
        (349, 'Mountain-100 Black, 42', 'Black', 'Top-of-the-line competition mountain bike. Performance-enhancing 
        options include the innovative HL Frame, super-smooth front suspension, and traction for all terrain.', 4, 
        3374.99),
        (350, 'Mountain-100 Black, 44', 'Black', 'Top-of-the-line competition mountain bike. Performance-enhancing 
        options include the innovative HL Frame, super-smooth front suspension, and traction for all terrain.', 4, 
        3374.99),
        (351, 'Mountain-100 Black, 48', 'Black', 'Top-of-the-line competition mountain bike. Performance-enhancing 
        options include the innovative HL Frame, super-smooth front suspension, and traction for all terrain.', 4, 
        3374.99),
        (5, 'Blade', 'NA', ' ', 1, 14.99),
        (353, 'Mountain-200 Silver, 38', 'Silver', 'Serious back-country riding. Perfect for all levels of 
        competition. Uses the same HL Frame as the Mountain-100.', 4, 2319.99),
        (355, 'Mountain-200 Silver, 42', 'Silver', 'Serious back-country riding. Perfect for all levels of 
        competition. Uses the same HL Frame as the Mountain-100.', 4, 2319.99),
        (357, 'Mountain-200 Silver, 46', 'Silver', 'Serious back-country riding. Perfect for all levels of 
        competition. Uses the same HL Frame as the Mountain-100.', 4, 2319.99),
        (359, 'Mountain-200 Black, 38', 'Black', 'Serious back-country riding. Perfect for all levels of 
        competition. Uses the same HL Frame as the Mountain-100.', 4, 2294.99),
        (361, 'Mountain-200 Black, 32', 'Black', 'Serious back-country riding. Perfect for all levels of 
        competition. Uses the same HL Frame as the Mountain-100.', 4, 2294.99),
        (465, 'Half-Finger Gloves, M', 'Black', 'Full padding, improved finger flex, durable palm, 
        adjustable closure..', 0, 24.49),
        (477, 'Water Bottle - 30 oz.', 'NA', 'AWC logo water bottle - holds 30 oz; leak-proof.', 0, 4.99),
        (478, 'Mountain Bottle Cage', 'NA', 'Tough aluminum cage holds bottle securly on tough terrain.', 0, 9.99),
        (479, 'Road Bottle Cage', 'NA', 'Aluminum cage is lighter than our mountain version; perfect for long 
        distance trips.', 0, 8.99),
        (480, 'Patch Kit/8 Patches', 'NA', 'Includes 8 different size patches, glue and sandpaper.', 0, 2.29),
        (485, 'Fender Set - Mountain', 'NA', 'Clip-on fenders fit most mountain bikes.', 0, 21.98),
        (13, 'Chain Stays', 'NA', ' ', 1, NULL),
        (488, 'Short-Sleeve Classic Jersey, S', 'Yellow', 'Short sleeve classic breathable jersey with superior 
        moisture control, front zipper, and 3 back pockets.', 0, 53.99),  
        (489, 'Short-Sleeve Classic Jersey, M', 'Yellow', 'Short sleeve classic breathable jersey with superior 
        moisture control, front zipper, and 3 back pockets.', 0, 53.99),  
        (491, 'Short-Sleeve Classic Jersey, XL', 'Yellow', 'Short sleeve classic breathable jersey with superior 
        moisture control, front zipper, and 3 back pockets.', 0, 53.99),  
        (528, 'Mountain Tire Tube', 'NA', 'Self-sealing tube.', 0, 4.99),          
        (529, 'Road Tire Tube', 'NA', 'Conventional all-purpose tube.', 0, 3.99), 
        (530, 'Touring Tire Tube', 'NA', 'General purpose tube.', 0, 4.99), 
        (17, 'Mountain End Cap', 'NA', ' ', 1, 12.49),
        (537, 'HL Mountain Tire', 'NA', 'Incredible traction, lightweight carbon reinforced.', 0, 35.00),
        (541, 'Touring Tire', 'NA', 'High-density rubber.', 0, 28.99),
        (561, 'Touring-1000 Yellow, 46', 'Yellow', 'Travel in style and comfort. Designed for maximum comfort and 
        safety. Wide gear range takes on all hills. High-tech aluminum alloy construction provides durability 
        without added weight.', 4, 2384.07),
        (562, 'Touring-1000 Yellow, 50', 'Yellow', 'Travel in style and comfort. Designed for maximum comfort and 
        safety. Wide gear range takes on all hills. High-tech aluminum alloy construction provides durability 
        without added weight.', 4, 2384.07),
        (564, 'Touring-1000 Yellow, 60', 'Yellow', 'Travel in style and comfort. Designed for maximum comfort and 
        safety. Wide gear range takes on all hills. High-tech aluminum alloy construction provides durability 
        without added weight.', 4, 2384.07),
        (573, 'Touring-1000 Blue, 46', 'Blue', 'Travel in style and comfort. Designed for maximum comfort and 
        safety. Wide gear range takes on all hills. High-tech aluminum alloy construction provides durability 
        without added weight.', 4, 2384.07),
        (574, 'Touring-1000 Blue, 50', 'Blue', 'Travel in style and comfort. Designed for maximum comfort and 
        safety. Wide gear range takes on all hills. High-tech aluminum alloy construction provides durability 
        without added weight.', 4, 2384.07),
        (575, 'Touring-1000 Blue, 54', 'Blue', 'Travel in style and comfort. Designed for maximum comfort and 
        safety. Wide gear range takes on all hills. High-tech aluminum alloy construction provides durability 
        without added weight.', 4, 2384.07),
        (604, 'Road-750 Black, 44', 'Black', 'Entry level adult bike; offers a comfortable ride cross-country or 
        down the block. Quick-release hubs and rims.', 4, 539.99);""",

              

        """
        INSERT INTO region(regionID, region, land, gruppe, preisaufschlag)
        VALUES
        (1, 'Nordwesten', 'USA', 'Nordamerika', 0),
        (2, 'Nordosten', 'USA', 'Nordamerika', 0),
        (3, 'Zentral', 'USA', 'Nordamerika', 0),
        (4, 'Südwesten', 'USA', 'Nordamerika', 0),
        (5, 'Südosten', 'USA', 'Nordamerika', 0),
        (6, 'Kanada', 'Kanada', 'Nordamerika', 10),
        (7, 'Frankreich', 'Frankreich', 'Europa', 50),
        (8, 'Deutschland', 'Deutschland', 'Europa', 50),
        (9, 'Australien', 'Australien', 'Pazifik', 200),
        (10, 'Vereinigtes_Königreich', 'Vereinigtes Königreich', 'Europa', 120);""",

        """
        INSERT INTO modell(modellID, modellname)
        VALUES
        (1, 'Cycling Cap'),
        (2, 'Fender Set - Moountain'),
        (3, 'Half-Finger Gloves'),
        (4, 'HL Mountain Tire'),
        (5, 'Mountain Bottle Cage'),
        (6, 'Mountain Tire Tube'),
        (7, 'Mountain-100'),
        (8, 'Mountain-200'),
        (9, 'Patch kit'),
        (10, 'Road Bottle Cage'),
        (11, 'Road Tire Tube'),
        (12, 'Road-750'),
        (13, 'Short-Sleeve Classic Jersey'),
        (14, 'Sport-100'),
        (15, 'Touring Tire'),
        (16, 'Touring Tire Tube'),
        (17, 'Touring-1000'),
        (18, 'Water Bottle'),
        (19, 'Taillight'),
        (20, 'LL Headset');""",

        """
        INSERT INTO linie(linienID, linienbezeichnung)
        VALUES
        (1, ''),
        (2, 'Sport'),
        (3, 'Mountain'),
        (4, 'Road'),
        (5, 'Touring');""",


        """
        INSERT INTO kategorie(kategorieID, bezeichnung)
        VALUES
        (1,''),
        (2,'Clothing'),
        (3, 'Bikes'),
        (4, 'Accessories'),
        (5, 'Components');""",

        """
        INSERT INTO produktkategorie(produktID, kategorieID)
        VALUES
        (485, 4),
        (537, 4),
        (478, 4),
        (528, 4),
        (480, 4),
        (479, 4),
        (529, 4),
        (214, 4),
        (217, 4),
        (222, 4),
        (541, 4),
        (530, 4),
        (477, 4),
        (344, 3),
        (345, 3),
        (346, 3),
        (347, 3),
        (348, 3),
        (349, 3),
        (350, 3),
        (351, 3),
        (353, 3),
        (355, 3),
        (357, 3),
        (359, 3),
        (361, 3),
        (394, 5),
        (604, 3),
        (561, 3),
        (562, 3),
        (564, 3),
        (573, 3),
        (574, 3),
        (575, 3),
        (225, 2),
        (465, 2),
        (488, 2),
        (489, 2),
        (491, 2);""",

        """
        INSERT INTO produktmodell(produktID, modellID)
        VALUES
        (225, 1),
        (485, 2),
        (465, 3),
        (537, 4),
        (478, 5),
        (528, 6),
        (344, 7),
        (345, 7),
        (346, 7),
        (347, 7),
        (348, 7),
        (349, 7),
        (350, 7),
        (351, 7),
        (353, 8),
        (355, 8),
        (357, 8),
        (359, 8),
        (361, 8),
        (480, 9),
        (479, 10),
        (529, 11),
        (604, 12),
        (488, 13),
        (489, 13),
        (491, 13),
        (214, 14),
        (217, 14),
        (222, 14),
        (541, 15),
        (530, 16),
        (561, 17),
        (562, 17),
        (564, 17),
        (573, 17),
        (574, 17),
        (575, 17),
        (477, 18),
        (394, 20);""",




        """
        INSERT INTO linienmodell(modellID, linienID)
        VALUES
        (1, 2),
        (2, 3),
        (3, 2),
        (4, 3),
        (5, 3),
        (6, 3),
        (7, 3),
        (8, 3),
        (9, 2),
        (10, 4),
        (11, 4),
        (12, 4),
        (13, 2),
        (14, 2),
        (15, 5),
        (16, 5),
        (17, 5),
        (18, 2);""",

        """
        INSERT INTO verkauf(verkaufsID, datum, anzahl, kundenID, produktID)
        VALUES
        ('SO43701', '2014-01-01', 2,    11003,  346),
        ('SO43704', '2014-01-02', 4,    11005,  351),
        ('SO43705', '2014-01-02', 4,    11011,  344),
        ('SO43736', '2014-01-10', 1,    11002,  346),
        ('SO43743', '2014-01-12', 1,    11007,  347),
        ('SO43765', '2014-01-17', 1,    11010,  346),
        ('SO43767', '2014-01-18', 1,    11001,  350),
        ('SO43793', '2014-01-22', 2,    11000,  344),
        ('SO43810', '2014-01-26', 1,    11004,  345),
        ('SO43819', '2014-01-27', 1,    11006,  346),
        ('SO43826', '2014-01-28', 1,    11008,  348),
        ('SO43837', '2014-01-30', 4,    11009,  350),
        ('SO51198', '2016-01-02', 1,    11006,  357),
        ('SO51198', '2016-01-02', 1,    11006,  478),
        ('SO51198', '2016-01-02', 1,    11006,  477),
        ('SO51238', '2016-01-04', 1,    11002,  359),
        ('SO51282', '2016-01-07', 4,    11008,  361),
        ('SO51282', '2016-01-07', 4,    11008,  477),
        ('SO51282', '2016-01-07', 4,    11008,  478),
        ('SO51282', '2016-01-07', 4,    11008,  480),            
        ('SO51315',	'2016-01-09', 1,	11003,	361),
        ('SO51315',	'2016-01-09', 1,	11003,	478),
        ('SO51315',	'2016-01-09', 1,	11003,	477),
        ('SO51315',	'2016-01-09', 1,	11003,	225),
        ('SO51421',	'2016-01-15', 1,	11010,	361),
        ('SO51493',	'2016-01-20', 2,	11001,	353),
        ('SO51493',	'2016-01-20', 2,	11001,	485),
        ('SO51493',	'2016-01-20', 2,	11001,	477),
        ('SO51493',	'2016-01-20', 2,	11001,	478),
        ('SO51493',	'2016-01-20', 2,	11001,	491),
        ('SO51493',	'2016-01-20', 2,	11001,	225),
        ('SO51522',	'2016-01-22', 1,	11000,	353),
        ('SO51522',	'2016-01-22', 1,	11000,	485),
        ('SO51562',	'2016-01-24', 1,	11009,	359),
        ('SO51562',	'2016-01-24', 1,	11009,	480),
        ('SO51581',	'2016-01-25', 1,	11007,	361),
        ('SO51581',	'2016-01-25', 1,	11007,	528),
        ('SO51581',	'2016-01-25', 1,	11007,	537),
        ('SO51581',	'2016-01-25', 1,	11007,	485),
        ('SO51581',	'2016-01-25', 1,	11007,	222),
        ('SO51595',	'2016-01-26', 1,	11004,	355),
        ('SO51595',	'2016-01-26', 1,	11004,	485),
        ('SO51595',	'2016-01-26', 1,	11004,	214),
        ('SO51612',	'2016-01-27', 2,	11005,	355),
        ('SO51612',	'2016-01-27', 2,	11005,	537),
        ('SO51612',	'2016-01-27', 2,	11005,	528),
        ('SO51612',	'2016-01-27', 2,	11005,	480),
        ('SO51650',	'2016-01-29', 1,	11011,	361),
        ('SO53237',	'2016-02-27', 1,	11002,	561),
        ('SO53237',	'2016-02-27', 1,	11002,	222),
        ('SO53765',	'2016-03-03', 1,	11008,	561),
        ('SO53765',	'2016-03-03', 1,	11008,	214),
        ('SO54508',	'2016-03-17', 1,	11012,	537),
        ('SO54508',	'2016-03-17', 1,	11012,	528),
        ('SO54508',	'2016-03-17', 1,	11012,	217),
        ('SO54705',	'2016-03-20', 1,	11007,	564),
        ('SO54705',	'2016-03-20', 1,	11007,	214),
        ('SO54706',	'2016-03-20', 1,	11011,	574),
        ('SO54706',	'2016-03-20', 1,	11011,	489),
        ('SO54898',	'2016-03-24', 1,	11014,	529),
        ('SO54898',	'2016-03-24', 1,	11014,	217),
        ('SO56137',	'2016-04-15', 1,	11013,	529),
        ('SO56137',	'2016-04-15', 1,	11013,	217),
        ('SO57222',	'2016-04-01', 1,	11014,	537),
        ('SO57222',	'2016-05-01', 1,	11014,	528),
        ('SO57222',	'2016-05-01', 1,	11014,	217),
        ('SO57222',	'2016-05-01', 1,	11014,	465),
        ('SO57293',	'2016-05-02', 2,	11004,	562),
        ('SO57293',	'2016-05-02', 2,	11004,	217),
        ('SO57361',	'2016-05-03', 4,	11005,	562),
        ('SO57418',	'2016-05-04', 1,	11000,	573),
        ('SO57418',	'2016-05-04', 1,	11000,	541),
        ('SO57418',	'2016-05-04', 1,	11000,	530),
        ('SO57418',	'2016-05-04', 1,	11000,	214),
        ('SO57418',	'2016-05-04', 1,	11000,	488),
        ('SO57736',	'2016-05-10', 4,	11009,	575),
        ('SO57736',	'2016-05-10', 4,	11009,	217),
        ('SO57783',	'2016-05-11', 1,	11003,	564),
        ('SO57783',	'2016-05-11', 1,	11003,	541),
        ('SO57783',	'2016-05-11', 1,	11003,	530),
        ('SO57783',	'2016-05-11', 1,	11003,	480),
        ('SO58007',	'2016-05-15', 1,	11006,	562),
        ('SO58533',	'2016-05-24', 4,	11010,	575),
        ('SO58533',	'2016-05-24', 4,	11010,	225),
        ('SO68413',	'2016-10-17', 1,	11012,	529),
        ('SO68413',	'2016-10-17', 1,	11012,	480),
        ('SO72773',	'2016-12-12', 1,	11001,	604),
        ('SO72773',	'2016-12-12', 1,	11001,	477),
        ('SO72773',	'2016-12-12', 1,	11001,	479),
        ('SO72773',	'2016-12-12', 1,	11001,	217),
        ('SO72774', '2016-12-14', 3,    11011,  480);""",


        """
        INSERT INTO verkaufsregion(verkaufsID, kundenID, produktID, regionID)
        VALUES
        ('SO43701', 11003,  346, 9),
        ('SO43704', 11005,  351, 9),
        ('SO43705', 11011,  344, 9),
        ('SO43736', 11002,  346, 9),
        ('SO43743', 11007,  347, 9),
        ('SO43765', 11010,  346, 9),
        ('SO43767', 11001,  350, 9),
        ('SO43793', 11000,  344, 9),
        ('SO43810', 11004,  345, 9),
        ('SO43819', 11006,  346, 9),
        ('SO43826', 11008,  348, 9),
        ('SO43837', 11009,  350, 9),
        ('SO51198', 11006,  357, 9),
        ('SO51198', 11006,  478, 9),
        ('SO51198', 11006,  477, 9),
        ('SO51238', 11002,  359, 9),
        ('SO51282', 11008,  361, 9),
        ('SO51282', 11008,  477, 9),
        ('SO51282', 11008,  478, 9),
        ('SO51282', 11008,  480, 9),            
        ('SO51315',	11003,	361, 9),
        ('SO51315',	11003,	478, 9),
        ('SO51315',	11003,	477, 9),
        ('SO51315',	11003,	225, 9),
        ('SO51421',	11010,	361, 9),
        ('SO51493',	11001,	353, 9),
        ('SO51493',	11001,	485, 9),
        ('SO51493',	11001,	477, 9),
        ('SO51493',	11001,	478, 9),
        ('SO51493',	11001,	491, 9),
        ('SO51493',	11001,	225, 9),
        ('SO51522',	11000,	353, 9),
        ('SO51522',	11000,	485, 9),
        ('SO51562',	11009,	359, 9),
        ('SO51562',	11009,	480, 9),
        ('SO51581',	11007,	361, 9),
        ('SO51581', 11007,	528, 9),
        ('SO51581',	11007,	537, 9),
        ('SO51581',	11007,	485, 9),
        ('SO51581',	11007,	222, 9),
        ('SO51595',	11004,	355, 9),
        ('SO51595',	11004,	485, 9),
        ('SO51595',	11004,	214, 9),
        ('SO51612',	11005,	355, 9),
        ('SO51612',	11005,	537, 9),
        ('SO51612',	11005,	528, 9),
        ('SO51612',	11005,	480, 9),
        ('SO51650',	11011,	361, 9),
        ('SO53237',	11002,	561, 9),
        ('SO53237',	11002,	222, 9),
        ('SO53765',	11008,	561, 9),
        ('SO53765',	11008,	214, 9),
        ('SO54508',	11012,	537, 1),
        ('SO54508',	11012,	528, 1),
        ('SO54508',	11012,	217, 1),
        ('SO54705',	11007,	564, 9),
        ('SO54705',	11007,	214, 9),
        ('SO54706',	11011,	574, 9),
        ('SO54706',	11011,	489, 9),
        ('SO54898',	11014,	529, 1),
        ('SO54898',	11014,	217, 1),
        ('SO56137',	11013,	529, 1),
        ('SO56137',	11013,	217, 1),
        ('SO57222',	11014,	537, 1),
        ('SO57222',	11014,	528, 1),
        ('SO57222',	11014,	217, 1),
        ('SO57222',	11014,	465, 1),
        ('SO57293',	11004,	562, 9),
        ('SO57293',	11004,	217, 9),
        ('SO57361',	11005,	562, 1),
        ('SO57418',	11000,	573, 9),
        ('SO57418',	11000,	541, 9),
        ('SO57418',	11000,	530, 9),
        ('SO57418',	11000,	214, 9),
        ('SO57418',	11000,	488, 9),
        ('SO57736',	11009,	575, 9),
        ('SO57736',	11009,	217, 9),
        ('SO57783',	11003,	564, 9),
        ('SO57783',	11003,	541, 9),
        ('SO57783',	11003,	530, 9),
        ('SO57783',	11003,	480, 9),
        ('SO58007',	11006,	562, 9),
        ('SO58533',	11010,	575, 9),
        ('SO58533',	11010,	225, 9),
        ('SO68413',	11012,	529, 1),
        ('SO68413',	11012,	480, 1),
        ('SO72773',	11001,	604, 9),
        ('SO72773',	11001,	477, 9),
        ('SO72773',	11001,	479, 9),
        ('SO72773',	11001,	217, 9),
        ('SO72774', 11011,  480, 9);"""
]

for statement in insertquery:
    result = cursor.execute(statement)
connection.commit()
connection.close()
print('Inserts done.')


