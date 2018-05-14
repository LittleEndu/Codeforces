# Overkill...

a,b,c=[input() for i in "___"]
print(max([eval(i.format(a,b,c)) for i in ["{}+{}+{}","{}*{}*{}","{}+{}*{}","{}*{}+{}","({}+{})*{}","{}*({}+{})"]]))
