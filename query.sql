CREATE DATABASE ecommerce_oct;

USE ecommerce_oct;

CREATE TABLE roles(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

CREATE TABLE `users`(
	id INT PRIMARY KEY AUTO_INCREMENT,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    email VARCHAR(50) UNIQUE,
    `password` VARCHAR(100),
    role_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE RESTRICT
);

CREATE TABLE user_profile(
    id INT PRIMARY KEY AUTO_INCREMENT,
    gender VARCHAR(20),
    passport VARCHAR(100),
    bio TEXT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
 )



CREATE TABLE product(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) UNIQUE,
    quantity INT,
    price DECIMAL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
 );
 
CREATE TABLE category(
 	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE 
 );
 

CREATE TABLE product_category(
 	id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    category_id INT,
    FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE RESTRICT
 );
 

-- https://drawsql.app/teams/damilarearise/diagrams/ecommerce-schema


INSERT INTO roles (name) VALUES
('Admin'),
('Seller'),
('Customer');

INSERT INTO users
(firstname, lastname, email, password, role_id)
VALUES
('Damilare', 'Arise', 'damilare@example.com', 'demo_hash_001', 1),
('Ada', 'Okafor', 'ada@example.com', 'demo_hash_002', 2),
('John', 'Adeyemi', 'john@example.com', 'demo_hash_003', 3),
('Grace', 'Adebayo', 'grace@example.com', 'demo_hash_004', 3),
('David', 'Eze', 'david@example.com', 'demo_hash_005', 2),
('Sarah', 'Bello', 'sarah@example.com', 'demo_hash_006', 3),
('Michael', 'Ojo', 'michael@example.com', 'demo_hash_007', 3),
('Esther', 'James', 'esther@example.com', 'demo_hash_008', 2),
('Samuel', 'Ibrahim', 'samuel@example.com', 'demo_hash_009', 3),
('Victoria', 'Olawale', 'victoria@example.com', 'demo_hash_010', 3);



INSERT INTO user_profile (gender, passport, bio, user_id) VALUES
('Male', 'passport1.jpg', 'Software developer', 1),
('Female', 'passport2.jpg', 'Student', 2),
('Male', 'passport3.jpg', 'Business owner', 3),
('Female', 'passport4.jpg', 'Designer', 4),
('Male', 'passport5.jpg', 'Teacher', 5),
('Female', 'passport6.jpg', 'Student', 6),
('Male', 'passport7.jpg', 'Entrepreneur', 7),
('Female', 'passport8.jpg', 'Developer', 8),
('Male', 'passport9.jpg', 'Student', 9),
('Female', 'passport10.jpg', 'Business owner', 10);


INSERT INTO category (name) VALUES
('Electronics'),
('Fashion'),
('Food'),
('Books'),
('Sports');


