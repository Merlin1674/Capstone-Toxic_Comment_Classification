# Must haves
* Business understanding
* Metrik vorgegeben: ROC für die einzelnen Labels --> Mittelwert daraus
* Analyse von Datei/Daten, auch der "Nice to have"-Daten
* Recherche über Multi-label-modell
* Anfangsrecherche für Multilinguale Modelle

* EDA:
  * was brauchen wir? --Y n-grams, strukturelle Informationen
  * blanciert/nicht balanciert?,
  * Überlagerungen vorhanden?
  * Visualisierung von Worthäufigkeiten (TF-IDFVectorizer)
  * Erste Untersuchung Korrelationen?
* Baselinemodell auswählen

* Preprocessing:
  * Anforderungen an Preprocessing z.B. bzgl. Word2Vec identifizieren.
  * Data cleaning

* Baselinemodell erstellen

* Auswahl der weiteren/verbesserten Modellansätze

* Feature engineering

* Story line?
* Visualisierung der Modelle

* Folien/Vortrag

# Nice to haves
* Multiliguales Modell
  https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification/overview/description
* Russischer Datensatz
  https://www.kaggle.com/blackmoon/russian-language-toxic-comments
  (https://www.kaggle.com/blackmoon/russian-language-toxic-comments)


# Way of working
* Daten alle lokal in "data"-Ordner
* Data in .gitignore aufführen
* Der ursprünglöliche datensatz muss lokal vorhanden sein und darf nicht geändert werden.
* Wenn neu csv-Dateien erstellt werden sollen, soll die in einem eigenen Notebook erstellt werden. --> Absprache mit allen anderen.
* Alle arbeiten in eigenem Branch
* Zusätzlicher Def-Branch, in dem von den privaten Branches gemerged werden darf, wenn die Versionen aufgeräumt und verwendbar (Notebooks müssen dafür fehlerfrei komplett durchlaufen) sind. 
* In den main-Branch wird nur aus dem Def-Branch gemerged.
* Regelmäßig den Def-Branch in den eigenen Branch mergen.
* Notebooks:
  * Jeder hat ein eigenes Notebook
  * Es gibt noch ein Convert-Notebook für die csv-Dateienerstellung.
* Zusätzlicher Ordner für Reviews und Wochenberichte
* MD-File für nützliche Links und Recherche-Quellen
* Planungssachen im Def-Branch!
* Jeden Morgen kurze Besprechung, wo wir stehen und was für diesen und nächsten Tag getan werden muss --> Wer macht was?
*  
