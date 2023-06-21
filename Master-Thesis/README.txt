Physik-Masterarbeit
===================

In diesem Ordner befindet sich meine Physik-Masterarbeit, die ich im WS 13/14-SS 2014
geschrieben habe. Die wichtigste Datei in diesem Ordner ist **thesis.tex**, in der
alle Texte stehen. Alle Bilder befinden sich unter *figures*, alle PLots wurden
mit Mathematica 9 erzeugt, die Quelltexte sind lauffähig unter *Mathematica*.
Die Literatur wurde mit Bibtex und dem *Living Reviews in Relativity*-Style (LRR) gemacht.
Sie befindet sich in **literature.bib**.

Zum Kompilieren der Masterarbeit bietet sich das Bash-Script `compile.sh` an. Mit
Aufruf durch `compile.sh release` wird ein komprimiertes PDF (ca 20% Platzbedarf)
generiert und in den *release*-Ordner kopiert. Ansonsten befinden sich alle
Latex-Zwischendateien sowie das generierte PDF im *build*-Ordner.

Die Grafiken in der Masterarbeit stammen von/wurden erzeugt mit:

   * Mathematica 9, Export als PDF.
   * Inkscape (Zeichnungen), mit `overpic` angereichert.
   * Aus anderen Papers, in dem Fall wurde das PDF von ArXiV (Rohdownload)
     beschafft oder ein JPG runtergeladen.

Als Schrift wurde *Linux Libertine* eingesetzt. Der Latex-Dokumenttyp ist *report*,
um Kapitel benutzen zu können. Das sonstige Layout (viel Hyperref) orientiert sich
an LRR und der Master-Calc-Reihe.
