import frappe

# def sales_manager_user_permission(doc, method):
#     if doc.custom_added_by:
#         existing_permission = frappe.db.exists("User Permission", {
#             "user": doc.custom_added_by,
#             "allow": "Customer",
#             "for_value": doc.name
#         })

#         if not existing_permission:
#             user_permission = frappe.get_doc({
#                 'doctype': 'User Permission',
#                 'user': doc.custom_added_by,
#                 'allow': 'Customer',
#                 'for_value': doc.name,
#                 'apply_for_all_doctypes': 1 
#             })
#             user_permission.insert()
#             frappe.db.commit()
        
#         else:
#             frappe.msgprint(f"User Permission already exists for {doc.custom_added_by} on Customer {doc.name}")

#     else:
#         frappe.msgprint("No Sales Manager assigned to this customer.")






# def get_permission_query_conditions(user):
#     if "Sales Manager" in frappe.get_roles(user):
#         return f"`tabCustomer`.`custom_sales_manager` = '{user}'"
#     return ""

# def has_permission(doc, user):
#     if "Sales Manager" in frappe.get_roles(user):
#         return doc.custom_sales_manager == user
#     return True




import frappe

def get_permission_query_conditions(user):
    if "Administrator" in frappe.get_roles(user):
        return ""

    if "Sales Manager" in frappe.get_roles(user):
        return f"`tabCustomer`.`custom_sales_manager` = '{user}'"
    
    return ""

def has_permission(doc, user):
    if "Administrator" in frappe.get_roles(user):
        return True
    
    if "Sales Manager" in frappe.get_roles(user):
        return doc.custom_sales_manager == user
    
    return True
