import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dữ liệu
uploaded_file = st.file_uploader("📁 Tải lên file amazon.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # xử lý tiếp...
else:
    st.warning("⚠️ Vui lòng tải lên file amazon.csv để tiếp tục.")
    st.stop()


st.title("📊 Phân tích dữ liệu Amazon")

# 1. Ma trận tương quan
st.header("1. Ma trận tương quan giữa các thuộc tính")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df[['discounted_price', 'discount_percentage', 'rating_count', 'rating']].corr(),
            annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)
st.pyplot(fig)

# 2. Phân phối giá sau giảm
st.header("2. Phân phối giá sau giảm")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(df['discounted_price'], bins=30, kde=True, color='#1f77b4', ax=ax)
st.pyplot(fig)

# 3. Điểm đánh giá trung bình theo danh mục
st.header("3. Điểm đánh giá trung bình theo danh mục")
avg_rating = df.groupby('category_level_1')['rating'].mean().sort_values()
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=avg_rating.index, y=avg_rating.values, color='#ff7f0e', ax=ax)
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# 4. Mức giảm giá vs Số lượng đánh giá
st.header("4. Mức giảm giá vs Số lượng đánh giá")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='discount_percentage', y='rating_count', data=df, color='#2ca02c', alpha=0.6, ax=ax)
st.pyplot(fig)

# 5. Top 5 sản phẩm có số lượng đánh giá cao nhất
st.header("5. Top 5 sản phẩm được đánh giá nhiều nhất")
top_products = df.nlargest(5, 'rating_count')[['product_name', 'rating_count']]
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='rating_count', y='product_name', data=top_products, color='#d62728', ax=ax)
st.pyplot(fig)

# 6. Giá sau giảm vs Điểm đánh giá
st.header("6. Giá sau giảm vs Điểm đánh giá")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='discounted_price', y='rating', data=df, color='#9467bd', alpha=0.6, ax=ax)
st.pyplot(fig)
