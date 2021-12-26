#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Food_Ordering_App():
    
    admin={}

    def admin_signup(self,admin_name,password):
        self.admin[admin_name]=password
        return 'Admin signed up'
    
    def admin_login(self,admin_name,password):
        if admin_name in self.admin:
            self.admin[admin_name]==password
            return 'Admin logged in successful'
        else:
            return 'Incorrect password or admin code'
        

class user():
    users={}
    
    def user_registration(self,username,phone_number,email,address,password):
        self.users[username]=password
        self.phone_number=phone_number
        self.email=email
        self.address=address
        return 'User registered successfully'
    
    def user_login(self,username,password):
        if username in self.users:
            self.users[username]==password
            return 'Login successfull'
        else:
            return 'Incorect password OR user'
        
    def food_items(self):
        foods=[{'name':'Tandoori Chicken','price':320,'qut':'4 pieces'},{'name':'Vegan Burger','price':320,'qut':'1 pieces'},
                           {'name':'Truffle Cake','qut':'500gm','price':900}]
        for i in foods:
            print(f"{foods.index(i)+1}. {i['name']} ({i['qut']}) [INR {i['price']}]")
        choices=input('enter the choices(1/2/3):')  
        if choices=='1':
            print('Are you sure to place Tandoori Chicken as your order!!!')
        elif choices=='2':
            print('Are you sure to place Vegan Burger as your order!!!')
        elif choices=='3':
            print('Are you sure to place Truffle Cake as your order!!!')
        select={1:'Yes',2:'No'}
        for value in select:
            print(str(value),select[value])

        confirmation = int(input())
        print('Order Placed!')
        print('Enjoy Eating')

        
loginadmin=Food_Ordering_App()
print(loginadmin.admin_signup(input('enter the admin code:'),input('enter the password:')))
print(loginadmin.admin_login(input('enter the admin code:'),input('enter the password:')))

loginuser=user()
print(loginuser.user_registration(input('enter the username:'),input('enter the phone number:'),
                                  input('enter the email:'),input('enter the address:'),input('enter the password:')))
print(loginuser.user_login(input('enter the login username:'),input('enter the password:')))

food=user()
print(food.food_items())

