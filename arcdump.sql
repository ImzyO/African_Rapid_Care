-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: arc_dev_db
-- ------------------------------------------------------
-- Server version	8.0.31-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- @block Drop database
DROP DATABASE IF EXISTS arc_dev_db;

-- Create database + user if doesn't exist
CREATE DATABASE IF NOT EXISTS arc_dev_db;
CREATE USER IF NOT EXISTS 'arc_dev'@'localhost' IDENTIFIED BY 'arc_dev_pwd';
GRANT ALL PRIVILEGES ON `arc_dev_db`.* TO 'arc_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'arc_dev'@'localhost';
FLUSH PRIVILEGES;

USE arc_dev_db;

--
-- Table structure for table `appointment_status`
--

DROP TABLE IF EXISTS `appointment_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointment_status` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `appointment_status` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment_status`
--

LOCK TABLES `appointment_status` WRITE;
/*!40000 ALTER TABLE `appointment_status` DISABLE KEYS */;
INSERT INTO `appointment_status` VALUES ('670d7964-7e6a-43a5-936b-9a0165714ff0','2022-11-24 10:42:45','2022-11-24 10:42:50','Done'),('730a8a28-83f3-422c-9435-ee4327c2b0b7','2022-11-24 10:43:29','2022-11-24 10:43:30','In progress'),('9fe5fc0c-9265-446e-b6f0-82590a3128b4','2022-11-24 10:44:00','2022-11-24 10:44:01','Cancelled');
/*!40000 ALTER TABLE `appointment_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointments` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `start_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `end_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `symptoms` varchar(1024) NOT NULL,
  `appointment_type` varchar(128) NOT NULL,
  `office_id` varchar(60) NOT NULL,
  `patient_id` varchar(60) NOT NULL,
  `appointment_status_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `office_id` (`office_id`),
  KEY `patient_id` (`patient_id`),
  KEY `appointment_status_id` (`appointment_status_id`),
  CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`office_id`) REFERENCES `offices` (`id`),
  CONSTRAINT `appointments_ibfk_2` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`id`),
  CONSTRAINT `appointments_ibfk_3` FOREIGN KEY (`appointment_status_id`) REFERENCES `appointment_status` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `distances`
--

DROP TABLE IF EXISTS `distances`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `distances` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `patient_id` varchar(60) NOT NULL,
  `office_id` varchar(60) NOT NULL,
  `distance_text` varchar(60) NOT NULL,
  `distance` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `patient_id` (`patient_id`),
  KEY `office_id` (`office_id`),
  CONSTRAINT `distances_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`id`),
  CONSTRAINT `distances_ibfk_2` FOREIGN KEY (`office_id`) REFERENCES `offices` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `distances`
--

LOCK TABLES `distances` WRITE;
/*!40000 ALTER TABLE `distances` DISABLE KEYS */;
INSERT INTO `distances` VALUES ('45c14812-5655-45f0-84b8-158345a1c6da','2022-11-27 17:06:36','2022-11-27 17:06:36','bc6e7260-ea18-437c-83fb-51a9e113d42c','1234d3ec-231a-421b-b389-50f2114f3ce9','0 km',0),('5053dac5-120d-43e3-bc2e-dcdb5feaa764','2022-11-27 17:06:36','2022-11-27 17:06:36','bc6e7260-ea18-437c-83fb-51a9e113d42c','b189fb88-a0d4-488b-a389-4fe85d1cb1ae','0 km',0),('9de82809-66c7-4e9c-a0f2-8887302e0182','2022-11-27 17:06:36','2022-11-27 17:06:36','bc6e7260-ea18-437c-83fb-51a9e113d42c','cbc0ec6d-8ed0-4384-a1cf-447793c6f27b','0 km',0);
/*!40000 ALTER TABLE `distances` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_specialization`
--

DROP TABLE IF EXISTS `doctor_specialization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor_specialization` (
  `doctor_id` varchar(60) NOT NULL,
  `specialization_id` varchar(60) NOT NULL,
  PRIMARY KEY (`doctor_id`,`specialization_id`),
  KEY `specialization_id` (`specialization_id`),
  CONSTRAINT `doctor_specialization_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`),
  CONSTRAINT `doctor_specialization_ibfk_2` FOREIGN KEY (`specialization_id`) REFERENCES `specializations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_specialization`
--

