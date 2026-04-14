# PROYEK ANALISIS SENTIMEN

## Deskripsi
Proyek ini merupakan implementasi analisis sentimen menggunakan machine learning untuk mengklasifikasikan ulasan pengguna ke dalam tiga kategori sentimen:

- negatif
- netral
- positif

Dataset ulasan aplikasi diperoleh melalui proses scraping mandiri menggunakan Python, lalu diproses hingga siap dipakai untuk pelatihan model.

## Dataset
- Sumber data: hasil scraping Google Play Store
- File utama:
  - `dataset/gojek_reviews.csv` (data mentah hasil scraping)
  - `dataset/gojek_reviews_labeled.csv` (data setelah cleaning + labeling)
- Jumlah data pelatihan:  40.000++ sampel (setelah preprocessing)

## Tahapan Proyek
1. Data scraping
2. Data cleaning dan preprocessing teks
3. Pelabelan sentimen berdasarkan skor rating
4. Ekstraksi fitur:
	- TF-IDF
	- Word2Vec
5. Pelatihan model:
	- Logistic Regression + TF-IDF (80/20)
	- SGDClassifier + Word2Vec (80/20)
	- Linear SVC + TF-IDF char n-gram (75/25)
6. Evaluasi model (accuracy, classification report, confusion matrix)
7. Inference pada data baru

## Model Terbaik
Berdasarkan hasil evaluasi saat ini, model paling stabil adalah:

- **Skema A: Logistic Regression + TF-IDF**

Model ini menghasilkan nilai akurasi tertinggi dan performa macro F1 yang paling baik dibandingkan skema lain pada eksperimen ini.

## Struktur Folder
- `data_scrapping/scrapping.py` : kode scraping data
- `notebook/training.ipynb` : notebook end-to-end preprocessing, training, evaluasi, inference
- `dataset/gojek_reviews.csv` : dataset hasil scraping
- `dataset/gojek_reviews_labeled.csv` : dataset hasil labeling
- `requirements.txt` : daftar dependency
- `README.md` : dokumentasi proyek

## Cara Menjalankan
1. Install dependency:

```bash
pip install -r requirements.txt
```

2. (Opsional) Jalankan scraping ulang:

```bash
python data_scrapping/scrapping.py
```

3. Buka dan jalankan notebook:

- `notebook/training.ipynb`

## Catatan
- Notebook sudah disusun lengkap mulai dari data preparation sampai inference.
- Hasil evaluasi bisa berbeda tipis jika data scraping diperbarui.
- Kelas netral memiliki distribusi lebih kecil sehingga metrik kelas netral cenderung lebih rendah.
