frappe.ui.form.on('Sales Order Item', {
    fat_content: function (frm, cdt, cdn) {
        let row = frappe.get_doc(cdt, cdn);
        calculate_rate_and_amount(row, cdt, cdn);
    },

    qty: function (frm, cdt, cdn) {
        let row = frappe.get_doc(cdt, cdn);
        calculate_rate_and_amount(row, cdt, cdn);
    },
    rate: function (frm, cdt, cdn) {
        let row = frappe.get_doc(cdt, cdn);
        calculate_rate_and_amount(row, cdt, cdn);
    },
});

function calculate_rate_and_amount(row, cdt, cdn) {
    if (row.rate && row.fat_content) {
        row.rate = row.fat_content * 8.0;
        frappe.model.set_value(cdt, cdn, 'rate', row.rate);
    }
    if (row.rate && row.qty) {
        row.amount = row.qty * row.rate;
        frappe.model.set_value(cdt, cdn, 'amount', row.amount);
    }
}



