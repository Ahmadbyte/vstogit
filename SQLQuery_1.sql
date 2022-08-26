CREATE TABLE Empl (
    ID int NOT NULL PRIMARY KEY,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);

INSERT into Empl(ID, LastName, FirstName,Age)
VALUES(1, 'srk', 'ahmad', 23)

SELECT * from Empl