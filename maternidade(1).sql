-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 06-Dez-2024 às 23:59
-- Versão do servidor: 10.4.28-MariaDB
-- versão do PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `maternidade`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `bebe`
--

CREATE TABLE `bebe` (
  `codigo` int(11) NOT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `altura` float DEFAULT NULL,
  `data` date DEFAULT NULL,
  `cpf` int(11) DEFAULT NULL,
  `codigo_eq` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `bebe`
--

INSERT INTO `bebe` (`codigo`, `nome`, `peso`, `altura`, `data`, `cpf`, `codigo_eq`) VALUES
(4545, 'Lais da Silva', 2.5, 50, '2024-12-06', 1111, 101),
(5454, 'Pedro da Siva', 3.5, 55, '2024-12-06', 1111, 101);

-- --------------------------------------------------------

--
-- Estrutura da tabela `equipe_medica`
--

CREATE TABLE `equipe_medica` (
  `codigo_eq` int(11) NOT NULL,
  `nome_eq` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `equipe_medica`
--

INSERT INTO `equipe_medica` (`codigo_eq`, `nome_eq`) VALUES
(101, 'Alfa'),
(222, 'Beta'),
(333, 'Teta');

-- --------------------------------------------------------

--
-- Estrutura da tabela `mae`
--

CREATE TABLE `mae` (
  `cpf` int(11) NOT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `endereco` varchar(100) DEFAULT NULL,
  `telefone` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `mae`
--

INSERT INTO `mae` (`cpf`, `nome`, `endereco`, `telefone`) VALUES
(1111, 'Maria do Carmo', 'Rua das Flores', '9998-1110'),
(2222, 'Ana Maria', 'Rua XYZ', '99458-1110');

-- --------------------------------------------------------

--
-- Estrutura da tabela `profissional`
--

CREATE TABLE `profissional` (
  `matricula` int(11) NOT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `especialidade` varchar(20) DEFAULT NULL,
  `telefone` varchar(11) DEFAULT NULL,
  `crm` int(11) DEFAULT NULL,
  `codigo_eq` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `profissional`
--

INSERT INTO `profissional` (`matricula`, `nome`, `especialidade`, `telefone`, `crm`, `codigo_eq`) VALUES
(1000, 'Eduardo Souza', 'Obstetra', '99845-5211', 1010, 101),
(1010, 'Eduardo Souza', 'Obstetra', '99845-5211', 1010, 101),
(2000, 'Paulo Costa', 'Instrumentador', '99845-5211', 0, 101),
(3000, 'Joana Pires', 'Pediatra', '98946-5271', 1011, 101);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `bebe`
--
ALTER TABLE `bebe`
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `cpf` (`cpf`),
  ADD KEY `codigo_eq` (`codigo_eq`);

--
-- Índices para tabela `equipe_medica`
--
ALTER TABLE `equipe_medica`
  ADD PRIMARY KEY (`codigo_eq`);

--
-- Índices para tabela `mae`
--
ALTER TABLE `mae`
  ADD PRIMARY KEY (`cpf`);

--
-- Índices para tabela `profissional`
--
ALTER TABLE `profissional`
  ADD PRIMARY KEY (`matricula`),
  ADD KEY `codigo_eq` (`codigo_eq`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `bebe`
--
ALTER TABLE `bebe`
  ADD CONSTRAINT `bebe_ibfk_1` FOREIGN KEY (`cpf`) REFERENCES `mae` (`cpf`),
  ADD CONSTRAINT `bebe_ibfk_2` FOREIGN KEY (`codigo_eq`) REFERENCES `equipe_medica` (`codigo_eq`);

--
-- Limitadores para a tabela `profissional`
--
ALTER TABLE `profissional`
  ADD CONSTRAINT `profissional_ibfk_1` FOREIGN KEY (`codigo_eq`) REFERENCES `equipe_medica` (`codigo_eq`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;