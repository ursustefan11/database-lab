from faker import Faker
import multiprocessing
import pyodbc
import random
import pycountry
import datetime
import time

conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=JARVIS;DATABASE=NewSample;Trusted_Connection=yes'

num_inserts_per_core = 5000
max_employees = 150

fake = Faker()


def getCurrency(cursor):
    currency = fake.currency()
    count = cursor.execute("SELECT TOP(1) currency_id FROM Financial.Currency ORDER BY currency_id DESC").fetchval() or 0
    check = cursor.execute("SELECT currency_id FROM Financial.Currency WHERE currency_code = ?", currency[0]).fetchval()

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
        return check


def getStatus(cursor):
    status = ['Pending', 'Paid', 'Failed', 'Refunded', 'Cancelled']
    randVal = random.randint(0, len(status)-1)
    count = cursor.execute("SELECT TOP(1) status_id FROM Financial.PaymentStatus ORDER BY status_id DESC").fetchval() or 0
    check = cursor.execute("SELECT status_id FROM Financial.PaymentStatus WHERE status_name = ?", status[randVal]).fetchval()

    if not check:
        cursor.execute("INSERT INTO Financial.PaymentStatus VALUES (?)", status[randVal])
        cursor.commit()
        return count+1
    else:
        return check
    

def insertPayment(cursor, invoice_id, price, date):
    payment = {
        'invoice_id': invoice_id,
        'status_id': getStatus(cursor),
        'currency_id': getCurrency(cursor),
        'payment_date': date,
        'total_amount': price,
    }
    cursor.execute("INSERT INTO Financial.Payments VALUES (?, ?, ?, ?, ?)",
                   payment['invoice_id'],
                   payment['status_id'],
                   payment['currency_id'],
                   payment['payment_date'],
                   payment['total_amount'])
    cursor.commit()


def insertInvoice(cursor, order_id, price, date):
    invoice = {
        'order_id': order_id,
        'invoice_date': date,
    }
    cursor.execute("INSERT INTO Financial.Invoices VALUES (?, ?)",
                   invoice['order_id'],
                   invoice['invoice_date']
                   )
    cursor.commit()
    count = cursor.execute("SELECT TOP(1) invoice_id FROM Financial.Invoices").fetchval()

    insertPayment(cursor, count, price, date)


def getAttribute(cursor):
    attr = ['Small', 'Extra-Small', 'Medium', 'Large', 'Extra-Large']
    randVal = random.randrange(len(attr))
    check = cursor.execute("SELECT attribute_id FROM Inventory.Attributes WHERE attribute_value = ?", attr[randVal]).fetchval()
    
    if check is None:
        attribute = {
            'attribute_name': "Size",
            'attribute_value': attr[randVal]
        }
        cursor.execute("INSERT INTO Inventory.Attributes VALUES (?, ?)",
                        attribute['attribute_name'],
                        attribute['attribute_value']
                        )
        cursor.commit()
        count = cursor.execute("SELECT TOP(1) attribute_id FROM Inventory.Attributes ORDER BY attribute_id DESC").fetchval()
        return count
    else:
        return check
    

def getCategory(cursor):
    values = ["Electronics", "Clothing", "Home Decor", "Beauty", "Books", "Sports Equipment", "Toys", "Furniture", "Jewelry", "Automotive", "Health and Fitness", "Pet Supplies", "Food and Beverages", "Tools and Hardware", "Music Instruments"]
    count = cursor.execute("SELECT TOP(1) category_id FROM Inventory.Categories ORDER BY category_id DESC").fetchval() or 0
    randomVal = values[random.randrange(len(values))]
    check = cursor.execute("SELECT category_id FROM Inventory.Categories WHERE category_name = ?", randomVal).fetchval()

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
            return check
    else:
        return check
    

