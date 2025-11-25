import streamlit as st
import math

# --- Konfigurasi Halaman ---
st.set_page_config(layout="wide", page_title="Virtual Lab Permutasi dan Kombinasi")
st.title("🔢 Virtual Lab Permutasi dan Kombinasi")
st.markdown("Interaktif untuk membedakan dan menghitung **Permutasi** (Urutan Penting) dan **Kombinasi** (Urutan Tidak Penting).")

# --- Fungsi Dasar Matematis ---
@st.cache_data
def calculate_factorial(n):
    """Menghitung faktorial n!"""
    return math.factorial(n)

@st.cache_data
def calculate_permutation(n, r):
    """Menghitung Permutasi P(n, r) = n! / (n-r)!"""
    if n < r:
        return 0
    return calculate_factorial(n) // calculate_factorial(n - r)

@st.cache_data
def calculate_combination(n, r):
    """Menghitung Kombinasi C(n, r) = n! / (r! * (n-r)!)"""
    if n < r:
        return 0
    numerator = calculate_factorial(n)
    denominator = calculate_factorial(r) * calculate_factorial(n - r)
    return numerator // denominator

# --- Konten Utama (Tab) ---
tab1, tab2, tab3, tab4 = st.tabs([
    "💡 Perbedaan Konsep", 
    "🔠 Permutasi (P(n, r))", 
    "⭐ Kombinasi (C(n, r))",
    "🔁 Permutasi Unsur Sama"
])

# ----------------------------------------------------
# --- TAB 1: Perbedaan Konsep ---
# ----------------------------------------------------
with tab1:
    st.header("💡 Kunci Perbedaan: Apakah Urutan Penting?")
    
    st.subheader("Tabel Perbandingan")
    
    col_p, col_c = st.columns(2)
    
    with col_p:
        st.subheader("Permutasi")
        st.error("Urutan **PENTING**")
        st.markdown("*Contoh:* Memilih Ketua, Sekretaris, Bendahara.")
        st.markdown("> Susunan (A, B, C) **BERBEDA** dengan (C, B, A).")
        st.latex(r"P(n, r) = \frac{n!}{(n-r)!}")
    
    with col_c:
        st.subheader("Kombinasi")
        st.success("Urutan **TIDAK PENTING**")
        st.markdown("*Contoh:* Memilih 3 anggota tim dari 5 orang.")
        st.markdown("> Kelompok {A, B, C} **SAMA** dengan {C, B, A}.")
        st.latex(r"C(n, r) = \frac{n!}{r!(n-r)!}")

    st.markdown("---")
    st.subheader("Latih Pilihan Anda")
    
    q1 = st.radio("Soal: Memilih 2 kartu dari 52 kartu remi. Permutasi atau Kombinasi?", 
                  ['Pilih salah satu', 'Permutasi', 'Kombinasi'], 
                  key='q1_radio')
    if q1 == 'Permutasi':
        st.error("Salah! Urutan kartu yang diambil tidak mengubah kelompok kartu Anda.")
    elif q1 == 'Kombinasi':
        st.success("Benar! Urutan kartu (King, Queen) sama dengan (Queen, King).")
        
    q2 = st.radio("Soal: Menyusun angka 4 digit dari 1, 2, 3, 4. Permutasi atau Kombinasi?", 
                  ['Pilih salah satu', 'Permutasi', 'Kombinasi'], 
                  key='q2_radio')
    if q2 == 'Permutasi':
        st.success("Benar! Angka 1234 berbeda dengan 4321.")
    elif q2 == 'Kombinasi':
        st.error("Salah! Urutan angka membuat nilai angka berbeda.")

# ----------------------------------------------------
# --- TAB 2: Permutasi Unsur Berbeda (P(n, r)) ---
# ----------------------------------------------------
with tab2:
    st.header("🔠 Kalkulator Permutasi $r$ dari $n$ Unsur Berbeda")
    st.markdown("Gunakan rumus ini ketika **urutan hasil penyusunan itu penting**.")
    
    col_input, col_result = st.columns(2)
    
    with col_input:
        st.subheader("Tentukan Parameter")
        n_p = st.slider("Jumlah total objek (n)", 1, 10, 5, key='n_p')
        r_p = st.slider("Jumlah objek yang disusun (r)", 1, n_p, 3, key='r_p')
        
        st.warning(f"Anda menyusun **{r_p}** objek dari **{n_p}** objek yang berbeda.")
        st.markdown("**Contoh Soal:** Dari {5} calon, dipilih Ketua, Sekretaris, dan Bendahara {3 jabatan}.")
        
    
    with col_result:
        result_p = calculate_permutation(n_p, r_p)
        st.subheader("Hasil Perhitungan")
        st.latex(r"P(" + str(n_p) + r", " + str(r_p) + r") = \frac{" + str(n_p) + r"!}{(" + str(n_p) + r" - " + str(r_p) + r")!} = " + str(result_p))
        
        st.metric(label="Banyaknya Susunan (Urutan Diperhatikan)", value=f"{result_p} cara")


