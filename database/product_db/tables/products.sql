USE product_db;

CREATE TABLE products
(
    product_id INT
    AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR
    (200) NOT NULL,
    brand VARCHAR
    (100) NOT NULL,
    price DECIMAL
    (10,2) NOT NULL,
    description TEXT,
    image VARCHAR
    (255),
    stock INT NOT NULL,
    category_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_product_category
        FOREIGN KEY
    (category_id)
        REFERENCES categories
    (category_id)
);

    INSERT INTO categories
        (category_name)
    VALUES
        ('Laptops'),
        ('Electronics'),
        ('Fashion'),
        ('Books');