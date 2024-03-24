'''9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.'''

import privileges_admin_module as PAM

user1 = PAM.Admin('Antonio', 'Rivera Martinez', 'Asheville', 'NC', 49)
user1.privileges.show_privileges()