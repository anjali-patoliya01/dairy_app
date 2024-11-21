import frappe

def validate_quality_inspection(doc, method):
    for item in doc.items:  
        if item.quality_inspection:             
            quality_inspection = frappe.get_doc("Quality Inspection", item.quality_inspection)
            if quality_inspection.test_status == "Rejected":  
                frappe.throw(
                    f"Item {item.item_code} is a rejected Quality Inspection\n"
                    f"(ID: {quality_inspection.name}). You cannot purchase it."
                )