# ----------------------------------------------------
# --- TAB 3: Kombinasi (C(n, r)) ---
# ----------------------------------------------------
with tab3:
    st.header("⭐ Kalkulator Kombinasi $r$ dari $n$ Unsur Berbeda")
    st.markdown("Gunakan rumus ini ketika **urutan hasil pemilihan itu tidak penting**.")
    
    col_input, col_result = st.columns(2)
    
    with col_input:
        st.subheader("Tentukan Parameter")
        n_c = st.slider("Jumlah total objek (n)", 1, 10, 5, key='n_c')
        r_c = st.slider("Jumlah objek yang dipilih (r)", 1, n_c, 3, key='r_c')
        
        st.success(f"Anda memilih **{r_c}** objek dari **{n_c}** objek yang berbeda.")
        st.markdown("**Contoh Soal:** Dari {5} orang, dipilih {3} orang untuk menjadi anggota tim.")
        
    
    with col_result:
        result_c = calculate_combination(n_c, r_c)
        st.subheader("Hasil Perhitungan")
        st.latex(r"C(" + str(n_c) + r", " + str(r_c) + r") = \frac{" + str(n_c) + r"!}{" + str(r_c) + r"!(" + str(n_c) + r" - " + str(r_c) + r")!} = " + str(result_c))
        
        st.metric(label="Banyaknya Kelompok (Urutan Tidak Diperhatikan)", value=f"{result_c} cara")
        st.markdown(f"**Perbandingan:** Kombinasi ({result_c}) selalu lebih kecil atau sama dengan Permutasi ({calculate_permutation(n_c, r_c)}) untuk n dan r yang sama.")

# ----------------------------------------------------
# --- TAB 4: Permutasi Unsur Sama ---
# ----------------------------------------------------
with tab4:
    st.header("🔁 Permutasi dengan Unsur yang Sama")
    st.markdown("Lab ini membantu menghitung susunan dari sekumpulan objek di mana terdapat objek yang sama atau berulang (misalnya kata 'MAMA').")
    
    st.subheader("Rumus")
    st.latex(r"P = \frac{n!}{k_1! \cdot k_2! \cdot \ldots \cdot k_m!}")
    
    st.subheader("Simulasi dengan Kata")
    word = st.text_input("Masukkan sebuah kata (misalnya: MATEMATIKA)", "KATAK", max_chars=15).upper()
    n_total = len(word)
    
    from collections import Counter
    counts = Counter(word)
    repeated_chars = {char: count for char, count in counts.items() if count > 1}
    
    st.info(f"Total huruf (n): **{n_total}**")
    
    k_factors = []
    if not repeated_chars:
        st.warning("Tidak ada huruf yang berulang. Permutasi = n!")
        final_result = calculate_factorial(n_total)
        denominator_str = "1"
        denominator_val = 1
    else:
        # Perhitungan
        denominator_str = ""
        denominator_val = 1
        for char, count in repeated_chars.items():
            st.write(f"- Huruf '{char}' muncul **{count}** kali ($k$ = {count}).")
            k_factors.append(count)
            denominator_str += f"{count}!"
            denominator_val *= calculate_factorial(count)
            if len(k_factors) < len(repeated_chars):
                denominator_str += " \cdot "
        
        numerator = calculate_factorial(n_total)
        final_result = numerator // denominator_val
        
        # Menampilkan langkah perhitungan
        st.subheader("Langkah Perhitungan")
        st.latex(r"P = \frac{" + str(n_total) + r"!}{" + denominator_str + r"} = \frac{" + str(numerator) + r"}{" + str(denominator_val) + r"} = " + str(final_result))


    st.metric(label=f"Banyaknya Susunan Kata '{word}' yang Berbeda", value=f"{final_result} cara")
