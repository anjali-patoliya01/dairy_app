frappe.ui.form.on('Stock Entry', {
    refresh: function(frm) {
        // Calculate Pending Stock
        frm.set_value('custom_pending_stock', frm.doc.custom_total_milk_bought - frm.doc.custom_total_milk_sold);

        // Calculate Stock After Transfer
        frm.set_value('custom_stock_after_transfer', frm.doc.custom_pending_stock - frm.doc.custom_quantity_transferred);
    },
    custom_total_milk_bought: function(frm) {
        frm.trigger('refresh');
    },
    custom_total_milk_sold: function(frm) {
        frm.trigger('refresh');
    },
    custom_quantity_transferred: function(frm) {
        frm.trigger('refresh');
    }
});
