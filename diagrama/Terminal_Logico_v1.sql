-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Terminal_Rodoviario
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Terminal_Rodoviario
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Terminal_Rodoviario` DEFAULT CHARACTER SET utf8 ;
USE `Terminal_Rodoviario` ;

-- -----------------------------------------------------
-- Table `Terminal_Rodoviario`.`Passageiro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Terminal_Rodoviario`.`Passageiro` (
  `CPF` VARCHAR(15) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `Passageiro_Bilhete` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`CPF`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Terminal_Rodoviario`.`Funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Terminal_Rodoviario`.`Funcionario` (
  `CPF` VARCHAR(15) NOT NULL,
  `funcao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`CPF`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Terminal_Rodoviario`.`Onibus`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Terminal_Rodoviario`.`Onibus` (
  `placa` VARCHAR(10) NOT NULL,
  `destino` VARCHAR(45) NOT NULL,
  `assentos_comerciais` VARCHAR(40) NOT NULL,
  `assentos_executivos` VARCHAR(40) NOT NULL,
  `Onibus_Funcionario` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`placa`),
  INDEX `FK_Escala_idx` (`Onibus_Funcionario` ASC) VISIBLE,
  CONSTRAINT `FK_Escala`
    FOREIGN KEY (`Onibus_Funcionario`)
    REFERENCES `Terminal_Rodoviario`.`Funcionario` (`CPF`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Terminal_Rodoviario`.`Empresa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Terminal_Rodoviario`.`Empresa` (
  `CNPJ` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `veiculos` VARCHAR(45) NOT NULL,
  `Empresa_Onibus` VARCHAR(45) NOT NULL,
  `Empresa_Funcionario` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`CNPJ`),
  INDEX `FK_Possui_idx` (`Empresa_Onibus` ASC) VISIBLE,
  INDEX `FK_Emprega_idx` (`Empresa_Funcionario` ASC) VISIBLE,
  CONSTRAINT `FK_Possui`
    FOREIGN KEY (`Empresa_Onibus`)
    REFERENCES `Terminal_Rodoviario`.`Onibus` (`placa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_Emprega`
    FOREIGN KEY (`Empresa_Funcionario`)
    REFERENCES `Terminal_Rodoviario`.`Funcionario` (`CPF`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Terminal_Rodoviario`.`Viagem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Terminal_Rodoviario`.`Viagem` (
  `ID_viagem` VARCHAR(10) NOT NULL,
  `origem` VARCHAR(45) NOT NULL,
  `chassi` VARCHAR(45) NOT NULL,
  `preço` DECIMAL(7,2) NOT NULL,
  `datahora_ida` DATETIME NOT NULL,
  `datahora_volta` DATETIME NOT NULL,
  `Viagem_Onibus` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID_viagem`),
  INDEX `FK_Realiza_idx` (`Viagem_Onibus` ASC) VISIBLE,
  CONSTRAINT `FK_Realiza`
    FOREIGN KEY (`Viagem_Onibus`)
    REFERENCES `Terminal_Rodoviario`.`Onibus` (`placa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Terminal_Rodoviario`.`Passageiro_Contato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Terminal_Rodoviario`.`Passageiro_Contato` (
  `CPF` VARCHAR(45) NOT NULL,
  `Contato` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`CPF`),
  CONSTRAINT `FK_Contato`
    FOREIGN KEY (`CPF`)
    REFERENCES `Terminal_Rodoviario`.`Passageiro` (`CPF`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Terminal_Rodoviario`.`Empresa_Endereço`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Terminal_Rodoviario`.`Empresa_Endereço` (
  `CNPJ` VARCHAR(45) NOT NULL,
  `endereço` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`CNPJ`),
  CONSTRAINT `FK_EmpresaEndereço`
    FOREIGN KEY (`CNPJ`)
    REFERENCES `Terminal_Rodoviario`.`Empresa` (`CNPJ`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Terminal_Rodoviario`.`Empresa_Contato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Terminal_Rodoviario`.`Empresa_Contato` (
  `CNPJ` VARCHAR(45) NOT NULL,
  `Contato` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`CNPJ`),
  CONSTRAINT `FK_Contato`
    FOREIGN KEY (`CNPJ`)
    REFERENCES `Terminal_Rodoviario`.`Empresa` (`CNPJ`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Terminal_Rodoviario`.`Contrata`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Terminal_Rodoviario`.`Contrata` (
  `Empresa_CNPJ` VARCHAR(45) NOT NULL,
  `Passageiro_CPF` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`Empresa_CNPJ`, `Passageiro_CPF`),
  INDEX `fk_Empresa_has_Passageiro_Passageiro1_idx` (`Passageiro_CPF` ASC) VISIBLE,
  INDEX `fk_Empresa_has_Passageiro_Empresa1_idx` (`Empresa_CNPJ` ASC) VISIBLE,
  CONSTRAINT `fk_Empresa_has_Passageiro_Empresa1`
    FOREIGN KEY (`Empresa_CNPJ`)
    REFERENCES `Terminal_Rodoviario`.`Empresa` (`CNPJ`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Empresa_has_Passageiro_Passageiro1`
    FOREIGN KEY (`Passageiro_CPF`)
    REFERENCES `Terminal_Rodoviario`.`Passageiro` (`CPF`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Terminal_Rodoviario`.`Bilhete`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Terminal_Rodoviario`.`Bilhete` (
  `ID` VARCHAR(15) NOT NULL,
  `Classe` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_Passageiro_has_Viagem_Passageiro1_idx` (`ID` ASC) VISIBLE,
  CONSTRAINT `fk_Passageiro_has_Viagem_Passageiro1`
    FOREIGN KEY (`ID`)
    REFERENCES `Terminal_Rodoviario`.`Passageiro` (`CPF`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_Bilhete`
    FOREIGN KEY (`ID`)
    REFERENCES `Terminal_Rodoviario`.`Viagem` (`ID_viagem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