def getProducts(cursor):
    values = ["Stellar Laptop", "Cosmic Coffee Maker", "Luminary Smartphone", "Infinity Fitness Tracker", "Zenith Headphones", "Radiant Smart TV", "Nova Digital Camera", "Sapphire Bluetooth Speaker", "Whispering Vacuum Cleaner", "Celestial Blender", "Harmony Electric Toothbrush", "Tranquil Microwave Oven", "Eclipse Hair Dryer", "Petal Power Drill", "Serenity Air Purifier", "Vivid Steam Iron", "Silent Robotic Vacuum", "Zephyr Espresso Machine", "Enchanted Massage Chair", "Dreamy Slow Cooker", "Azure Power Bank", "Mystic Electric Kettle", "Lush Air Fryer", "Twilight Gaming Console", "Harmonic Cordless Phone", "Whirlwind Electric Shaver", "Dusk Portable Bluetooth Speaker", "Moonlight Smart Thermostat", "Tranquil Digital Scale", "Radiant Rice Cooker", "Ethereal Food Processor", "Vibrant Curling Iron", "Calm Sewing Machine", "Whispering Blender", "Glistening Portable Fan", "Jade Laptop Stand", "Sparkling Smart Watch", "Dreamy Fitness Bike", "Harmony Hair Straightener", "Celestial Electric Grill", "Rhythmic Handheld Vacuum", "Sapphire Food Steamer", "Zenith Wireless Charger", "Luminous Ironing Board", "Mystical Air Conditioner", "Harmonic Cordless Drill", "Tranquil Coffee Grinder", "Petal Electric Toothbrush", "Serenity Soundbar", "Vivid Robot Vacuum", "Silent Hair Clippers", "Zephyr Clothes Steamer", "Enchanted Bluetooth Headphones", "Dreamy Portable Projector", "Azure Wireless Mouse", "Twilight Air Fryer", "Eclipse Electric Kettle", "Lush Handheld Blender", "Whispering Slow Cooker", "Glistening Gaming Mouse", "Radiant Rice Cooker", "Mystic Espresso Machine", "Calm Cordless Phone", "Whirlwind Portable Bluetooth Speaker", "Jade Food Processor", "Sparkling Electric Shaver", "Harmony Smart TV", "Tranquil Fitness Tracker", "Vivid Hair Dryer", "Sapphire Power Drill", "Zenith Air Purifier", "Luminous Microwave Oven", "Mystical Robotic Vacuum", "Harmonic Massage Chair", "Twilight Digital Camera", "Enchanted Bluetooth Speaker", "Dreamy Electric Toothbrush", "Petal Vacuum Cleaner", "Serenity Blender", "Radiant Portable Fan", "Azure Laptop", "Silent Smart Thermostat", "Zephyr Digital Scale", "Ethereal Steam Iron", "Vibrant Espresso Machine", "Celestial Slow Cooker", "Rhythmic Hair Dryer", "Glistening Power Bank", "Whispering Electric Kettle", "Calm Air Fryer", "Jade Gaming Console", "Sparkling Cordless Phone", "Mystic Electric Shaver", "Lush Portable Bluetooth Speaker", "Zenith Smart Watch", "Harmony Digital Camera", "Tranquil Fitness Bike", "Eclipse Hair Straightener"]
    randVal = random.randrange(len(values))
    check = cursor.execute("SELECT product_id FROM Inventory.Products WHERE product_name = ?", values[randVal]).fetchval()
    
    if check is None:
        price = round(random.uniform(0.1, 10), 2)
        products = {
            'product_name': values[randVal],
            'product_number': fake.pystr_format().upper(),
            'category_id': getCategory(cursor),
            'description': fake.bs(),
            'supplier_price': price,
            'sale_price': price*2.5,
            'attribute_id': getAttribute(cursor),
            'weight_kg': round(random.uniform(0.1, 30), 2)
        }
        cursor.execute("INSERT INTO Inventory.Products VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    products['product_name'],
                    products['product_number'],
                    products['category_id'],
                    products['description'],
                    products['supplier_price'],
                    products['sale_price'],
                    products['attribute_id'],
                    products['weight_kg']
                    )
        cursor.commit()
        count = cursor.execute("SELECT TOP(1) product_id FROM Inventory.Products ORDER BY product_id DESC").fetchval()
        val = [count, "1"]
        return count
    else:
        val = [check, "2"]
        return check


