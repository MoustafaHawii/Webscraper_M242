# Webscraper (M242)

**digitec.py**

Es wird Preis und Zeit wie geplant rausgesucht und ausgegeben. (digitec.py)

**mobileZone.py**

Es wird Preis und Zeit wie geplant rausgesucht und ausgegeben. (mobileZone.py)

**apple.py**

Apple hat einen Schutz, welcher schwierig zu umgehen ist. Lösungsansatz mit "ajax-url". (file nicht mehr vorhanden)

**microspot.py**

Microspot hat einen Schutz, welcher schwierig zu umgehen ist. Lösungsansatz mit "ajay-url". (file nicht mehr vorhanden)

**mediamarkt.py**

Es wird Preis und Zeit wie geplant rausgesucht und ausgegeben. (mediamarkt.py)

**dqSolution.py**

Es wird Preis und Zeit wie geplant rausgesucht und ausgegeben. (dqSolution.py)

**melectro.py**

Gibt den falschen Code aus, da der benötigte Preis und der erhaltene Wert unter der gleichen "class/id" gespeichert sind. (melectro.py)

**computerli.py**

Es wird Preis und Zeit wie geplant rausgesucht und ausgegeben. (computerli.py)

**main.py**

In "main.py" werden von allen shops die Preise und Zeit geholt, durch diese Strucktur ist der Code übersichtilicher.

**execute.py**

In "execute.py" läuft ein Script welches alle 24h "main.py" ausführt. Ursprünglich wollte ich das Script auf meinem Raspberry Pi, mit Hilfe von Cron Job ausführen, da mein Raspberry Pi aber aus unerklärlichen Gründen kein Betriebssystem einlesen kann, muss ich auf dieses Pythonscript greifen. https://pypi.org/project/schedule/

**database.py**

Erstellt eine SQLite Datenbank mit Python. Zuerst wird die Funktion "create_connection()" erstellt, diese verbindet sich mit der SQLite Datenbank

Zunächst definieren wir eine Funktion namens create_connection(), die eine Verbindung zu einer SQLite-Datenbank herstellt, die durch die Datenbankdatei db_file angegeben wird. Innerhalb der Funktion rufen wir die Funktion connect() des Moduls sqlite3 auf.

Die connect() Funktion öffnet eine Verbindung zu einer SQLite-Datenbank. Sie gibt ein Connection-Objekt zurück, das die Datenbank repräsentiert. Mithilfe des Connection-Objekts können Sie verschiedene Datenbankoperationen durchführen.

Falls ein Fehler auftritt, fangen wir ihn innerhalb des try except Blocks ab und zeigen die Fehlermeldung an. Wenn alles in Ordnung ist, zeigen wir die Version der SQLite-Datenbank an.

Zweitens übergeben wir den Pfad der Datenbankdatei an die Funktion create_connection(), um die Datenbank zu erstellen. Beachten Sie, dass das Präfix r in r "C:\sqlite\db\pythonsqlite.db" Python anweist, dass wir eine rohe Zeichenkette übergeben.

**insertSQlite.py**

Ich dachte ich könnte über diese Klasse die Werte aus dem Scraper in die Datenbank speichern, jedoch habe ich in folgenden Tutorial "https://www.youtube.com/watch?v=xBbK2kvHXwE" herausgefunden, dass ich das in den entsprechenden Scraper machen kann.
