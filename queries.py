import sqlite3

# Mit der Datenbank verbinden oder sie erstellen, falls sie nicht existiert
connection = sqlite3.connect("CustomerSales.db")

# Einen Cursor erstellen
cursor = connection.cursor()

# Eine Abfrage ausführen
verkauf_kunde_produkt_region = (
    "SELECT verkauf.*, kunde.*, produkt.*, region.* "
    "FROM verkaufsregion "
    "JOIN verkauf ON verkaufsregion.verkaufsID = verkauf.verkaufsID "
    "JOIN kunde ON verkaufsregion.kundenID = kunde.kundenID "
    "JOIN produkt ON verkaufsregion.produktID = produkt.produktID "
    "JOIN region ON verkaufsregion.regionID = region.regionID;"
)
cursor.execute(verkauf_kunde_produkt_region)

# Daten aus der ausgeführten Abfrage abrufen
ergebnisse = cursor.fetchall()

# Die Ergebnisse anzeigen
for zeile in ergebnisse:
    print(zeile)

# Den Cursor und die Verbindung schließen
cursor.close()
connection.close()