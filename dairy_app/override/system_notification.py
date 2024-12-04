import frappe

def notify_on_quality_inspection(doc, method):
    """
    Sends system notifications when Quality Inspection is approved or rejected.
    """
    # if doc.doctype != "Quality Inspection" or not doc.status:
    #     return

    if doc.custom_milk_test_status == "Accepted":
        send_system_notification(
            doc,
            role="Supplier Manager",
            message=f"Quality Inspection {doc.name} has been approved for Supplier: {doc.supplier}"
        )
        send_system_notification(
            doc,
            role="Sales Manager",
            message=f"Quality Inspection {doc.name} has been approved. The milk is ready for sales."
        )
    elif doc.custom_milk_test_status == "Rejected":
        send_system_notification(
            doc,
            role="Supplier Manager",
            message=f"Quality Inspection {doc.name} has been rejected for Supplier: {doc.supplier}"
        )
        send_system_notification(
            doc,
            role="Sales Manager",
            message=f"Quality Inspection {doc.name} has been rejected. You can't sale this milk.."
        )

def send_system_notification(doc, role, message):
    """
    Sends system notifications to all users with the specified role.
    """

    users = frappe.get_all(
        "User Role",
        fields=["parent"],
        filters={"role": role}
    )

    for user in users:
        user_id = user.get("parent")
        if user_id:
            frappe.publish_realtime(
                event="msgprint",
                message=message,
                user=user_id,
                after_commit=True  
            )


   # f""" 
                #             Quality Inspection {doc.name} has been approved.
                #             <a href="/app/quality-inspection/{doc.name}">View Document</a>
                #         """,