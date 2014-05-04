-- phpMyAdmin SQL Dump
-- version 4.0.9
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 02, 2014 at 04:57 AM
-- Server version: 5.6.14
-- PHP Version: 5.5.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `guarddb`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE IF NOT EXISTS `customers` (
  `UserID` int(11) NOT NULL,
  `PrimarySerialNumber` int(11) NOT NULL,
  `Email Address` text NOT NULL,
  `Password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `plants`
--

CREATE TABLE IF NOT EXISTS `plants` (
  `PlantID` int(11) NOT NULL,
  `DisplayName` varchar(30) NOT NULL,
  `LatinScientificName` varchar(50) NOT NULL,
  `Picture` text NOT NULL,
  KEY `PlantID` (`PlantID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `plants`
--

INSERT INTO `plants` (`PlantID`, `DisplayName`, `LatinScientificName`, `Picture`) VALUES
(2, 'granny smith apple', 'domestica', 'to be added'),
(1, 'grass', 'latin name', 'pic');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `USERID` int(11) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `PrimarySerialNumber` varchar(8) NOT NULL,
  PRIMARY KEY (`USERID`),
  UNIQUE KEY `USERID` (`USERID`),
  UNIQUE KEY `USERID_2` (`USERID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`USERID`, `Email`, `Password`, `PrimarySerialNumber`) VALUES
(1, 'test@gmail.com', 'test', 'JTT1'),
(2, 'jyfong@gmail.com', 'testing', '1HPC'),
(3, 'name@test.com', 'test', '69FC'),
(4, '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `zones`
--

CREATE TABLE IF NOT EXISTS `zones` (
  `ZoneID` int(11) NOT NULL,
  `USERID` int(11) NOT NULL,
  `Points` int(11) NOT NULL,
  `Devices` int(11) NOT NULL,
  PRIMARY KEY (`ZoneID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
