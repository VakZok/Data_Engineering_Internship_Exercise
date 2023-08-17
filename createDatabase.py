import sqlite3

# Mit Datenbank verbinden (oder eine erstellen, falls noch keine existiert)
conn = sqlite3.connect('CustomerSales.db')

# Cursor-Objekt erstellen -> ermöglicht die Interaktion mit der DB über SQL
cursor = conn.cursor()


### Relevant, falls DB neu aufgesetzt werden soll
# Alle Tabellen-Namen aus der Datenbank abrufen
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Bereits vorhandene Tabellen löschen -> DB frisch aufsetzten
for table in tables:
    table_name = table[0]
    drop_table_sql = f"DROP TABLE IF EXISTS {table_name};"
    cursor.execute(drop_table_sql)


# Erstellung der Tabellen
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

# Änderungen bestätigen und Verbindung schließen
conn.commit()
conn.close()

print("Database setup successfully.")