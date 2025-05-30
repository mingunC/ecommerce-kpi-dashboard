import pandas as pd
import streamlit as st
import plotly.express as px
import sqlite3
import os


def create_mock_data():
    data = {
        'order_id': range(1, 1001),
        'product': ['Frypan'] * 300 + ['Knife'] * 250 + ['Pressure Cooker'] * 350 + ['Lid'] * 100,
        'price': [75000] * 300 + [45000] * 250 + [120000] * 350 + [25000] * 100,
        'conversion': [1] * 240 + [0] * 60 + [1] * 200 + [0] * 50 + [1] * 280 + [0] * 70 + [1] * 80 + [0] * 20,
        'order_date': pd.date_range(start='2025-01-01', periods=1000, freq='H'),
        'campaign': ['Social'] * 400 + ['Search'] * 400 + ['Display'] * 200
    }
    df = pd.DataFrame(data)
    conn = sqlite3.connect('ecommerce.db')
    df.to_sql('orders', conn, if_exists='replace', index=False)
    conn.close()
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/mock_data.csv', index=False)
    return df


def calculate_kpis():
    conn = sqlite3.connect('ecommerce.db')
    total_revenue = pd.read_sql_query(
        "SELECT SUM(price) as revenue FROM orders WHERE conversion = 1", conn
    ).iloc[0]['revenue']
    conversion_rate = pd.read_sql_query(
        "SELECT AVG(conversion)*100 as conv_rate FROM orders", conn
    ).iloc[0]['conv_rate']
    avg_order_value = pd.read_sql_query(
        "SELECT AVG(price) as avg_value FROM orders WHERE conversion = 1", conn
    ).iloc[0]['avg_value']
    product_sales = pd.read_sql_query(
        "SELECT product, SUM(price) as revenue FROM orders WHERE conversion = 1 GROUP BY product", conn
    )
    campaign_sales = pd.read_sql_query(
        "SELECT campaign, SUM(price) as revenue FROM orders WHERE conversion = 1 GROUP BY campaign", conn
    )
    conn.close()
    return total_revenue, conversion_rate, avg_order_value, product_sales, campaign_sales


def main():
    st.set_page_config(page_title="Fissler eCommerce KPI Dashboard", layout="wide")
    st.title("Fissler Korea eCommerce KPI Dashboard")

    if not os.path.exists('ecommerce.db'):
        create_mock_data()

    total_revenue, conversion_rate, avg_order_value, product_sales, campaign_sales = calculate_kpis()

    col1, col2, col3 = st.columns(3)
    col1.metric("총 매출", f"₩{int(total_revenue):,}")
    col2.metric("전환율", f"{conversion_rate:.2f}%")
    col3.metric("평균 주문 가치", f"₩{int(avg_order_value):,}")

    st.subheader("판매 데이터 분석")
    conn = sqlite3.connect('ecommerce.db')

    df = pd.read_sql_query(
        "SELECT order_date, SUM(price) as revenue FROM orders WHERE conversion = 1 GROUP BY order_date", conn
    )
    fig1 = px.line(df, x='order_date', y='revenue', title="시간별 매출 추이", color_discrete_sequence=['#4CAF50'])
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.pie(product_sales, values='revenue', names='product', title="제품별 매출 비중",
                  color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.bar(campaign_sales, x='campaign', y='revenue', title="캠페인별 매출", color='campaign',
                  color_discrete_sequence=px.colors.qualitative.Bold)
    st.plotly_chart(fig3, use_container_width=True)

    conn.close()


if __name__ == "__main__":
    main()