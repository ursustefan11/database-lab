from faker import Faker
import multiprocessing
import pyodbc
import random
import pycountry
import datetime
import time

num_inserts_per_core = 500
max_employees = 150

fake = Faker()


def getCurrency(cursor):
    currency = fake.currency()
    count = cursor.execute("SELECT COUNT(*) FROM Financial.Currency").fetchval()
    check = cursor.execute("SELECT currency_id FROM Financial.Currency WHERE currency_code = ?", currency[0]).fetchone()

    if not check:
        c = {
            'currency_code': currency[0],
            'currency_name': currency[1]
        }
        cursor.execute("INSERT INTO Financial.Currency VALUES (?, ?, ?)",
                       c['currency_code'],
                       c['currency_name'],
                       None
                       )
        cursor.commit()
        return count+1
    else:
        return check.currency_id if hasattr(check, 'currency_id') else count


def getStatus(cursor):
    status = ['Pending', 'Paid', 'Failed', 'Refunded', 'Cancelled']
    randVal = random.randint(0, len(status)-1)
    count = cursor.execute("SELECT COUNT(*) FROM Financial.PaymentStatus").fetchval()
    check = cursor.execute("SELECT status_id FROM Financial.PaymentStatus WHERE status_name = ?", status[randVal]).fetchone()

    if not check:
        cursor.execute("INSERT INTO Financial.PaymentStatus VALUES (?)", status[randVal])
        cursor.commit()
        return count+1
    else:
        return check.status_id if hasattr(check, 'status_id') else count


def insertInvoice(cursor, order_id, price, date):
    invoice = {
        'order_id': order_id,
        'invoice_date': date,
        'total_amount': price,
        'currency_id': getCurrency(cursor),
        'status_id': getStatus(cursor)
    }
    cursor.execute("INSERT INTO Financial.Invoices VALUES (?, ?, ?, ?)",
                   invoice['order_id'],
                   invoice['invoice_date'],
                   invoice['total_amount'],
                   invoice['status_id']
                   )
    cursor.commit()


def getAttribute(cursor):
    attr = ['Small', 'Extra-Small', 'Medium', 'Large', 'Extra-Large']
    randomVal = attr[random.randrange(len(attr))]
    count = cursor.execute("SELECT COUNT(*) FROM Inventory.Attributes").fetchval()
    check = cursor.execute("SELECT attribute_id FROM Inventory.Attributes WHERE attribute_name = ?", randomVal).fetchone()
    
    if count < len(attr):
        if not check:
            attribute = {
                'attribute_name': "Size",
                'attribute_value': randomVal
            }
            cursor.execute("INSERT INTO Inventory.Attributes VALUES (?, ?)",
                           attribute['attribute_name'],
                           attribute['attribute_value']
                           )
            cursor.commit()
            return count+1
        else:
            return check.attribute_id if hasattr(check, 'attribute_id') else count
    else:
        return check.attribute_id if hasattr(check, 'attribute_id') else count
    

def getCategory(cursor):
    values = ["Electronics", "Clothing", "Home Decor", "Beauty", "Books", "Sports Equipment", "Toys", "Furniture", "Jewelry", "Automotive", "Health and Fitness", "Pet Supplies", "Food and Beverages", "Tools and Hardware", "Music Instruments"]
    count = cursor.execute("SELECT COUNT(*) FROM Inventory.Categories").fetchval()
    randomVal = values[random.randrange(len(values))]
    check = cursor.execute("SELECT category_id FROM Inventory.Categories WHERE category_name = ?", randomVal).fetchone()

    if count < len(values):
        if not check:
            category = {
                'category_name': randomVal,
                'description': fake.bs()
            }
            cursor.execute("INSERT INTO Inventory.Categories VALUES (?, ?)",
                           category['category_name'],
                           category['description'])
            cursor.commit()
            return count+1
        else:
            return check.category_id if hasattr(check, 'category_id') else count
    else:
        return check.category_id if hasattr(check, 'category_id') else count
    