def insertOrderItems(cursor, order_id, date):
    price = 0.0

    for _ in range(random.randrange(10)):
        product = getProducts(cursor)
        qty = random.randint(1, 10)

        # print(product)
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
    check = cursor.execute("SELECT session_id FROM Application.SessionType WHERE user_agent = ?", user_agent).fetchval()

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
        count = cursor.execute("SELECT TOP(1) session_id FROM Application.SessionType ORDER BY session_id DESC").fetchval()
        return count
    else:
        return check


def getShippingMethod(cursor):
    values = ["Standard Shipping", "Express Shipping", "Next-Day Delivery", "Same-Day Delivery", "Free Shipping", "International Shipping", "Expedited Shipping", "Store Pickup", "Freight Shipping",]
    randVal = random.randrange(len(values))
    count = cursor.execute("SELECT TOP(1) shipping_id FROM Sales.ShippingMethods ORDER BY shipping_id DESC").fetchval() or 0
    check = cursor.execute("SELECT shipping_id FROM Sales.ShippingMethods WHERE shipping_name = ?", values[randVal]).fetchval()

    if count < len(values):
        if not check:
            shipping_methods = {
                'shipping_name': values[randVal],
                'validFrom': fake.date_between(start_date='-2y', end_date='today')
            }
            cursor.execute("INSERT INTO Sales.ShippingMethods VALUES (?, ?)",
                           shipping_methods['shipping_name'],
                           shipping_methods['validFrom']
                           )
            cursor.commit()
            return count+1
        else:
            return check
    else:
        return check
    
    
def getPaymentMethod(cursor):
    values = ['Cash', 'Credit card', 'Debit card', 'Bank transfer', 'PayPal', 'Cryptocurrency']
    randVal = random.randint(0, len(values)-1)
    count = cursor.execute("SELECT TOP(1) payment_method_id FROM Sales.PaymentMethods ORDER BY payment_method_id DESC").fetchval() or 0
    check = cursor.execute("SELECT payment_method_id FROM Sales.PaymentMethods WHERE payment_name = ?", values[randVal]).fetchval()

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
            return check
    else:
        return check
    

def getPaymentStatus(cursor):
    values = ['Pending', 'Paid', 'Cancelled']
    randVal = random.randrange(len(values))
    count = cursor.execute("SELECT TOP(1) status_id FROM Financial.PaymentStatus ORDER BY order_id DESC").fetchval() or 0
    check = cursor.execute("SELECT payment_method_id FROM Sales.PaymentMethods WHERE payment_name = ?", values[randVal]).fetchval()

    if count < len(values):
        if not check:
            cursor.execute("INSERT INTO Financial.PaymentStatus VALUES (?)", values[randVal])
            cursor.commit()
            return count+1
    else:
        return check
    

def getOrderStatus(cursor):
    values = ['Pending', 'Processing', 'Shipped', 'Delivered']
    randVal = random.randrange(len(values))
    count = cursor.execute("SELECT TOP(1) order_status_id FROM Sales.OrderStatus ORDER BY order_status_id DESC").fetchval() or 0
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
    count = cursor.execute("SELECT TOP(1) discount_id FROM Sales.Discounts ORDER BY discount_id DESC").fetchval() or 0
    check = cursor.execute("SELECT discount_id FROM Sales.Discounts WHERE discount_percentage = ?", percentage[randVal]).fetchval()
    
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
            return check
    else:
        return check


def getDepartment(cursor, role):
    # groups = ['Leadership', 'Management', "Tehnical", "Project Management", "Financial", "Support"]
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
    check = cursor.execute("SELECT department_id FROM HR.Departments WHERE department_name = ?", mapping[role]).fetchval()

    if check is None:
        employee_count = cursor.execute("SELECT TOP(1) employee_id FROM HR.Employees ORDER BY employee_id DESC").fetchval()
        department = {
            'department_name': mapping[role],
            'manager_id': random.randint(1, employee_count) if employee_count else None
        }
        cursor.execute("INSERT INTO HR.Departments VALUES (?, ?)",
                        department['department_name'],
                        department['manager_id']
                        )
        cursor.commit()
        count = cursor.execute("SELECT TOP(1) department_id FROM HR.Departments ORDER BY department_id DESC").fetchval()
        return count
    else:
        return check


