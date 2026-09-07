# Proyek Portofolio Web - Pemrograman Berbasis Platform (CSGE602022)

**Nama:** Joceline Nadine Immanuella  
**NPM:** 2506656835  
**Kelas:** PBP A  
**Program Studi:** S1 Sistem Informasi, Fakultas Ilmu Komputer, Universitas Indonesia  
**Link Deployment PWS:** [http://joceline-nadine-myportofolio.pws.cs.ui.ac.id](http://joceline-nadine-myportofolio.pws.cs.ui.ac.id)

---

### Tugas 1

#### 1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti `<section>`, `<article>`, atau `<aside>`? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?

**Jawaban:**  
Ya, dalam merancang struktur website portofolio ini, saya menggunakan elemen semantik HTML5 secara terstruktur, seperti `<header>`, `<main>`, `<section>`, `<article>`, dan `<footer>`.

Penggunaan elemen semantik ini sangat membantu saya dalam membangun static web karena:
1. **Membuat Struktur Dokumen Jauh Lebih Terorganisir:** Dengan membagi halaman ke dalam `<section>` untuk setiap modul (seperti modul profil hero, sorotan prestasi, riwayat pendidikan, dan kontak) serta `<article>` untuk kartu-kartu entitas mandiri (seperti kartu peran organisasi dan penghargaan), struktur file HTML menjadi sangat mudah dibaca dan dipahami alurnya dibanding hanya menumpuk tag `<div>`.
2. **Meningkatkan Standar Aksesibilitas (Accessibility):** Tag semantik membantu peramban web dan pembaca layar (*screen reader*) memahami hierarki konten dengan tepat, sehingga informasi portofolio dapat diakses secara inklusif.
3. **Mempermudah Pengelolaan Gaya pada CSS:** Struktur yang semantik memudahkan saya saat menulis selector CSS dan menerapkan tata letak Bento Grid tanpa risiko terjadinya konflik gaya antar bagian.

---

#### 2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?

**Jawaban:**  
**Tantangan Tata Letak yang Dihadapi:**
- Tantangan utama terletak pada penataan sistem grid multikolom pada layout Bento. Pada layar desktop yang lebar, kartu-kartu informasi dapat dibagi menjadi 2 hingga 3 kolom sejajar. Namun, saat dibuka pada layar ponsel yang sempit, kartu-kartu tersebut menjadi terlalu sempit dan teks di dalamnya sulit dibaca.
- Penyesuaian proporsi bingkai foto profil serta grid kartu kepemimpinan dan penghargaan agar tetap proporsional dan nyaman dibaca di ponsel tanpa merusak hierarki elemen lainnya.

**Evaluasi dan Penataan Ulang untuk Tampilan Mobile:**
- **Penyederhanaan Kolom Grid:** Menggunakan CSS Media Queries (`@media (max-width: 960px)` dan `@media (max-width: 600px)`), saya mengubah tata letak multikolom menjadi 1 kolom penuh vertikal (`grid-template-columns: 1fr`). Hal ini membuat alur membaca di ponsel menjadi alami (cukup menggulir ke bawah).
- **Penyesuaian Hierarki Visual:** Pada layar mobile, informasi identitas utama (nama, NPM, dan program studi) tetap diprioritaskan di bagian paling atas, diikuti oleh foto profil dengan ukuran yang disesuaikan secara proporsional.
- **Penggunaan Unit Relatif:** Saya memanfaatkan satuan fleksibel seperti `clamp()`, `rem`, dan `gap` agar ukuran tipografi serta jarak antar elemen menyesuaikan resolusi layar secara dinamis tanpa menyebabkan *horizontal overflow*.

---

#### 3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?

**Jawaban:**  
**Batasan yang Dirasakan pada Web Statis:**
- **Pembaruan Data Masih Manual:** Setiap kali ingin menambahkan sertifikat, dokumentasi, atau pengalaman organisasi baru, saya harus mengubah kode HTML secara langsung pada file `index.html`. Hal ini kurang efisien untuk jangka panjang.
- **Interaktivitas yang Terbatas:** Interaksi pengguna masih bersifat satu arah (hanya membaca konten dan melihat tautan), belum ada mekanisme interaktif seperti pengiriman pesan langsung dari pengunjung.
- **Ketiadaan Fitur Penyaringan (*Filtering/Search*):** Pengunjung belum bisa memfilter pengalaman atau prestasi berdasarkan kategori tertentu (misalnya memfilter kategori teknologi saja atau kepemimpinan saja) secara instan.

**Fungsionalitas Dinamis yang Ingin Ditambahkan ke Depan:**
1. **Integrasi Model Database Django (Pola MVT):** Menyimpan data pendidikan, pengalaman, sertifikat, dan keahlian ke dalam model database Django, sehingga pengelolaan konten dapat dilakukan secara praktis melalui Django Admin.
2. **Formulir Kontak Berbasis Django Forms:** Menyediakan formulir pesan interaktif dengan validasi sisi server dan penyimpanan pesan ke database.
3. **Fitur Filter dan Pencarian Dinamis:** Menambahkan fungsionalitas untuk menyaring dan mencari riwayat pencapaian berdasarkan kategori atau tahun secara dinamis.

---

### AI Disclosure

- **Alat yang Digunakan:** Gemini (Google AI)
- **Bagaimana AI Digunakan:** Saya memanfaatkan Gemini sebagai sarana konsultasi dan tanya jawab untuk menunjang proses belajar mandiri. Saya bertanya mengenai rekomendasi praktik terbaik dalam menyusun elemen semantik HTML5, strategi responsive layout di CSS dengan media queries, saran penataan palet warna yang harmonis, serta rekomendasi istilah profesional dalam bahasa Inggris yang tepat untuk resume.
- **Proses Pengerjaan Mandiri:** Seluruh perancangan konsep layout Bento Grid, penulisan kode HTML, penyusunan dan kurasi isi portofolio, pembuatan stylesheet CSS bertema Sage Green yang estetis, hingga pengujian responsivitas pada browser saya pelajari dan kerjakan secara mandiri. Saran yang diberikan oleh Gemini saya jadikan referensi belajar dan selalu saya telaah serta sesuaikan sendiri sebelum diimplementasikan ke dalam kode proyek.