def getProducts(cursor):
    values = ["Stellar Laptop", "Cosmic Coffee Maker", "Luminary Smartphone", "Infinity Fitness Tracker", "Zenith Headphones", "Radiant Smart TV", "Nova Digital Camera", "Sapphire Bluetooth Speaker", "Whispering Vacuum Cleaner", "Celestial Blender", "Harmony Electric Toothbrush", "Tranquil Microwave Oven", "Eclipse Hair Dryer", "Petal Power Drill", "Serenity Air Purifier", "Vivid Steam Iron", "Silent Robotic Vacuum", "Zephyr Espresso Machine", "Enchanted Massage Chair", "Dreamy Slow Cooker", "Azure Power Bank", "Mystic Electric Kettle", "Lush Air Fryer", "Twilight Gaming Console", "Harmonic Cordless Phone", "Whirlwind Electric Shaver", "Dusk Portable Bluetooth Speaker", "Moonlight Smart Thermostat", "Tranquil Digital Scale", "Radiant Rice Cooker", "Ethereal Food Processor", "Vibrant Curling Iron", "Calm Sewing Machine", "Whispering Blender", "Glistening Portable Fan", "Jade Laptop Stand", "Sparkling Smart Watch", "Dreamy Fitness Bike", "Harmony Hair Straightener", "Celestial Electric Grill", "Rhythmic Handheld Vacuum", "Sapphire Food Steamer", "Zenith Wireless Charger", "Luminous Ironing Board", "Mystical Air Conditioner", "Harmonic Cordless Drill", "Tranquil Coffee Grinder", "Petal Electric Toothbrush", "Serenity Soundbar", "Vivid Robot Vacuum", "Silent Hair Clippers", "Zephyr Clothes Steamer", "Enchanted Bluetooth Headphones", "Dreamy Portable Projector", "Azure Wireless Mouse", "Twilight Air Fryer", "Eclipse Electric Kettle", "Lush Handheld Blender", "Whispering Slow Cooker", "Glistening Gaming Mouse", "Radiant Rice Cooker", "Mystic Espresso Machine", "Calm Cordless Phone", "Whirlwind Portable Bluetooth Speaker", "Jade Food Processor", "Sparkling Electric Shaver", "Harmony Smart TV", "Tranquil Fitness Tracker", "Vivid Hair Dryer", "Sapphire Power Drill", "Zenith Air Purifier", "Luminous Microwave Oven", "Mystical Robotic Vacuum", "Harmonic Massage Chair", "Twilight Digital Camera", "Enchanted Bluetooth Speaker", "Dreamy Electric Toothbrush", "Petal Vacuum Cleaner", "Serenity Blender", "Radiant Portable Fan", "Azure Laptop", "Silent Smart Thermostat", "Zephyr Digital Scale", "Ethereal Steam Iron", "Vibrant Espresso Machine", "Celestial Slow Cooker", "Rhythmic Hair Dryer", "Glistening Power Bank", "Whispering Electric Kettle", "Calm Air Fryer", "Jade Gaming Console", "Sparkling Cordless Phone", "Mystic Electric Shaver", "Lush Portable Bluetooth Speaker", "Zenith Smart Watch", "Harmony Digital Camera", "Tranquil Fitness Bike", "Eclipse Hair Straightener"]
    count = cursor.execute("SELECT COUNT(*) FROM Inventory.Products").fetchval()
    randVal = random.randrange(len(values))
    check = cursor.execute("SELECT product_id FROM Inventory.Products WHERE name = ?", values[randVal]).fetchone()
    
    if count < len(values):
        price = round(random.uniform(0.1, 10), 2)
        if not check:
            products = {
                'name': values[randVal],
                'product_number': fake.pystr_format().upper(),
                'category_id': getCategory(cursor),
                'description': fake.bs(),
                'supplier_price': price,
                'sale_price': price*2.5,
                'attribute_id': getAttribute(cursor),
                'weight_kg': round(random.uniform(0.1, 30), 2)
            }
            cursor.execute("INSERT INTO Inventory.Products VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           products['name'],
                           products['product_number'],
                           products['category_id'],
                           products['description'],
                           products['supplier_price'],
                           products['sale_price'],
                           products['attribute_id'],
                           products['weight_kg']
                           )
            cursor.commit()
            return count+1
        else:
            return check.product_id if hasattr(check, 'product_id') else count
    else:
        return check.product_id if hasattr(check, 'product_id') else count


def insertOrderItems(cursor, order_id, date):

    for _ in range(random.randint(1, 10)):
        product = getProducts(cursor)
        qty = random.randint(1, 10)
        price = 0.0
        orderitem = {
            'order_id': order_id,
            'product_id': product,
            'quantity': qty,
            'price': product*qty
        }
        price += product*qty
        cursor.execute("INSERT INTO Sales.OrderItems VALUES(?, ?, ?, ?)",
                      orderitem['order_id'],
                      orderitem['product_id'],
                      orderitem['quantity'],
                      orderitem['price'])
        cursor.commit()

    insertInvoice(cursor, order_id, price, date)


