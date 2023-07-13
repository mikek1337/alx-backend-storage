-- trigger that reset attribute valid_email after update email

DELIMITER $$
CREATE TRIGGER `valid_email` AFTER UPDATE ON `users` FOR EACH ROW
BEGIN
    IF NEW.email LIKE '%@%' THEN
        SET NEW.valid_email = 1;
    ELSE
        SET NEW.valid_email = 0;
    END IF;
END$$