def getRole(cursor):
    roles = ['CEO', 'CTO', 'CFO', 'COO',
             'HR Manager', 'Marketing Director', 'Sales Manager',
             'Software Engineer', 'Data Analyst',
             'Project Manager', 'Operations Coordinator',
             'Accountant',
             'Quality Assurance Specialist', 'Customer Support Representative', 'Administrative Assistant'] 
    
    count = cursor.execute("SELECT TOP(1) role_id FROM HR.Roles ORDER BY role_id DESC").fetchval() or 0
    randVal = random.randrange(len(roles))
    check = cursor.execute("SELECT role_id FROM HR.Roles WHERE role_name = ?", roles[randVal]).fetchval()
    
    if count < len(roles):
        if not check:
            role = {
                'role_name': roles[randVal],
                'department_id': getDepartment(cursor, roles[randVal]),
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
            return check
    else:
        return check


def insertEmployee(cursor):
    count = cursor.execute("SELECT TOP(1) employee_id FROM HR.Employees ORDER BY employee_id DESC").fetchval() or 0
    
    if count < max_employees:
        date = fake.date_between(start_date='-1y', end_date='today')
        max_date = date + datetime.timedelta(days=14)
        currently_employed = random.randint(0, 1)
        employment_termination = None if currently_employed == 0 else fake.date_between(start_date=date, end_date='today')
        last_modified = date if not employment_termination else employment_termination

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

    orders = {
        'customer_id': customer_id,
        'employee_id': insertEmployee(cursor),
        'discount_id': getDiscount(cursor),
        'order_status_id': getOrderStatus(cursor),
        'payment_method_id': getPaymentMethod(cursor),
        'shipping_id': getShippingMethod(cursor),
        'order_date': date,
        'expected_delivery': fake.date_between(start_date=date, end_date=max_date),
        'session_id': getUserSession(cursor)
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
                orders['session_id']
                )
    cursor.commit()
    order_id = cursor.execute("SELECT TOP(1) order_id FROM Sales.Orders ORDER BY order_id DESC").fetchval()
    insertOrderItems(cursor, order_id, date)


def insertCountry(cursor):
    country = fake.country()
    check = cursor.execute("SELECT country_id FROM Application.Country WHERE country_name = ?", country).fetchval()
    
    if not check:
        country_data = pycountry.countries.get(name=country)
        abbr = country_data.alpha_2 if hasattr(country_data, 'alpha_2') else None
        cursor.execute("INSERT INTO Application.Country VALUES (?, ?)",
                       country,
                       abbr
                       )
        cursor.commit()
        count = cursor.execute("SELECT TOP(1) country_id FROM Application.Country ORDER BY country_id DESC").fetchval()
        return count
    else:
        return check


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
    count = cursor.execute("SELECT TOP(1) address_id FROM Application.Address ORDER BY address_id DESC").fetchval()
    return count


def insertTitle(cursor):
    title_name = fake.prefix()
    check = cursor.execute("SELECT title_id, title_name FROM Application.Titles WHERE title_name = ?", title_name).fetchval()

    if not check:
        cursor.execute("INSERT INTO Application.Titles (title_name) VALUES (?)", title_name)
        cursor.commit()
        count = cursor.execute("SELECT TOP(1) title_id FROM Application.Titles ORDER BY title_id DESC").fetchval()
        return count
    else:
        return check


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
            'date_of_birth': fake.date_between(start_date='-50y', end_date='-10y'),
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
        count = cursor.execute("SELECT TOP(1) customer_id FROM Sales.Customers ORDER BY customer_id DESC").fetchval()
        insertOrders(cursor, count)
        
    # print(f"{num_inserts_per_core} customers inserted successfully!")
    connection.close()


def main ():
    cpu_count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cpu_count)
    test = [conn_string] * cpu_count

    pool.map(insertCustomer, test)

    pool.close()
    pool.join()


if __name__ == '__main__':
    start = time.time()
    main()
    # insertCustomer(conn_string)
    end_ms = round((time.time() - start) * 1000)
    end = round((time.time()- start))
    print(f"Elapsed {end_ms}ms ({end}s)")