# "r" - Lesen - Standardwert. Öffnet eine Datei zum Lesen, Fehler, wenn die Datei nicht existiert
# "a" - Append - Öffnet eine Datei zum Anhängen, erstellt die Datei, wenn sie nicht vorhanden ist
# "w" - Write - Öffnet eine Datei zum Schreiben, erstellt die Datei, wenn sie nicht vorhanden ist
# "x" - Create - Erzeugt die angegebene Datei, gibt einen Fehler zurück, wenn die Datei existiert

# Kann Optional angefügt werden
# "t" - Text - Standardwert. Text-Modus

# "b" - Binary - Binary mode (z. B. Bilder)

file = open("text.txt", "r")
print(file.read(3))
print(file.readline())
file.close()

f = open("text.txt", "a")
f.write("\nJetzt steht hier mehr drin!")
f.close()

f = open("text.txt", "w")
f.write("Ich habe alles überschrieben!")
f.close()