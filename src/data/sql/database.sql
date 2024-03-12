-- MYSQL_ROOT_PASSWORD=$(kubectl get secret --namespace mysql mysql-cluster -o jsonpath="{.data.mysql-root-password}" | base64 --decode)
-- kubectl run mysql-cluster-client --rm --tty -i --restart='Never' --image  docker.io/bitnami/mysql:8.0.28-debian-10-r51 --namespace mysql --command -- bash
-- mysql -h mysql-cluster.mysql.svc.cluster.local -uroot -p "$MYSQL_ROOT_PASSWORD"

SHOW DATABASES;
-- CREATE DATABASE discoverydb;
USE discoverydb;
SHOW TABLES;
-- SELECT * FROM pipeline;
-- SELECT * FROM reservation;
-- EXIT;

DROP TABLE IF EXISTS `MECservers`;

-- discoverydb.MECservers definition

CREATE TABLE `MECservers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `lat` varchar(100) DEFAULT NULL,
  `lng` varchar(100) DEFAULT NULL,
  `organization` varchar(100) DEFAULT NULL,
  `resources` json DEFAULT NULL,
  `sb_services` json DEFAULT NULL,
  `props` json DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `MEC-tile`;

-- discoverydb.`MEC-tile` definition

CREATE TABLE `MEC-tile` (
  `mec_id` int(11) NOT NULL,
  `tile` varchar(100) NOT NULL,
  FOREIGN KEY (`mec_id`) REFERENCES MECservers(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `nb_services`;

-- discoverydb.nb_services definition

CREATE TABLE `nb_services` (
  `service_id` int(11) NOT NULL AUTO_INCREMENT,
  `mec_id` int(11) NOT NULL,
  `service_name` varchar(100) NOT NULL,
  `ip` varchar(15) DEFAULT NULL,
  `port` int(11) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `props` json DEFAULT NULL,
  PRIMARY KEY (`service_id`),
  FOREIGN KEY (`mec_id`) REFERENCES MECservers(`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
