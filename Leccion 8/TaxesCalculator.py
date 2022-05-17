def calcular_total(pago_sin_impuesto, impuesto):
    return impuesto * 0.01 * pago_sin_impuesto + pago_sin_impuesto


valor = float(input("Digite el monto del pago: "))
impuesto =float(input("Digite el monto del impuesto: "))

total = calcular_total(valor, impuesto)

print(f'El valor con el impuesto del {impuesto}% es de {total}')