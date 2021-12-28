from flask import Flask,render_template,request,url_for,redirect,jsonify,session,make_response
from flask import request
import json
import time
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
app = Flask(__name__)
app.secret_key = '@#$$$%$'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login'
mysql = MySQL(app)
agent = ''
@app.route('/')
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user_mast WHERE user_name = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account != None:
            session['username'] = username
        if account:
            session['loggedin'] = True
            session['username'] = username
            session['id'] = account['id']
            session['username'] = account['user_name']
            print('This is the account of username '+account[username])
            msg = 'Logged in successfully !'
            make_response(jsonify(msg),200)
            return render_template('new.html')
        else:
            msg = 'Incorrect username / password !'
    return render_template('index.html', msg = msg)
cust_type = None
cust_price = None
@app.route('/login', methods =['GET', 'POST'])
def customermanagent():
  cursor = mysql.connection.cursor()
  cursor.execute('SELECT cust_name,cust_address,cust_code,cust_type FROM cust_mast')
  customer = cursor.fetchall()
  cursor.execute('SELECT item_name FROM item_mast')
  productname = cursor.fetchall()
  #print(productname)
  productlist = []
  for i in productname:
   for ii in i:
    if ii == "," or "(":
      continue
    else:
        pass
   productlist.append(ii)
  #print(productlist)
  new = list(customer)
  new_wo = []
  cursor.execute("SELECT item_name FROM item_mast")
  prod = cursor.fetchall()
  for i in new:
    new_wo.append(list(i))
  print('This is the product list '+str(productlist))
  print('This the orginal product ' +str(prod))
  return render_template('new.html',new_wo = new_wo,productlist = productlist)
@app.route('/login/select', methods = ['GET', 'POST'])
def priceselector():
        cust_name = []
        cust_type = ''
        customercode = ''
        if request.method == 'POST':
            print('Incomin')
            global code
            req = request.get_json()  # parse as JSON
            customer = req['Customercode']
            for i in customer.split():
                if i.isdigit():
                    customercode = customercode+i
            print(customercode)
            code = customercode
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT cust_type,cust_val FROM cust_mast WHERE cust_code = %s",[customercode])
            cust_type = cursor.fetchall()
            #return 'OK', 200
            for i in cust_type:
                #print(i)
                for ii in i:
                    cust_name.append(ii)
            #cust_price = cust_name[0]
            #res = make_response(jsonify({"Cust_type":cust_type}),200)
            #return jsonify({'CustomerType':"001"})
        return jsonify({'CustomerType':str(cust_type)})
@app.route('/login/product',methods = ['POST', 'GET'])
def pricefetch():
        if request.method == 'POST':
            req = request.get_json()
            product = req['Productname']
            print(type(product))
            print(product)
            customer_type = req['Customertype']
            customer_type = customer_type.lstrip("Avail:")
            print(customer_type)
            customer_type = json.loads(customer_type)
            customer_type = customer_type['CustomerType']
            for i in customer_type:
                if i.isalpha():
                    customer_type = i
            print(customer_type)
            cursor = mysql.connection.cursor()
            if customer_type =='W'or'w':
                cursor.execute("SELECT price_5 FROM item_mast WHERE item_name = %s",[product])
                global price
                price = cursor.fetchone()
            elif cust_price == 'R':
                cursor.execute("SELECT price_1 FROM item_mast")
                price = cursor.fetchone()
            else:
                pass
        print(str(price) +" this is price")
        res = make_response(jsonify({'Price':price}),200)
        return res
@app.route('/login/logout',methods = ['GET', 'POST'])
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))
@app.route('/login/upload',methods = ['POST', 'GET'])
def upload():
 cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
 req = ''
 data = []
 username = ''
 
 if request.method == 'POST':
    req = request.get_json()
    print(str(req),"this is req")
    # for i in req:
    #     if i == "id**Product name**Quantity**Price**":
    #         continue
    #     else:
    #         data.append(i)
 aa = ''
 aaa = []
 cod = []
 
 #req.pop(0)
 if 'username' in session:
              username = session['username']
              print('This is the username '+username)
 else:
     print('Error while saving the session') 

 username = session.get('username')
 print('This is the username '+str(username))
 for i in req:
     print('This is req data '+i)
     if i == 'line,Product name,Quantity,Price,':
         continue
     else:
         data.append(i)
     aa = i
     #aa = aa.replace(',',' ')
     print("aa = "+str(aa))
     print(aa)
     print(type(aa))
 print(aa)
 print('This is the data '+str(data))
 #aaa = aa[3]
