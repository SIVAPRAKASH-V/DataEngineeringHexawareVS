----CREATE TABLE pets (
----    pet_id INT PRIMARY KEY IDENTITY(1,1), -- Auto-incrementing primary key
----    name NVARCHAR(100) NOT NULL,
----    age INT NOT NULL CHECK (age > 0), -- Age should be a positive integer
----    breed NVARCHAR(100) NOT NULL
----);

----CREATE TABLE donations (
----    donation_id INT PRIMARY KEY IDENTITY(1,1), -- Auto-incrementing primary key
----    donor_name NVARCHAR(100) NOT NULL,
----    amount DECIMAL(10, 2) NOT NULL CHECK (amount >= 10), -- Minimum donation amount is $10
----    donation_date DATETIME NOT NULL DEFAULT GETDATE() -- Records the date and time of the donation
----);



----CREATE TABLE adoption_events (
----    event_id INT PRIMARY KEY IDENTITY(1,1), -- Auto-incrementing primary key
----    event_name NVARCHAR(100) NOT NULL,
----    event_date DATETIME NOT NULL,
----    location NVARCHAR(100) NOT NULL
----);

----CREATE TABLE participants (
----    participant_id INT PRIMARY KEY IDENTITY(1,1), -- Auto-incrementing primary key
----    event_id INT NOT NULL, -- Foreign key referencing the adoption_events table
----    participant_name NVARCHAR(100) NOT NULL,
----    FOREIGN KEY (event_id) REFERENCES adoption_events(event_id) -- Establishes relationship
----);
----CREATE TABLE dogs (
----    id INT PRIMARY KEY, -- Foreign Key from pets
----    dog_breed NVARCHAR(50),
----    FOREIGN KEY (id) REFERENCES pets(pet_id)
----);
----CREATE TABLE cats (
----    id INT PRIMARY KEY, -- Foreign Key from pets
----    cat_color NVARCHAR(50),
----    FOREIGN KEY (id) REFERENCES pets(pet_id)
----);


--INSERT INTO pets (name, age, breed) 
--VALUES 
--('Buddy', 3, 'Golden Retriever'),
--('Mittens', 2, 'Siamese'),
--('Max', 5, 'Beagle'),
--('Whiskers', 4, 'Persian'),
--('Charlie', 2, 'Labrador'),
--('Luna', 3, 'Sphynx');
--INSERT INTO donations (donor_name, amount) 
--VALUES 
--('Alice Johnson', 50.00),
--('Bob Smith', 25.00),
--('Catherine Lee', 100.00),
--('David Martin', 75.00),
--('Eve Taylor', 15.00);
--INSERT INTO adoption_events (event_name, event_date, location) 
--VALUES 
--('Spring Adoption Fair', '2024-04-15', 'Central Park'),
--('Summer Paw-tacular', '2024-08-10', 'Greenfield Shelter'),
--('Holiday Adoption Bash', '2024-12-05', 'City Hall'),
--('Autumn Paws Event', '2024-10-20', 'Downtown Square');

--INSERT INTO participants (event_id, participant_name) 
--VALUES 
--(1, 'John Doe'),
--(1, 'Jane Smith'),
--(2, 'Michael Brown'),
--(3, 'Sarah Connor'),
--(4, 'Peter Parker');
--INSERT INTO dogs (id, dog_breed) 
--VALUES 
--(1, 'Golden Retriever'),
--(3, 'Beagle'),
--(5, 'Labrador');
--INSERT INTO cats (id, cat_color) 
--VALUES 
--(2, 'White'),
--(4, 'Gray'),

--(6, 'Black');
