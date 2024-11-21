# Copyright (c) 2024, Sigzen and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    """
    Generates a milk purchase summary report.
    """
    if not filters:
        filters = {}

    columns = [
        {"label": "Date", "fieldname": "posting_date", "fieldtype": "Date", "width": 120},
        {"label": "Liters Purchased", "fieldname": "qty", "fieldtype": "Float", "width": 150},
        {"label": "Total Cost", "fieldname": "amount", "fieldtype": "Currency", "width": 150},
    ]

    milk_purchases = frappe.get_all(
        "Purchase Invoice",  
        fields=["name", "posting_date"],
        filters=filters,
        order_by="posting_date asc"
    )

    data = []
    total_liters = 0
    total_cost = 0

    for purchase in milk_purchases:
        child_items = frappe.get_all(
            "Purchase Invoice Item",  
            fields=["qty", "amount"],
            filters={"parent": purchase.name}
        )
        liters = sum((item.qty) for item in child_items)
        cost = sum((item.amount) for item in child_items)
   



        total_liters += liters
        total_cost += cost


        data.append({
            "posting_date": purchase.posting_date,
            "qty": liters,
            "amount": cost,
        })

    data.append({
        "posting_date": "Total",
        "qty": total_liters,
        "amount": total_cost,
    })

    return columns, data
