import sqlite3

# Mit Datenbank verbinden (oder eine erstellen, falls noch keine existiert)
conn = sqlite3.connect('CustomerSales.db')

# Cursor-Objekt erstellen -> ermöglicht die Interaktion mit der DB über SQL
cursor = conn.cursor()

# Tabellen löschen (falls sie bereits existieren)
cursor.execute('DROP TABLE IF EXISTS kunde')
cursor.execute('DROP TABLE IF EXISTS produkt')
cursor.execute('DROP TABLE IF EXISTS region')
cursor.execute('DROP TABLE IF EXISTS linie')
cursor.execute('DROP TABLE IF EXISTS modell')
cursor.execute('DROP TABLE IF EXISTS kategorie')
cursor.execute('DROP TABLE IF EXISTS verkauf')
cursor.execute('DROP TABLE IF EXISTS produktmodell')
cursor.execute('DROP TABLE IF EXISTS produktkategorie')
cursor.execute('DROP TABLE IF EXISTS linienmodell')

# CREATE TABLE-Anweisungen mit Checks für TEXT-Datentyp
cursor.execute('''
    CREATE TABLE kunde (
        kundenID INTEGER PRIMARY KEY,
        vorname TEXT NOT NULL,
        nachname TEXT NOT NULL,
        geburtstag DATE NOT NULL,
        familienstand TEXT NOT NULL CHECK(familienstand IN ('L', 'V')),
        geschlecht TEXT NOT NULL CHECK(geschlecht IN ('M', 'W', 'D')),
        jahreseinkommen INTEGER NOT NULL,
        bildungsstand TEXT NOT NULL CHECK(bildungsstand IN ('Bachelor', 'Schulabschluss', 'Oberschule', 'unvollstaendiger Abschluss', 'unvollstaendige Oberschule')),
        beruf TEXT NOT NULL CHECK(beruf IN ('Sachbearbeiter', 'Profi', 'Fachmann', 'Management', 'Handwerker')),
        hausbesitzer BOOLEAN NOT NULL,
        anzahl_autos INTEGER NOT NULL,
        adresse TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE produkt (
        produktID INTEGER PRIMARY KEY,
        produktname TEXT NOT NULL,
        farbe TEXT NOT NULL,
        produktbeschreibung TEXT NOT NULL,
        herstellungszeit INTEGER NOT NULL,
        listenpreis NUMERIC(6,2)
    )
''')

cursor.execute('''
    CREATE TABLE region (
        regionID INTEGER PRIMARY KEY,
        region TEXT NOT NULL,
        land TEXT NOT NULL,
        gruppe TEXT NOT NULL,
        preisaufschlag INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE linie (
        linienID INTEGER PRIMARY KEY,
        linienbezeichnung TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE modell (
        modellID INTEGER PRIMARY KEY,
        modellname TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE kategorie (
        kategorieID INTEGER PRIMARY KEY,
        bezeichnung TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE verkauf (
        verkaufsID TEXT NOT NULL,
        datum DATE NOT NULL,
        anzahl INTEGER NOT NULL,
        kundenID INTEGER NOT NULL,
        produktID INTEGER NOT NULL,
        PRIMARY KEY (verkaufsID, kundenID, produktID),
        FOREIGN KEY (kundenID) REFERENCES kunde(kundenID),
        FOREIGN KEY (produktID) REFERENCES produkt(produktID)
    )
''')

cursor.execute('''
    CREATE TABLE verkaufsregion (
        verkaufsID TEXT NOT NULL,
        kundenID INTEGER NOT NULL,
        produktID INTEGER NOT NULL,
        regionID INTEGER NOT NULL,
        PRIMARY KEY (verkaufsID, kundenID, produktID, regionID),
        FOREIGN KEY (verkaufsID) REFERENCES verkauf(verkaufsID),
        FOREIGN KEY (kundenID) REFERENCES kunde(kundenID),
        FOREIGN KEY (produktID) REFERENCES produkt(produktID),
        FOREIGN KEY (regionID) REFERENCES region(regionID)
    )
''')

cursor.execute('''
    CREATE TABLE produktmodell (
        produktID INTEGER NOT NULL,
        modellID INTEGER NOT NULL,
        PRIMARY KEY (produktID, modellID),
        FOREIGN KEY (produktID) REFERENCES produkt(produktID),
        FOREIGN KEY (modellID) REFERENCES modell(modellID)
    )
''')

cursor.execute('''
    CREATE TABLE produktkategorie (
        produktID INTEGER NOT NULL,
        kategorieID INTEGER NOT NULL,
        PRIMARY KEY (produktID, kategorieID),
        FOREIGN KEY (produktID) REFERENCES produkt(produktID),
        FOREIGN KEY (kategorieID) REFERENCES kategorie(kategorieID)
    )
''')

cursor.execute('''
    CREATE TABLE linienmodell (
        modellID INTEGER NOT NULL,
        linienID INTEGER NOT NULL,
        PRIMARY KEY (modellID, linienID),
        FOREIGN KEY (modellID) REFERENCES modell(modellID),
        FOREIGN KEY (linienID) REFERENCES linie(linienID)
    )
''')

# aenderungen bestaetigen und Verbindung schließen
conn.commit()
conn.close()