from datetime import datetime
from flask import request, render_template, url_for, redirect, json

''' Import functions'''
from application import app


from application import db

#######################################################
#                 HealthView Routes                   #
#######################################################
'''
@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/yee', methods=['POST', 'GET'])
def hom():

    if request.method == "GET":
        try:
            return render_template('home.html', empty=-1)
        except:
            return "There was an issue loading the page."

    elif request.method == "POST":
        
        data = request.form
        suburb = data.get('suburb')
        suburb_data = Suburb.query.filter_by(name=suburb).first()
        print(suburb_data)
        if suburb_data is None:
            return render_template('home.html', suburb_name=suburb, empty = 0)
        
        # get all data related to given suburb
        all_data = Covid.query.filter_by(suburb_id=suburb_data.id).order_by(Covid.date_created).all()
        # Get most recent data
        recent_data = all_data[:14]
        # calculate sum of recent data
        sum = 0
        dates = []
        data = []
        for i in recent_data:
            string = i.date_created.date().strftime("%d/%m")
            data.append(i.num_cases)
            dates.append(string)
            sum += i.num_cases

        population = {
            'bondi': 15000,
            'maroubra': 31000
        }
        rate = "{0:.4%}".format(sum / population['bondi'])
        return render_template('home.html', sum=sum, suburb_name=suburb.title(), empty=1, labels=dates, data=data, rate=rate)


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == "POST":
        data = request.form
        suburb = data.get('suburb')
        date_str = data.get('date')
        num_cases = data.get('num_cases')
        # find suburb in database and get suburb id
        suburb_data = Suburb.query.filter_by(name=suburb).all()
        if suburb_data is None:
            return "invalid suburb or suburb doesnt exist"
        try:
            suburb_id = suburb_data[0].id
        except IndexError:
            return "invalid suburb or suburb doesnt exist"
        date_created = datetime.strptime(date_str, '%Y-%m-%d').date()
        new_covid = Covid(suburb_id=suburb_id, date_created=date_created, num_cases=num_cases)
        try:
            db.session.add(new_covid)
            db.session.commit()
            return redirect('/admin')
        except:
            print(new_covid.suburb_id, date_created, num_cases)

            return "There was an issue assing your task"
    else:
        covid = Covid.query.filter_by().all()
        suburb = Suburb.query.filter_by().all()
        print(covid)
        return render_template('admin.html', covid=covid, suburb=suburb)

    return render_template('admin.html')

@app.route('/suburb', methods=['POST', 'GET'])
def suburb():
    if request.method == "POST":
        data = request.form
        suburb = data.get('suburb')

        suburb_data = Suburb.query.filter_by(name=suburb).first()
        if suburb_data is not None:
            return "this suburb already exists"
    
        new_suburb = Suburb(name=suburb)
        try:
            db.session.add(new_suburb)
            db.session.commit()
            return redirect('/suburb')
        except:
            return "There was an issue assing your task"
    else:
        suburb = Suburb.query.filter_by().all()
        return render_template('suburb.html', suburb=suburb)


'''
#######
# login page
## pick consumer or business
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
    res = [
        {
            "id": 0,
            "items": ["Samsung 1TB SSD", "USB adapter"],
            "status": 1
        },
        {
            "id": 1,
            "items": ["Logitech Gaming Mouse", "Logitech Mouse Pad", "Computer Case"],
            "status": 0
        },
        {
            "id": 2,
            "items": ["200GB SanDisk MicroSD"],
            "status": 2
        },
        {
            "id": 3,
            "items": ["Mechanical Keyboard", "4K monitor"],
            "status": 0
        },
        {
            "id": 4,
            "items": ["Samsung 1TB SSD", "USB adapter", "1m HDMI Cable"],
            "status": 1
        }
    ]
    return render_template("index.html", orders=res)


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
        "invoice_signature": "Thanks for your business"
    }
    return render_template("profile.html", person=person)

@app.route('/items')
def items():
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
    items = [
        {
            "id": 0,
            "name": "Samsung 1TB SSD",
            "price": "$100",
            "stock": 5,
            "description": "Save all your data externally with this 1TB SSD",
            "size": "small"
        },
        {
            "id": 1,
            "name": "USB adapter",
            "price": "$8",
            "stock": 20,
            "description": "Connect iOS devices to standard USB connections",
            "size": "small"
        },
        {
            "id": 2,
            "name": "Logitech Gaming Mouse",
            "price": "$200",
            "stock": 8,
            "description": "High quality gaming mouse to power up your gaming setup",
            "size": "small"
        },
        {
            "id": 3,
            "name": "Logitech Mouse Pad",
            "price": "$70",
            "stock": 15,
            "description": "High quality gaming mouse pad to power up your gaming setup",
            "size": "small"
        },
        {
            "id": 4,
            "name": "Computer Case",
            "price": "$80",
            "stock": 20,
            "description": "Secure your PC with this computer case",
            "size": "large"
        },
        {
            "id": 5,
            "name": "200GB SanDisk MicroSD",
            "price": "$120",
            "stock": 10,
            "description": "Extra space for whatever you need",
            "size": "small"
        },
        {
            "id": 6,
            "name": "Mechanical Keyboard",
            "price": "$200",
            "stock": 10,
            "description": "Best keyboard for your everyday life",
            "size": "medium"
        },
        {
            "id": 7,
            "name": "4K monitor",
            "price": "$400",
            "stock": 3,
            "description": "High resolution monitor",
            "size": "large"
        },
        {
            "id": 8,
            "name": "1m HDMI Cable",
            "price": "$10",
            "stock": 25,
            "description": "HDMI Cable",
            "size": "medium"
        },
        
    ]
    return render_template("items.html", items=res)

@app.route('/order')
def orders():
    return render_template("order.html")

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