def getUserSession(cursor):
    user_agent = fake.user_agent()
    check = cursor.execute("SELECT session_id FROM Application.SessionType WHERE user_agent = ?", user_agent).fetchone()
    count = cursor.execute("SELECT COUNT(*) FROM Application.SessionType").fetchval()

    if not check:
        session = {
            'session_key': fake.md5(),
            'user_agent': user_agent
        }
        cursor.execute("INSERT INTO Application.SessionType VALUES(?, ?)",
                    session['session_key'],
                    session['user_agent']
                    )
        cursor.commit()
        val = count+1
        return val
    else:
        return check.session_id if hasattr(check, 'session_id') else count


def getShippingMethod(cursor):
    values = ["Standard Shipping", "Express Shipping", "Next-Day Delivery", "Same-Day Delivery", "Free Shipping", "International Shipping", "Expedited Shipping", "Store Pickup", "Freight Shipping",]
    randVal = random.randrange(len(values))
    count = cursor.execute("SELECT COUNT(*) FROM Sales.ShippingMethods").fetchval()
    check = cursor.execute("SELECT shipping_id FROM Sales.ShippingMethods WHERE shipping_name = ?", values[randVal]).fetchone()

    if count < len(values):
        if not check:
            shipping_methods = {
                'shipping_name': values[randVal],
                'validFrom': fake.date_between(start_date='-2y', end_date='today')
            }
            cursor.execute("INSERT INTO Sales.ShippingMethods VALUES (?, ?)",
                           shipping_methods['shipping_name'],
                           shipping_methods['validFrom'])
            cursor.commit()
            return count+1
        else:
            return check.shipping_id
    else:
        return check.shipping_id
    
    
def getPaymentMethod(cursor):
    values = ['Cash', 'Credit card', 'Debit card', 'Bank transfer', 'PayPal', 'Cryptocurrency']
    randVal = random.randint(0, len(values)-1)
    count = cursor.execute("SELECT COUNT(*) FROM Sales.PaymentMethods").fetchval()
    check = cursor.execute("SELECT payment_method_id FROM Sales.PaymentMethods WHERE payment_name = ?", values[randVal]).fetchone()

    if count < len(values):
        if not check:
            methods = {
                'payment_name': values[randVal],
                'validFrom': fake.date_between(start_date='-2y', end_date='today')
            }
            cursor.execute("INSERT INTO Sales.PaymentMethods VALUES (?, ?)",
                        methods['payment_name'],
                        methods['validFrom']
                        )
            cursor.commit()
            return count+1
        else:
            return check.payment_method_id if hasattr(check, 'payment_method_id') else random.randint(1, count)
    else:
        return check.payment_method_id if hasattr(check, 'payment_method_id') else random.randint(1, count)


def getPaymentStatus(cursor):
    values = ['Pending', 'Paid', 'Cancelled']
    randVal = random.randrange(len(values))
    count = cursor.execute("SELECT COUNT(*) FROM Financial.PaymentStatus").fetchval()
    check = cursor.execute("SELECT payment_method_id FROM Sales.PaymentMethods WHERE payment_name = ?", values[randVal]).fetchone()

    if count < len(values):
        if not check:
            cursor.execute("INSERT INTO Financial.PaymentStatus VALUES (?)", values[randVal])
            cursor.commit()
            return count+1
    else:
        return check.payment_method_id
    

def getOrderStatus(cursor):
    values = ['Pending', 'Processing', 'Shipped', 'Delivered']
    randVal = random.randrange(len(values))
    count = cursor.execute("SELECT COUNT(*) FROM Sales.OrderStatus").fetchval()
    check = cursor.execute("SELECT order_status_id FROM Sales.OrderStatus WHERE order_status = ?", values[randVal]).fetchval()

    if count < len(values):
        if not check:
            cursor.execute("INSERT INTO Sales.OrderStatus VALUES (?)", values[randVal])
            cursor.commit()
            return count+1
        else:
            return check
    else:
        return check
    

def getDiscount(cursor):
    percentage = [10, 20, 30, 40, 50, 60, 70]
    randVal = random.randrange(len(percentage))
    count = cursor.execute("SELECT count(*) FROM Sales.Discounts").fetchval()
    check = cursor.execute("SELECT discount_id FROM Sales.Discounts WHERE discount_percentage = ?", percentage[randVal]).fetchone()
    
    if count < len(percentage):
        if not check:
            discount = {
                'discount_percentage': percentage[randVal],
                'description': fake.bs()
            }
            cursor.execute("INSERT INTO Sales.Discounts VALUES (?, ?)",
                        discount['discount_percentage'],
                        discount['description']
                        )
            cursor.commit()
            return count+1
        else:
            return check.discount_id
    else:
        return check.discount_id


