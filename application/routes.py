from datetime import datetime
from flask import request, render_template, url_for, redirect

''' Import functions'''
from application import app


@app.route('/')
def home():
    # radio buttons
    return render_template("login.html")


@app.route('/dashboard')
def dashboard():
    '''
    [
        {
            "id":,
            "items": [string],
            "status": 0|1|2
        }
    ]
    '''
    orders = [
        {
            "id": 0,
            "order": ["Samsung 1TB SSD", "USB adapter"],
            "status": 1
        },
        {
            "id": 1,
            "order": ["Logitech Gaming Mouse", "Logitech Mouse Pad", "Computer Case"],
            "status": 0
        },
        {
            "id": 2,
            "order": ["200GB SanDisk MicroSD"],
            "status": 2
        },
        {
            "id": 3,
            "order": ["Mechanical Keyboard", "4K monitor"],
            "status": 0
        },
        {
            "id": 4,
            "order": ["Samsung 1TB SSD", "USB adapter", "1m HDMI Cable"],
            "status": 1
        }
    ]
    return render_template("index.html", orders=orders)


@app.route('/profile')
def profile():
    person = {
        "username": "adammbq",
        "email": "techfounder101@thebest.com.au",
        "first_name": "DeMar",
        "last_name": " Wang",
        "address": "69, Full Send Ave",
        "city": "Esshay",
        "country": "Australia",
        "invoice_signature": "Thanks for business, please pay asap"
    }
    return render_template("profile.html", person=person)
items = [
        {
            "id": 0,
            "name": "Samsung 1TB SSD",
            "price": "100",
            "stock": 5,
            "description": "Save all your data externally with this 1TB SSD",
            "size": "small"
        },
        {
            "id": 1,
            "name": "USB adapter",
            "price": "8",
            "stock": 20,
            "description": "Connect iOS devices to standard USB connections",
            "size": "small"
        },
        {
            "id": 2,
            "name": "Logitech Gaming Mouse",
            "price": "200",
            "stock": 8,
            "description": "High quality gaming mouse to power up your gaming setup",
            "size": "small"
        },
        {
            "id": 3,
            "name": "Logitech Mouse Pad",
            "price": "70",
            "stock": 15,
            "description": "High quality gaming mouse pad to power up your gaming setup",
            "size": "small"
        },
        {
            "id": 4,
            "name": "Computer Case",
            "price": "80",
            "stock": 20,
            "description": "Secure your PC with this computer case",
            "size": "large"
        },
        {
            "id": 5,
            "name": "200GB SanDisk MicroSD",
            "price": "120",
            "stock": 10,
            "description": "Extra space for whatever you need",
            "size": "small"
        },
        {
            "id": 6,
            "name": "Mechanical Keyboard",
            "price": "200",
            "stock": 10,
            "description": "Best keyboard for your everyday life",
            "size": "medium"
        },
        {
            "id": 7,
            "name": "4K monitor",
            "price": "400",
            "stock": 3,
            "description": "High resolution monitor",
            "size": "large"
        },
        {
            "id": 8,
            "name": "1m HDMI Cable",
            "price": "10",
            "stock": 25,
            "description": "HDMI Cable",
            "size": "medium"
        },
        
    ]
@app.route('/items', methods=["POST","GET"])
def item():
    '''
    [
        {
            "id":,
            "name":,
            "price":,
            "stock":,
            "description":,
            "size":
        }
    ]
    '''

    if request.method == "POST":
        data = request.form
        #print(data.get("name"))
        new_item = {
            "id": len(items),
            "name": data.get("name"),
            "price": data.get('ppr'),
            "stock": data.get('stock'),
            "size": data.get('size'),
            "description" : data.get('description')
        }

        items.append(new_item)
        print(items[-2:])

        return render_template("items.html", items=items)
    else:
        try:
            return render_template('items.html', items=items)
        except:
            return "There was an issue loading the page."

    #return render_template("items.html", items=res)

@app.route('/order')
def orders():
    '''
    [
        {
            "id":,
            "total":,
            "date":,
            "items":[]
        }
    ]
    '''
    orders = [
        {
            "id": 4,
            "status": 1,
            "total": "118",
            "date": "18/06/2020",
            "cart": ["Samsung 1TB SSD", "USB adapter", "1m HDMI Cable"]
        },
        {
            "id": 3,
            "status": 2,
            "total": "600",
            "date": "16/06/2020",
            "cart": ["Mechanical Keyboard", "4K monitor"]
        },
        {
            "id": 2,
            "status": 2,
            "date": "15/06/2020",
            "total": "120",

            "cart": ["200GB SanDisk MicroSD"]
        },
        {
            "id": 1,
            "status": 2,
            "total": "350",
            "date": "14/06/2020",
            "cart": ["Logitech Gaming Mouse", "Logitech Mouse Pad", "Computer Case"]
        },
        {
            "id": 0,
            "status": 2,
            "total": "108",
            "date": "13/06/2020",
            "cart": ["Samsung 1TB SSD", "USB adapter"]
        }
    ]
    return render_template("order.html", orders=orders)


'''
@app.route('/items', methods=["POST","GET"])
def items():
    if request.method == "POST":
        data = request.form
        new_item = {
            "name": data.get("name"),
            "ppr": data.get('ppr'),
            "stock": data.get('stock'),
            "size": data.get('size'),
            description = data.get('description')
        }
        items.append(new_item)
        return render_template("items.html", items=items)
    else:
        try:
            return render_template('items.html', items=items)
        except:
            return "There was an issue loading the page."
'''







