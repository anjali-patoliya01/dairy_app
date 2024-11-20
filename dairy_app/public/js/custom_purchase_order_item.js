frappe.ui.form.on('Purchase Order Item', {
    fat_content: function (frm, cdt, cdn) {
        calculate_rate_and_amount(frm, cdt, cdn);
    },
    qty: function (frm, cdt, cdn) {
        calculate_rate_and_amount(frm, cdt, cdn);
    },
    rate: function (frm, cdt, cdn) {
        calculate_rate_and_amount(frm, cdt, cdn);
    }
});

function calculate_rate_and_amount(frm, cdt, cdn) {
    let row = frappe.get_doc(cdt, cdn);
    if (row.fat_content) {
        let new_rate = row.fat_content * 8.0;
        frappe.model.set_value(cdt, cdn, 'rate', new_rate);
    }
    if (row.qty && row.rate) {
        let new_amount = row.qty * row.rate;
        frappe.model.set_value(cdt, cdn, 'amount', new_amount);
    }
    frm.refresh_field('items'); 
}

