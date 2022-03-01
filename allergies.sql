DROP TABLE IF EXISTS FOOD

CREATE TABLE FOOD(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(30),
    dairy BOOLEAN,
    gluten BOOLEAN,
    nut BOOLEAN,
    soy BOOLEAN,
    egg BOOLEAN,
    fish BOOLEAN
);

INSERT INTO FOOD(name, dairy, gluten, nut, soy, egg, fish) VALUES
(waffles, true, true, false, false, false, false),
(pancakes, true, true, false, false, true, false),
(devilled eggs, true, false, false, true, true, false),
(fried chicken, false, false, false, false, false, false),
(regular pizza, true, true, false, false, false, false),
(anchovie pizza, true, true, false, false, false, true),
(cheeseburger, true, true, false, false, false, false),
(hamburger, true, false, false, false, false, false),
(pb&j, false, true, true, false, false, false);