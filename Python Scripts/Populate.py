from faker import Faker
import random
import pyodbc
import multiprocessing

# Initiate connection with the database
connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=JARVIS;DATABASE=NewSample;Trusted_Connection=yes'
fake = Faker()
# generalConnection = pyodbc.connect(connection_string)
# generalCursor = generalConnection.cursor()
# generalCursor.execute("SET STATISTICS XML ON")


# Generate data for Sales.Customers table
def generateSalesCustomers (count):
    customers = []
    for _ in range(count):
        customer = {
            'title': random.choice([None, fake.prefix()]),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'date_of_birth': fake.date_of_birth(),
            'marital_status': random.randint(0, 1),
            'email': fake.email(),
            'email_consent': random.randint(0, 1),
            'phone_number': fake.phone_number(),
            'sms_consent': random.randint(0, 1),
            'addressLine1': fake.street_address(),
            'addressLine2': random.choice([None, None, None, fake.building_number(), f'# {random.randint(0, 999)}']),
            'city': fake.city(),
            'country': fake.country(),
            'postcode': fake.postcode(),
            'register_date': fake.date_this_decade()
        }
        customers.append(customer)
    
    return customers


# Generate data for Sales.Orders table
def generateSalesOrders (count, cursor):
    customerCount = cursor.execute("SELECT count(customer_id) FROM Sales.Customers").fetchval()

    if customerCount > 0:
        orders = []
        for _ in range(count):
            order = {
                'buyer_id': random.randint(1, customerCount),
                'order_date': fake.date_between(start_date='-1y', end_date='today'),
                'total_amount': random.uniform(10, 1000),
                'status': random.choice(['Pending', 'Processing', 'Shipped', 'Delivered'])
            }
            orders.append(order)

        return orders
    else:
        return False


# Generate data for Products table
def generateInventoryProducts ():
    product_names = ["Stellar Laptop", "Cosmic Coffee Maker", "Luminary Smartphone", "Infinity Fitness Tracker", "Zenith Headphones", "Radiant Smart TV", "Nova Digital Camera", "Sapphire Bluetooth Speaker", "Whispering Vacuum Cleaner", "Celestial Blender", "Harmony Electric Toothbrush", "Tranquil Microwave Oven", "Eclipse Hair Dryer", "Petal Power Drill", "Serenity Air Purifier", "Vivid Steam Iron", "Silent Robotic Vacuum", "Zephyr Espresso Machine", "Enchanted Massage Chair", "Dreamy Slow Cooker", "Azure Power Bank", "Mystic Electric Kettle", "Lush Air Fryer", "Twilight Gaming Console", "Harmonic Cordless Phone", "Whirlwind Electric Shaver", "Dusk Portable Bluetooth Speaker", "Moonlight Smart Thermostat", "Tranquil Digital Scale", "Radiant Rice Cooker", "Ethereal Food Processor", "Vibrant Curling Iron", "Calm Sewing Machine", "Whispering Blender", "Glistening Portable Fan", "Jade Laptop Stand", "Sparkling Smart Watch", "Dreamy Fitness Bike", "Harmony Hair Straightener", "Celestial Electric Grill", "Rhythmic Handheld Vacuum", "Sapphire Food Steamer", "Zenith Wireless Charger", "Luminous Ironing Board", "Mystical Air Conditioner", "Harmonic Cordless Drill", "Tranquil Coffee Grinder", "Petal Electric Toothbrush", "Serenity Soundbar", "Vivid Robot Vacuum", "Silent Hair Clippers", "Zephyr Clothes Steamer", "Enchanted Bluetooth Headphones", "Dreamy Portable Projector", "Azure Wireless Mouse", "Twilight Air Fryer", "Eclipse Electric Kettle", "Lush Handheld Blender", "Whispering Slow Cooker", "Glistening Gaming Mouse", "Radiant Rice Cooker", "Mystic Espresso Machine", "Calm Cordless Phone", "Whirlwind Portable Bluetooth Speaker", "Jade Food Processor", "Sparkling Electric Shaver", "Harmony Smart TV", "Tranquil Fitness Tracker", "Vivid Hair Dryer", "Sapphire Power Drill", "Zenith Air Purifier", "Luminous Microwave Oven", "Mystical Robotic Vacuum", "Harmonic Massage Chair", "Twilight Digital Camera", "Enchanted Bluetooth Speaker", "Dreamy Electric Toothbrush", "Petal Vacuum Cleaner", "Serenity Blender", "Radiant Portable Fan", "Azure Laptop", "Silent Smart Thermostat", "Zephyr Digital Scale", "Ethereal Steam Iron", "Vibrant Espresso Machine", "Celestial Slow Cooker", "Rhythmic Hair Dryer", "Glistening Power Bank", "Whispering Electric Kettle", "Calm Air Fryer", "Jade Gaming Console", "Sparkling Cordless Phone", "Mystic Electric Shaver", "Lush Portable Bluetooth Speaker", "Zenith Smart Watch", "Harmony Digital Camera", "Tranquil Fitness Bike", "Eclipse Hair Straightener"]

    products = []
    for i in range(len(product_names)):
        price =  round(random.uniform(1, 500), 2)
        product = {
            'name': product_names[i],
            'product_number': fake.pystr_format(),
            'description': fake.sentence(nb_words=10),
            'price': round(0.4*price, 2),
            'color': random.choice(['Black', 'Silver', 'Blue', 'Red', 'Green', 'Yellow', None]),
            'size': random.choice(['Small', 'Extra-Small', 'Medium', 'Large', 'Extra-Large', None]),
            'weight': round(random.uniform(0.1, 10), 2),
            'list_price': price,
            'weight_measurement_code': random.choice(['kg', 'lbs', None])
        }
        products.append(product)

    return products


