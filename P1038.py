precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}
cod, qtd = map (int, input().split())
total = precos[cod]  * qtd
print("Total: R$ {:.2f}".format(total))