def getDepartment(cursor, role):
    groups = ['Leadership', 'Management', "Tehnical", "Project Management", "Financial", "Support"]
    count = cursor.execute("SELECT COUNT(*) FROM HR.Departments").fetchval()
    mapping = {
        'CEO': 'Leadership',
        'CTO': 'Leadership',
        'CFO': 'Leadership',
        'COO': 'Leadership',
        'HR Manager': 'Management',
        'Marketing Director': 'Management',
        'Sales Manager': 'Management',
        'Software Engineer': 'Tehnical',
        'Data Analyst': 'Tehnical',
        'Quality Assurance Specialist': 'Tehnical',
        'Project Manager': 'Project Management',
        'Operations Coordinator': 'Project Management',
        'Accountant': 'Financial',
        'Customer Support Representative': 'Support',
        'Administrative Assistant': 'Support'
    }

    if count < len(groups):
        check = cursor.execute("SELECT COUNT(department_name) FROM HR.Departments WHERE department_name = ?", mapping[role]).fetchval()

        if not check:
            employee_count = cursor.execute("SELECT COUNT(*) FROM HR.Employees").fetchval()
            department = {
                'department_name': mapping[role],
                'manager_id': random.randint(1, employee_count) if employee_count else None
            }
            cursor.execute("INSERT INTO HR.Departments VALUES (?, ?)",
                           department['department_name'],
                           department['manager_id']
                           )
            cursor.commit()
            count = cursor.execute("SELECT COUNT(*) FROM HR.Departments").fetchval()
            return count
        else:
            val = cursor.execute("SELECT department_id FROM HR.Departments WHERE department_name = ?", mapping[role]).fetchval()
            return val
    else:
        val = cursor.execute("SELECT department_id FROM HR.Departments WHERE department_name = ?", mapping[role]).fetchval()
        return val


def getRole(cursor):
    roles = ['CEO', 'CTO', 'CFO', 'COO',
             'HR Manager', 'Marketing Director', 'Sales Manager',
             'Software Engineer', 'Data Analyst',
             'Project Manager', 'Operations Coordinator',
             'Accountant',
             'Quality Assurance Specialist', 'Customer Support Representative', 'Administrative Assistant'] 
    count = cursor.execute("SELECT COUNT(*) FROM HR.Roles").fetchval()
    
    if count < len(roles):
        for el in roles:
            check = cursor.execute("SELECT role_name FROM HR.Roles WHERE role_name = ?", el).fetchval()
            if not check:
                role = {
                    'role_name': el,
                    'department_id': getDepartment(cursor, el),
                    'description': fake.bs()
                }
                cursor.execute("INSERT INTO HR.Roles VALUES (?, ?, ?)",
                            role['role_name'],
                            role['department_id'],
                            role['description']
                            )
                cursor.commit()
                return count+1
    else:
        return random.randint(1, count) if count > 0 else count


def insertEmployee(cursor):
    count = cursor.execute("SELECT COUNT(*) FROM HR.Employees").fetchval()
    date = fake.date_between(start_date='-1y', end_date='today')
    max_date = date + datetime.timedelta(days=14)
    currently_employed = random.randint(0, 1)
    employment_termination = None if currently_employed == 0 else fake.date_between(start_date=date, end_date='today')
    last_modified = date if not employment_termination else employment_termination
    
    if count < max_employees:
        employee = {
            'national_id_number': fake.random_number(digits=10),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'address_id': insertAddress(cursor),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
            'role_id': getRole(cursor),
            'vacation_hours': random.randint(0, 99),
            'sick_leave_hours': random.randint(0, 99),
            'hire_date': date,
            'currently_employed': currently_employed,
            'employment_termination': employment_termination,
            'last_modified': last_modified,
        }
        cursor.execute("INSERT INTO HR.Employees VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       employee['national_id_number'],
                       employee['first_name'],
                       employee['last_name'],
                       employee['address_id'],
                       employee['email'],
                       employee['phone_number'],
                       employee['role_id'],
                       employee['vacation_hours'],
                       employee['sick_leave_hours'],
                       employee['hire_date'],
                       employee['currently_employed'],
                       employee['employment_termination'],
                       employee['last_modified']
                       )
        cursor.commit()
        return count+1
    else:
        return random.randint(1, count) if count > 1 else count