LOCK TABLES `doctor_specialization` WRITE;
/*!40000 ALTER TABLE `doctor_specialization` DISABLE KEYS */;
INSERT INTO `doctor_specialization` VALUES ('7e598c38-36bd-41e5-9ac7-fee0b3265718','3dd0c344-c327-4826-93c3-ee2949826655'),('fe76efff-5c62-4080-9d14-4c3b9d7659bc','3dd0c344-c327-4826-93c3-ee2949826655'),('c303b501-a8d3-44d6-bc1c-5be6a97bbe3a','c676b194-e03c-4f19-8d98-c51ca8a5964b');
/*!40000 ALTER TABLE `doctor_specialization` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctors`
--

DROP TABLE IF EXISTS `doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctors` (
  `id` varchar(60) NOT NULL,
  `doctor_info` varchar(1024) NOT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`),
  CONSTRAINT `doctors_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctors`
--

LOCK TABLES `doctors` WRITE;
/*!40000 ALTER TABLE `doctors` DISABLE KEYS */;
INSERT INTO `doctors` VALUES ('7e598c38-36bd-41e5-9ac7-fee0b3265718','Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dolorem, omnis aperiam architecto aliquam perspiciatis porro dolores quod cum, esse libero fuga nobis unde ea odio.',NULL),('c303b501-a8d3-44d6-bc1c-5be6a97bbe3a','Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dolorem, omnis aperiam architecto aliquam perspiciatis porro dolores quod cum, esse libero fuga nobis unde ea odio.',NULL),('fe76efff-5c62-4080-9d14-4c3b9d7659bc','Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dolorem, omnis aperiam architecto aliquam perspiciatis porro dolores quod cum, esse libero fuga nobis unde ea odio.',NULL);
/*!40000 ALTER TABLE `doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hospital_affiliation`
--

DROP TABLE IF EXISTS `hospital_affiliation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hospital_affiliation` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `hospital_name` varchar(100) NOT NULL,
  `hospital_phone_number` varchar(100) NOT NULL,
  `hospital_country` varchar(100) NOT NULL,
  `hospital_city` varchar(100) NOT NULL,
  `hospital_address` varchar(100) NOT NULL,
  `hospital_type` varchar(100) NOT NULL,
  `doctor_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `hospital_affiliation_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospital_affiliation`
--

LOCK TABLES `hospital_affiliation` WRITE;
/*!40000 ALTER TABLE `hospital_affiliation` DISABLE KEYS */;
INSERT INTO `hospital_affiliation` VALUES ('79176e29-2a7f-46f2-b083-332d88cc9163','2022-11-23 16:50:32','2022-11-23 16:50:33','hospital2','99999999','H2country','H2city','H2address','Public','7e598c38-36bd-41e5-9ac7-fee0b3265718'),('8388c291-306c-442e-996e-fe5fd670a3e1','2022-11-23 16:51:19','2022-11-23 16:51:19','hospital3','99999999','H3country','H3city','H3address','Public','c303b501-a8d3-44d6-bc1c-5be6a97bbe3a'),('f7386701-9a52-48cb-bf6c-b13273c4e753','2022-11-23 16:49:30','2022-11-23 16:49:33','hospital1','99999999','H1country','H1city','H1address','Public','fe76efff-5c62-4080-9d14-4c3b9d7659bc');
/*!40000 ALTER TABLE `hospital_affiliation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `office_hours`
--

DROP TABLE IF EXISTS `office_hours`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `office_hours` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `day_of_the_week` varchar(10) NOT NULL,
  `start_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `end_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `availability` varchar(10) NOT NULL,
  `office_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `office_id` (`office_id`),
  CONSTRAINT `office_hours_ibfk_1` FOREIGN KEY (`office_id`) REFERENCES `offices` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `office_hours`
--

LOCK TABLES `office_hours` WRITE;
/*!40000 ALTER TABLE `office_hours` DISABLE KEYS */;
INSERT INTO `office_hours` VALUES ('0101326e-96d2-4ebd-ad87-eea5dc6a70aa','2022-11-27 16:56:03','2022-11-27 16:56:03','Thursday','2022-11-24 15:00:00','2022-11-24 16:00:00','Yes','cbc0ec6d-8ed0-4384-a1cf-447793c6f27b'),('0e13448a-6506-42f4-85b5-b6c6d6ca0348','2022-11-23 16:55:09','2022-11-23 16:55:11','Thursday','2022-11-24 08:00:00','2022-11-24 09:00:00','Yes','cbc0ec6d-8ed0-4384-a1cf-447793c6f27b'),('17ab4bc9-c3f5-4576-b3d0-1c7c851603d3','2022-11-27 16:59:09','2022-11-27 16:59:09','Thursday','2022-11-24 13:00:00','2022-11-24 14:00:00','Yes','1234d3ec-231a-421b-b389-50f2114f3ce9'),('1fa40a6c-5bb9-45e3-ab12-9720dc0f3a64','2022-11-27 16:59:09','2022-11-27 16:59:09','Thursday','2022-11-24 14:00:00','2022-11-24 15:00:00','Yes','1234d3ec-231a-421b-b389-50f2114f3ce9'),('2d9cfc81-1d18-47d7-b3fd-247f7ca781a5','2022-11-27 16:58:20','2022-11-27 16:58:20','Thursday','2022-11-24 12:00:00','2022-11-24 13:00:00','Yes','b189fb88-a0d4-488b-a389-4fe85d1cb1ae'),('4c8545ff-cbc6-4f7c-a4b6-4091f85bf777','2022-11-27 16:56:03','2022-11-27 16:56:03','Thursday','2022-11-24 09:00:00','2022-11-24 10:00:00','Yes','cbc0ec6d-8ed0-4384-a1cf-447793c6f27b'),('4e4f0adf-2700-4957-a412-710567aee42d','2022-11-27 16:56:03','2022-11-27 16:56:03','Thursday','2022-11-24 11:00:00','2022-11-24 12:00:00','Yes','cbc0ec6d-8ed0-4384-a1cf-447793c6f27b'),('4eea26e6-3a12-4ddd-9737-6bd6cce919be','2022-11-27 16:58:20','2022-11-27 16:58:20','Thursday','2022-11-24 14:00:00','2022-11-24 15:00:00','Yes','b189fb88-a0d4-488b-a389-4fe85d1cb1ae'),('506d17ce-470e-44fc-950b-a5224a1c67d8','2022-11-23 16:55:31','2022-11-23 16:55:33','Thursday','2022-11-24 08:00:00','2022-11-24 09:00:00','Yes','1234d3ec-231a-421b-b389-50f2114f3ce9'),('5126d255-1a08-40b0-b3cb-66265a0bb840','2022-11-27 16:59:09','2022-11-27 16:59:13','Thursday','2022-11-24 17:00:00','2022-11-24 18:00:00','Yes','1234d3ec-231a-421b-b389-50f2114f3ce9'),('5a82d509-3742-4fc0-8dc4-229e9bd75ebc','2022-11-27 16:59:09','2022-11-27 16:59:09','Thursday','2022-11-24 15:00:00','2022-11-24 16:00:00','Yes','1234d3ec-231a-421b-b389-50f2114f3ce9'),('6be50c39-ab3b-4e8c-a45a-454592a124b9','2022-11-27 16:59:09','2022-11-27 16:59:09','Thursday','2022-11-24 10:00:00','2022-11-24 11:00:00','Yes','1234d3ec-231a-421b-b389-50f2114f3ce9'),('74d61258-31b6-4da9-afd5-7da16ce5c6b4','2022-11-27 16:56:03','2022-11-27 16:56:03','Thursday','2022-11-24 13:00:00','2022-11-24 14:00:00','Yes','cbc0ec6d-8ed0-4384-a1cf-447793c6f27b'),('75b6971e-2174-452b-a86f-9ca2e9a1cfa3','2022-11-27 16:59:09','2022-11-27 16:59:09','Thursday','2022-11-24 09:00:00','2022-11-24 10:00:00','Yes','1234d3ec-231a-421b-b389-50f2114f3ce9'),('7bc553e3-3a13-484f-93aa-9a8a07c54f20','2022-11-27 16:59:09','2022-11-27 16:59:09','Thursday','2022-11-24 11:00:00','2022-11-24 12:00:00','Yes','1234d3ec-231a-421b-b389-50f2114f3ce9'),('880a1b44-9be3-4232-9795-8b3696da57f2','2022-11-27 16:56:03','2022-11-27 16:56:03','Thursday','2022-11-24 16:00:00','2022-11-24 17:00:00','Yes','cbc0ec6d-8ed0-4384-a1cf-447793c6f27b'),('906c2a94-80fa-4441-ad9c-ffa1f497488c','2022-11-27 16:58:20','2022-11-27 16:58:23','Thursday','2022-11-24 17:00:00','2022-11-24 18:00:00','Yes','b189fb88-a0d4-488b-a389-4fe85d1cb1ae'),('97376739-509c-460e-9d39-a524c9ec2dd5','2022-11-27 16:58:20','2022-11-27 16:58:20','Thursday','2022-11-24 10:00:00','2022-11-24 11:00:00','Yes','b189fb88-a0d4-488b-a389-4fe85d1cb1ae'),('a0816c3b-8fdd-4d0e-8e83-ef1674b235dc','2022-11-23 16:55:19','2022-11-23 16:55:21','Thursday','2022-11-24 08:00:00','2022-11-24 09:00:00','Yes','b189fb88-a0d4-488b-a389-4fe85d1cb1ae'),('a1c5db4d-6a8e-4216-b879-88d08cb9b539','2022-11-27 16:59:09','2022-11-27 16:59:09','Thursday','2022-11-24 12:00:00','2022-11-24 13:00:00','Yes','1234d3ec-231a-421b-b389-50f2114f3ce9'),('a84d71d8-b635-44bd-a04f-33a382c65b1e','2022-11-27 16:59:09','2022-11-27 16:59:09','Thursday','2022-11-24 16:00:00','2022-11-24 17:00:00','Yes','1234d3ec-231a-421b-b389-50f2114f3ce9'),('bb650106-632d-4946-a20e-6443d2afe08a','2022-11-27 16:58:20','2022-11-27 16:58:20','Thursday','2022-11-24 11:00:00','2022-11-24 12:00:00','Yes','b189fb88-a0d4-488b-a389-4fe85d1cb1ae'),('c8d92d2e-8c80-4984-abda-11bf373beac6','2022-11-27 16:58:20','2022-11-27 16:58:20','Thursday','2022-11-24 16:00:00','2022-11-24 17:00:00','Yes','b189fb88-a0d4-488b-a389-4fe85d1cb1ae'),('d154526c-ff30-4dfb-8971-82d90baa32ae','2022-11-27 16:56:03','2022-11-27 16:56:07','Thursday','2022-11-24 17:00:00','2022-11-24 18:00:00','Yes','cbc0ec6d-8ed0-4384-a1cf-447793c6f27b'),('d5d22312-93f5-4a3c-a767-43d9f3c3b4be','2022-11-27 16:58:20','2022-11-27 16:58:20','Thursday','2022-11-24 15:00:00','2022-11-24 16:00:00','Yes','b189fb88-a0d4-488b-a389-4fe85d1cb1ae'),('de00e093-fd9f-480d-a1f8-7d20159fec8d','2022-11-27 16:56:03','2022-11-27 16:56:03','Thursday','2022-11-24 14:00:00','2022-11-24 15:00:00','Yes','cbc0ec6d-8ed0-4384-a1cf-447793c6f27b'),('ec9d4214-3589-46d0-8e1e-edae657f33cc','2022-11-27 16:56:03','2022-11-27 16:56:03','Thursday','2022-11-24 12:00:00','2022-11-24 13:00:00','Yes','cbc0ec6d-8ed0-4384-a1cf-447793c6f27b'),('f9c97159-0b99-4299-ac57-6ae965f5e135','2022-11-27 16:56:03','2022-11-27 16:56:03','Thursday','2022-11-24 10:00:00','2022-11-24 11:00:00','Yes','cbc0ec6d-8ed0-4384-a1cf-447793c6f27b'),('fbb7d2b4-9b05-4688-8fff-727dea468f4b','2022-11-27 16:58:20','2022-11-27 16:58:20','Thursday','2022-11-24 09:00:00','2022-11-24 10:00:00','Yes','b189fb88-a0d4-488b-a389-4fe85d1cb1ae'),('fd8766da-5f8b-432f-8bc4-11e7bf127d46','2022-11-27 16:58:20','2022-11-27 16:58:20','Thursday','2022-11-24 13:00:00','2022-11-24 14:00:00','Yes','b189fb88-a0d4-488b-a389-4fe85d1cb1ae');
/*!40000 ALTER TABLE `office_hours` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `offices`
--

DROP TABLE IF EXISTS `offices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `offices` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `country` varchar(128) NOT NULL,
  `city` varchar(128) NOT NULL,
  `office_address` varchar(128) NOT NULL,
  `info` varchar(1024) NOT NULL,
  `hospital_id` varchar(60) NOT NULL,
  `doctor_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `doctor_id` (`doctor_id`),
  KEY `hospital_id` (`hospital_id`),
  CONSTRAINT `offices_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`),
  CONSTRAINT `offices_ibfk_2` FOREIGN KEY (`hospital_id`) REFERENCES `hospital_affiliation` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `offices`
--

LOCK TABLES `offices` WRITE;
/*!40000 ALTER TABLE `offices` DISABLE KEYS */;
INSERT INTO `offices` VALUES ('1234d3ec-231a-421b-b389-50f2114f3ce9','2022-11-23 16:54:23','2022-11-23 16:54:24',6.17969,1.21263,'O3country','O3city','O3address','O3info','8388c291-306c-442e-996e-fe5fd670a3e1','c303b501-a8d3-44d6-bc1c-5be6a97bbe3a'),('b189fb88-a0d4-488b-a389-4fe85d1cb1ae','2022-11-23 16:53:29','2022-11-23 16:53:30',6.14394,1.20831,'O2country','O2city','O2address','O2info','79176e29-2a7f-46f2-b083-332d88cc9163','7e598c38-36bd-41e5-9ac7-fee0b3265718'),('cbc0ec6d-8ed0-4384-a1cf-447793c6f27b','2022-11-23 16:52:42','2022-11-23 16:52:44',6.27969,1.11263,'O1country','O1city','O1address','O1info','f7386701-9a52-48cb-bf6c-b13273c4e753','fe76efff-5c62-4080-9d14-4c3b9d7659bc');
/*!40000 ALTER TABLE `offices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patients` (
  `id` varchar(60) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `country` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`),
  CONSTRAINT `patients_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` VALUES ('bc6e7260-ea18-437c-83fb-51a9e113d42c',0,0,'Samoa','Samoa city','Samoa city Samoa',NULL);
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `patient_id` varchar(60) NOT NULL,
  `doctor_id` varchar(60) NOT NULL,
  `review_info` varchar(1024) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `patient_id` (`patient_id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`id`),
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `specializations`
--

DROP TABLE IF EXISTS `specializations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `specializations` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `specialization_name` varchar(100) NOT NULL,
  `sp_info` varchar(1024) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specializations`
--

LOCK TABLES `specializations` WRITE;
/*!40000 ALTER TABLE `specializations` DISABLE KEYS */;
INSERT INTO `specializations` VALUES ('3dd0c344-c327-4826-93c3-ee2949826655','2022-11-25 20:36:08','2022-11-25 20:36:11','Generalist','Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dolorem, omnis aperiam architecto aliquam perspiciatis porro dolores quod cum, esse libero fuga nobis unde ea odio. Eius voluptate quidem at maiores!'),('5c33ea58-b285-4c39-8748-14c97115c077','2022-11-25 20:37:23','2022-11-25 20:37:25','Pediatricien','Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dolorem, omnis aperiam architecto aliquam perspiciatis porro dolores quod cum, esse libero fuga nobis unde ea odio. Eius voluptate quidem at maiores!'),('c676b194-e03c-4f19-8d98-c51ca8a5964b','2022-11-25 20:36:44','2022-11-25 20:36:46','Psycologist','Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dolorem, omnis aperiam architecto aliquam perspiciatis porro dolores quod cum, esse libero fuga nobis unde ea odio. Eius voluptate quidem at maiores!');
/*!40000 ALTER TABLE `specializations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL,
  `phone_number` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `birthdate` datetime NOT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('7e598c38-36bd-41e5-9ac7-fee0b3265718','2022-11-23 16:46:04','2022-11-23 16:46:05','doctor2','doctor2@gmail.com','d9e6762dd1c8eaf6d61b3c6192fc408d4d6d5f1176d0c29169bc24e71c3f274ad27fcd5811b313d681f7e55ec02d73d499c95455b6b5bb503acf574fba8ffe85','123456789','Maryam','Umar','female','2022-11-23 16:46:04','doctor'),('bc6e7260-ea18-437c-83fb-51a9e113d42c','2022-11-27 17:06:36','2022-11-27 17:06:36','patient1','patient1@gmail.com','d9e6762dd1c8eaf6d61b3c6192fc408d4d6d5f1176d0c29169bc24e71c3f274ad27fcd5811b313d681f7e55ec02d73d499c95455b6b5bb503acf574fba8ffe85','99999999','Musa','Jalloh','male','2022-11-09 00:00:00','patient'),('c303b501-a8d3-44d6-bc1c-5be6a97bbe3a','2022-11-23 16:47:34','2022-11-23 16:47:35','doctor3','doctor3@gmail.com','d9e6762dd1c8eaf6d61b3c6192fc408d4d6d5f1176d0c29169bc24e71c3f274ad27fcd5811b313d681f7e55ec02d73d499c95455b6b5bb503acf574fba8ffe85','123456789','Jacques','Koffi','Male','2022-11-23 16:47:34','doctor'),('fe76efff-5c62-4080-9d14-4c3b9d7659bc','2022-11-23 16:44:58','2022-11-23 16:45:00','doctor1','doctor1@gmail.com','d9e6762dd1c8eaf6d61b3c6192fc408d4d6d5f1176d0c29169bc24e71c3f274ad27fcd5811b313d681f7e55ec02d73d499c95455b6b5bb503acf574fba8ffe85','123456789','John','Doe','male','2022-11-23 16:44:58','doctor');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-27 17:07:12
