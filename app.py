import streamlit as st
import pandas as pd
from database import *

# Create table
create_table()

st.title("💰 Personal Expense Tracker")

menu = ["Add Expense", "View Expenses", "Delete Expense"]

choice = st.sidebar.selectbox("Menu", menu)

# -------------------------
# ADD EXPENSE
# -------------------------

if choice == "Add Expense":

    st.subheader("Add New Expense")

    amount = st.number_input("Amount", min_value=0.0)

    category = st.selectbox(
        "Category",
        ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"]
    )

    date = st.date_input("Date")

    note = st.text_input("Note")

    if st.button("Add Expense"):

        add_expense(amount, category, str(date), note)

        st.success("Expense Added Successfully!")

# -------------------------
# VIEW EXPENSES
# -------------------------

elif choice == "View Expenses":

    st.subheader("All Expenses")

    data = get_expenses()

    df = pd.DataFrame(
        data,
        columns=["ID", "Amount", "Category", "Date", "Note"]
    )

    st.dataframe(df)

    if len(df) > 0:

        st.subheader("Spending by Category")

        category_chart = df.groupby("Category")["Amount"].sum()

        st.bar_chart(category_chart)

        st.subheader("Total Spending")

        st.metric("Total Amount", df["Amount"].sum())

# -------------------------
# DELETE EXPENSE
# -------------------------

elif choice == "Delete Expense":

    st.subheader("Delete Expense")

    expense_id = st.number_input("Enter Expense ID")

    if st.button("Delete"):

        delete_expense(expense_id)

        st.warning("Expense Deleted")