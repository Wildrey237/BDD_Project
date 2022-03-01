-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le : mar. 01 mars 2022 à 09:01
-- Version du serveur :  10.3.34-MariaDB-0ubuntu0.20.04.1
-- Version de PHP : 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `HappyFly`
--

-- --------------------------------------------------------

--
-- Structure de la table `Circuit`
--

CREATE TABLE `Circuit` (
  `ID` int(11) NOT NULL,
  `descriptif` text DEFAULT NULL,
  `dateDepart` date DEFAULT NULL,
  `nbrPlacesDisponibles` int(3) DEFAULT NULL,
  `dureeEnHeure` int(3) DEFAULT NULL,
  `prixInscription` float DEFAULT NULL,
  `villeDepartID` int(11) NOT NULL,
  `villeArriveeID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `Circuit`
--

INSERT INTO `Circuit` (`ID`, `descriptif`, `dateDepart`, `nbrPlacesDisponibles`, `dureeEnHeure`, `prixInscription`, `villeDepartID`, `villeArriveeID`) VALUES
(1, 'Visitez les lieux les plus connus de l\'Espagne.', '2022-04-25', 90, 70, 250, 1, 5),
(2, 'Visitez les lieux les plus connus de France ! ', '2022-05-20', 70, 48, 175, 6, 10),
(3, 'Venez visiter l\'Angleterre grâce à notre circuit touristique.', '2022-06-15', 45, 35, 125, 11, 15),
(4, 'L\'Italie vous émerveillera de part ses paysages et monuments.', '2022-07-11', 75, 30, 110, 16, 20),
(5, 'Visitez l\'Allemagne, Pays rempli d\'histoires.', '2022-03-07', 55, 30, 160, 21, 25),
(6, 'Découvrez la Turquie, Pays vivant de part son histoire.', '2022-07-07', 85, 96, 400, 26, 30),
(7, 'Visitez l\'Autriche, berceau des grands musiciens classiques, ainsi que ses magnifiques montagnes.', '2022-07-26', 45, 30, 250, 31, 35),
(8, 'Découvrez la Suisse, pays magnifique et impressionnant.', '2022-08-09', 65, 24, 110, 36, 40),
(9, 'Vivez la mythologie grecque en découvrant la Grèce.', '2022-08-18', 70, 168, 300, 41, 45),
(10, 'Découvrez la gastronomie et les activités sportives du Pays-Bas', '2022-09-07', 35, 24, 75, 46, 50);

-- --------------------------------------------------------

--
-- Structure de la table `Compte`
--

CREATE TABLE `Compte` (
  `compteID` int(11) NOT NULL,
  `nom` varchar(50) DEFAULT NULL,
  `prenom` varchar(50) DEFAULT NULL,
  `mdp` varchar(50) DEFAULT NULL,
  `DateDeNaissance` date DEFAULT NULL,
  `role` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `Compte`
--

INSERT INTO `Compte` (`compteID`, `nom`, `prenom`, `mdp`, `DateDeNaissance`, `role`) VALUES
(1, 'Client', 'Jevisite', 'clientjevisite', '2003-09-29', 0),
(2, 'Administrateur', 'root', 'root', '2003-06-29', 1);

-- --------------------------------------------------------

--
-- Structure de la table `Etape`
--

CREATE TABLE `Etape` (
  `ordre` int(2) NOT NULL,
  `dateEtape` date DEFAULT NULL,
  `dureeEnMinute` int(4) DEFAULT NULL,
  `circuit_ID` int(11) NOT NULL,
  `LieuDeVisite_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `Etape`
--

INSERT INTO `Etape` (`ordre`, `dateEtape`, `dureeEnMinute`, `circuit_ID`, `LieuDeVisite_ID`) VALUES
(1, '2022-04-25', 60, 1, 1),
(2, '2022-04-25', 120, 1, 2),
(3, '2022-04-26', 30, 1, 3),
(4, '2022-04-27', 150, 1, 4),
(5, '2022-04-27', 35, 1, 5),
(6, '2022-05-20', 45, 2, 6),
(7, '2022-05-20', 70, 2, 7),
(8, '2022-05-20', 80, 2, 8),
(9, '2022-05-21', 120, 2, 9),
(10, '2022-05-21', 35, 2, 10),
(11, '2022-06-15', 180, 3, 11),
(12, '2022-06-15', 40, 3, 12),
(13, '2022-06-16', 35, 3, 13),
(14, '2022-06-16', 80, 3, 14),
(15, '2022-06-16', 35, 3, 15),
(16, '2022-07-11', 55, 4, 16),
(17, '2022-07-11', 70, 4, 17),
(18, '2022-07-11', 55, 4, 18),
(19, '2022-07-12', 90, 4, 19),
(20, '2022-07-12', 20, 4, 20),
(21, '2022-03-07', 60, 5, 21),
(22, '2022-03-07', 75, 5, 22),
(23, '2022-03-08', 40, 5, 23),
(24, '2022-03-08', 75, 5, 24),
(25, '2022-03-08', 50, 5, 25),
(26, '2022-07-07', 35, 6, 26),
(27, '2022-07-07', 65, 6, 27),
(28, '2022-07-08', 80, 6, 28),
(29, '2022-07-09', 90, 6, 29),
(30, '2022-07-09', 60, 6, 30),
(31, '2022-07-26', 30, 7, 31),
(32, '2022-07-26', 40, 7, 32),
(33, '2022-07-26', 60, 7, 33),
(34, '2022-07-26', 75, 7, 34),
(35, '2022-07-27', 25, 7, 35),
(36, '2022-08-09', 50, 8, 36),
(37, '2022-08-09', 35, 8, 37),
(38, '2022-08-09', 40, 8, 38),
(39, '2022-08-09', 75, 8, 39),
(40, '2022-08-09', 80, 8, 40),
(41, '2022-08-18', 70, 9, 41),
(42, '2022-08-19', 90, 9, 42),
(43, '2022-08-20', 120, 9, 43),
(44, '2022-08-21', 135, 9, 44),
(45, '2022-08-22', 50, 9, 45),
(46, '2022-09-07', 70, 10, 46),
(47, '2022-09-07', 80, 10, 47),
(48, '2022-09-07', 95, 10, 48),
(49, '2022-09-07', 105, 10, 49),
(50, '2022-09-07', 110, 10, 50);

-- --------------------------------------------------------

--
-- Structure de la table `LieuDeVisite`
--

CREATE TABLE `LieuDeVisite` (
  `ID` int(11) NOT NULL,
  `label` varchar(100) DEFAULT NULL,
  `descriptif` text DEFAULT NULL,
  `prixVisite` float DEFAULT NULL,
  `Ville_villeID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `LieuDeVisite`
--

INSERT INTO `LieuDeVisite` (`ID`, `label`, `descriptif`, `prixVisite`, `Ville_villeID`) VALUES
(1, 'L’Alhambra', 'Vous cherchez quoi faire à Grenade ? L’Alhambra, palais le plus fréquenté d’Espagne, est sans doute le lieu le plus emblématique à visiter dans la ville. Déclarée Patrimoine Mondial de l’Unesco en 1984, la cité fait partie des 21 candidats finalistes pour devenir l’une des 7 nouvelles merveilles du monde.\r\n\r\nEmblématique de l’apogée de l’art andalou, la Torre de Comares fut construite sur l’initiative de Yusuf I. Le célèbre Patio de los Leones vit le jour sur la volonté de Mohamed V.', 19, 1),
(2, 'La vieille ville de San Sebastian', 'Visiter San Sebastian commence obligatoirement par une visite de la vieille ville, quartier typique qui vous invite à la promenade. Arpentez ses ruelles, admirez ses édifices emblématiques, vibrez au cœur du vrai centre social de la ville. Vous découvrirez également les deux plus anciennes églises de la ville, l’église Saint-Vincent et la Basilique Santa Maria, ainsi que sa célèbre place de la Constitution, située au cœur de ce petit village dans la ville.', 0, 2),
(3, 'L’Alcazaba', 'Édifié au XI ème siècle par les Maures, ce palais servait à la fois de lieu de résidence aux gouverneurs musulmans et de forteresse pour protéger et défendre la ville et la province, des catholiques.\r\n\r\nLe site est extrêmement bien conservé et entretenu. Lors de votre visite, vous pourrez découvrir des cours intérieures, des patios, des fontaines et des jardins somptueux. Construit sur une colline surplombant Malaga, le lieu offre en plus une vue dégagée sur la mer et le port en contrebas.', 2.1, 3),
(4, 'La Sagrada Familia', 'La Sagrada Familia est l’œuvre la plus réputée de l’architecte catalan Gaudí, qui façonna le paysage architectural Barcelonais jusqu’à sa mort en 1926. Classée au patrimoine mondial de l’UNESCO, c’est le monument le plus visité d’Espagne et le plus emblématique de Barcelone.\r\n\r\nVous comprendrez d’ailleurs immédiatement pourquoi en arrivant devant la Basilique: le bâtiment est impressionnant, avec tous ses détails et références catholiques. Son style architectural unique mélangeant art gothique et Art Nouveau vous en mettra plein à les yeux!', 33, 4),
(5, 'La Cathédrale Sainte-Marie de Tolède', 'La Cathédrale Sainte-Marie de Tolède est un édifice de style gothique dont la construction a débuté en 1226 pour s’achever au XVème siècle. Elle renferme de magnifiques chefs-d’œuvre dont des peintures de Goya, Caravage, Velázquez et du Greco. La façade gothique de ce symbole de la puissance de l’Espagne catholique est à voir absolument.', 10, 5),
(6, 'La Basilique Notre-Dame de la Garde', 'Surnommé la Bonne Mère, ce monument emblématique de Marseille, construit sur une colline à 150 mètres d’altitude, domine toute la cité phocéenne. Depuis l’esplanade de Notre-Dame, vous pourrez contempler un panorama à 360° sur la ville et la mer.\r\n\r\nHaut lieu de pèlerinage depuis 800 ans, la basilique est dédiée à Marie, dont la statue qui se trouve au sommet du clocher est la protectrice de la ville et des marins. Recouverte d’or, elle pèse plus de 9700 kg!', 0, 6),
(7, 'Place de la Bourse et son Miroir d’Eau', ' La place de la bourse (ancienne Place royale) construite au XVIIIe siècle est un lieu emblématique de la vie bordelaise. Elle se situe sur les quais de Bordeaux en face du célèbre miroir d’eau où vous pourrez vous rafraîchir en cas de forte chaleur. Cette place qui prend la forme d’un arc de cercle est un bon exemple du développement de Bordeaux au XVIIIe siècle lorsque la ville s’est enrichie grâce au commerce triangulaire et à la traite négrière. Vous pourrez y admirer l’architecture de Bordeaux qui est une architecture traditionnelle de l’architecte Gabriel qui est classée aux monuments historique et qui abrite aujourd’hui le Tribunal de commerce et la Chambre de commerce et de l’industrie.', 0, 7),
(8, 'Le Vieux Lyon', 'Datant pour une partie de l’époque Médiévale et pour l’autre de la période Renaissance, le Vieux Lyon (également appelé quartier Saint-Jean) est un des quartiers historiques de la ville.\r\n\r\nClassé au patrimoine de l’UNESCO, ce quartier surprend par ses petites rues pavées, sa grande Cathédrale et ses musées atypiques.', 0, 8),
(9, 'La place du Capitole', 'Lieu d’intérêt emblématique de la ville, la place est située en plein centre historique de Toulouse. Petite particularité, cette immense place (12 000 m² tout de même!) ne possède aucune construction. Elle est uniquement réservée aux piétons et accueille un grand marché quotidien.\r\n\r\nSur le sol de la place, vous pourrez admirer le symbole de Toulouse, la croix occitane.', 0, 9),
(10, 'La Place de la Comédie et l’Esplanade Charles de Gaulle\r\n', 'La Place de la Comédie avec sa Fontaine des Trois Grâces, une fontaine datant de 1776, est le cœur de la ville intra-muros. Sur le côté sud-ouest de la place se dresse le théâtre (Opéra Comédie). De là, les grands boulevards rayonnent vers la vieille ville (la plus grande partie de la zone piétonne), que l’on appelle l’Écusson (voir ci-dessous). Dans le quartier, se nichent, cachés derrière des façades anodines, de superbes hôtels particuliers. Habituellement fermés au public, certaines cours de ces demeures du 17 et 18ème siècles peuvent être découvertes grâce à des visites guidées.', 0, 10),
(11, 'The Beatles Story', 'Cet endroit est le rendez-vous incontournable pour tous les amoureux du célèbre groupe de rock anglais. Ouvert depuis 1990, ce lieu magique vous replonge dans la légende de John, Paul, George et Ringo grâce à divers supports et souvenirs collectors. Situé dans le quartier de l’Albert Dock, le Beatles Story propose aussi de monter dans un bus spécial pour faire le Magical Mystery Tour. Le musée est ouvert tous les jours. L’été, il est ouvert de 9h à 19h et l’hiver de 10h à 18h. Le prix d’entrée pour un adulte est de 17.80€.', 17.8, 11),
(12, 'Castlefield', 'Ce quartier légèrement excentré abrite l’ancien fort romain de Mamucium, reconstitué et qui a donné son nom à la ville. Pourvue de nombreux canaux, de bars au bord de l’eau et de jolis espaces verts, Castelfield est un endroit décontracté et très convivial. Vous y découvrirez également de nombreuses maisons de style victorien.\r\n\r\nVous pourrez aussi admirer le Bridgewater Canal, le premier canal industriel au monde construit en 1764 ! On y trouve également le Castlefield Bowl, qui accueille des concerts de rock et de musique classique, et le centre artistique HOME. Ce dernier propose des projections de films, des expositions et pièces de théâtre. Pour démarrer votre visite de Manchester, ne manquez surtout pas ce quartier culturel et animé, de jour comme de nuit !', 0, 12),
(13, 'Le British National Railway Museum', 'Le National Railway Museum, est un musée ferroviaire situé à York, il fait partie du groupement des musées des sciences et de l\'industrie de Grande-Bretagne. Le musée est ouvert depuis 1975, en regroupant dans un même endroit différentes collections de matériel roulant préservé dès le XIXᵉ siècle.', 0, 13),
(14, 'Le Château d’Édimbourg', 'La première chose à faire à Édimbourg tombe sous le sens ! Haut perché sur la colline escarpée de Castle Rock, comme s’il surveillait la cité juste en-dessous, le château d’Edimbourg est l’attraction incontournable à faire à Edimbourg. Au sein de ses murs de pierres noircies se trouvent les Honours of Scotland (les bijoux et joyaux de la couronne d’Ecosse) enfermés au cœur du Palais royal où sont accrochés aux murs des tableaux historiques. On trouve aussi au sein du château les appartements de la Reine Marie Ire d’Écosse, le Great Hall (une salle du 15ème siècle où le parlement écossais s’est réunit jusqu’en 1639) et le Mons Meg, un canon de siège géant du 15ème siècle construit à Mons en 1449. Tout tourne autour de la place d’armes sur laquelle se dresse le Scottish National War Memorial.', 20, 14),
(15, 'Le centre-ville d’Oxford', 'Visiter Oxford commence obligatoirement par une visite du centre-ville, quartier typique et pittoresque qui vous invite à la promenade. Flânez dans ses rues piétonnes, et découvrez le « Covered market » (marché couvert). Ce vieux marché couvert fondé en 1770 abrite de nombreux petits magasins et des échoppes pour se restaurer. Vous vous laisserez complètement emporter par l’ambiance de la ville. En savoir plus sur la visite de la ville d’Oxford et de son université.\r\n\r\n', 0, 15),
(16, 'Le Dôme de Florence', 'Le site le plus populaire à visiter à Florence est certainement son Duomo (cathédrale), la Cattedrale de Santa Maria del Fiore. La construction de l’immense cathédrale gothique a débuté en 1296, a été consacrée en 1436, et peut aujourd’hui accueillir jusqu’à 20 000 personnes.\r\n\r\nSon extérieur, fait de marbre vert, rose et blanc, possède plusieurs portes élaborées et des statues qui méritent le coup d’oeil. A l’intérieur, le dôme de Brunelleschi est un véritable chef-d’œuvre. L’entrée dans la cathédrale est gratuite mais prenez un billet pour gravir les 463 marches jusqu’à son sommet (comptez 10€) : la vue en vaut le coup. Ce ticket vous permettra en outre de monter à la tour Campanile de Giotto, d’entrer au Baptistère Saint-Jean, et à la crypte Santa Reparata.', 10, 16),
(17, 'Le Colisée', 'Monument extraordinaire qui accueillait les combats de gladiateurs autrefois, le Colisée remonte à l’an 72. L’amphithéâtre Flavien (c’est aussi comme ça qu’on l’appelle) a été construit pour accueillir un public pouvant aller jusqu’à 50.000 personnes. Le site, qui fut le théâtre de nombreuses morts horribles, est un lieu historique et une étape incontournable pour tout amateur d’Histoire et d’architecture. Très prisé par les touristes, le Colisée défit le temps et a notamment inspiré le film Gladiator. Il est aussi considéré comme le plus grand amphithéâtre de l’Empire romain au monde : sans nul doute donc, il est une référence pour visiter Rome.', 12, 17),
(18, 'La place Saint Marc', 'La Place Saint-Marc est certainement l’endroit le plus emblématique à visiter à Venise : c’est la place principale de la ville, un lieu de rencontres et de rendez-vous pour les habitants mais aussi pour les touristes.\r\n\r\nC’est véritablement la plaque tournante de Venise : vous serez obligés d’y passer pour aller visiter la Basilique Saint-Marc, le palais des Doges, mais aussi le Campanile de Saint-Marc et tous les autres monuments incontournables.', 27.5, 18),
(19, 'Piazza del Campo', 'Place principale de la ville, ce lieu est connu à la fois pour sa forme incurvée et son sol penché à l’image d’un amphithéâtre mais aussi pour l’attraction la plus populaire de Sienne, le Palio. Cette course de chevaux a lieu deux fois par an, en juillet et en août, et oppose les 17 contrades de la ville.\r\n\r\nSur la Piazza del Campo ne manquez pas la visite du Palazzo Pubblico et de sa tour. Grimpez tout en haut de la Torre del Mangia afin de profiter d’un point de vue imprenable sur la ville.', 0, 19),
(20, 'La maison de Juliette', 'Comment séjourner à Vérone sans voir le fameux balcon de Juliette ? Cette maison fut construite au 12e siècle et elle appartenait à la famille Dal Cappello (d’où le rapprochement avec une certaine famille Capulet). Ce balcon est une véritable attraction touristique : tous les amoureux s’y précipitent et les murs sont chargés de billets doux afin de laisser une empreinte de son passage. L’accès à la cour est gratuit mais la visite de la maison est payante. A noter que vous pouvez toucher la statue de Juliette dans la cour, notamment son sein gauche (dont la couleur a changé tellement il a été poli par les millions de touristes) car il serait un signe de fécondité et d’amour éternel. Un véritable lieu romantique pour voler un baiser à votre moitié, n’est-ce pas ?', 6, 20),
(21, 'La vieille ville de Bamberg', 'Il n\'y a pas de meilleur endroit pour commencer une visite à pied de la vieille ville de Bamberg qu\'à Obere Brücke, le pont supérieur réservé aux piétons. De là, vous serez récompensé par de superbes vues sur Klein-Venedig, ou «Petite Venise», avecses vieilles maisons de pêcheurs pittoresques.\r\n\r\nMais ce pour quoi vous êtes vraiment ici, c\'est le superbe vieil hôtel de ville Altes Rathaus. Perché un peu précaire au milieu du pont, c\'est l\'un des monuments historiques les plus photographiés de Bavière. Alors qu\'un hôtel de ville y était situé.dès 1386, la structure existante a été reconstruite entre 1744 et 1756 pour desservir à la fois la Bürgerstadt et la ville épiscopale.', 0, 21),
(22, 'Hambourg et son centre-ville', 'Pour ceux qui aiment faire du shopping, le « innenstadt » d’Hambourg se laisse découvrir en 3 heures de temps au maximum : les rues principales sont la Mönckebergstrasse et la Spitalerstrasse. Dans ces deux artères, vous trouverez tout ce dont vous rêvez (et avez peut-être besoin) comme des vêtements, des chaussures, des disques, du multimédias, de la décoration. A 10 mn de ces deux rues se trouvent des boutiques de créateurs au merveilleux Alsterpassage avec ses magasins de luxe.', 0, 22),
(23, 'Le Mur de Berlin', 'C’est l’une des attractions touristiques incontournables à faire à Berlin ! Vous ne pouvez pas passer à côté de ce monument. Et c’est compréhensible quand on connaît l’histoire (assez récente) du Mur de Berlin. Ce dernier fut en grande partie détruit de juin à novembre 1990 mais un tronçon est resté debout. La partie la plus célèbre est celle le long de la Spree (rivière), appelée la East Side Gallery, pour ses œuvres peintes sur le Mur.\r\n\r\nSi vous souhaitez en apprendre plus sur l’histoire du Mur et sur cette période de division, il y a non loin de là le Gedenkstätte Berliner Mauer, ou Mémorial du Mur de Berlin, juste en face d’un parc commémoratif.', 12.5, 23),
(24, 'Fuggerei', 'La Fuggerei est le plus vieil ensemble de logements sociaux du monde existant encore. Elle a été créée dans le faubourg de Jakob - la Jakobervorstadt - à Augsbourg, en Allemagne, par Jacob Fugger dit le Riche ((de) Jakob Fugger von der Lilie) de la richissime famille des Fugger en 1516. La charte de fondation date de 1521. Elle continue de fonctionner pratiquement à l\'identique jusqu\'à nos jours.', 0, 24),
(25, 'La résidence de Würzburg', 'La résidence de Wurtzbourg, pouvant être abrégée en la Résidence, est une construction de style baroque située sur la Residenzplatz au centre de la ville de Wurtzbourg, chef-lieu de la Basse-Franconie. Elle a été occupée par les princes-évêques. Le château compte parmi les plus belles réalisations du baroque tardif de l\'Allemagne du Sud et peut être considéré, par son importance dans l\'architecture européenne, au même titre que le château de Schönbrunn à Vienne ou celui de Versailles. L\'Unesco a élevé le bâtiment en 1981 au titre de Patrimoine mondial de l\'humanité.', 9, 25),
(26, 'Une croisière sur le Bosphore', 'Un voyage à Istanbul n’est pas complet sans une croisière sur le Bosphore. Cela offre non seulement un bel aperçu de la ville, mais les rives à la fois européenne et asiatique du célèbre chenal ont beaucoup à offrir : un grand nombre d’anciens palais et demeures s’y trouvent, ainsi que la Tour de Léandre.\r\n\r\nConcernant la durée de la croisière, vous avez le choix entre une visite courte (si vous êtes pressés) ou longue (sur une journée). L’été, la croisière au coucher du soleil est très demandée. Par conséquent, pensez à réserver à l’avance si vous souhaitez faire la croisière sur ce créneau horaire.', 20, 26),
(27, 'Musée Mevlana', 'Le musée Mevlâna, situé à Konya, en Turquie, est le mausolée de Jalal ad-Din Muhammad Rumi, un mystique soufi persan. C\'était aussi la loge des derviches de l\'ordre Mevlevi, mieux connue sous le nom de derviches tourneurs.', 0, 27),
(28, 'La vieille ville', 'Destination touristique phare de la Turquie méditerranéenne, Antalya rime également avec tourisme de masse et consommation ostentatoire des touristes aisés et fortunés. Malgré tout, la ville a su conserver son charme historique et son authenticité. La vieille ville d’Antalya notamment, a gardé ses lettres de noblesse. Nommé Kaleici, le vieux quartier est un dédale de rues piétonnes et commerçantes. Kaleici est construit sur un éperon rocheux au flanc d’une falaise abrupte, en contrebas de laquelle se trouve un ancien port, réhabilité aujourd’hui en port de plaisance moderne. C’est évidemment l’incontournable pour tout le monde venant visiter Antalya.', 0, 28),
(29, 'Tokatlı Canyon', 'Si vous aimez faire des promenades dans la nature et qui aiment grimper quelques marches, vous devriez absolument aller dans cet hôtel magnifique Canyon. Il ne vous donnera l\'impression d\'être dans un Wild West. La richesse naturelle des chutes d\'eau, des arbres et des fleurs sont tout simplement magnifiques. Vous pouvez prendre un pique-nique ou y apprécier un en-cas dans le restaurant à l\'intérieur du canyon.', 0, 29),
(30, 'Parc national de Göreme et sites rupestres de Cappadoce', 'Göreme, située parmi les formations rocheuses en cheminées de fée, est une ville de Cappadoce, une région historique de Turquie.', 35, 30),
(31, 'Le palais de la Hofburg', 'S’il y a bien une chose à faire à Vienne c’est de visiter le Palais de la Hofburg. Rien ne symbolise la culture et le patrimoine de l’Autriche plus que son palais impérial de la Hofburg. Les Habsbourg ont habité ici pendant plus de six siècles, du premier empereur (Rodolphe Ier en 1273) au dernier (Charles Ier en 1918).\r\n\r\nLa Hofburg doit sa taille et sa diversité architecturale à la surenchère de chacun de ses nouveaux empereurs : de nouvelles sections ont été ajoutées au fil des siècles comme l’aile Léopold de style baroque, l’aile de la chancellerie du 18ème siècle, l’aile d’Amalia et la Burgkapelle (Chapelle Royale).', 15, 31),
(32, 'Bregenz Festival', 'Le festival de Brégence1 ou festival de Bregenz est un festival culturel qui a lieu tous les étés à Brégence, la capitale de la province autrichienne du Vorarlberg.\r\n\r\nLe festival est notamment réputé pour sa grande scène flottante sur le bord du lac de Constance, ses décors de scène de grande ampleur et son acoustique particulière, le Bregenz Open Acoustics, obtenue grâce à une technique de diffusion sonore directionnelle développée pour ce lieu.\r\n\r\nL\'orchestre résident du festival est l\'orchestre symphonique de Vienne.', 0, 32),
(33, 'Le Schlossberg', 'Rien de tel pour se faire une première impression de Graz que d’aller l’observer d’en haut ! Direction le Schlossberg, une colline culminant à 123 mètres et surplombant la ville.', 0, 33),
(34, 'La Forteresse de Hohensalzburg', 'C’est le symbole par excellence de la ville : son édification a débuté au 11ème siècle et s’est terminée au 16ème siècle. C’est aujourd’hui l’un des châteaux forts les mieux conservés de toute l’Europe. Facilement identifiable depuis le cœur de Salzbourg, il domine la ville à plus de 100 m d’altitude et la vue est tout simplement magnifique. De multiples pièces peuvent être visitées comme le salon doré, la salle aux piliers en marbre, la chambre des tortures, le donjon, les terribles oubliettes…', 0, 34),
(35, 'Grüner See', 'Le Grüner See est un lac de Styrie en Autriche, près du hameau de Tragöß dans la commune de Tragöss-Sankt Katharein. Le lac est entouré par les montagnes du massif du Hochschwab et ses forêts. Il a la particularité de ne se remplir que pendant quelques semaines au moment de la fonte des neiges et de se vider en quelques jours. Le reste de l\'année, c\'est un parc naturel. Le nom du lac provient de son eau vert émeraude.', 0, 35),
(36, 'Le Musée Olympique', 'Visiter Lausanne implique nécessairement de faire un arrêt au Musée Olympique. La ville suisse est en effet étroitement liée aux Jeux, ce qui lui a même valu le titre de Capitale Olympique il y a quelques années. Elle abrite le siège du Comité International des Jeux Olympiques et s’apprête à accueillir les jeux d’hiver de 2020.\r\n\r\nLe Musée Olympique classé bien culturel d’importance national depuis 1995, permet de se replonger dans l’histoire du sport à travers les expositions permanentes et temporaires présentées sur 3 étages. A l’extérieur, le parc olympique met en avant diverses installations sportives comme de vraies œuvres d’art, le tout couronné par un panorama exceptionnel donnant sur le lac Léman et les Alpes. La visite est payante mais séduira petits et grands grâce aux activités interactives et aux films qui sont projetés.', 19.17, 36),
(37, 'Balade dans le centre-ville historique de Neuchâtel', 'Tournée vers le lac éponyme et dominée par son château, la capitale du canton possède le charme d’une cité millénaire. Vous découvrirez la ville, son architecture et ses monuments au cours de vos déambulations hasardeuses ou lors de balades commentées par des guides passionnants.\r\n\r\nSi elle fait preuve de dynamisme, la cité semble figée dans le temps. Vous apprécierez la beauté des façades du XVIIIe siècle de la place des Halles, l’étonnante tour de Diesse et son horloge rouge du XIe siècle ainsi que l’état de préservation de son château du Xe siècle.', 0, 37),
(38, 'Le musée d\'histoire de Berne et le musée d\'Einstein', 'Les deux sont rassemblés dans un seul et même bâtiment, un ancien château de style néogothique datant de 1894. Le Musée d’Histoire de Berne se trouve être l’un des principaux musées suisses, consacrés à l’histoire et la civilisation. On peut y découvrir divers objets de collection relatant l’histoire, l’archéologie et l’ethnographie de la région. En tout, on y trouve 500 000 éléments retraçant l’âge de la pierre à l’époque actuelle. Quant au Musée d’Einstein, il relate la vie et le parcours professionnel de ce célébrissime physicien.', 17.25, 38),
(39, 'Le Kapellbrücke', 'Le pont dit Kapellbrücke, est un pont de bois et une attraction touristique majeure de la ville de Lucerne en Suisse. Ce pont couvert médiéval est, avec le Cervin, l\'un des sujets les plus photographiés en Suisse. Le nom de Kapellbrücke s\'explique par la proximité de la chapelle Saint-Pierre. Construit en 1333, il est reconstruit en 1994 après un incendie.', 0, 39),
(40, 'Bibliothèque de l\'abbaye de Saint-Gall', 'La bibliothèque de l\'abbaye de Saint-Gall, fondée au VIIIᵉ siècle, et reconstruite au XVIIIᵉ siècle en style baroque rococo, est une des plus importantes et anciennes bibliothèques monastiques du monde.', 17.25, 40),
(41, 'L’acropole d’Athènes et le Parthénon', 'Inscrit au patrimoine mondial de l’UNESCO, dominant la capitale, c’est l’un des sites antique les plus visités de toute la Grèce et l’attraction touristique principale d’Athènes.\r\n\r\nÉrigé au sommet du site, le Parthénon est le monument le plus connu de l’Acropole. Construit au V ème siècle avant J.C, en même temps qu’une bonne partie des autres bâtiments à l’initiative de Périclès, le temple est dédié à Athéna. Il est considéré comme le premier édifice de l’Antiquité à avoir été construit entièrement en marbre et pèse environ 20 000 tonnes.', 20, 41),
(42, 'Le front de mer et la Tour Blanche\r\n', 'Pour découvrir et visiter Thessalonique, rien de tel qu’une première balade en front de mer, entre la Tour Blanche et le port. Ancienne fortification byzantine réhabilitée en musée, la Tour Blanche est un emblématique de la ville.\r\n\r\nSous l’Empire Ottoman, elle était une prison et un lieu d’exécutions et de torture : de nombreux rebelles janissaires y furent décapités, sur ordre du sultan Mahmud II. Construite au 13ème siècle, elle faisait partie du mur d’enceinte, détruit en 1866.', 4, 42),
(43, 'Órmos Ammoúdi', 'La baie d\'Amoudi est une baie de l\'île grecque de Santorin. La caractéristique est située dans les hautes falaises volcaniques de l\'ouest de Santorin en dessous de la ville d\'Oia.', 0, 43),
(44, 'La ville moderne de Corinthe', 'Hormis quelques musées et restaurants où goûter aux spécialités grecques, il y a peu d’attractions à voir dans la nouvelle ville de Corinthe. La ville moderne est la cité qui fut reconstruite après le séisme dévastateur de 1858, à 3 kilomètres de l’ancienne ville. Que faire à la nouvelle ville de Corinthe ? Le musée du folklore de Corinthe retrace l’histoire de la ville, et expose vêtements, bijoux, d’anciennes broderies et des outils traditionnels. Si l’on dit qu’il y a peut de choses à faire à Corinthe, flâner le long du petit port et aux terrasses de cafés typiques comporte néanmoins son petit charme.', 0, 44),
(45, 'La vieille ville de Rhodes', 'Avec 49 541 habitants (2011), la ville de Rhodes est la capitale de l’île éponyme, fondée en 408 avant J-C. Sa vieille ville médiévale, enfermée dans l’enceinte de hauts remparts construits du temps des Chevaliers de Rhodes, est classée sur la liste des monuments du patrimoine mondial de l’UNESCO depuis 1988.\r\n\r\nElle est considérée comme la plus grande ville fortifiée d’Europe, et la mieux conservée. Érigée entre 1309 et 1523, c’est une vieille cité byzantine entièrement piétonne, où vous pourrez contempler un mariage singulier de styles d’architectures historiques : influences gothiques dans la haute-ville et style ottoman en basse-ville. C’est l’incontournable d’un séjour pour visiter Rhodes.', 0, 45),
(46, 'Musée Prinsenhof', 'Visiter Delft, c’est aussi, un peu, remonter le temps. Le très beau bâtiment, situé sur la jolie place Agathaplein, était à l’origine un couvent réservé aux femmes jusqu’au XVIème siècle. Puis Guillaume d’Orange, à l’origine de l’indépendance et de la création de la République hollandaise, a réaménagé une partie pour en faire sa résidence.\r\n\r\nSinon, le Prinsenhof rassemble des collections qui racontent l’histoire de l’indépendance des Pays-Bas, de la faïence de Delft et de l’âge d’or du pays au XVIIème siècle.', 5, 46),
(47, 'Les parcs d’attractions à Drievliet et Duinrell', 'Vous voyagez en famille et vous vous demandez que faire à La Haye ? Les parcs d’attractions bien sûr ! Les nombreuses attractions spectaculaires du parc de Duinrell ne manqueront pas de ravir petits et grands. Toupie aquatique, Splash, Mad Mill… Fous rires garantis ! Vous pouvez même dormir sur place dans les bungalows que propose le site, ou bien au camping. Le parc Drievliet est quant à lui riche en attractions décoiffantes, qu’il s’agisse de manèges ou de toboggans, mais propose également de nombreuses activités pour les plus jeunes.', 26, 47),
(48, 'Croisière sur les canaux', 'C’est assez cliché certes, mais vous devez vraiment faire un tour le long des canaux si vous venez visiter Amsterdam. La croisière se déroule tout en souplesse et en détente, en passant devant des bâtiments pittoresques et sous de vieux ponts de pierre. Plusieurs croisières à Amsterdam sont possibles : de la simple balade à la croisière de luxe. En général, une croisière dure environ 1 à 2 heures.\r\n\r\nSi vous avez aimé naviguer sur ces canaux, vous pouvez poursuivre votre voyage en visitant le musée des canaux qui retrace l’histoire d’Amsterdam et vous explique l’utilité et la fabrication des canaux.', 14, 48),
(49, 'Museum Giethoorn \'t Olde Maat Uus', 'Musée vivant reconstituant village fermier historique avec acteurs costumés, boutique de cadeaux et café.', 6.5, 49),
(50, 'moulins à vent de Kinderdijk', 'Les moulins à vent de Kinderdijk sont un groupe de 19 moulins à vent monumentaux dans le polder d\'Alblasserwaard, dans la province de la Hollande méridionale, aux Pays-Bas.', 0, 50);

-- --------------------------------------------------------

--
-- Structure de la table `Media`
--

CREATE TABLE `Media` (
  `mediaID` int(11) NOT NULL,
  `LieuDeVisite_ID` int(11) NOT NULL,
  `images` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `ModificationCompte`
--

CREATE TABLE `ModificationCompte` (
  `ModificateurCompteID` int(11) NOT NULL,
  `CompteModifiéID` int(11) NOT NULL,
  `dateModification` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `Pays`
--

CREATE TABLE `Pays` (
  `paysID` int(11) NOT NULL,
  `nom` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `Pays`
--

INSERT INTO `Pays` (`paysID`, `nom`) VALUES
(1, 'Espagne'),
(2, 'France'),
(3, 'Royaume-Uni'),
(4, 'Italie'),
(5, 'Allemagne'),
(6, 'Turquie'),
(7, 'Autriche'),
(8, 'Suisse'),
(9, 'Grèce'),
(10, 'Pays-Bas');

-- --------------------------------------------------------

--
-- Structure de la table `Reservation`
--

CREATE TABLE `Reservation` (
  `reservationID` int(11) NOT NULL,
  `compteReservationID` int(11) NOT NULL,
  `CircuitID` int(11) NOT NULL,
  `dateReservation` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `Ville`
--

CREATE TABLE `Ville` (
  `villeID` int(11) NOT NULL,
  `nom` varchar(60) DEFAULT NULL,
  `Pays_paysID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `Ville`
--

INSERT INTO `Ville` (`villeID`, `nom`, `Pays_paysID`) VALUES
(1, 'Grenade', 1),
(2, 'Saint-Sébastien', 1),
(3, 'Malaga', 1),
(4, 'Barcelone', 1),
(5, 'Tolède', 1),
(6, 'Marseille', 2),
(7, 'Bordeaux', 2),
(8, 'Lyon', 2),
(9, 'Toulouse', 2),
(10, 'Montpellier', 2),
(11, 'Liverpool', 3),
(12, 'Manchester', 3),
(13, 'York', 3),
(14, 'Édimbourg', 3),
(15, 'Oxford', 3),
(16, 'Florence', 4),
(17, 'Rome', 4),
(18, 'Venise', 4),
(19, 'Sienne', 4),
(20, 'Vérone', 4),
(21, 'Bamberg', 5),
(22, 'Hambourg', 5),
(23, 'Berlin', 5),
(24, 'Augsbourg ', 5),
(25, 'Wurtzbourg', 5),
(26, 'Istanbul', 6),
(27, 'Konya', 6),
(28, 'Antalya', 6),
(29, 'Safranbolu', 6),
(30, 'Göreme', 6),
(31, 'Vienne', 7),
(32, 'Bregenz', 7),
(33, 'Graz', 7),
(34, 'Salzburg', 7),
(35, 'Eisenerz', 7),
(36, 'Lausanne', 8),
(37, 'Neuchâtel', 8),
(38, 'Berne', 8),
(39, 'Lucerne', 8),
(40, 'Saint-Gall', 8),
(41, 'Athènes', 9),
(42, 'Thessalonique', 9),
(43, 'Oia', 9),
(44, 'Corinthe', 9),
(45, 'Rhodes', 9),
(46, 'Delft', 10),
(47, 'La Haye', 10),
(48, 'Amsterdam', 10),
(49, 'Giethoorn', 10),
(50, 'Kinderdijk', 10);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `Circuit`
--
ALTER TABLE `Circuit`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `fk_Circuit_Ville1_idx` (`villeDepartID`),
  ADD KEY `fk_Circuit_Ville2_idx` (`villeArriveeID`);

--
-- Index pour la table `Compte`
--
ALTER TABLE `Compte`
  ADD PRIMARY KEY (`compteID`);

--
-- Index pour la table `Etape`
--
ALTER TABLE `Etape`
  ADD PRIMARY KEY (`circuit_ID`,`LieuDeVisite_ID`,`ordre`),
  ADD KEY `fk_etape_circuit_idx` (`circuit_ID`),
  ADD KEY `fk_Etape_LieuDeVisite1_idx` (`LieuDeVisite_ID`);

--
-- Index pour la table `LieuDeVisite`
--
ALTER TABLE `LieuDeVisite`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `fk_LieuDeVisite_Ville1_idx` (`Ville_villeID`);

--
-- Index pour la table `Media`
--
ALTER TABLE `Media`
  ADD PRIMARY KEY (`mediaID`),
  ADD KEY `fk_Medias_LieuDeVisite1_idx` (`LieuDeVisite_ID`);

--
-- Index pour la table `ModificationCompte`
--
ALTER TABLE `ModificationCompte`
  ADD PRIMARY KEY (`ModificateurCompteID`,`CompteModifiéID`),
  ADD KEY `fk_Compte_has_Compte_Compte2_idx` (`CompteModifiéID`),
  ADD KEY `fk_Compte_has_Compte_Compte1_idx` (`ModificateurCompteID`);

--
-- Index pour la table `Pays`
--
ALTER TABLE `Pays`
  ADD PRIMARY KEY (`paysID`);

--
-- Index pour la table `Reservation`
--
ALTER TABLE `Reservation`
  ADD PRIMARY KEY (`reservationID`,`compteReservationID`,`CircuitID`),
  ADD KEY `fk_Reservation_Compte1_idx` (`compteReservationID`),
  ADD KEY `fk_Reservation_Circuit1_idx` (`CircuitID`);

--
-- Index pour la table `Ville`
--
ALTER TABLE `Ville`
  ADD PRIMARY KEY (`villeID`),
  ADD KEY `fk_Ville_Pays1_idx` (`Pays_paysID`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `Circuit`
--
ALTER TABLE `Circuit`
  ADD CONSTRAINT `fk_Circuit_Ville1` FOREIGN KEY (`villeDepartID`) REFERENCES `Ville` (`villeID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Circuit_Ville2` FOREIGN KEY (`villeArriveeID`) REFERENCES `Ville` (`villeID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `Etape`
--
ALTER TABLE `Etape`
  ADD CONSTRAINT `fk_Etape_LieuDeVisite1` FOREIGN KEY (`LieuDeVisite_ID`) REFERENCES `LieuDeVisite` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_etape_circuit` FOREIGN KEY (`circuit_ID`) REFERENCES `Circuit` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `LieuDeVisite`
--
ALTER TABLE `LieuDeVisite`
  ADD CONSTRAINT `fk_LieuDeVisite_Ville1` FOREIGN KEY (`Ville_villeID`) REFERENCES `Ville` (`villeID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `Media`
--
ALTER TABLE `Media`
  ADD CONSTRAINT `fk_Medias_LieuDeVisite1` FOREIGN KEY (`LieuDeVisite_ID`) REFERENCES `LieuDeVisite` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `ModificationCompte`
--
ALTER TABLE `ModificationCompte`
  ADD CONSTRAINT `fk_Compte_has_Compte_Compte1` FOREIGN KEY (`ModificateurCompteID`) REFERENCES `Compte` (`compteID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Compte_has_Compte_Compte2` FOREIGN KEY (`CompteModifiéID`) REFERENCES `Compte` (`compteID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `Reservation`
--
ALTER TABLE `Reservation`
  ADD CONSTRAINT `fk_Reservation_Circuit1` FOREIGN KEY (`CircuitID`) REFERENCES `Circuit` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Reservation_Compte1` FOREIGN KEY (`compteReservationID`) REFERENCES `Compte` (`compteID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `Ville`
--
ALTER TABLE `Ville`
  ADD CONSTRAINT `fk_Ville_Pays1` FOREIGN KEY (`Pays_paysID`) REFERENCES `Pays` (`paysID`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
