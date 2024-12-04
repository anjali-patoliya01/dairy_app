import frappe

def execute(filters=None):
    """
    Generates a stock summary report highlighting pending stock (liters) available for transfer or further sale.
    """
    if not filters:
        filters = {}

    columns = [
        {"label": "Item", "fieldname": "item_code", "fieldtype": "Data", "width": 150},
        {"label": "Pending Stock (Liters)", "fieldname": "pending_stock", "fieldtype": "Float", "width": 200},
    ]

    stock_filters = {}

    if filters.get("item_code"):
        stock_filters["item_code"] = filters.get("item_code")
    
    if filters.get("warehouse"):
        stock_filters["warehouse"] = filters.get("warehouse")
    
    if filters.get("from_date") and filters.get("to_date"):
        stock_filters["posting_date"] = ["between", (filters.get("from_date"), filters.get("to_date"))]

    stock_entries = frappe.get_all(
        "Stock Ledger Entry",  
        fields=["item_code", "actual_qty"],
        filters=stock_filters,
        order_by="posting_date asc"
    )

    data = {}
    for entry in stock_entries:
        item_code = entry.get("item_code")
        actual_qty = entry.get("actual_qty", 0)

        if item_code in data:
            data[item_code] += actual_qty
        else:
            data[item_code] = actual_qty

    report_data = []
    for item_code, pending_stock in data.items():
        report_data.append({
            "item_code": item_code,
            "pending_stock": pending_stock,
        })

    return columns, report_data
