# Login incorreto: se o usuário não for admin

admin = input('Você é admin? (sim/não): ')
admin_verificado = admin.lower()

if not admin == 'sim':
    print('Login incorreto')
else:
    print('Login correto')