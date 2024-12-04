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


function calculate_rate_and_amount(frm, cdt, cdn) {
    let row = frappe.get_doc(cdt, cdn);
    frappe.call({
        method: "frappe.client.get_value",
        args: {
            doctype: "Sale Milk Setting", 
            fieldname: "sale_fat_rate", 
        },
        callback: function (response) {
            if (response && response.message) {
                let sale_fat_rate = response.message.sale_fat_rate || 0;
                if (row.fat_content) {
                    let new_rate = row.fat_content * sale_fat_rate;
                    frappe.model.set_value(cdt, cdn, 'rate', new_rate);
                }
                if (row.qty && row.rate) {
                    let new_amount = row.qty * row.rate;
                    frappe.model.set_value(cdt, cdn, 'amount', new_amount);
                }
                frm.refresh_field('items'); 
            } else {
                frappe.msgprint(__('Unable to fetch Fat Rate.'));
            }
        }
    });
}