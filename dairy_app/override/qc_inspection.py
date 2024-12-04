import frappe
from frappe import _
# from erpnext.stock.doctype.quality_inspection.quality_inspection import QualityInspection
# from frappe.utils import cint

# class QualityInspectionOverride(QualityInspection):
# def validate(self):
# 	if not self.readings and self.item_code:
# 		self.get_item_specification_details()

# 	if self.inspection_type == "In Process" and self.reference_type == "Job Card":
# 		item_qi_template = frappe.db.get_value("Item", self.item_code, "quality_inspection_template")
# 		parameters = get_template_details(item_qi_template)
# 		for reading in self.readings:
# 			for d in parameters:
# 				if reading.specification == d.specification:
# 					reading.update(d)
# 					reading.status = "Accepted"

# 	if self.readings:
# 		self.inspect_and_set_status()
