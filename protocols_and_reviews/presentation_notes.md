#Brainstorming

## Introduction
* Herausarbeiten - des Warums? Und dann das Wie? 
	Warum
    * herausarbeiten, warum es wichtig ist toxische Kommentare zu identifizieren
    * Statistics - New Yorker wendet API an und weist user darauf hin, dass comment toxisch sein könnte - 35% ändern daraufhin ihren Comment ab
    * Newsplattformen müssen Diskussionen abschalten, weil es zu viele toxische comments gibt und Content-Moderatoren nicht hinterher kommen
    * Mit echtem Beispiel unterstreichen
*  wie funktioniert die API
* Zeigen - wie 35% der Leute, die sich umentscheiden, aufgrund von Hinweisen von der Perspective API
* Challenge nur kurz vorstellen 

## Data
    * Idee: Wordcloud als Einsteig in das Thema
        * Ähnlichkeit der Klassen
    * Multi-Label Classification -> Chart Label Counts
        * Unbalanciertheit
    * Chart label count per comment
    * zeigen, was für Daten wir haben - Wordcouds optional

## Herangehensweise
* Schaubild
    * mit neuen Schritten (Augmentation etc.)


## Ergebnisse
* Roberta
    * F1
    * ROC AUC Curve -> ROC AUC Plot für das Gesamtmodell
    * Vergleich zum besten Modell aus der Challenge (TODO: Was für ein Modell haben die verwendet?)

## Fehleranalyse
* wichtigsten Schwachstellen herausarbeiten
* False positive mit Beispiel - Kontextproblematik
* False negatives mit Beispiel
    * "anal butt" comment
* Subjektivität beim labeln - Beispiel
* Out-of-vocabulary words
    * A common problem for the task is the occurrence of words that are not present in the training data. These words include slang or misspellings, but also intentionally obfuscated content.
    * Ungenügend Daten
    * Vortrainierte Modelle wurden auf Wikipedia und Googles bookcorpus trianiert. Deswegen fehlen hier toxische Vokabeln

## Future Work
* Weitere Transformer ausprobieren - XLNet
* mehr Daten nutzen - evtl. auch aus anderen Quellen wie z.B. Twitter
* weiteres Fine-Tuning
* Ensemble-Modelle
