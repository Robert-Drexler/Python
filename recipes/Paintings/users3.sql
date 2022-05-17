-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema users2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema users2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `users2` DEFAULT CHARACTER SET utf8 ;
USE `users2` ;

-- -----------------------------------------------------
-- Table `users2`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `users2`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `users2`.`paintings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `users2`.`paintings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `description` VARCHAR(255) NULL,
  `price` INT NULL,
  `artist` VARCHAR(45) NULL,
  `quantity` INT NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now(),
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_paintings_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_paintings_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `users2`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
