s = int(input ("Digite a senha:"))
  
cs = int(input ("Confirme a senha:"))
  
while cs == s:
    print("As senhas são correspondentes.")
    break
else:
    print("A senha está incorreta.")
    s = int(input ("Digite a senha:"))
    cs = int(input ("Confirme a senha:"))