INSERT INTO product (title, quantity, price) VALUES
('Laptop', 10, 450000),
('Smartphone', 20, 250000),
('Tablet', 15, 180000),
('Desktop Computer', 8, 500000),
('Keyboard', 30, 15000),
('Mouse', 40, 8000),
('Monitor', 12, 120000),
('Printer', 7, 95000),
('Headphones', 25, 18000),
('Power Bank', 35, 12000),
('Smart Watch', 18, 35000),
('USB Cable', 50, 3000),
('Flash Drive', 40, 5000),
('External Hard Drive', 10, 85000),
('Router', 14, 28000),
('Bluetooth Speaker', 22, 25000),
('Webcam', 16, 20000),
('Microphone', 11, 30000),
('Projector', 5, 220000),
('Phone Charger', 45, 4500),
('T-Shirt', 30, 7000),
('Jeans', 20, 15000),
('Sneakers', 18, 35000),
('Jacket', 12, 25000),
('Cap', 25, 5000),
('Wristwatch', 15, 18000),
('Handbag', 17, 22000),
('Sunglasses', 20, 9000),
('Belt', 28, 6000),
('Socks', 50, 2000),
('Dress', 14, 18000),
('Formal Shirt', 16, 12000),
('Sandals', 21, 10000),
('School Bag', 19, 15000),
('Wallet', 24, 7000),
('Suit', 6, 85000),
('Scarf', 18, 4000),
('Slippers', 35, 3500),
('Shorts', 22, 8000),
('Wristband', 30, 2500),
('Rice', 40, 85000),
('Beans', 30, 45000),
('Vegetable Oil', 25, 28000),
('Sugar', 35, 12000),
('Salt', 50, 2000),
('Flour', 28, 18000),
('Milk', 24, 15000),
('Cornflakes', 20, 12000),
('Noodles', 60, 1500),
('Tomato Paste', 40, 3000),
('Electric Kettle', 12, 18000),
('Blender', 10, 35000),
('Microwave', 6, 120000),
('Gas Cooker', 8, 85000),
('Refrigerator', 5, 450000),
('Washing Machine', 4, 380000),
('Cooking Pot', 15, 22000),
('Dinner Plate', 30, 3000),
('Spoon Set', 25, 5000),
('Water Bottle', 35, 4500),
('Cutlery Set', 18, 12000),
('Novel', 20, 5000),
('Mathematics Textbook', 15, 8000),
('Physics Textbook', 12, 7500),
('Chemistry Textbook', 14, 7000),
('Biology Textbook', 16, 6500),
('English Dictionary', 10, 9000),
('Programming in Python', 18, 12000),
('Web Development Guide', 12, 15000),
('Database Systems', 9, 14000),
('Data Science Handbook', 11, 18000),
('Machine Learning Basics', 13, 16000),
('History Book', 17, 6000),
('Geography Textbook', 14, 7000),
('Business Management', 10, 11000),
('Accounting Textbook', 12, 9500),
('Physics Workbook', 20, 4500),
('Football', 25, 12000),
('Basketball', 18, 15000),
('Volleyball', 14, 10000),
('Tennis Racket', 8, 28000),
('Skipping Rope', 30, 3500),
('Gym Gloves', 16, 6000),
('Yoga Mat', 12, 12000),
('Football Boots', 10, 35000),
('Sports Jersey', 20, 9000),
('Water Bottle Holder', 18, 5000),
('Dumbbells', 10, 25000),
('Resistance Bands', 22, 7000),
('Swimming Goggles', 15, 8000),
('Sports Socks', 30, 2500),
('Tennis Ball', 24, 4000),
('Cricket Bat', 6, 22000),
('Badminton Racket', 9, 18000),
('Protective Helmet', 7, 30000),
('Fitness Tracker', 11, 40000),
('Running Shoes', 13, 45000),
('Exercise Bench', 4, 95000),
('Punching Bag', 5, 55000),
('Sports Backpack', 14, 18000);

INSERT INTO product_category (product_id, category_id) VALUES
-- Electronics + Sports
(1, 1), (1, 5),
(2, 1),
(3, 1), (3, 4),
(4, 1),
(5, 1), (5, 2),
(6, 1),
(7, 1), (7, 5),
(8, 1),
(9, 1), (9, 5),
(10, 1),

-- Fashion + Sports
(21, 2), (21, 5),
(22, 2),
(23, 2), (23, 5),
(24, 2),
(25, 2), (25, 5),
(26, 2),
(27, 2),
(28, 2), (28, 5),
(29, 2),
(30, 2), (30, 5),

-- Food + Home & Kitchen
(41, 3), (41, 3),
(42, 3),
(43, 3), (43, 3),
(44, 3),
(45, 3), (45, 3),
(46, 3),
(47, 3),
(48, 3),
(49, 3), (49, 3),
(50, 3),

-- Books + Electronics
(61, 4), (61, 1),
(62, 4),
(63, 4), (63, 1),
(64, 4),
(65, 4),
(66, 4), (66, 1),
(67, 4),
(68, 4), (68, 1),
(69, 4),
(70, 4),

-- Sports + Fashion
(77, 5), (77, 2),
(78, 5),
(79, 5), (79, 2),
(80, 5),
(81, 5), (81, 2),
(82, 5),
(83, 5), (83, 2),
(84, 5),
(85, 5), (85, 2);