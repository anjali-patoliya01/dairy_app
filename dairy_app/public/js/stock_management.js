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
    },


    on_submit: function(frm) {
        if (frm.doc.purpose === 'Material Transfer' && frm.doc.vehicle) {
            frappe.call({
                method: 'frappe.client.insert',
                args: {
                    doc: {
                        doctype: 'Vehicle Stock Log',
                        parent: frm.doc.vehicle,
                        parentfield: 'stock_log', 
                        parenttype: 'Vehicle',
                        date: frappe.datetime.now_date(),
                        stock_entry_reference: frm.doc.name,
                        item: frm.doc.items[0].item_code, 
                        quantity_transferred: frm.doc.items[0].qty
                    }
                },
                callback: function(r) {
                    if (!r.exc) {
                        frappe.msgprint(__('Vehicle Stock Log updated successfully.'));
                    }
                }
            });
        }
    }
},
);