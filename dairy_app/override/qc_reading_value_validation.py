import frappe
from frappe import _

def validate_reading_values(doc, method):
    if doc.status in ["Accepted", "Rejected"]:
        if not doc.readings:
            frappe.throw(_(f"Readings table is empty. Please add readings before setting the status to {doc.status}."))

        for reading in doc.readings:
            if not reading.reading_value:
                frappe.throw(_(f"Reading Value is missing for parameter: {reading.parameter}. Please fill all Reading Values before setting the status to {doc.status}"))


        frappe.msgprint(_("All Reading Values are valid. Proceeding with the status change."))

