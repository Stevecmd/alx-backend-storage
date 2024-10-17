-- Create a stored procedure ComputeAverageWeightedScoreForUsers that
-- computes and stores the average weighted score for all students

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE weighted_sum FLOAT;
    DECLARE total_weight INT;
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN user_cursor;

    read_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate the weighted sum of scores for the user
        SELECT SUM(c.score * p.weight) INTO weighted_sum
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Calculate the total weight for the user
        SELECT SUM(p.weight) INTO total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Update the user's average score
        IF total_weight = 0 THEN
            UPDATE users
            SET average_score = 0
            WHERE id = user_id;
        ELSE
            UPDATE users
            SET average_score = weighted_sum / total_weight
            WHERE id = user_id;
        END IF;
    END LOOP;

    CLOSE user_cursor;
END //

DELIMITER ;