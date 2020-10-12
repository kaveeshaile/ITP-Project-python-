
CREATE TABLE `completed_events` (
  `Event_ID` int NOT NULL ,
  `Event_type` varchar(45) DEFAULT NULL,
  `Location` varchar(45) DEFAULT NULL,
  `Contact` char(10) DEFAULT NULL,
  `Customer_ID` char(10) DEFAULT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY (`Event_ID`),
  KEY `Customer_ID_idx` (`Customer_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `voltage_entertainment`.`event`(`Event_type`,`Location`,`Contact`,`Customer_ID`,`Date`,`Status`)
VALUES('gettogether','Malabe',9784755556,88, '2008-7-08','waiting');



drop trigger  move_to_completed;

-- when customer canceled--
CREATE TRIGGER move_to_completed
AFTER DELETE ON event
FOR EACH ROW
INSERT INTO completed_events(Event_ID, Event_type, Location, Contact, Customer_ID,Date,Status) 
VALUES (old.Event_ID, old.Event_type, old.Location, old.Contact, old.Customer_ID,old.Date,'canceld');


-- when event marked as completed--
DELIMITER //
CREATE TRIGGER move_after_completed AFTER UPDATE ON event
FOR EACH ROW
BEGIN
   IF NEW.Status = 'completed' THEN
    INSERT INTO completed_events(Event_ID, Event_type, Location, Contact, Customer_ID,Date,Status) 
VALUES (old.Event_ID, old.Event_type, old.Location, old.Contact, old.Customer_ID,old.Date,'completed'); 
   END IF;
END;//
DELIMITER ;


 
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
INSERT INTO resources (Resources_ID,Facility_ID) 
VALUES (NEW.id,'videography');  
END;//
DELIMITER ;

drop trigger move_video_to_resources; 
