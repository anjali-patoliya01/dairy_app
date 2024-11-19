// Copyright (c) 2024, Sigzen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Milk sale', {
    quantityin_liter: function(frm) {
        calculate_rate_and_cost(frm);
    },
    rate_per_fat: function(frm) {
        calculate_rate_and_cost(frm);
    },
    fat_content: function(frm) {
        calculate_rate_and_cost(frm);
    }
});

function calculate_rate_and_cost(frm) {
    let rate_per_fat = frm.doc.rate_per_fat || 0;                
    let fat_content = frm.doc.fat_content || 0;          
    let quantityin_liter = frm.doc.quantityin_liter || 0;  

    let rate_per_liter = rate_per_fat * fat_content 

    frm.set_value('rate_per_liter', rate_per_liter);

    let total_amount = quantityin_liter* rate_per_liter;

    frm.set_value('total_amount', total_amount);
}