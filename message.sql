CREATE TABLE paddy_calculator (
    id INT AUTO_INCREMENT PRIMARY KEY,
    num_bags INT NOT NULL,
    bag_weight FLOAT NOT NULL,
    price_per_bag FLOAT NOT NULL,
    total_weight_kg FLOAT NOT NULL,
    total_amount FLOAT NOT NULL
);
