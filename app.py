tdi = input("seu tipo de imovel é comercial, casa ou apartamento?  ")
if tdi != "comercial" and tdi != "casa" and tdi != "apartamento":
    print("Tipo de imóvel inválido. Por favor, insira 'comercial', 'casa' ou 'apartamento'.")   

cons = float(input("Qual o consumo de agua do imóvel em m³?  "))
if tdi == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif tdi == "apartamento" and cons < 10:
     print("Consumo econômico – excelente controle de água!")
      
elif tdi == "apartamento"  and cons >= 10 and cons <=25 or tdi == "casa" and cons >= 10 and cons <=25:
    print("Consumo moderado – dentro do padrão residencial.")
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")