ingreso_mensual = 120000
gasto_mensual = 8000
# if anidados y elif
if ingreso_mensual > 10000:
    print ("Estas bien economicamente en cualquier parte del mundo")
    if ingreso_mensual - gasto_mensual < 0:
        print ("Estas en deficit")
    elif ingreso_mensual - gasto_mensual >3000:
        print ("Bien pa estas bien")
    else:
        print("Ey man estas gastando una banda, hay que ver si te alcanza")
elif ingreso_mensual > 1000:
    print ("Estas bien economicamente en latinoamerica")
elif ingreso_mensual > 500:
    print ("Estas bien economicamente en argentina")
elif ingreso_mensual > 200:
    print ("Estas bien economicamente en venezuela")
else:
    print ("sos pobre")
