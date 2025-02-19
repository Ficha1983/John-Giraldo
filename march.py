figura = input (" seleccione la figura a calcular, 11 para rombo, 2 para rectangulo, 3para  cuadrado, 4 para trapecio")
pi = 3.1416
var1 = int(input("ingrese valor "))
var2 = int(input("ingrese valor "))
var3 =int (2)

match figura:
    case "1":
        res = ((var1 * var2)/2)
        print(  "el area del rombo es:", res)
    case "2":
        res = (var1 * var2)
        print(  "el area del rectangulo es:", res)
    case "3":
        res = var1 * var2
        print(  "el area del cuadro es:", res)
    case "4":
        res = var1 * var2
        print(  "el area del trapecio es:", res)
