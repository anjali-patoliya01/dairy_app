// Copyright (c) 2024, Sigzen and contributors
// For license information, please see license.txt


frappe.ui.form.on('Daily Milk Collection', {
    quantity_in_liter_: function(frm) {
        calculate_rate_and_cost(frm);
    },
    fat_rate: function(frm) {
        calculate_rate_and_cost(frm);
    },
    fat_content: function(frm) {
        calculate_rate_and_cost(frm);
    }
});

function calculate_rate_and_cost(frm) {
    let fat_rate = frm.doc.fat_rate || 0;                
    let fat_content = frm.doc.fat_content || 0;          
    let quantity_in_liter_ = frm.doc.quantity_in_liter_ || 0;  

    let rate_per_liter = fat_rate * fat_content 

    frm.set_value('rate_per_liter', rate_per_liter);

    let total_cost = quantity_in_liter_ * rate_per_liter;

    frm.set_value('total_cost', total_cost);
}

