create_statements='''
CREATE TABLE "employees" (
    -- Clustered
    "id" integer  NOT NULL ,
    "first_name" varchar(50)  NOT NULL ,
    "last_name" varchar(50)  NOT NULL ,
    "city" varchar(50)  NOT NULL ,
    "state" varchar(50)  NULL ,
    "country" varchar(50)  NULL ,
    "hire_date" date  NOT NULL ,
    "termination_date" date  NULL ,
    "job_title" varchar(50)  NOT NULL ,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "id"
    )
)

GO

CREATE TABLE "products" (
    -- Clustered
    "id" integer  NOT NULL ,
    "category_id" integer  NOT NULL ,
    "brand" varchar(50)  NOT NULL ,
    "product_name" varchar(200)  NOT NULL ,
    "price" integer  NOT NULL ,
    CONSTRAINT "pk_products" PRIMARY KEY (
        "id"
    )
)

GO

CREATE TABLE "transactions" (
    -- Clustered
    "id" integer  NOT NULL ,
    "customer_id" integer  NOT NULL ,
    "product_id" integer  NOT NULL ,
    "employee_id" integer  NULL ,
    "timestamp" date  NOT NULL ,
    "transaction_type" varchar(10)  NOT NULL ,
    CONSTRAINT "pk_transactions" PRIMARY KEY (
        "id"
    )
)

GO

CREATE TABLE "customers" (
    -- Clustered
    "id" integer  NOT NULL ,
    "first_name" varchar(50)  NOT NULL ,
    "last_name" varchar(50)  NOT NULL ,
    "city" varchar(50)  NOT NULL ,
    "state" varchar(50)  NULL ,
    "country" varchar(50)  NOT NULL ,
    CONSTRAINT "pk_customers" PRIMARY KEY (
        "id"
    )
)

GO

CREATE TABLE "product_categories" (
    -- Clustered
    "id" integer  NOT NULL ,
    "product_category" varchar(100)  NOT NULL ,
    CONSTRAINT "pk_product_categories" PRIMARY KEY (
        "id"
    )
)

GO

ALTER TABLE "products" ADD CONSTRAINT "fk_products_category_id" FOREIGN KEY("category_id")
REFERENCES "product_categories" ("id")
GO

ALTER TABLE "transactions" ADD CONSTRAINT "fk_transactions_customer_id" FOREIGN KEY("customer_id")
REFERENCES "customers" ("id")
GO

ALTER TABLE "transactions" ADD CONSTRAINT "fk_transactions_product_id" FOREIGN KEY("product_id")
REFERENCES "products" ("id")
GO

ALTER TABLE "transactions" ADD CONSTRAINT "fk_transactions_employee_id" FOREIGN KEY("employee_id")
REFERENCES "employees" ("id")
GO
'''