-- a sql database that help to creates a trigger that decreases 
-- Quantity of an item after adding a new order

CREATE TRIGGER decrement
AFTER INSERT
ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE NAME = NEW.item_name;
