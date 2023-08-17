import sqlite3
import pandas as pd

# Mit der Datenbank verbinden
connection = sqlite3.connect("CustomerSales.db")

# Cursor erstellen
cursor = connection.cursor()

# Query 1: Übersicht aller Verkäufe + Kunden-, Produkt-, und Regionsinformationen
verkauf_kunde_produkt_region = (
    "SELECT verkauf.*, kunde.*, produkt.*, region.* "
    "FROM verkaufsregion "
    "JOIN verkauf ON verkaufsregion.verkaufsID = verkauf.verkaufsID "
    "JOIN kunde ON verkaufsregion.kundenID = kunde.kundenID "
    "JOIN produkt ON verkaufsregion.produktID = produkt.produktID "
    "JOIN region ON verkaufsregion.regionID = region.regionID;"
)

verkauf_kunde_produkt_region_ergebnis = pd.read_sql_query(verkauf_kunde_produkt_region, connection)

# Query 3: Produkte, die ein Modell besitzen, aber keine Produktlinie
produkte_mit_Modell_ohne_Linie = (
    "SELECT DISTINCT produkt.*, produktmodell.modellID, linienmodell.linienID "
    "FROM produktmodell "
    "JOIN produkt ON produktmodell.produktID = produkt.produktID "
    "LEFT JOIN modell ON produktmodell.modellID = modell.modellID "
    "LEFT JOIN linienmodell ON modell.modellID = linienmodell.modellID "
    "WHERE linienmodell.modellID IS NULL; "
)

produkte_mit_Modell_ohne_Linie_ergebnis = pd.read_sql_query(produkte_mit_Modell_ohne_Linie, connection)

# Query 4: Der Kunde / die Kundin, der/die am häufigsten Bestellungen aufgegeben hat
kunde_mit_häufigste_Bestellungen = (
    "SELECT kunde.*, COUNT(verkauf.verkaufsID) AS anzahl_bestellungen "
    "FROM kunde "
    "JOIN verkauf ON kunde.kundenID = verkauf.kundenID "
    "GROUP BY kunde.kundenID "
    "ORDER BY anzahl_bestellungen DESC "
    "LIMIT 1; "
)

kunde_mit_häufigste_Bestellungen_ergebnis = pd.read_sql_query(kunde_mit_häufigste_Bestellungen, connection)

# Die Ergebnisse anzeigen
print("Query 1: Übersicht aller Verkäufe + Kunden-, Produkt-, und Regionsinformationen:")
print(verkauf_kunde_produkt_region_ergebnis)
print("\nQuery 3: Produkte, die ein Modell besitzen, aber keine Produktlinie:")
print(produkte_mit_Modell_ohne_Linie_ergebnis)
print("\nQuery 4: Der Kunde / die Kundin, der/die am häufigsten Bestellungen aufgegeben hat:")
print(kunde_mit_häufigste_Bestellungen_ergebnis)
print("\nQueries done.")

# Den Cursor und die Verbindung schließen
cursor.close()
connection.close()