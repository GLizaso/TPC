# github.com/wtpc/HO-python

def multiplo(numero, multiplo):

    restodiv = numero%multiplo

    if restodiv == 0:
        return True

    else:
        return False


multiplosTres = []
multiplosCinco = []


for i in range(1000):
    if multiplo(i,3):
        multiplosTres.append(i)
    if multiplo(i,5):
        multiplosCinco.append(i)


total = multiplosTres + multiplosCinco
sinRepe = []

for x in total:
    if x not in sinRepe:
        sinRepe.append(x)

suma=sum(sinRepe)
print(suma)
