-- When New videographer added --
DELIMITER $$
CREATE TRIGGER video_prefix
BEFORE INSERT ON videography
FOR EACH ROW
BEGIN
  INSERT INTO  video_prefix VALUES (NULL);
  SET NEW.id = CONCAT('Video', LPAD(LAST_INSERT_ID(), 3, '0'));
END $$
DELIMITER ;


-- copy videographer id to parent table (resources) --
DELIMITER //
CREATE TRIGGER move_video_to_resources AFTER INSERT ON videography
FOR EACH ROW
BEGIN
INSERT INTO resources (Resources_ID) 
VALUES (NEW.id);  
END;//
DELIMITER ;
