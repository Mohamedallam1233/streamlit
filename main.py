import streamlit as st
import pandas as pd
# Your data goes here
data = {

"basics_statistics": {
    "num_coupons": 1,
    "num_customer_info": 14,
    "num_orders": 12,
    "num_order_items": 31,
    "num_product": 8,
    "num_category": 9,
    },
    "restaurant_statistics": {
        "total_orders": 2,
        "total_quantity_sold": 35,
        "total_sales_before_discount": "3730.00",
        "total_sales_after_discount": "3665.00",
        "total_coupon_savings": "65.00"
    },
    "total_sales": {
        "total_sales_year": "6620",
        "total_sales_month": "4025",
        "total_sales_day": "3600"
    },
    "total_quantity_sold": {
        "total_quantity_sold_year": 101,
        "total_quantity_sold_month": 46,
        "total_quantity_sold_day": 34
    },
    "top_customers": [
        {
            "customer_name": "shrouk mamdouh ",
            "total_sales": "3600.00"
        },
        {
            "customer_name": "Mohamed Yosry Allame",
            "total_sales": "65.00"
        }
    ],
    "top_categories": [
        {
            "category_name": "اختبار 2",
            "total_sales": "1920.00"
        },
        {
            "category_name": "اختبار 3",
            "total_sales": "1650.00"
        },
        {
            "category_name": "وجبات",
            "total_sales": "130.00"
        },
        {
            "category_name": "اختبار 4",
            "total_sales": "15.00"
        },
        {
            "category_name": "اختبار 5",
            "total_sales": "15.00"
        }
    ],
    "top_products": [
        {
            "product_name": "allam",
            "total_sales": "1920.00"
        },
        {
            "product_name": "12345",
            "total_sales": "1650.00"
        },
        {
            "product_name": "مكرونة",
            "total_sales": "130.00"
        },
        {
            "product_name": "dd",
            "total_sales": "15.00"
        },
        {
            "product_name": "dc",
            "total_sales": "15.00"
        }
    ],
    "active_users_data": [
        {
            "customer_name": "shrouk mamdouh ",
            "total_orders": 1,
            "total_quantity": 34,
            "total_cost_before_discount": "3600.00",
            "total_cost_after_discount": "3600.00",
            "most_selected_product": "allam",
            "quantity_of_most_selected_product": 20,
            "most_selected_category": "اختبار 2",
            "quantity_of_most_selected_category": 20
        },
        {
            "customer_name": "Mohamed Yosry Allame",
            "total_orders": 1,
            "total_quantity": 1,
            "total_cost_before_discount": "130.00",
            "total_cost_after_discount": "65.00",
            "most_selected_product": "مكرونة",
            "quantity_of_most_selected_product": 1,
            "most_selected_category": "وجبات",
            "quantity_of_most_selected_category": 1
        }
    ]
}
df_total_sales = pd.DataFrame.from_dict(data["total_sales"], orient='index', columns=['Sales'])
df_top_customers = pd.DataFrame(data["top_customers"], columns=['customer_name', 'total_sales'] )
df_top_categories = pd.DataFrame(data["top_categories"], columns=['category_name', 'total_sales'])
df_top_products = pd.DataFrame(data["top_products"], columns=['product_name', 'total_sales'])
df_active_users_data = pd.DataFrame(data["active_users_data"], columns=[
    'customer_name', 'total_orders', 'total_quantity', 'total_cost_before_discount',
    'total_cost_after_discount', 'most_selected_product', 'quantity_of_most_selected_product',
    'most_selected_category', 'quantity_of_most_selected_category'
])

styles = [
        dict(selector="tr", props=[("background-color", "yellow")]),
        dict(selector="tr:nth-child(even)", props=[("background-color", "lightblue")]),
        dict(selector="tr:nth-child(odd)", props=[("background-color", "lightgreen")]),
    ]

# Title of the dashboard
st.title("Sales Analysis Dashboard")

# Sidebar with navigation
st.sidebar.subheader("Navigation")
selected_page = st.sidebar.radio("Go to", ["Basic Statistics", "Restaurant Statistics", "Total Sales",
                                          "Top Customers", "Top Categories", "Top Products", "Active Users Data"])

# Display selected page
if selected_page == "Basic Statistics":
    st.subheader("Basic Statistics")
    for key, value in data["basics_statistics"].items():
        # Create a card-like structure using st.markdown() and HTML
        st.markdown(
            f"<div style='width: 500px; height: 150px; display: flex; flex-direction: column; "
            f"align-items: center; justify-content: center; border-radius: 8px; margin: 10px; padding: 10px; "
            f"background-color: #3366cc; color: white;'>"
            f"<h3>{key}</h3>"
            f"<p style='font-size: 24px; font-weight: bold;'>{value}</p>"
            "</div>",
            unsafe_allow_html=True
        )
# Display selected page
elif selected_page == "Restaurant Statistics":
    st.subheader("Restaurant Statistics")
    for key, value in data["restaurant_statistics"].items():
        st.markdown(
            f"<div style='width: 500px; height: 150px; display: flex; flex-direction: column; "
            f"align-items: center; justify-content: center; border-radius: 8px; margin: 10px; padding: 10px; "
            f"background-color: #3366cc; color: white;'>"
            f"<h3>{key}</h3>"
            f"<p style='font-size: 24px; font-weight: bold;'>{value}</p>"
            "</div>",
            unsafe_allow_html=True
        )


elif selected_page == "Total Sales":
    st.subheader("Total Sales")

    # Display the table with custom styles
    st.table(df_total_sales.style.set_table_styles(styles))

elif selected_page == "Top Customers":
    st.subheader("Top Customers")

    # Display the table with custom styles
    st.table(df_top_customers.style.set_table_styles(styles))

elif selected_page == "Top Categories":
    st.subheader("Top Categories")

    # Display the table with custom styles
    st.table(df_top_categories.style.set_table_styles(styles))

elif selected_page == "Top Products":
    st.subheader("Top Products")

    # Display the table with custom styles
    st.table(df_top_products.style.set_table_styles(styles))

elif selected_page == "Active Users Data":
    st.subheader("Active Users Data")

    # Display the table with custom styles
    st.table(df_active_users_data.style.set_table_styles(styles))

# Footer or additional information
st.sidebar.markdown("---")
st.sidebar.text("© 2024 Sales Analysis Dashboard")