# Generate data for Inventory.Suppliers table
def generateInventorySuppliers(count):
    suppliers = []
    for _ in range(count):
        supplier = {
            'supplier_name': fake.company(),
            'supplier_category': random.randint(1, 5),
            'contact_person': fake.name(),
            'contact_person_email': fake.email(),
            'phone_number': fake.phone_number(),
            'company_address': fake.address(),
            'bank_name': random.choice(['Horizon Bank', 'Unity Trust Bank', 'Crestview Bank', 'Evergreen Financial', 'Liberty National Bank', 'Aurora Bank', 'Pacific Coast Bank', 'Magnolia Bank', 'Stellar Bank', 'Cascade Financial', 'Sunrise Bank', 'Tranquil Trust Bank', 'Haven Financial', 'Golden Oak Bank', 'Summit City Bank']),
            'bank_account_code': random.randint(1000, 9999),
            'bank_account_number': random.randint(10000, 99999),
            'payment_days': random.choice([7, 14, 30]),
            'validFrom': fake.date_this_decade(),
            'validTo': fake.date_this_decade()
        }
        suppliers.append(supplier)
    
    return suppliers


# Generate data for Inventory.PurchaseOrders table
def generateEcommerceOrders(count, cursor):
    customerCount = cursor.execute("SELECT count(*) FROM Sales.Customers").fetchval()

    if customerCount > 0:
        orders = []
        for _ in range(count):
            order = {
                'customer_id': random.randint(1, customerCount),
                'order_date': fake.date_this_decade(),
                'total_amount': round(random.uniform(100, 1000), 2),
                'expected_delivery': fake.future_date(end_date='+30d'),
                'status': random.choice([0, 1])
            }
            orders.append(order)
        
        return orders
    else:
        return False


# Generate data for Inventory.PurchaseOrderItems table
def generateEcommerceOrderItems(count, cursor):
    ordersCount = cursor.execute("SELECT count(*) FROM Ecommerce.Orders").fetchval()
    productsCount = cursor.execute("SELECT count(*) FROM Inventory.Products").fetchval()
    

    if productsCount > 1 and ordersCount > 1:
        items = []
        for _ in range(count):
            productid = random.randint(1, productsCount)
            productPrice = cursor.execute(f"SELECT price FROM Inventory.Products WHERE product_id = {productid}").fetchval()
            qty = random.randint(1, 25)
            item = {
                'order_id': random.randint(1, ordersCount),
                'product_id' : productid,
                'quantity': random.randint(1, 15),
                'price': productPrice*qty,
            }
            items.append(item)
        
        return items
    else:
        return False


