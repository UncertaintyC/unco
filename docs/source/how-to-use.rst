How To Use
==========

This is where you describe how to get set up on a clean install, including the
commands necessary to get the raw data (using the `sync_data_from_s3` command,
for example), and then how to make the cleaned, final data sets.

Eingabe Daten
-------------
Als Eingabe erwartet UnCo eine Tabelle im csv-Format, bei dem die erste Zeile die Namen der Spalten beinhalten und die erste Spalte einen Primärschlüssel in Form einer ID speichert.
Die anderen Spalten müssen einen Namen #name# einer nomisma Klasse haben, sodass auch "http://nomisma.org/ontology#has#name#" einer URI von nomisma entspricht, mit welcher
eine Wertzuweisung dieser Klasse erstellt werden kann.
Die Werte in diesen Spalten sind dabei passende Objekte der Klasse #name#.