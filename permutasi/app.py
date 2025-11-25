import streamlit as st
import math

# --- Konfigurasi Halaman ---
st.set_page_config(layout="wide", page_title="Virtual Lab Permutasi")
st.title("🔢 Virtual Lab Permutasi")
st.markdown("Interaktif untuk memahami Permutasi Unsur Berbeda dan Permutasi dengan Unsur yang Sama.")

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

# --- Konten Utama (Tab) ---
tab1, tab2, tab3 = st.tabs(["💡 Konsep Dasar", "🔠 Permutasi Unsur Berbeda (P(n, r))", "🔁 Permutasi Unsur Sama"])

# ----------------------------------------------------
# --- TAB 1: Konsep Dasar ---
# ----------------------------------------------------
with tab1:
    st.header("💡 Apa itu Permutasi?")
    
    st.markdown("""
    **Permutasi** adalah susunan yang dibentuk dari sekumpulan objek di mana **urutan itu penting**. 
    Berbeda dengan Kombinasi, dalam Permutasi, urutan A-B berbeda dengan B-A.

    ### Contoh Sederhana
    Misalkan ada 3 huruf: A, B, C.
    * **Susunan (Permutasi) yang mungkin:** ABC, ACB, BAC, BCA, CAB, CBA. (Total 6 susunan)
    * **Rumus umum:** $n!$ (Faktorial dari jumlah objek).
    
    """)
    
    col_faktorial, col_rumus = st.columns(2)
    
    with col_faktorial:
        st.subheader("Kalkulator Faktorial (n!)")
        n_fact = st.slider("Pilih nilai n", 0, 10, 4, key='fact_slider')
        result_fact = calculate_factorial(n_fact)
        st.latex(f"{n_fact}! = {result_fact}")
        st.info(f"Artinya, ada {result_fact} cara untuk menyusun {n_fact} objek.")

    with col_rumus:
        st.subheader("Rumus Umum Permutasi")
        st.latex(r"P(n, r) = \frac{n!}{(n-r)!}")
        st.markdown("**Keterangan:**")
        st.markdown("- **n:** Jumlah total objek.")
        st.markdown("- **r:** Jumlah objek yang dipilih (disusun).")
        st.markdown("- **Urutan DIPERHATIKAN.**")
        
    st.markdown("---")

# ----------------------------------------------------
# --- TAB 2: Permutasi Unsur Berbeda (P(n, r)) ---
# ----------------------------------------------------
with tab2:
    st.header("🔠 Permutasi $r$ dari $n$ Unsur Berbeda")
    st.markdown("Gunakan lab ini untuk menghitung banyaknya cara menyusun **r** objek dari total **n** objek yang tersedia, di mana semua objek berbeda.")
    
    col_input, col_result = st.columns(2)
    
    with col_input:
        st.subheader("Tentukan Parameter")
        n_diff = st.slider("Jumlah total objek (n)", 1, 10, 5, key='n_diff')
        r_diff = st.slider("Jumlah objek yang disusun (r)", 1, n_diff, 3, key='r_diff')
        
        st.warning(f"Anda menyusun **{r_diff}** objek dari **{n_diff}** objek yang berbeda.")
        
        # Contoh ilustrasi
        st.markdown("#### Ilustrasi Soal")
        st.markdown(f"**Soal:** Ada **{n_diff}** kandidat. Akan dipilih Ketua, Sekretaris, dan Bendahara (3 jabatan yang berbeda). Berapa banyak susunan kepengurusan yang mungkin?")
        
    
    with col_result:
        result_diff = calculate_permutation(n_diff, r_diff)
        st.subheader("Hasil Perhitungan")
        st.latex(r"P(" + str(n_diff) + r", " + str(r_diff) + r") = \frac{" + str(n_diff) + r"!}{(" + str(n_diff) + r" - " + str(r_diff) + r")!} = " + str(result_diff))
        
        st.metric(label="Banyaknya Susunan yang Mungkin", value=f"{result_diff} cara")
        
        st.markdown("---")
        st.subheader("P(n, n) - Menyusun semua objek")
        result_n_n = calculate_permutation(n_diff, n_diff)
        st.latex(r"P(" + str(n_diff) + r", " + str(n_diff) + r") = " + str(n_diff) + r"! = " + str(result_n_n))


# ----------------------------------------------------
# --- TAB 3: Permutasi Unsur Sama ---
# ----------------------------------------------------
with tab3:
    st.header("🔁 Permutasi dengan Unsur yang Sama")
    st.markdown("Lab ini membantu menghitung susunan dari sekumpulan objek di mana terdapat objek yang sama atau berulang (misalnya kata 'MAMA').")
    
    st.subheader("Rumus")
    st.latex(r"P = \frac{n!}{k_1! \cdot k_2! \cdot \ldots \cdot k_m!}")
    st.markdown("**Keterangan:**")
    st.markdown("- **n:** Jumlah total objek.")
    st.markdown("- $k_1, k_2, \ldots$: Jumlah objek yang sama (berulang) untuk setiap jenisnya.")

    st.subheader("Simulasi dengan Kata")
    word = st.text_input("Masukkan sebuah kata (misalnya: MATEMATIKA)", "KATAK", max_chars=15).upper()
    n_total = len(word)
    
    # Menghitung frekuensi setiap huruf
    from collections import Counter
    counts = Counter(word)
    
    # Filter hanya huruf yang berulang (k > 1)
    repeated_chars = {char: count for char, count in counts.items() if count > 1}
    
    st.info(f"Total huruf (n): **{n_total}**")
    st.markdown("Huruf yang berulang ($k_i$):")
    
    k_factors = []
    
    if not repeated_chars:
        st.warning("Tidak ada huruf yang berulang. Permutasi = n! (Permutasi Unsur Berbeda)")
        final_result = calculate_factorial(n_total)
        # Menampilkan k_i = 1
        for char, count in counts.items():
            st.write(f"- Huruf '{char}' muncul {count} kali.")
    else:
        # Menghitung penyebut (k1! * k2! * ...)
        denominator_str = ""
        denominator_val = 1
        
        for char, count in repeated_chars.items():
            st.write(f"- Huruf '{char}' muncul **{count}** kali ($k$ = {count}).")
            k_factors.append(count)
            denominator_str += f"{count}!"
            denominator_val *= calculate_factorial(count)
            
            if len(k_factors) < len(repeated_chars):
                denominator_str += " \cdot "
        
        # Perhitungan akhir
        numerator = calculate_factorial(n_total)
        final_result = numerator // denominator_val
        
        # Menampilkan langkah perhitungan
        st.subheader("Langkah Perhitungan")
        st.latex(r"P = \frac{" + str(n_total) + r"!}{" + denominator_str + r"} = \frac{" + str(numerator) + r"}{" + str(denominator_val) + r"} = " + str(final_result))


    st.metric(label=f"Banyaknya Susunan Kata '{word}' yang Berbeda", value=f"{final_result} cara")
