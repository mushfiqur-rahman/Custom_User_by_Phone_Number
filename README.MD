## Custom User by Phone Number

## First I created a app accounts

* I override default user model in accounts > model
* I created two form like UserCreate and Change Form
* Create a class in admin.py that inherit of BaseUserAdmin
* Then Register User & Inherited class UserAdmin
* You have to register with BD phone number. If you want to change country then you have to define at settings that changed base.py file. 
____
> Secret key generate command
 
 ```bash script
 $ .\manage.py shell
 ```
 ```bash script
 >>> from django.core.management.utils import get_random_secret_key
 ```
 ```bash script
 >>> print(get_random_secret_key())
 ```
 ```bash script
 >>> exit()
 ```