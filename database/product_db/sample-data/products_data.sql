USE product_db;

INSERT INTO products
(product_name, brand, price, description, image, stock, category_id)
VALUES

('Apple iPhone 16 Pro', 'Apple', 129999.00,
'Apple iPhone 16 Pro with A18 Pro chip and 256GB storage.',
'images/products/iphone16pro.jpg',
25, 1),

('Samsung Galaxy S25 Ultra', 'Samsung', 119999.00,
'Samsung flagship smartphone with AI features.',
'images/products/galaxys25ultra.jpg',
20, 1),

('OnePlus 13', 'OnePlus', 69999.00,
'OnePlus flagship smartphone with Snapdragon processor.',
'images/products/oneplus13.jpg',
30, 1),

('Apple MacBook Air M4', 'Apple', 124999.00,
'MacBook Air with Apple M4 chip.',
'images/products/macbookairm4.jpg',
15, 2),

('Dell XPS 15', 'Dell', 149999.00,
'Premium Dell laptop for professionals.',
'images/products/dellxps15.jpg',
10, 2),

('Sony WH-1000XM6', 'Sony', 34999.00,
'Noise cancelling wireless headphones.',
'images/products/sonywh1000xm6.jpg',
35, 3),

('Apple AirPods Pro 2', 'Apple', 24999.00,
'Wireless earbuds with Active Noise Cancellation.',
'images/products/airpodspro2.jpg',
40, 3),

('Apple Watch Series 10', 'Apple', 49999.00,
'Latest Apple smartwatch.',
'images/products/applewatch10.jpg',
18, 4),

('Samsung Galaxy Watch Ultra', 'Samsung', 59999.00,
'Premium smartwatch from Samsung.',
'images/products/galaxywatchultra.jpg',
15, 4),

('LG OLED C4 55 Inch', 'LG', 139999.00,
'55-inch OLED Smart TV.',
'images/products/lgoledc4.jpg',
8, 5);