# Copyright (c) 2024, Sigzen and contributors
# For license information, please see license.txt

import frappe

import frappe

def execute(filters=None):
    """
    Generates a milk sales summary report.
    """
    if not filters:
        filters = {}

    columns = [
        {"label": "Customer", "fieldname": "customer", "fieldtype": "data", "width": 150},
        {"label": "Posting Date", "fieldname": "posting_date", "fieldtype": "Date", "width": 150},
        {"label": "Liters Sold", "fieldname": "qty", "fieldtype": "Float", "width": 150},
        {"label": "Revenue", "fieldname": "amount", "fieldtype": "Currency", "width": 150},
    ]


    sales_invoices = frappe.get_all(
        "Sales Invoice",  
        fields=["customer", "posting_date"],
        filters=filters,
        order_by="posting_date asc"
    )

    data = []
    total_liters = 0
    total_revenue = 0

    for invoice in sales_invoices:
        child_items = frappe.get_all(
            "Sales Invoice Item",  
            fields=["qty", "amount"],
            filters={"parent": invoice.name}
        )
        
        liters = sum((item.qty or 0) for item in child_items)
        revenue = sum((item.amount or 0) for item in child_items)

        total_liters += liters
        total_revenue += revenue


        data.append({
            'customer':invoice.customer,
            "posting_date": invoice.posting_date,
            "qty": liters,  
            "amount": revenue,  
        })


    if total_liters > 0 or total_revenue > 0:
        data.append({
            "posting_date": "Total",
            "qty": total_liters,
            "amount": total_revenue,
        })

    return columns, data


