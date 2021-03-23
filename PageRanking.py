#6 Webseiten (Nr.1)
'''
#6 Webseiten
#user auf webseiten
a = 300
b = 300
c = 300
d = 300
e = 300
f = 300

iterationen = int(input("Wie viele durchläufe sollten berechnet werden?\n"))
iterationenStr = str(iterationen)
#for schleife zur berechnung
for i in range(iterationen):
    a_neu = (0.8 * c) / 3 + \
            (0.2 * (a + b + c + d + e + f)) / 6 + \
            (0.8 * f) / 6
    b_neu = (0.8 * a) / 2 + (0.8 * e) + \
            (0.2 * (a + b + c + d + e + f)) / 6 + \
            (0.8 * f) / 6
    c_neu = (0.8 * a) / 2 + (0.8 * b) / 2 + (0.8 * d) + \
            (0.2 * (a + b + c + d + e + f)) / 6 + \
            (0.8 * f) / 6
    d_neu = (0.8 * c) / 3 + (0.8 * b) / 2 + \
            (0.2 * (a + b + c + d + e + f)) / 6 + \
            (0.8 * f) / 6
    e_neu = 0 + \
            (0.2 * (a + b + c + d + e + f)) / 6 + \
            (0.8 * f) / 6
    f_neu = (0.8 * c) / 3 + \
            (0.2 * (a + b + c + d + e + f)) / 6 + \
            (0.8 * f) / 6

    a = a_neu
    b = b_neu
    c = c_neu
    d = d_neu
    e = e_neu
    f = f_neu

aStr = str(a)
bStr = str(b)
cStr = str(c)
dStr = str(d)
eStr = str(e)
fStr = str(f)

print("Es sind " + aStr + ", " + bStr + ", " + cStr + ", " + dStr + ", " + eStr + ", " + fStr + " User auf den Webseiten A bis F, nach " + iterationenStr + " durchläufen.")
'''

#3 Webseiten (Nr.2)
'''
#3 Webseiten
#User auf webseiten
a = 300
b = 300
c = 300

iterationen = int(input("Wie viele durchläufe sollten berechnet werden?\n"))
iterationenStr = str(iterationen)

#for schleife
for i in range(iterationen):
    a_neu = (0.8 * a) / 2 + (0.8 * b) / 2 + (0.8 * c) / 3 + (0.2 * (a + b + c)) / 3
    b_neu = (0.8 * a) / 2 + (0.8 * c) / 3 + (0.2 * (a + b + c)) / 3
    c_neu = (0.8 * b) / 2 + (0.8 * c) / 3 + (0.2 * (a + b +c)) / 3

    a = a_neu
    b = b_neu
    c = c_neu

aStr = str(a)
bStr = str(b)
cStr = str(c)

print("Es sind " + aStr + ", " + bStr + ", " + cStr + " User auf den Webseiten A bis C, nach " + iterationenStr + " durchläufen.")
'''

#6 Webseiten (Nr.3)
'''
a = 300
b = 300
c = 300
d = 300
e = 300
f = 300

iterationen = int(input("Wie viele durchläufe sollten berechnet werden?\n"))
iterationenStr = str(iterationen)

#for schleife
for i in range(iterationen):
    a_neu = (0.8 * c) / 4 + (0.8 * d) / 6 + (0.2 * (a + b + c + d + e + f)) / 6
    b_neu = (0.8 * a) / 2 + (0.8 * c) / 4 + (0.8 * d) / 6 + (0.8 * e) + (0.2 * (a + b + c + d + e + f)) / 6
    c_neu = (0.8 * a) / 2 + (0.8 * b) / 2 + (0.8 * d) / 6 + (0.2 * (a + b + c + d + e + f)) / 6
    d_neu = (0.8 * b) / 2 + (0.8 * c) / 4 + (0.8 * d) / 6 + (0.2 * (a + b + c + d + e + f)) / 6
    e_neu = (0.8 * d) / 6 + (0.8 * f) + (0.2 * (a + b + c + d + e + f)) / 6
    f_neu = (0.8 * c) / 4 + (0.8 * d) / 6 + (0.2 * (a + b + c + d + e + f)) / 6

    a = a_neu
    b = b_neu
    c = c_neu
    d = d_neu
    e = e_neu
    f = f_neu

aStr = str(a)
bStr = str(b)
cStr = str(c)
dStr = str(d)
eStr = str(e)
fStr = str(f)

print("Es sind " + aStr + ", " + bStr + ", " + cStr + ", " + dStr + ", " + eStr + ", " + fStr + " User auf den Webseiten A bis F, nach " + iterationenStr + " durchläufen.")
'''


#6 Webseiten
'''
#user auf webseiten
gesamt = int(input("Wie viele User sind es insgesamt?\n"))
a = gesamt / 6
b = gesamt / 6
c = gesamt / 6
d = gesamt / 6
e = gesamt / 6
f = gesamt / 6

#surf und sprunganteil
surfer = float(input("Wie hoch ist der Surfanteil?(z.B. 0.8, 0.7, 0.6, usw)\n"))
jumper = 1 - surfer

#anzahl der wechsel
iterationen = int(input("Wie viele durchläufe sollten berechnet werden?\n"))
iterationenStr = str(iterationen)

#for schleife zur berechnung
for i in range(iterationen):
    a_neu = (surfer * c) / 3 + \
            (jumper * gesamt) / 6 + \
            (surfer * f) / 6
    b_neu = (surfer * a) / 2 + (surfer * e) + \
            (jumper * gesamt) / 6 + \
            (surfer * f) / 6
    c_neu = (surfer * a) / 2 + (surfer * b) / 2 + (surfer * d) + \
            (jumper * gesamt) / 6 + \
            (surfer * f) / 6
    d_neu = (surfer * c) / 3 + (surfer * b) / 2 + \
            (jumper * gesamt) / 6 + \
            (surfer * f) / 6
    e_neu = 0 + \
            (jumper * gesamt) / 6 + \
            (surfer * f) / 6
    f_neu = (surfer * c) / 3 + \
            (jumper * gesamt) / 6 + \
            (surfer * f) / 6

    a = a_neu
    b = b_neu
    c = c_neu
    d = d_neu
    e = e_neu
    f = f_neu

#ausgabe der user zahlen
gesamt_neu = a+b+c+d+e+f
print(gesamt_neu)
print(a / gesamt_neu)
print(b / gesamt_neu)
print(c / gesamt_neu)
print(d / gesamt_neu)
print(e / gesamt_neu)
print(f / gesamt_neu)


#umwandeln in strings
aStr = str(a)
bStr = str(b)
cStr = str(c)
dStr = str(d)
eStr = str(e)
fStr = str(f)

print("Es sind " + aStr + ", " + bStr + ", " + cStr + ", " + dStr + ", " + eStr + ", " + fStr + " User auf den Webseiten A bis F, nach " + iterationenStr + " durchläufen.")
'''