#  print(aaa)
#  aaa = aaa.replace(',','')
#  print(aaa)
 print(aa)
 print('this is print '+str(aaa))
 print(type(aa))
 aa = list(aa)
 print(aa)
 for i in aa:
     print(f"the index of {i} = {aa.index(i)}")
     cod.append(i)
 print('cod = '+str(cod))

#  item_name = cod[1]
#  item_qty = cod[2]
#  item_price = cod[3]
#  item_new = ''
#  for i in item_price:
#      if i == ',':
#          continue
#      else:
#          item_new += i
#  newlist = [item_name,item_qty,item_new]
#  print(f"newlist = {newlist}")
#  for i in newlist:
#      print(i)
 newlist = []
 newdata = []
 newlistofdata = []
 newdata = [[i] for i in data]
 print(newdata[-1])
 USER = newdata[-1]
 ag = ''
 for i in USER:
     agent = i
 print('This is the credent '+str(USER))
 print('This is the new data '+str(newdata))
 for i in newdata:
    print("This is newdata "+str(newdata))
    for ii in i:
        newlistofdata.append(ii.split(','))
        #  for ii in i:
        #      newlistofdata = ii.split(',')
        #      print(newlistofdata)
        #      if ii == '':
        #          newlistofdata.remove(i)
        #          newdata.append(newlistofdata)
        #      print("this is newlist of data"+str(newlistofdata))
 
 print('This is the newlistofdata '+str(newlistofdata))
 USER = newlistofdata[-1]
 if 'username' in session:
    username = session['username']
    print('This is the username '+username)
 else:
    print('Error saving username to the session ')
 print(type(newlistofdata))
 newlistofdata = list(newlistofdata)
 newlistofdata.pop()
 for i in newlistofdata:
        print('This is the i '+str(i))
        i.pop()
 print('This is popped newlist ' +str(newlistofdata))
 print('This is the requested data '+str(req))
 cursor.execute('SELECT cust_name FROM cust_mast WHERE cust_code = %s',[code])
 cust_name = cursor.fetchone()
 cust_name = cust_name['cust_name']
 print('This is the cust_name '+cust_name+str(type(cust_name)))
 print('This is the cust name '+cust_name)
 for i in newlistofdata:
             print('This is the i '+str(i))
             item_name = i[1]
             item_qty = i[2]
             item_price = i[3]
             print('This is the customer name '+str(code))
             print('This is the item name '+item_name)
             print('This is the item quantity '+item_qty)
             print('This is the item price '+item_price)
            #  #def func():
             cursor = mysql.connection.cursor()
            #     #"INSERT INTO order_mast ('line','product_name','item_qty','item_price') VALUES(%s,%s,%s,%s)",['',str(item_name),int(item_qty),int(item_price)])
             #cursor.execute("INSERT INTO order_mast ('line','product_name','item_qty','item_price') VALUES(%s,%s,%s,%s)",['',str(item_name),int(item_qty),int(item_price)])
             print('This is the credent' +str(USER))
             cursor.execute("insert into order_mast values(NULL,'%s','%s','%s','%s','%s')"%(str(cust_name),agent,str(item_name),int(item_qty),int(item_price)))
            #     #cursor.execute("insert into order_mast values('Ujala','20','20')")
             mysql.connection.commit()
 #print(item_name)
 #cursor.execute("START TRANSACTION")
                #cursor.execute("DELETE FROM order_mast WHERE product_name = 'Ujala'")`
 #func()
 print('This is newdata '+str(newdata))
 print('This is the newlist of data in the given list '+str(newlistofdata))
 return make_response(jsonify("Up"),200)
@app.route('/login/order' ,methods = ['GET', 'POST'])
def orders():
     orderlist = []
     cursor = mysql.connection.cursor()
     def func():
          global agent
          if request.method == 'POST':
            agent = request.get_json()
            print(agent)
     func()
     print('This is the agent '+agent)
     cursor.execute('SELECT * FROM order_mast WHERE user_name = %s',[agent])
     fetch = cursor.fetchall()
     print(fetch)
     make_response(jsonify(fetch),200)
     return render_template('order.html',orderlist = fetch)
@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)
if __name__ == "__main__":
   app.run(debug=True)