# Generate data for HR.Employees table
def generateHrEmployees(count, conn):
    jobTitles = conn.execute("SELECT name FROM HR.Departments").fetchall()
    employees = []

    if len(jobTitles) > 0:
        for _ in range(count):
            employee = {
                'first_name': fake.first_name(),
                'national_id_number': fake.ean(length=13), 
                'last_name': fake.last_name(),
                'email': fake.email(),
                'phone_number': fake.phone_number(),
                'hire_date': fake.date_between(start_date='-10y', end_date='today'),
                'job_title': jobTitles[random.randint(0, len(jobTitles)-1)].name,
                'vacation_hours': random.randint(0, 99),
                'sick_leave_hours': random.randint(0, 99),
                'last_modified': fake.date()
            }
            employees.append(employee)
        return employees
    else:
        return False


# Generate data for HR.Departments table
def generateHrDepartments(conn):
    managerCount = conn.execute("SELECT COUNT(*) FROM HR.Employees").fetchval()
    departments = []
    groups = ['Leadership', 'Leadership', 'Leadership', 'Leadership', 'Management', 'Management', 'Management', "Tehnical", "Tehnical", "Project Management", "Project Management", "Financial", "Support", "Support", "Support",]
    roles = ['CEO', 'CTO', 'CFO', 'COO', 'HR Manager', 'Marketing Director', 'Sales Manager', " Software Engineer", "Data Analyst", 'Project Manager', 'Operations Coordinator', 'Accountant', 'Quality Assurance Specialist', 'Customer Support Representative', 'Administrative Assistant']
    manager = random.randint(1, managerCount) if managerCount > 0 else None

    for i in range(len(roles)):
        department = {
            'name': roles[i],
            'group_name': groups[i],
            'manager_id': manager
        }
        departments.append(department)
    return departments


# Generate data for Financial.Invoices table
def generateFinancialInvoices(count, conn):
    customerCount = conn.execute("SELECT count(*) FROM Sales.Customers").fetchval()
    invoices = []

    if customerCount > 1:
        for _ in range(count):
            invoice = {
                'customer_id': random.randint(1, customerCount),
                'invoice_date': fake.date_between(start_date='-1y', end_date='today'),
                'total_amount': round(random.uniform(10, 1000), 2),
                'status': random.choice(['Pending', 'Paid', 'Cancelled'])
            }
            invoices.append(invoice)
        return invoices
    else:
        return False


# Generate data for Financial.Payments table
def generateFinancialPayments(count, conn):
    invoicesCount = conn.execute("SELECT COUNT(*) FROM Financial.Invoices").fetchval()
    payments = []
    
    if invoicesCount > 1:
        for _ in range(count):
            payment = {
                'invoice_id': random.randint(1, invoicesCount),
                'payment_date': fake.date_between(start_date='-1y', end_date='today'),
                'amount': round(random.uniform(1, 500), 2)
            }
            payments.append(payment)
        return payments
    else:
        return False




