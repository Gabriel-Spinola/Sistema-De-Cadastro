# Sistema De Cadastro

## Como rodar o programa
 É necessario que você tenha o pyhon 3.9 pra cima e pip instalados
 
 1. Você tem que baixar e roda um virtualenv
``` 
pip install virtualenv

virtualenv mypython

mypython\Scripts\activate
```

2. Instalar o [Django](https://www.djangoproject.com) dentro do virtualenv
```
cd mypython

pip install django
```

3. E por fim rodar o servidor
```
cd ../
cd login

python manage.py runserver
```

 ## Como entrar como administrador:
 Após instalar a aplicação, vá até o endereço http://127.0.0.1:8000/admin/:
 
 
   username: username <br>
   email: email@adress.com <br>
   password: password <br>
