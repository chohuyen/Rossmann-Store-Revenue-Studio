import pandas as pd
import numpy as np

def load_data(data_dir="data/raw"):
    """Đọc dữ liệu thô từ thư mục data/raw"""
    train = pd.read_csv(f"{data_dir}/train.csv", low_memory=False)
    test = pd.read_csv(f"{data_dir}/test.csv", low_memory=False)
    store = pd.read_csv(f"{data_dir}/store.csv", low_memory=False)
    return train, test, store

def preprocess_data(train, test, store):
    """Tiền xử lý và gộp dữ liệu, tạo các đặc trưng thời gian"""
    # Gộp thông tin cửa hàng
    train = train.merge(store, on="Store", how="left")
    test = test.merge(store, on="Store", how="left")
    
    # Chuyển đổi định dạng ngày tháng
    train["Date"] = pd.to_datetime(train["Date"])
    test["Date"] = pd.to_datetime(test["Date"])
    
    for df in [train, test]:
        df["Year"] = df["Date"].dt.year
        df["Month"] = df["Date"].dt.month
        df["Day"] = df["Date"].dt.day
        df["DayOfWeek"] = df["Date"].dt.dayofweek
        df["WeekOfYear"] = df["Date"].dt.isocalendar().week.astype(int)
        
        # Xử lý missing values cơ bản
        df["CompetitionDistance"].fillna(df["CompetitionDistance"].median(), inplace=True)
        df["Open"].fillna(1, inplace=True)
        
    return train, test

if __name__ == "__main__":
    print("Đang tải và xử lý dữ liệu...")
    train, test, store = load_data()
    train_df, test_df = preprocess_data(train, test, store)
    print(f"Kích thước train sau khi xử lý: {train_df.shape}")
    print(f"Kích thước test sau khi xử lý: {test_df.shape}")
