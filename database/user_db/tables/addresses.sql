USE user_db;

CREATE TABLE addresses (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    address_line VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    pincode VARCHAR(10) NOT NULL,
    country VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_user_address
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);