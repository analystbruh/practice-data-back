create_statements = '''
CREATE TABLE Employees (

    id integer  NOT NULL PRIMARY KEY,
    first_name TEXT  NOT NULL ,
    last_name TEXT  NOT NULL ,
    city TEXT  NOT NULL ,
    state TEXT  NULL ,
    country TEXT  NULL ,
    hire_date TEXT  NOT NULL ,
    termination_date TEXT  NULL ,
    job_title TEXT  NOT NULL
);



CREATE TABLE Products (

    id integer  NOT NULL PRIMARY KEY,
    category_id integer  NOT NULL ,
    brand TEXT  NOT NULL ,
    product_name TEXT  NOT NULL ,
    price integer  NOT NULL ,
    FOREIGN KEY(category_id) REFERENCES Product_Categories(id)
);



CREATE TABLE Transactions (

    id integer  NOT NULL PRIMARY KEY,
    customer_id integer  NOT NULL ,
    product_id integer  NOT NULL ,
    employee_id integer  NULL ,
    timestamp TEXT  NOT NULL ,
    transaction_type TEXT  NOT NULL ,
    FOREIGN KEY(customer_id) REFERENCES Customers(id),
    FOREIGN KEY(product_id) REFERENCES Products(id),
    FOREIGN KEY(employee_id) REFERENCES Employees(id)
);



CREATE TABLE Customers (

    id integer  NOT NULL PRIMARY KEY,
    first_name TEXT  NOT NULL ,
    last_name TEXT  NOT NULL ,
    city TEXT  NOT NULL ,
    state TEXT  NULL ,
    country TEXT  NOT NULL
);



CREATE TABLE Product_Categories (

    id integer  NOT NULL PRIMARY KEY ,
    product_category TEXT  NOT NULL
);
'''