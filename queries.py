import sqlite3
import pandas as pd

# Mit der Datenbank verbinden
connection = sqlite3.connect("CustomerSales.db")

# Cursor erstellen
cursor = connection.cursor()

# Erste Abfrage ausführen
verkauf_kunde_produkt_region = (
    "SELECT verkauf.*, kunde.*, produkt.*, region.* "
    "FROM verkaufsregion "
    "JOIN verkauf ON verkaufsregion.verkaufsID = verkauf.verkaufsID "
    "JOIN kunde ON verkaufsregion.kundenID = kunde.kundenID "
    "JOIN produkt ON verkaufsregion.produktID = produkt.produktID "
    "JOIN region ON verkaufsregion.regionID = region.regionID;"
)

result = pd.read_sql_query(verkauf_kunde_produkt_region, connection)

# Die Ergebnisse anzeigen
print(result)

# Den Cursor und die Verbindung schließen
cursor.close()
connection.close()