def insertOrders(cursor, customer_id):
    date = fake.date_between(start_date='-1y', end_date='today')
    max_date = date + datetime.timedelta(days=14)
    savethis = getUserSession(cursor)
    # print(savethis)

    orders = {
        'customer_id': customer_id,
        'employee_id': insertEmployee(cursor),
        'discount_id': getDiscount(cursor),
        'order_status_id': getOrderStatus(cursor),
        'payment_method_id': getPaymentMethod(cursor),
        'shipping_id': getShippingMethod(cursor),
        'order_date': date,
        'expected_delivery': fake.date_between(start_date=date, end_date=max_date),
        'session_id': savethis
    }
    cursor.execute("INSERT INTO Sales.Orders VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   orders['customer_id'],
                   orders['employee_id'],
                   orders['discount_id'],
                   orders['order_status_id'],
                   orders['payment_method_id'],
                   orders['shipping_id'],
                   orders['order_date'],
                   orders['expected_delivery'],
                   orders['session_id'])
    cursor.commit()
    
    order_id = cursor.execute("SELECT COUNT(*) FROM Sales.Orders").fetchval()
    insertOrderItems(cursor, order_id, date)


def insertCountry(cursor):
    country = fake.country()
    exists = cursor.execute("SELECT COUNT(*) FROM Application.Country WHERE country_name = ?", country).fetchval()
    
    if exists == 0:
        country_data = pycountry.countries.get(name=country)
        abbr = country_data.alpha_2 if hasattr(country_data, 'alpha_2') else None
        cursor.execute("INSERT INTO Application.Country VALUES (?, ?)",
                       country,
                       abbr
                       )
        cursor.commit()
        count = cursor.execute("SELECT COUNT(*) FROM Application.Country").fetchval()
        return count
    elif exists == 1:
        val = cursor.execute("SELECT country_id FROM Application.Country WHERE country_name = ?", country).fetchval()
        return val


def insertAddress(cursor):
    address = {
        'addressLine1': fake.street_address(),
        'addressLine2': random.choice([None, None, None, fake.building_number(), f'# {random.randint(0, 999)}']),
        'city': fake.city(),
        'country_id': insertCountry(cursor),
        'postcode': fake.postcode()
    }

    cursor.execute("INSERT INTO Application.Address VALUES (?, ?, ?, ?, ?)",
                   address['addressLine1'],
                   address['addressLine2'],
                   address['city'],
                   address['country_id'],
                   address['postcode']
                   )
    cursor.commit()
    count = cursor.execute("SELECT COUNT(*) FROM Application.Address").fetchval()
    
    return count


def insertTitle(cursor):
    title_name = fake.prefix()
    check = cursor.execute("SELECT title_id, title_name FROM Application.Titles WHERE title_name = ?", title_name).fetchone()

    if not check:
        cursor.execute("INSERT INTO Application.Titles (title_name) VALUES (?)", title_name)
        cursor.commit()
        count = cursor.execute("SELECT COUNT(*) FROM Application.Titles").fetchval()
        return count
    else:
        return check.title_id


def insertCustomer(conn_string):
    connection = pyodbc.connect(conn_string)
    cursor = connection.cursor()
    for i in range(num_inserts_per_core):
        customer = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'title_id': insertTitle(cursor),
            'marital_status': random.randint(0, 1),
            'phone_number': fake.phone_number(),
            'address_id': insertAddress(cursor),
            'email': fake.email(),
            'email_consent': random.randint(0, 1),
            'date_of_birth': fake.date_of_birth(),
            'sms_consent': random.randint(0, 1),
            'register_date': fake.date_this_decade()
        }

        cursor.execute("INSERT INTO Sales.Customers (first_name, last_name, title_id, marital_status, phone_number, address_id, email, email_consent, date_of_birth, sms_consent, register_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    customer['first_name'],
                    customer['last_name'],
                    customer['title_id'],
                    customer['marital_status'],
                    customer['phone_number'],
                    customer['address_id'],
                    customer['email'],
                    customer['email_consent'],
                    customer['date_of_birth'],
                    customer['sms_consent'],
                    customer['register_date']
                    )
        cursor.commit()
        count = cursor.execute("SELECT COUNT(*) FROM Sales.Customers").fetchval()
        insertOrders(cursor, count)
        
    # print(f"{num_inserts_per_core} customers inserted successfully!")
    connection.close()


def main ():
    conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=JARVIS;DATABASE=NewSample;Trusted_Connection=yes'
    cpu_count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cpu_count)
    test = [conn_string] * cpu_count

    pool.map(insertCustomer, test)

    pool.close()
    pool.join()


if __name__ == '__main__':
    start = time.time()
    main()
    # conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=JARVIS;DATABASE=NewSample;Trusted_Connection=yes'
    # insertCustomer(conn_string)
    end_ms = round((time.time() - start) * 1000)
    end = round((time.time()- start))
    print(f"Elapsed {end_ms}ms ({end}s)")