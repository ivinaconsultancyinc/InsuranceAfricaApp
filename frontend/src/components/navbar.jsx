# Write the components to their respective files
with open("Navbar.jsx", "w") as f:
    f.write(navbar_code)

with open("Notification.jsx", "w") as f:
    f.write(notification_code)

with open("DataTable.jsx", "w") as f:
    f.write(data_table_code)

print("Navbar.jsx, Notification.jsx, and DataTable.jsx have been created in the frontend/components folder.")

