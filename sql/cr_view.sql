drop view node_summary;
create view node_summary as
  select node.id,
         user.user_name,
         compiler.compiler_name,
         compiler.major_version,
         compiler.minor_version,
         os.os_name
  from node
         left join user on user.user_name_id = node.login_id
         left join computer on computer.computer_id = node.computer_id
         left join compiler on compiler.compiler_id = computer.compiler_id
         left join os on os.os_id = computer.os_id;