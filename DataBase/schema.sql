CREATE TABLE IF NOT EXISTS orders  (
    id serial PRIMARY KEY,
    order_id bigint NOT NULL UNIQUE,
    delivery_date DATE NOT NULL,
    price_usd DECIMAL(20, 10) NOT NULL,
    price_rub DECIMAL(20, 10) NOT NULL
);
