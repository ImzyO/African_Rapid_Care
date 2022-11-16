-- MySQL dump  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: arc_dev_db
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- @block Drop database
DROP DATABASE IF EXISTS arc_dev_db2;

-- Create database + user if doesn't exist
CREATE DATABASE IF NOT EXISTS arc_dev_db2;
CREATE USER IF NOT EXISTS 'arc_dev2'@'localhost' IDENTIFIED BY 'arc_dev_pwd';
GRANT ALL PRIVILEGES ON `arc_dev_db2`.* TO 'arc_dev2'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'arc_dev2'@'localhost';
FLUSH PRIVILEGES;

USE arc_dev_db2;

-- 
-- @block Table structure for table `users`
--
 DROP TABLE IF EXISTS users;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

-- @block Table structure for table `patients`
--
DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patients` (
    `id` varchar(60) NOT NULL,
--    `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
--    `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
--    `user_id` varchar(60) NOT NULL,
    `latitude` float NOT NULL,
    `longitude` float NOT NULL,
    `country` varchar(100) NOT NULL,
    `city` varchar(100) NOT NULL,
    `address` varchar(200) NOT NULL,
--    `user_name` varchar(100) NOT NULL,
--    `email` varchar(100) NOT NULL,
--    `password` varchar(200) NOT NULL,
--    `phone_number` varchar(100) NOT NULL,
--    `first_name` varchar(100) NOT NULL,
--    `last_name` varchar(100) NOT NULL,
--    `gender` varchar(100) NOT NULL,
--    `birthdate` datetime NOT NULL,
    PRIMARY KEY (`id`),
    KEY `id` (`id`),
--    KEY `created_at` (`created_at`),
--    KEY `updated_at` (`updated_at`),
    CONSTRAINT `patients_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`)
--    CONSTRAINT `patients_ibfk_2` FOREIGN KEY (`created_at`) REFERENCES `users` (`created_at`),
--    CONSTRAINT `patients_ibfk_3` FOREIGN KEY (`updated_at`) REFERENCES `users` (`updated_at`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- @block Table structure for table `reviews`
--
DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reviews` (
    `id` varchar(60) NOT NULL,
--    `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
--    `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
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
-- @block Table structure for table `specializations`
--
DROP TABLE IF EXISTS `specializations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
-- @block Table structure for table `doctor_specialization`
--
DROP TABLE IF EXISTS `doctor_specialization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `doctor_specialization` (
    `doctor_id` varchar(60) NOT NULL,
    `specialization_id` varchar(60) NOT NULL,
    `ds_info` varchar(1024) NOT NULL,
    PRIMARY KEY (`doctor_id`, `specialization_id`),
    KEY `specialization_id` (`specialization_id`),
    CONSTRAINT `doctor_specialization_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`),
    CONSTRAINT `doctor_specialization_ibfk_2` FOREIGN KEY (`specialization_id`) REFERENCES `specializations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- @block Table structure for table `doctors`
--
DROP TABLE IF EXISTS `doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `doctors` (
    `id` varchar(60) NOT NULL,
--    `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
--    `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
--    `userd_id` varchar(60) NOT NULL,
    `doctor_info` varchar(1024) NOT NULL,
--    `user_name` varchar(100) NOT NULL,
--    `email` varchar(100) NOT NULL,
--    `password` varchar(200) NOT NULL,
--    `phone_number` varchar(100) NOT NULL,
--    `first_name` varchar(100) NOT NULL,
--    `last_name` varchar(100) NOT NULL,
--    `gender` varchar(100) NOT NULL,
--    `birthdate` datetime NOT NULL,
    PRIMARY KEY (`id`),
    KEY `id` (`id`),
--    KEY `created_at` (`created_at`),
--    KEY `updated_at` (`updated_at`),
    CONSTRAINT `doctors_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`)
--    CONSTRAINT `doctors_ibfk_2` FOREIGN KEY (`created_at`) REFERENCES `users` (`created_at`),
--    CONSTRAINT `doctors_ibfk_3` FOREIGN KEY (`updated_at`) REFERENCES `users` (`updated_at`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

-- @block Table structure for table `hospital_affiliation`
--
DROP TABLE IF EXISTS `hospital_affiliation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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


-- @block Table structure for table `offices`
--
DROP TABLE IF EXISTS `offices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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

-- @block Table structure for table `office_hours`
--
DROP TABLE IF EXISTS `office_hours`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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

-- @block Table structure for table `appointments`
--
DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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


-- @block Table structure for table `appointment_status`
--
DROP TABLE IF EXISTS `appointment_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `appointment_status` (
    `id` varchar(60) NOT NULL,
    `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,

    `appointment_status` varchar(128) NOT NULL,
    `patient_id` varchar(60) NOT NULL,
    `appointment_status_id` varchar(60) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-14  15:41:40