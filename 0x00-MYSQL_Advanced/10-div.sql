-- create a function safeDiv that divides first with second

CREATE FUNCTION safeDiv(IN a INT, IN b INT)
RETURNS INT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END
```