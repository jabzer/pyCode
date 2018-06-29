create table if not exists tasks(
  id integer primary key autoincrement ,
  name char(100) not null ,
  closed bool not null
);

insert or ignore into tasks (id,name,closed) values (0,'开始 pyramid',0);
insert or ignore into tasks (id,name,closed) values (1,'快速入门',0);
insert or ignore into tasks (id,name,closed) values (2,'开门',0);