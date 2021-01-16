# ----función que dice el tipo de dato que hay guardado en una variable y su valor-----#

dato = 24
dato2 = "string"
dato3 = 32.5
dato4 = True
dato5 = False

def tipoDatoVAr(dat):
    res = ""
    if type(dat) == int:
        dat1 = str(dat)
        res = "el dato ingresado: <" + dat1 + "> es  de tipo entero (int)"
    elif type(dat) == str:
        dat1 = str(dat)
        res = "el dato ingresado: <" + dat1 + "> es de tipo string (str)"
    elif type(dat) == float:
        dat1 = str(dat)
        res = "el dato ingresado: <" + dat1 + "> es decimal o de punto flotante (float)"
    else:
        if dat == True:
            dat1 = "True"
        else:
            dat1 = "False"
        res = "el dato ingresado: <" + dat1 + "> es boolean "
    return res

print(tipoDatoVAr(dato))
