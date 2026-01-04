# Uebungsblatt-Overfitting-MLP-Dhanuka

# 1.MLP Entwickeln.

Die Datei PercepImpl.py

# 2.Vorwärtslauf im MLP

**2.1 Gegeben sei ein MLP mit 25 Zellen in der Eingangsschicht, 64 Zellen in der ersten versteckten Schicht, 32 Zellen in der zweiten versteckten Schicht und 4 Zellen in der Ausgabe Schicht (die Bias-Zellen nicht mitgezählt). In allen Zellen wird die ReLU Aktivierungsfunktion verwendet.**

Die Gewichte und Bias angeben:

w1:( 25 x 3 ) und b1:( 25 x 1)
w2:( 64 x 25 ) und b2:( 64 x 1)
w3:( 32 x 64 ) und b3:( 32 x 1 )

**2.2 Wie wird die Ausgabe berechnet? Schreiben Sie den Vorwärtslauf in Matrix-Notation auf. Wie könnte man die Ausgabe deuten; welches Problem könnte durch dieses Netzwerk möglicherweise gelöst werden?**

X : Datensatz

A1: w1 * X + b1
A2: w2 * A1 + b2
A3: w3 * A2 + b3

Z1,Z2,Z3: Relu Funktion

X -> w1 * X + b1 -> Z1 -> A1 -> w2 * A1 + b2 -> Z2 -> A2 -> w3 * A2 + b3 -> Z3 -> A3

Da wir in der Ausgabe Schicht 4 Zellen haben, vermute ich, dass man mit diesem MLP die Klassifikationsprobleme lösen kann.

# 3. Tensor Flow Playground Aufgabe

**Wie verhält sich die Entscheidungsgrenze?**

**Kreisförmig:**

Mit 2 Neuronen sieht man, dass es keine richtige Entscheidungsgrenze gibt, die die Daten richtig klassifiziert. Auch wenn man da die Aktivierungsfunktionen anwendet, bekommt man für jede Akt.-Funktion eine andere Entscheidungsgrenze. Meistens war es eine Parable oder eine Box.

Ab 3 Neuronen, hat man gesehen, dass die Entscheidungsgrenze Kreisförmig wird und alle Punkte richtig klassifiziert werden. Hier sieht man auch deutlich, dass die Aktivierungsfunktion einen Einfluss auf die Form der Entscheidungsgrenze hat. Wenn man das MLP mit Relu trainiert, hat die Entscheidungsgrenze eine boxartige Form, aber wenn man denselben MLP mit Tanh oder Sigmoid trainiert, bekommt man eine Kreisförmige Grenze.

**Spiral Datensatz:**

Bei dem Spiral Datensatz war die Entscheidungsgrenze immer linear, außer wenn man mehrere Neuronen und Schichten hat. Als die Anzahl der Neuronen und die Schichten größer geworden ist, ist die Entscheidungsgrenze langsamer Spiralförmig geworden. Aber er hat meistens nicht geschafft, alle Punkte richtig zu klassifizieren, manchmal hat er 90% der Punkte richtig klassifiziert, ansonsten meist falsch.

Was können Sie über Training und Test-Kosten sagen? Entsteht eine Überanpassung?

Anhand die beiden Trainings- und Test-Werten, könnte man direkt feststellen, wie gut das MLP die Punkte richtig klassifiziert hat. Als die beiden Werte niedrig waren, könnte man davon ausgehen, dass die 95% aller Punkte richtig klassifiziert waren. Bei manchen MLP gab es auch Überanpassung, das könnte man auch anhand die Entscheidungsgrenze erkennen, weil es manchmal ein Zig-Zag Muster gab.

**Wie schnell wird die Entscheidungsgrenze berechnet?**

**Kreisförmig:**

Beim kreisförmigen Datensatz wurde die Berechnung schneller, als die Anzahl der Neuronen und Schichten größer wurde. Auch die Wahl der Aktivierungsfunktion war wichtig. Ich habe eine MLP mit drei Schichten und sieben Neuronen trainiert. Mit der ReLU-Aktivierungsfunktion bekam ich den Wert 000,061. Mit der  Tanh-Aktivierungsfunktion war der Wert kleiner und lag bei 000,032.

**Spiralförmig:**

Ähnlich wie beim Kreisförmig, aber es gab Unterschiede.

**Können alle Datenpunkte jedes mal korrekt klassifiziert werden?Warum?**

**Kreisförmig:**

Mit 2 Neuronen würden die Datenpunkte völlig falsch klassifiziert, aber als die Anzahl der Neuronen und Schichten größer geworden ist, würden die Datenpunkte richtig klassifiziert. Etwas genauer zu sein, ab 3 Neuronen, würden die Datenpunkte richtig klassifiziert.

**Spiralförmig:**

Ähnlich wie beim Kreisförmig, aber erst ab 3 Schichten mit 7 Neuronen, können die MLP die Punkte richtig klassifizieren.Aber, es würden nicht alle Punkte richtig klassifiziert, sondern ca. 80%-90% alle Punkte wurden richtig klassifiziert.

**Unterschiede zwischen den Ausgaben Schicht der Ersten Schicht und letzte Schicht?**

**Ausgabe Schicht der ersten Schicht:** Einfach, roh Merkmale.

**Letzte Schicht:** komplexe, zusammengesetzte Merkmale.

Wenn man das Noise-Level auf 15 erhöht, sieht man den Verlauf der Entscheidungsgraph Zig-Zag förmig aus. Es ist noch schwer geworden, manche MLPs zu trainieren. 