# Insert data into Sales.Customers table
def insertSalesCustomers(count):
    salesCustomerConn = pyodbc.connect(connection_string)
    salesCustomerCursor = salesCustomerConn.cursor()
    customers = generateSalesCustomers(count)

    for customer in customers:
        salesCustomerCursor.execute("INSERT INTO Sales.Customers (title, first_name, last_name, date_of_birth, marital_status, email, email_consent, phone_number, sms_consent, addressLine1, addressLine2, city, country, postcode, register_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       customer['title'], customer['first_name'], customer['last_name'], customer['date_of_birth'], customer['marital_status'], customer['email'], customer['email_consent'], customer['phone_number'], customer['sms_consent'], customer['addressLine1'], customer['addressLine2'], customer['city'], customer['country'], customer['postcode'], customer['register_date'])
    print(f"Inserted {count} into Sales.Customers")

    salesCustomerConn.commit()
    salesCustomerConn.close()


# Insert data into Sales.Orders table
def insertSalesOrders(count):
    salesOrdersConn = pyodbc.connect(connection_string)
    salesOrdersCursor = salesOrdersConn.cursor()
    orders = generateSalesOrders(count, salesOrdersCursor)

    if orders:
        for order in orders:
            salesOrdersCursor.execute("INSERT INTO Sales.Orders (buyer_id, order_date, total_amount, status) VALUES (?, ?, ?, ?)",
                        order['buyer_id'], order['order_date'], order['total_amount'], order['status'])
        print(f"Inserted {count} into Sales.Orders")

    salesOrdersConn.commit()
    salesOrdersConn.close()


# Insert data into Inventory.Products table
def insertInventoryProducts():
    inventoryProductConn = pyodbc.connect(connection_string)
    inventoryProductCursor = inventoryProductConn.cursor()
    productCount = inventoryProductCursor.execute("SELECT COUNT(*) FROM INVENTORY.PRODUCTS").fetchval()
    
    products = generateInventoryProducts()

    if productCount < len(products):
        for product in products:
            inventoryProductCursor.execute("INSERT INTO Inventory.Products (name, product_number, description, price, color, size, weight, list_price, weight_measurement_code) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        product['name'], product['product_number'], product['description'], product['price'], product['color'], product['size'], product['weight'], product['list_price'], product['weight_measurement_code'])
        print(f"Inserted {len(products)} into Inventory.Products")

    inventoryProductConn.commit()
    inventoryProductConn.close()


# Insert data into Inventory.Suppliers table
def insertInventorySuppliers(count):
    inventorySuppliersConn = pyodbc.connect(connection_string)
    inventorySuppliersCursor = inventorySuppliersConn.cursor()
    suppliers = generateInventorySuppliers(count)

    for supplier in suppliers:
        inventorySuppliersCursor.execute("INSERT INTO Inventory.Suppliers (supplier_name, supplier_category, contact_person, contact_person_email, phone_number, company_address, bank_name, bank_account_code, bank_account_number, payment_days, validFrom, validTo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       supplier['supplier_name'], supplier['supplier_category'], supplier['contact_person'], supplier['contact_person_email'], supplier['phone_number'], supplier['company_address'], supplier['bank_name'], supplier['bank_account_code'], supplier['bank_account_number'], supplier['payment_days'], supplier['validFrom'], supplier['validTo'])
    print(f"Inserted {count} into Inventory.Suppliers")

    inventorySuppliersCursor.commit()
    inventorySuppliersConn.close()


# Insert data into Ecommerce.Orders table
def insertEcommerceOrders(count):
    ecomOrdersConn = pyodbc.connect(connection_string)
    ecomOrdersCursor = ecomOrdersConn.cursor()
    orders = generateEcommerceOrders(count, ecomOrdersCursor)

    if orders:
        for order in orders:
            ecomOrdersCursor.execute("INSERT INTO Ecommerce.Orders (customer_id, order_date, total_amount, status) VALUES (?, ?, ?, ?)",
                        order['customer_id'], order['order_date'], order['total_amount'], order['status'])
        print(f"Inserted {count} into Ecommerce.Orders")
    
    ecomOrdersCursor.commit()
    ecomOrdersConn.close()


# Insert data into Ecommerce.OrderItems table
def insertEcommerceOrderItems(count):
    ecomOrderItemsConn = pyodbc.connect(connection_string)
    ecomOrderItemsCursor = ecomOrderItemsConn.cursor()
    items = generateEcommerceOrderItems(count, ecomOrderItemsCursor)

    if items:
        for item in items:
            ecomOrderItemsCursor.execute("INSERT INTO Ecommerce.OrderItems (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)",
                        item['order_id'], item['product_id'], item['quantity'], item['price'])
        print(f"Inserted {count} into Ecommerce.OrderItems")

    ecomOrderItemsCursor.commit()
    ecomOrderItemsConn.close()


# Insert data into HR.Employees table
def insertHrEmployees(count):
    hrEmployeesConn = pyodbc.connect(connection_string)
    hrEmployeesCursor = hrEmployeesConn.cursor()
    employees = generateHrEmployees(count, hrEmployeesCursor)

    if employees:
        for employee in employees:
                hrEmployeesCursor.execute("INSERT INTO HR.Employees (national_id_number, first_name, last_name, email, phone_number, hire_date, job_title, vacation_hours, sick_leave_hours, last_modified) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            employee['national_id_number'], employee['first_name'], employee['last_name'], employee['email'], employee['phone_number'], employee['hire_date'], employee['job_title'], employee['vacation_hours'], employee['sick_leave_hours'], employee['last_modified'])
        print(f"Inserted {count} into HR.Employees")

    hrEmployeesCursor.commit()
    hrEmployeesCursor.close()


# Insert data into HR.Departments table
def insertHrDepartments():
    HrDepartmentsConn = pyodbc.connect(connection_string)
    HrDepartmentsCursor = HrDepartmentsConn.cursor()
    departments = generateHrDepartments(HrDepartmentsCursor)
    rolesCount = HrDepartmentsCursor.execute("SELECT COUNT(*) FROM HR.Departments").fetchval()
    employeesCount = HrDepartmentsCursor.execute("SELECT COUNT(*) FROM HR.Employees").fetchval()

    if rolesCount < 15:
        if departments:
            for department in departments:
                    HrDepartmentsCursor.execute("INSERT INTO HR.Departments (name, group_name, manager_id) VALUES (?, ?, ?)",
                                department['name'], department['group_name'], department['manager_id'])
            print(f"Inserted {len(departments)} into HR.Departments")
    elif rolesCount == 15:
        withoutManagers = HrDepartmentsCursor.execute("SELECT department_id FROM HR.Departments WHERE manager_id IS NULL").fetchall()
        if len(withoutManagers) > 0:
            for row in withoutManagers:
                # print(row.department_id)
                addRandomManager = random.randint(1, employeesCount)
                HrDepartmentsCursor.execute("UPDATE HR.Departments SET manager_id = ? WHERE department_id = ?", addRandomManager, row.department_id)
            print("HR.Departments updated")

    HrDepartmentsCursor.commit()
    HrDepartmentsConn.close()


# Insert data into Financial.Invoices table
def insertFinancialInvoices(count):
    financialInvoicesConn = pyodbc.connect(connection_string)
    financialInvoicesCursor = financialInvoicesConn.cursor()
    invoices = generateFinancialInvoices(count, financialInvoicesConn)

    if invoices:
        for invoice in invoices:
                financialInvoicesCursor.execute("INSERT INTO Financial.Invoices (customer_id, invoice_date, total_amount, status) VALUES (?, ?, ?, ?)",
                            invoice['customer_id'], invoice['invoice_date'], invoice['total_amount'], invoice['status'])
        print(f"Inserted {count} into Financial.Invoices")

    financialInvoicesCursor.commit()
    financialInvoicesConn.close()


# Insert data into Financial.Payments table
def insertFinancialPayments(count):
    paymentsConn = pyodbc.connect(connection_string)
    paymentCursor = paymentsConn.cursor()
    payments = generateFinancialPayments(count, paymentCursor)

    if payments:
        for payment in payments:
                paymentCursor.execute("INSERT INTO Financial.Payments (invoice_id, payment_date, amount) VALUES (?, ?, ?)",
                            payment['invoice_id'], payment['payment_date'], payment['amount'])
        print(f"Inserted {count} into Financial.Payments")

    paymentCursor.commit()
    paymentsConn.close()




# Run, Forest, RUUUN!
def main():
    customer_thread = multiprocessing.Process(target=insertSalesCustomers, args=[41270])
    orders_thread =  multiprocessing.Process(target=insertSalesOrders, args=[824240])
    products_thread = multiprocessing.Process(target=insertInventoryProducts)
    suppliers_thread = multiprocessing.Process(target=insertInventorySuppliers, args=[1140])
    ecom_orders_thread = multiprocessing.Process(target=insertEcommerceOrders, args=[121010])
    ecom_order_items = multiprocessing.Process(target=insertEcommerceOrderItems, args=[151540])
    hr_departments =  multiprocessing.Process(target=insertHrDepartments)
    hr_employees = multiprocessing.Process(target=insertHrEmployees, args=[78])
    financial_invoices = multiprocessing.Process(target=insertFinancialInvoices, args=[65540])
    financial_payments = multiprocessing.Process(target=insertFinancialPayments, args=[45340])


    customer_thread.start()
    orders_thread.start()
    products_thread.start()
    suppliers_thread.start()
    ecom_orders_thread.start()
    ecom_order_items.start()
    hr_departments.start()
    hr_employees.start()
    financial_invoices.start()
    financial_payments.start()


    customer_thread.join()
    orders_thread.join()
    products_thread.join()
    suppliers_thread.join()
    ecom_orders_thread.join()
    ecom_order_items.join()
    hr_departments.join()
    hr_employees.join()
    financial_invoices.join()
    financial_payments.join()


# generalCursor.execute("SET STATISTICS XML OFF")

if __name__ == '__main__':
    main()
    print("Completed!")