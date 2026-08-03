

def numVocales(text):
    a=0
    e=0
    i=0
    o=0
    u=0

    for char in text.lower():
        if char=="a":
            a+=1
        elif char=="e":
            e+=1
        elif char=="i":
            i+=1
        elif char=="o":
            o+=1
        elif char=="u":
            u+=1
    
    return f"El texto tiene {a} a, {e} e, {i} i, {o} o, y {u} u"


print(numVocales("Estamos aprendiendo python"))