frappe.ui.form.on('Customer', {
    before_save: function(frm) {
        if (!frm.doc.sales_manager) {
            frm.set_value('custom_sales_manager', frappe.session.user);
        }
    }
});

