-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : jeu. 04 mai 2023 à 11:40
-- Version du serveur : 8.0.27
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `bddbibyaso1`
--

-- --------------------------------------------------------

--
-- Structure de la table `emprunt`
--

DROP TABLE IF EXISTS `emprunt`;
CREATE TABLE IF NOT EXISTS `emprunt` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titreLivre` varchar(255) NOT NULL,
  `nomEmprunteur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `dateEmprunt` date NOT NULL,
  `dateRetour` date NOT NULL,
  `idEmprunteur` int NOT NULL,
  `idLivre` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `em_fk` (`idEmprunteur`),
  KEY `liv_fk` (`idLivre`)
) ENGINE=InnoDB AUTO_INCREMENT=139 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `emprunt`
--

INSERT INTO `emprunt` (`id`, `titreLivre`, `nomEmprunteur`, `dateEmprunt`, `dateRetour`, `idEmprunteur`, `idLivre`) VALUES
(137, 'Les misérables', 'AIT ALLA', '2023-05-31', '2023-06-07', 16, 16),
(138, 'Les fables', 'ZAION', '2023-05-30', '2023-06-13', 17, 17);

-- --------------------------------------------------------

--
-- Structure de la table `emprunteur`
--

DROP TABLE IF EXISTS `emprunteur`;
CREATE TABLE IF NOT EXISTS `emprunteur` (
  `idEmprunteur` int NOT NULL AUTO_INCREMENT,
  `nomEmprunteur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `prenomEmprunteur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `codepostalEmprunteur` int NOT NULL,
  `villeEmprunteur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`idEmprunteur`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `emprunteur`
--

INSERT INTO `emprunteur` (`idEmprunteur`, `nomEmprunteur`, `prenomEmprunteur`, `codepostalEmprunteur`, `villeEmprunteur`) VALUES
(16, 'AIT ALLA', 'Yassine', 75015, 'Paris'),
(17, 'ZAION', 'Sofiane', 75015, 'Paris');

-- --------------------------------------------------------

--
-- Structure de la table `livre`
--

DROP TABLE IF EXISTS `livre`;
CREATE TABLE IF NOT EXISTS `livre` (
  `idLivre` int NOT NULL AUTO_INCREMENT,
  `titreLivre` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `nomAuteur` varchar(255) NOT NULL,
  `prenomAuteur` varchar(255) NOT NULL,
  `nomCollection` varchar(255) NOT NULL,
  `nbrExemplaire` int NOT NULL,
  PRIMARY KEY (`idLivre`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `livre`
--

INSERT INTO `livre` (`idLivre`, `titreLivre`, `nomAuteur`, `prenomAuteur`, `nomCollection`, `nbrExemplaire`) VALUES
(16, 'Les misérables', 'Victor', 'Hugo', 'Hachette', 9),
(17, 'Les fables', 'de la fontaine', 'Jean', 'Hachette', 9);

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

DROP TABLE IF EXISTS `utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `idUtilisateur` int NOT NULL AUTO_INCREMENT,
  `nomUtilisateur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `prenomUtilisateur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `emailUtilisateur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `telephoneUtilisateur` varchar(100) NOT NULL,
  `questionutilisateur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `reponseUtilisateur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `motdepasseUtilisateur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `confirmemotdepasseUtilisateur` varchar(100) NOT NULL,
  PRIMARY KEY (`idUtilisateur`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`idUtilisateur`, `nomUtilisateur`, `prenomUtilisateur`, `emailUtilisateur`, `telephoneUtilisateur`, `questionutilisateur`, `reponseUtilisateur`, `motdepasseUtilisateur`, `confirmemotdepasseUtilisateur`) VALUES
(27, 'Victor', 'Hugo', 'victorhugo@gmail.com', '0652326548', 'Prénom', 'victor', 'Victor@1', 'Victor@1'),
(25, 'AIT ALLA', 'Yassine', 'm.aitallayassine@gmail.com', '0650015167', 'Prénom', 'yassine', '123', '123'),
(26, 'ZAION', 'Sofiane', 'zaionsofiane@gmail.com', '0650015167', 'Prénom', 'sofiane', 'Sofiane@92', 'Sofiane@92');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `emprunt`
--
ALTER TABLE `emprunt`
  ADD CONSTRAINT `em_fk` FOREIGN KEY (`idEmprunteur`) REFERENCES `emprunteur` (`idEmprunteur`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `liv_fk` FOREIGN KEY (`idLivre`) REFERENCES `livre` (`idLivre`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
