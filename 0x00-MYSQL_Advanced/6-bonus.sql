-- store procedure that adds new correction to a student

DELIMITER $$
CREATE PROCEDURE `addBouns` (IN user_id INT, IN project_name VARCHAR(140), IN score INT)
BEGIN
    INSERT INTO corrections (user_id, project_name, score, created_at) VALUES (user_id, project_name, score, NOW());
END$$