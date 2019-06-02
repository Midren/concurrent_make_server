create table dbs.loging(
 `id` int not null auto_increment,
 `user_name` varchar(255) not null
);

create table dbs.compiler (
  `id` int not null auto_increment,
  `compiler_name` varchar(255) not null
);

create table dbs.os (
  `id` int not null auto_increment,
  `os_name` varchar(255) not null
);

create table dbs.computer (
  `id` int not null auto_increment,
  `compiler_id` int not null,
  `os_id` int not null,
  foreign key (compiler_id) references dbs.compiler(id),
  foreign key (os_id) references dbs.os(id),
  `compiler_version` float not null
);

create table dbs.node (
	`id` int not null auto_increment,
	`user_name_id` int not null,
	foreign key (user_name_id) references dbs.logins(id),
    primary key (id)
    );