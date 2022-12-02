ansi_oracle = '''
CREATE TABLE "store_transactions" (
    "transaction_id" integer NOT NULL,
    "customer_first_name" varchar(50) NOT NULL,
    "customer_last_name" varchar(50) NOT NULL,
    "customer_city" varchar(50) NOT NULL,
    "customer_state" varchar(50) NULL,
    "customer_country" varchar(50) NOT NULL,
    "product_category" varchar(100) NOT NULL,
    "brand" varchar(50) NOT NULL,
    "product_name" varchar(200) NOT NULL,
    "price" integer NOT NULL,
    "employee_first_name" varchar(50) NULL,
    "employee_last_name" varchar(50) NULL,
    "employee_city" varchar(50) NULL,
    "employee_state" varchar(50) NULL,
    "employee_country" varchar(50) NULL,
    "hire_date" date NULL,
    "termination_date" date NULL,
    "job_title" varchar(50) NULL,
    "timestamp" date NOT NULL,
    "transaction_type" varchar(10) NOT NULL
);
'''

sql_server = '''
CREATE TABLE [store_transactions] (
    [transaction_id] integer NOT NULL,
    [customer_first_name] varchar(50) NOT NULL,
    [customer_last_name] varchar(50) NOT NULL,
    [customer_city] varchar(50) NOT NULL,
    [customer_state] varchar(50) NULL,
    [customer_country] varchar(50) NOT NULL,
    [product_category] varchar(100) NOT NULL,
    [brand] varchar(50) NOT NULL,
    [product_name] varchar(200) NOT NULL,
    [price] integer NOT NULL,
    [employee_first_name] varchar(50) NULL,
    [employee_last_name] varchar(50) NULL,
    [employee_city] varchar(50) NULL,
    [employee_state] varchar(50) NULL,
    [employee_country] varchar(50) NULL,
    [hire_date] date NULL,
    [termination_date] date NULL,
    [job_title] varchar(50) NULL,
    [timestamp] date NOT NULL,
    [transaction_type] varchar(10) NOT NULL
);
'''

mysql_mariadb = '''
CREATE TABLE `store_transactions` (
    `transaction_id` integer NOT NULL,
    `customer_first_name` varchar(50) NOT NULL,
    `customer_last_name` varchar(50) NOT NULL,
    `customer_city` varchar(50) NOT NULL,
    `customer_state` varchar(50) NULL,
    `customer_country` varchar(50) NOT NULL,
    `product_category` varchar(100) NOT NULL,
    `brand` varchar(50) NOT NULL,
    `product_name` varchar(200) NOT NULL,
    `price` integer NOT NULL,
    `employee_first_name` varchar(50) NULL,
    `employee_last_name` varchar(50) NULL,
    `employee_city` varchar(50) NULL,
    `employee_state` varchar(50) NULL,
    `employee_country` varchar(50) NULL,
    `hire_date` date NULL,
    `termination_date` date NULL,
    `job_title` varchar(50) NULL,
    `timestamp` date NOT NULL,
    `transaction_type` varchar(10) NOT NULL
);
'''

postgresql = '''
CREATE TABLE store_transactions (
    transaction_id integer NOT NULL,
    customer_first_name varchar(50) NOT NULL,
    customer_last_name varchar(50) NOT NULL,
    customer_city varchar(50) NOT NULL,
    customer_state varchar(50) NULL,
    customer_country varchar(50) NOT NULL,
    product_category varchar(100) NOT NULL,
    brand varchar(50) NOT NULL,
    product_name varchar(200) NOT NULL,
    price integer NOT NULL,
    employee_first_name varchar(50) NULL,
    employee_last_name varchar(50) NULL,
    employee_city varchar(50) NULL,
    employee_state varchar(50) NULL,
    employee_country varchar(50) NULL,
    hire_date date NULL,
    termination_date date NULL,
    job_title varchar(50) NULL,
    timestamp date NOT NULL,
    transaction_type varchar(10) NOT NULL
);
'''

sqlite = '''
CREATE TABLE store_transactions (
    transaction_id integer NOT NULL,
    customer_first_name TEXT NOT NULL,
    customer_last_name TEXT NOT NULL,
    customer_city TEXT NOT NULL,
    customer_state TEXT NULL,
    customer_country TEXT NOT NULL,
    product_category TEXT NOT NULL,
    brand TEXT NOT NULL,
    product_name TEXT NOT NULL,
    price integer NOT NULL,
    employee_first_name TEXT NULL,
    employee_last_name TEXT NULL,
    employee_city TEXT NULL,
    employee_state TEXT NULL,
    employee_country TEXT NULL,
    hire_TEXT TEXT NULL,
    termination_TEXT TEXT NULL,
    job_title TEXT NULL,
    timestamp TEXT NOT NULL,
    transaction_type TEXT NOT NULL
);
'''

create_statements = [
    ansi_oracle,
    sql_server,
    mysql_mariadb,
    mysql_mariadb,
    ansi_oracle,
    postgresql,
    sqlite
]