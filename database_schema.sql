-- Created: September 28, 2025

-- Drop tables if they exist (for clean recreation)
DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;

-- Create Customers table
CREATE TABLE Customers (
    customerId INTEGER PRIMARY KEY,
    customerName TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT,
    address TEXT,
    createdAt DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create Orders table
CREATE TABLE Orders (
    orderId INTEGER PRIMARY KEY AUTOINCREMENT,
    customerId INTEGER NOT NULL,
    orderDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    totalAmount DECIMAL(10,2),
    status TEXT DEFAULT 'pending',
    FOREIGN KEY (customerId) REFERENCES Customers(customerId)
);

-- Create Items table
CREATE TABLE Items (
    itemId INTEGER PRIMARY KEY,
    orderId INTEGER NOT NULL,
    productName TEXT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity INTEGER DEFAULT 1,
    FOREIGN KEY (orderId) REFERENCES Orders(orderId)
);

-- Insert sample data into Customers table
INSERT INTO Customers (customerId, customerName, email, phone, address) VALUES
(1001, 'Juan Pérez', 'juan.perez@email.com', '+1-555-0101', '123 Main St, Madrid'),
(2847, 'María García', 'maria.garcia@email.com', '+1-555-0102', '456 Oak Ave, Barcelona'),
(3265, 'Carlos López', 'carlos.lopez@email.com', '+1-555-0103', '789 Pine Rd, Valencia'),
(4592, 'Ana Martínez', 'ana.martinez@email.com', '+1-555-0104', '321 Elm St, Sevilla'),
(5738, 'Luis Rodríguez', 'luis.rodriguez@email.com', '+1-555-0105', '654 Maple Dr, Bilbao');

-- Insert sample data into Orders table
INSERT INTO Orders (customerId, orderDate, totalAmount, status) VALUES
(1001, '2025-09-25 10:30:00', 89.97, 'completed'),
(2847, '2025-09-26 14:15:00', 156.48, 'completed'),
(1001, '2025-09-27 09:45:00', 45.99, 'pending'),
(3265, '2025-09-27 16:20:00', 234.50, 'shipped'),
(4592, '2025-09-28 08:10:00', 78.25, 'processing'),
(2847, '2025-09-28 11:30:00', 199.99, 'pending'),
(3265, '2025-09-28 13:45:00', 67.80, 'completed'),
(3265, '2025-09-28 15:20:00', 125.75, 'completed');

-- Insert sample data into Items table
INSERT INTO Items (itemId, orderId, productName, price, quantity) VALUES
-- Order 1 items
(1247, 1, 'Laptop Charger', 29.99, 1),
(8921, 1, 'USB Cable', 15.99, 2),
(5634, 1, 'Mouse Pad', 12.99, 1),
(3543, 1, 'Wireless Mouse', 25.99, 1),

-- Order 2 items
(7892, 2, 'Bluetooth Headphones', 89.99, 1),
(4156, 2, 'Phone Case', 19.99, 1),
(9283, 2, 'Screen Protector', 12.50, 2),
(6745, 2, 'Car Charger', 22.00, 1),

-- Order 3 items
(2847, 3, 'Coffee Mug', 15.99, 1),
(5921, 3, 'Notebook', 8.99, 2),
(8374, 3, 'Pen Set', 12.99, 1),

-- Order 4 items
(1659, 4, 'Gaming Keyboard', 129.99, 1),
(7234, 4, 'Gaming Mouse', 79.99, 1),
(4987, 4, 'Mouse Pad XL', 24.52, 1),

-- Order 5 items
(3821, 5, 'Water Bottle', 18.99, 1),
(9456, 5, 'Protein Bar', 3.99, 12),
(6183, 5, 'Gym Towel', 11.27, 1),

-- Order 6 items
(2574, 6, 'Smartwatch', 199.99, 1),

-- Order 7 items
(8639, 7, 'Book: Programming', 34.99, 1),
(1482, 7, 'Bookmark Set', 7.99, 2),
(5796, 7, 'Reading Light', 16.83, 1),

-- Order 8 items (Customer 3265)
(223, 8, 'Wireless Keyboard', 45.99, 1),
(113, 8, 'USB Hub', 29.99, 1),
(9632, 8, 'Cable Organizer', 12.99, 2),
(4758, 8, 'Desk Lamp', 36.78, 1);

-- Create useful indexes for better query performance
CREATE INDEX idx_orders_customer ON Orders(customerId);
CREATE INDEX idx_items_order ON Items(orderId);
CREATE INDEX idx_orders_date ON Orders(orderDate);

-- Sample queries to verify the data
SELECT 'Total number of customers:' as description, COUNT(*) as count FROM Customers
UNION ALL
SELECT 'Total number of orders:', COUNT(*) FROM Orders
UNION ALL
SELECT 'Total number of items:', COUNT(*) FROM Items;

-- Query to show order summary with customer information
SELECT 
    c.customerName,
    o.orderId,
    o.orderDate,
    o.totalAmount,
    o.status,
    COUNT(i.itemId) as itemCount
FROM Customers c
JOIN Orders o ON c.customerId = o.customerId
LEFT JOIN Items i ON o.orderId = i.orderId
GROUP BY c.customerId, o.orderId
ORDER BY o.orderDate DESC;
