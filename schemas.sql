CREATE TABLE listings (
  id INT PRIMARY KEY NOT NULL,
  number_of_reviews INT
);

CREATE TABLE reviewers (
  id INT PRIMARY KEY NOT NULL,
  number_of_reviews INT
);

CREATE TABLE reviews (
  id INT PRIMARY KEY NOT NULL,
  comments TEXT
);