-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 19, 2024 at 05:14 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `5collegestuatiodb`
--

-- --------------------------------------------------------

--
-- Table structure for table `attentb`
--

CREATE TABLE `attentb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Regno` varchar(250) NOT NULL,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Department` varchar(250) NOT NULL,
  `Batch` varchar(250) NOT NULL,
  `Year` varchar(250) NOT NULL,
  `Shift` varchar(250) NOT NULL,
  `Date` date NOT NULL,
  `Attendance` varchar(10) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `attentb`
--


-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `regtb`
--


-- --------------------------------------------------------

--
-- Table structure for table `studenttb`
--

CREATE TABLE `studenttb` (
  `id` bigint(20) NOT NULL auto_increment,
  `RegisterNo` varchar(250) NOT NULL,
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `Department` varchar(250) NOT NULL,
  `Batch` varchar(250) NOT NULL,
  `Year` varchar(250) NOT NULL,
  `Shift` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `studenttb`
--

