#Konstruieren Sie ein Netz mit drei Perceptron, welches für zwei Eingaben variablen x1 und x2
# die in der folgenden Abbildung blau-grau dargestellten Bereiche mit +1 klassifiziert. Benutzen Sie die
# sign-Funktion als Aktivierungsfunktion.

# Aus der Abbildung erkennt man, dass man bei den Werten x1 >= 2 und x2 >=3 im blau-grau bereich landet.

# Definiere den Sign(z) Funktion, damit den Wert, der den Bereich definiert ausgibt
def sign(z):
    if z >= 0:
        return 1
    else:
        return -1


class ThreePerceptronNetwork:
    def __init__(self):

        # Perzeptron 1 in der ersten Schicht. Er soll aktiviert werden x2 >= 3 ist.
        self.w1_11 = 0
        self.w1_12 = 1
        self.b1_1  = -3

        # Perzeptron 2 in der ersten Schicjt. Er soll aktiviert werden wenn x1 >= -2 ist
        self.w1_21 = 1
        self.w1_22 = 0
        self.b1_2  = -2

        # Perzeptron 3 in der Ausgabe Schicht. Er nimmt die Ausgaben der ersten beiden Perzeptrons als Eingabe.
        # Damit
        self.w2_1 = 1
        self.w2_2 = 1
        self.b2   = 0


    def forward(self, x):
        x1 = x[0]
        x2 = x[1]

        # Hier wird das erste Perzeptron berechnet und den sign Funktion angewendet
        z1 = self.w1_11 * x1 + self.w1_12 * x2 + self.b1_1
        y1 = sign(z1)

        # Zweiter Perzeptron berechnen und sign funktion anwenden
        z2 = self.w1_21 * x1 + self.w1_22 * x2 + self.b1_2
        y2 = sign(z2)

        # Die Ausgaben der ersten beiden Perzeptrons addieren und sign funktion anwenden. Damit wird dann das Bereich
        # festgestellt.
        z_out = self.w2_1 * y1 + self.w2_2 * y2 + self.b2
        output = sign(z_out)

        return output


if __name__ == "__main__":
    net = ThreePerceptronNetwork()

    # Test daten satz.
    # Die Punkte aus derm Abbildung abgelesen.
    test_points = [
        [0, 0],
        [1, 2],
        [3, 0],
        [0, 4],
        [3, 4]
    ]

    for point in test_points:
        result = net.forward(point)
        print(f"Eingabe {point} : Ausgabe {result}")


