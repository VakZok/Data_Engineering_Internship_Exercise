import sqlite3

# connect to database (or create one, if there is non yet)
conn = sqlite3.connect('CustomerSales.db')

# create cursor object -> allows interaction with DB using sql
cursor = conn.cursor()

# CREATE OR REPLACE TABLE-Anweisungen mit Checks für TEXT-Datentyp
cursor.execute('''
    CREATE TABLE OR REPLACE Kunden (
        KundenID INTEGER PRIMARY KEY,
        Geburtstag DATE NOT NULL,
        Vorname TEXT NOT NULL,
        Nachname TEXT NOT NULL,
        Adresse TEXT NOT NULL,
        Geschlecht TEXT NOT NULL CHECK(Geschlecht IN ('M', 'W', 'D')),
        Familienstand TEXT NOT NULL CHECK(Familienstand IN ('L', 'V')),
        Bildungsstand TEXT NOT NULL CHECK(Bildungsstand IN ('Bachelor', 'Schulabschluss', 'Oberschule', 'unvollständiger Abschluss', 'unvollständige Oberschule')),
        Beruf TEXT NOT NULL CHECK(Beruf IN ('Sachbearbeiter', 'Profi', 'Fachmann', 'Management', 'Handwerker')),
        Jahreseinkommen INTEGER NOT NULL,
        Hausbesitzer BOOLEAN NOT NULL,
        Anzahl_Autos INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE OR REPLACE Produkte (
        ProduktID INTEGER PRIMARY KEY,
        Produktname TEXT NOT NULL,
        Farbe TEXT NOT NULL CHECK(Farbe IN ('schwarz', 'weiss', 'grün', 'blau', 'rot', 'gelb', 'orange', 'violett', 'pink', 'braun', 'grau')),
        Produktbeschreibung TEXT NOT NULL,
        Herstellungszeit DATETIME NOT NULL,
        Listenpreis NUMERIC NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE OR REPLACE Regionen (
        RegionID INTEGER PRIMARY KEY,
        Region TEXT NOT NULL CHECK(Region IN ('Baden-Württemberg', 'Hessen', 'Bayern', 'Nordrhein-Westfalen', 'Sachsen', 'Niedersachsen', 'Rheinland-Pfalz')),
        Land TEXT NOT NULL CHECK(Land IN ('Deutschland', 'Frankreich', 'Schweiz', 'Österreich', 'Italien', 'Spanien', 'Niederlande')),
        Gruppe TEXT NOT NULL CHECK(Gruppe IN ('Gruppe A', 'Gruppe B', 'Gruppe C', 'Gruppe D', 'Gruppe E', 'Gruppe F', 'Gruppe G')),
        Preisaufschlag NUMERIC NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE OR REPLACE Linien (
        LinienID INTEGER PRIMARY KEY,
        LinienmodellID INTEGER,
        Linienbezeichnung TEXT NOT NULL,
        FOREIGN KEY (LinienmodellID) REFERENCES Linienmodelle(LinienmodellID)
    )
''')

cursor.execute('''
    CREATE TABLE OR REPLACE Modelle (
        ModellID INTEGER PRIMARY KEY,
        Modellname TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE OR REPLACE Kategorien (
        KategorieID INTEGER PRIMARY KEY,
        Bezeichnung TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE OR REPLACE Verkauf (
        VerkaufsID INTEGER PRIMARY KEY,
        KundenID INTEGER NOT NULL,
        ProduktID INTEGER NOT NULL,
        RegionID INTEGER NOT NULL,
        Datum DATE NOT NULL,
        Anzahl INTEGER NOT NULL,
        FOREIGN KEY (KundenID) REFERENCES Kunden(KundenID),
        FOREIGN KEY (ProduktID) REFERENCES Produkte(ProduktID),
        FOREIGN KEY (RegionID) REFERENCES Regionen(RegionID)
    )
''')

cursor.execute('''
    CREATE TABLE OR REPLACE Produktmodell (
        ProduktID INTEGER NOT NULL,
        ModellID INTEGER NOT NULL,
        PRIMARY KEY (ProduktID, ModellID),
        FOREIGN KEY (ProduktID) REFERENCES Produkte(ProduktID),
        FOREIGN KEY (ModellID) REFERENCES Modelle(ModellID)
    )
''')

cursor.execute('''
    CREATE TABLE OR REPLACE Produktkategorie (
        ProduktID INTEGER NOT NULL,
        KategorieID INTEGER NOT NULL,
        PRIMARY KEY (ProduktID, KategorieID),
        FOREIGN KEY (ProduktID) REFERENCES Produkte(ProduktID),
        FOREIGN KEY (KategorieID) REFERENCES Kategorien(KategorieID)
    )
''')

cursor.execute('''
    CREATE TABLE OR REPLACE Linienmodell (
        LinienmodellID INTEGER PRIMARY KEY,
        ModellID INTEGER NOT NULL
    )
''')

# Änderungen bestätigen und Verbindung schließen
conn.commit()
conn.close()