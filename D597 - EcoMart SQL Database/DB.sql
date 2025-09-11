-- Database: EcoMart

-- DROP DATABASE IF EXISTS "EcoMart";

CREATE DATABASE "EcoMart"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;




-- Table: public.accounting

-- DROP TABLE IF EXISTS public.accounting;

CREATE TABLE IF NOT EXISTS public.accounting
(
    order_id numeric NOT NULL,
    total_price money,
    total_cost money,
    total_profit money,
    CONSTRAINT order_id_fk FOREIGN KEY (order_id)
        REFERENCES public.orders (order_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.accounting
    OWNER to postgres;




-- Table: public.customer

-- DROP TABLE IF EXISTS public.customer;

CREATE TABLE IF NOT EXISTS public.customer
(
    customer_id numeric NOT NULL,
    customer_name text COLLATE pg_catalog."default",
    CONSTRAINT customer_pkey PRIMARY KEY (customer_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.customer
    OWNER to postgres;




-- Table: public.order_priority

-- DROP TABLE IF EXISTS public.order_priority;

CREATE TABLE IF NOT EXISTS public.order_priority
(
    priority_code "char" NOT NULL,
    priority_description text COLLATE pg_catalog."default",
    CONSTRAINT order_priority_pkey PRIMARY KEY (priority_code)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.order_priority
    OWNER to postgres;




-- Table: public.products

-- DROP TABLE IF EXISTS public.products;

CREATE TABLE IF NOT EXISTS public.products
(
    product_id numeric NOT NULL,
    product_name text COLLATE pg_catalog."default",
    price money,
    cost money,
    profit money,
    CONSTRAINT products_pkey PRIMARY KEY (product_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.products
    OWNER to postgres;




-- Table: public.sale_channel

-- DROP TABLE IF EXISTS public.sale_channel;

CREATE TABLE IF NOT EXISTS public.sale_channel
(
    channel_id numeric NOT NULL,
    channel_name text COLLATE pg_catalog."default",
    CONSTRAINT sale_channel_pkey PRIMARY KEY (channel_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.sale_channel
    OWNER to postgres;




-- Table: public.sale_country

-- DROP TABLE IF EXISTS public.sale_country;

CREATE TABLE IF NOT EXISTS public.sale_country
(
    country_id numeric NOT NULL,
    country_name text COLLATE pg_catalog."default",
    CONSTRAINT sale_country_pkey PRIMARY KEY (country_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.sale_country
    OWNER to postgres;




-- Table: public.sale_region

-- DROP TABLE IF EXISTS public.sale_region;

CREATE TABLE IF NOT EXISTS public.sale_region
(
    region_id numeric NOT NULL,
    region_name text COLLATE pg_catalog."default",
    CONSTRAINT sale_region_pkey PRIMARY KEY (region_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.sale_region
    OWNER to postgres;




-- Table: public.orders

-- DROP TABLE IF EXISTS public.orders;

CREATE TABLE IF NOT EXISTS public.orders
(
    order_id numeric NOT NULL,
    customer_id numeric,
    region_id numeric,
    country_id numeric,
    sales_channel numeric,
    order_priority "char",
    order_date date,
    ship_date date,
    product_id numeric,
    product_quantity numeric,
    total_price money,
    CONSTRAINT orders_pkey PRIMARY KEY (order_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.orders
    OWNER to postgres;
-- Index: idx_country_id

-- DROP INDEX IF EXISTS public.idx_country_id;

CREATE INDEX IF NOT EXISTS idx_country_id
    ON public.orders USING btree
    (country_id ASC NULLS LAST)
    INCLUDE(country_id)
    WITH (deduplicate_items=True)
    TABLESPACE pg_default;
-- Index: idx_order_id

-- DROP INDEX IF EXISTS public.idx_order_id;

CREATE INDEX IF NOT EXISTS idx_order_id
    ON public.orders USING btree
    (order_id ASC NULLS LAST)
    INCLUDE(order_id)
    WITH (deduplicate_items=True)
    TABLESPACE pg_default;
-- Index: idx_product_id

-- DROP INDEX IF EXISTS public.idx_product_id;

CREATE INDEX IF NOT EXISTS idx_product_id
    ON public.orders USING btree
    (product_id ASC NULLS LAST)
    INCLUDE(product_id)
    WITH (deduplicate_items=True)
    TABLESPACE pg_default;
-- Index: idx_region_id

-- DROP INDEX IF EXISTS public.idx_region_id;

CREATE INDEX IF NOT EXISTS idx_region_id
    ON public.orders USING btree
    (region_id ASC NULLS LAST)
    INCLUDE(region_id)
    WITH (deduplicate_items=True)
    TABLESPACE pg_default;





-- csv data imported used pgAdmin importation tool