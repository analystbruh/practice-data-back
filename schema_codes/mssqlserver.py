create_statements='''
SET XACT_ABORT ON

BEGIN TRANSACTION QUICKDBD

CREATE TABLE [employees] (
    -- Clustered
    [id] integer  NOT NULL ,
    [first_name] varchar(50)  NOT NULL ,
    [last_name] varchar(50)  NOT NULL ,
    [city] varchar(50)  NOT NULL ,
    [state] varchar(50)  NULL ,
    [country] varchar(50)  NULL ,
    [hire_date] date  NOT NULL ,
    [termination_date] date  NULL ,
    [job_title] varchar(50)  NOT NULL ,
    CONSTRAINT [PK_employees] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [products] (
    -- Clustered
    [id] integer  NOT NULL ,
    [category_id] integer  NOT NULL ,
    [brand] varchar(50)  NOT NULL ,
    [product_name] varchar(200)  NOT NULL ,
    [price] integer  NOT NULL ,
    CONSTRAINT [PK_products] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [transactions] (
    -- Clustered
    [id] integer  NOT NULL ,
    [customer_id] integer  NOT NULL ,
    [product_id] integer  NOT NULL ,
    [employee_id] integer  NULL ,
    [timestamp] date  NOT NULL ,
    [transaction_type] varchar(10)  NOT NULL ,
    CONSTRAINT [PK_transactions] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [customers] (
    -- Clustered
    [id] integer  NOT NULL ,
    [first_name] varchar(50)  NOT NULL ,
    [last_name] varchar(50)  NOT NULL ,
    [city] varchar(50)  NOT NULL ,
    [state] varchar(50)  NULL ,
    [country] varchar(50)  NOT NULL ,
    CONSTRAINT [PK_customers] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [product_categories] (
    -- Clustered
    [id] integer  NOT NULL ,
    [product_category] varchar(100)  NOT NULL ,
    CONSTRAINT [PK_product_categories] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

ALTER TABLE [products] WITH CHECK ADD CONSTRAINT [FK_products_category_id] FOREIGN KEY([category_id])
REFERENCES [product_categories] ([id])

ALTER TABLE [products] CHECK CONSTRAINT [FK_products_category_id]

ALTER TABLE [transactions] WITH CHECK ADD CONSTRAINT [FK_transactions_customer_id] FOREIGN KEY([customer_id])
REFERENCES [customers] ([id])

ALTER TABLE [transactions] CHECK CONSTRAINT [FK_transactions_customer_id]

ALTER TABLE [transactions] WITH CHECK ADD CONSTRAINT [FK_transactions_product_id] FOREIGN KEY([product_id])
REFERENCES [products] ([id])

ALTER TABLE [transactions] CHECK CONSTRAINT [FK_transactions_product_id]

ALTER TABLE [transactions] WITH CHECK ADD CONSTRAINT [FK_transactions_employee_id] FOREIGN KEY([employee_id])
REFERENCES [employees] ([id])

ALTER TABLE [transactions] CHECK CONSTRAINT [FK_transactions_employee_id]

COMMIT TRANSACTION QUICKDBD
'''