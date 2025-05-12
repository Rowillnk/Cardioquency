# VARIABLES # --------------------
age = int(input("Define tu edad:")) # EDAD

# CONDITIONS # -------------------
fcm = 220 - age                     # FRECUENCIA CARDIACA MÁXIMA
switch = True

# CONTADORES # -------------------
Res = 0
Mod = 0
Max = 0

# REALIZATION # ------------------
print(f"Tu Frecuencia Cardiaca Máxima es {fcm}")
while switch:
    fc = int(input("Indica tu frecuencia cardiaca (-1 para finalizar):"))               # FRECUENCIA CARDIACA
    if fc == -1:                    # SWITCH
        switch = False
    elif fc <= (fcm * 0.55):        # SI ES REPOSO (<= 55% FCM)
        Res += 1
    elif fc >= (fcm * 0.95):        # SI ES MÁXIMA (>= 95% FCM)
        Max += 1
    else:                           # CUALQUIER OTRO VALOR
        Mod += 1
print(f"Reposo: {Res}\nModerada: {Mod}\nMaxima: {Max}")