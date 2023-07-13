-- store procedure compute average score for each student 

DELIMITER $$
CREATE PROCEDURE `computeAverageScore` (IN user_id INT)
BEGIN
    DECLARE average FLOAT;
    DECLARE total FLOAT;
    DECLARE count INT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR SELECT score FROM corrections WHERE user_id = user_id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    SET total = 0;
    SET count = 0;
    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO average;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SET total = total + average;
        SET count = count + 1;
    END LOOP;
    CLOSE cur;
    IF count = 0 THEN
        SELECT 0;
    ELSE
        SELECT total / count;
    END IF;
END$$
