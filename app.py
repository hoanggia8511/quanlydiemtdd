import streamlit as st
import pandas as pd

# ===== 0. TIÊU ĐỀ =====
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# ===== 1. DỮ LIỆU 10 SINH VIÊN =====
# (Thay bằng dữ liệu trong đề của bạn)
data = {
    "Họ tên":     ["An", "Bình", "Châu", "Dũng", "Em", "Phúc", "Giang", "Hà", "Khoa", "Lan"],
    "Chuyên cần": [10, 9, 8, 7, 10, 6, 9, 8, 5, 10],
    "Giữa kỳ":    [8, 7, 6, 5, 9, 4, 8, 7, 3, 9],
    "Cuối kỳ":    [9, 8, 7, 4, 9, 5, 9, 6, 2, 10],
}
df = pd.DataFrame(data)

# ===== 2. TÍNH TỔNG KẾT VÀ XẾP LOẠI =====
# (Thay công thức/ngưỡng theo đề của bạn)
df["Tổng kết"] = (
    df["Chuyên cần"] * 0.2
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.5
).round(2)
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5: 
        return "Trung bình"
    else:
        return "Yếu"
df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)
# ===== 3. BẢNG ĐIỂM =====
st.subheader("Bảng điểm")
st.dataframe(df, use_container_width=True)

# ===== 4. ĐIỂM TRUNG BÌNH LỚP =====
st.subheader("Thống kê lớp")
diem_tb = df["Tổng kết"].mean()
st.metric("Điểm trung bình lớp", round(diem_tb, 2))

# ===== 5. CAO NHẤT VÀ THẤP NHẤT =====
sv_cao = df.loc[df["Tổng kết"].idxmax()]
sv_thap = df.loc[df["Tổng kết"].idxmin()]

st.write(f"Điểm tổng kết cao nhất: **{sv_cao['Họ tên']}** ({sv_cao['Tổng kết']:.2f})")
st.write(f"Điểm tổng kết thấp nhất: **{sv_thap['Họ tên']}** ({sv_thap['Tổng kết']:.2f})")

# ===== 6. SỐ SINH VIÊN ĐẠT (Tổng kết >= 5) =====
so_dat = (df["Tổng kết"] >= 5).sum()
st.write(f"✅ Số sinh viên đạt: **{so_dat}** / {len(df)}")

# ===== 7. SELECTBOX CHỌN SINH VIÊN =====
st.subheader("Tra cứu sinh viên")
ten_chon = st.selectbox("Chọn sinh viên:", df["Họ tên"])

sv = df[df["Họ tên"] == ten_chon].iloc[0]

st.write(f"Chuyên cần: **{sv['Chuyên cần']}**")
st.write(f"Giữa kỳ: **{sv['Giữa kỳ']}**")
st.write(f"Cuối kỳ: **{sv['Cuối kỳ']}**")
st.write(f"Điểm tổng kết: **{sv['Tổng kết']:.2f}**")
st.write(f"Xếp loại: **{sv['Xếp loại']}**")

# ===== 8. BIỂU ĐỒ CỘT ĐIỂM TỔNG KẾT =====
st.subheader("Biểu đồ điểm tổng kết")
st.bar_chart(df.set_index("Họ tên")["Tổng kết"])

# ===== 9. HỌ TÊN + MSSV Ở CUỐI TRANG (CHỮ NHỎ) =====
st.divider()
st.caption("Người thực hiện: Hán Trương Hoàng Thủ - MSSV: 058208007961")
