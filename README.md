# Proyek Portofolio Web - Pemrograman Berbasis Platform (CSGE602022)

- **Nama:** Joceline Nadine Immanuella  
- **NPM:** 2506656835  
- **Kelas:** PBP A  
- **Program Studi:** S1 Sistem Informasi, Fakultas Ilmu Komputer, Universitas Indonesia  
- **Link Deployment PWS:** [http://joceline-nadine-myportofolio.pws.cs.ui.ac.id](http://joceline-nadine-myportofolio.pws.cs.ui.ac.id)  
- **Link Repository GitHub:** [https://github.com/jocelinenadine-dev/myportofolio](https://github.com/jocelinenadine-dev/myportofolio)

---

### Tugas 1: Pembuatan Web Portofolio Statis dengan HTML5 & CSS3

#### 1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti `<section>`, `<article>`, atau `<aside>`? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?

**Jawaban:**  
Ya, dalam merancang website portofolio ini, saya memilih untuk menggunakan elemen semantik HTML5 seperti `<header>`, `<main>`, `<section>`, `<article>`, dan `<footer>`, bukan hanya menumpuk tag `<div>` saja.

Alasan dan bagaimana elemen semantik ini sangat membantu saya dalam membangun website:
1. **Membuat struktur kode jadi jauh lebih rapi dan jelas pembagiannya:**
   - Kalau semua bagian cuma dibungkus pakai tag `<div>`, kodenya jadi gampang bikin pusing saat sudah panjang karena kita tidak tahu kotak ini fungsinya untuk apa dan tag penutup `</div>`-nya milik siapa.
   - Dengan elemen semantik, saya bisa membagi isi website dengan sangat teratur:
     - Bagian paling atas untuk nama identitas dan status saya bungkus menggunakan `<header>`.
     - Seluruh badan utama halaman portofolio dibungkus di dalam satu tag `<main>`.
     - Bagian-bagian besar saya pisah ke dalam `<section>` masing-masing, seperti modul perkenalan profil utama (hero), kepemimpinan di luar kampus, daftar lomba/prestasi (awards), keahlian (skills), dan kontak.
     - Konten yang berupa kartu informasi mandiri (seperti riwayat pendidikan di UI dan SMAK 2 Penabur, kartu kegiatan organisasi, serta kartu penghargaan) saya bungkus memakai tag `<article>`.
     - Bagian penutup di paling bawah ditutup dengan tag `<footer>` untuk informasi hak cipta.
2. **Membantu aksesibilitas website untuk pembaca layar (*screen reader*):**
   - Tag semantik memberi tahu browser dan teknologi pembaca layar tentang fungsi sebenarnya dari setiap bagian halaman. Ini sangat membantu pengguna difabel yang menggunakan *screen reader* agar mereka bisa langsung melompat ke bagian yang ingin dibaca (misalnya langsung loncat ke `<main>` atau `<section>` tertentu) tanpa harus membaca kode yang berantakan.
3. **Mempermudah proses styling di CSS:**
   - Karena struktur HTML-nya sudah punya nama tag yang bermakna dan teratur, saya jadi jauh lebih gampang saat menulis selektor di CSS dan mengatur tata letak Bento Grid tanpa takut styling-nya bentrok atau berantakan.

---

#### 2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?

**Jawaban:**  
**Tantangan tata letak yang saya temui saat membuat website agar responsive:**
- **Layout Bento Grid yang gepeng dan sempit di layar HP:** Di layar laptop yang lebar, desain Bento Grid 12 kolom terlihat sangat rapi karena beberapa kartu bisa diletakkan berdampingan (ada yang 2 kolom dan 3 kolom). Namun, saat dibuka di layar HP yang sempit, kartu-kartu yang dipaksa berdampingan itu menjadi sangat kecil dan tulisan di dalamnya jadi bertumpuk dan tidak nyaman dibaca.
- **Teks panjang yang meluap keluar kotak (*overflow*):** Teks yang agak panjang seperti alamat email `jocelinenadine@gmail.com` dan tombol tautan media sosial sempat membuat halaman website bisa digeser-geser ke samping (terjadi *horizontal scroll* yang merusak tampilan mobile).
- **Penataan Foto Profil:** Di desktop, foto profil pas diletakkan di sebelah kanan tulisan bio. Namun di HP, jika dipaksakan berdampingan dengan teks, layarnya tidak cukup, sehingga fotonya harus ditata ulang agar posisinya turun ke bawah teks.

**Cara mengevaluasi dan mengatur posisi elemen di tampilan mobile:**
1. **Mengubah layout menjadi 1 kolom vertikal menggunakan Media Queries:**
   - Saya menggunakan Media Queries dengan breakpoint `@media (max-width: 960px)` untuk tablet dan `@media (max-width: 600px)` untuk HP.
   - Di layar HP, semua susunan grid yang tadinya multikolom langsung diubah menjadi 1 kolom lurus ke bawah (`grid-template-columns: 1fr`). Dengan begitu, pengunjung bisa membaca seluruh informasi dengan nyaman hanya dengan menggulir layar ke bawah.
2. **Menentukan urutan prioritas yang harus dilihat pengguna:**
   - Di layar kecil, informasi yang paling utama (Nama, NPM, Program Studi, dan Tagline singkat) ditaruh paling atas, baru setelah itu disusul oleh foto profil dengan batas lebar maksimal (`max-width: 260px`) agar foto tidak memenuhi seluruh layar ponsel.
   - Bagian pengalaman organisasi dan prestasi disusun urut dari yang paling baru (tahun 2026) agar yang pertama kali dibaca adalah kegiatan terkiniku.
3. **Menggunakan ukuran yang fleksibel (*clamp* dan *nowrap*):**
   - Untuk ukuran font judul, saya memanfaatkan fungsi `clamp()` agar ukuran teks bisa membesar dan mengecil secara otomatis mengikuti lebar layar tanpa perlu diatur ulang manual di setiap ukuran.
   - Memasang `white-space: nowrap` pada tombol kontak dan memastikan `overflow-x: hidden` agar tidak ada lagi masalah halaman tergeser ke samping di HP.

---

#### 3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?

**Jawaban:**  
**Batasan yang benar-benar saya rasakan saat membuat website statis ini:**
- **Sangat repot saat menambah atau mengubah isi data:** Saat saya memasukkan seluruh data pengalaman organisasi (seperti MPK, Google Student Ambassador, Duta GenRe, BEM, dll) dan daftar prestasi, semuanya harus diketik secara manual satu per satu langsung di dalam file `index.html`. Kalau ke depannya ada kegiatan baru, sertifikat baru, atau ada typo tulisan, saya harus membuka file HTML lagi, mencari baris kodenya di antara ratusan baris, lalu mengeditnya secara manual. Ini sangat tidak praktis dan rawan membuat kodenya rusak atau salah hapus tag.
- **Website hanya berfungsi sebagai pajangan satu arah:** Pengunjung yang membuka web ini cuma bisa membaca informasi dan mengklik tautan biasa. Belum ada fitur interaksi nyata di mana pengunjung bisa langsung mengirimkan pesan atau ajakan kolaborasi melalui halaman web dan datanya tersimpan ke sistem.
- **Konten menumpuk semua di satu halaman tanpa ada filter:** Karena datanya statis, semua daftar kepanitiaan, organisasi, dan lomba ditampilkan sekaligus dari atas ke bawah. Pengunjung harus menggulir halaman yang panjang untuk mencari informasi tertentu karena belum ada tombol untuk menyaring atau mencari data (misalnya ingin memfilter hanya kegiatan bidang teknologi atau hanya daftar lomba).

**Fungsionalitas dinamis yang ingin saya tambahkan nanti menggunakan Django:**
1. **Memisahkan data dan tampilan menggunakan Database Model Django (`models.py`):**
   - Saya ingin membuat tabel database untuk menyimpan data Riwayat Pendidikan, Pengalaman Organisasi, Prestasi, dan Keahlian.
   - Dengan begitu, di file HTML kita tidak perlu mengetik panjang-panjang, cukup memakai looping Django `{% for item in experiences %}`. Nantinya, kalau mau menambah atau mengedit isi portofolio, saya cukup login ke halaman Django Admin dan mengisi form data di sana tanpa perlu menyentuh kodingan HTML sama sekali.
2. **Membuat Formulir Kontak yang Terhubung ke Database (Django Forms):**
   - Menggantikan tautan email biasa dengan form kirim pesan interaktif yang dibuat menggunakan `forms.ModelForm` dan dilengkapi proteksi keamanan `{% csrf_token %}`. Pesan yang dikirim oleh pengunjung web bisa langsung tersimpan dengan aman ke database dan bisa saya baca lewat admin.
3. **Menambahkan Tombol Filter Kategori dan Pencarian:**
   - Menambahkan fitur filter kategori (misalnya tombol *Tech*, *Leadership*, *Awards*) agar pengunjung bisa memilih jenis pengalaman yang ingin mereka lihat tanpa perlu menggulir seluruh halaman web dari awal.

---

### AI Disclosure (Pernyataan Penggunaan Kecerdasan Buatan)

Dalam pengerjaan Tugas 1 Pemrograman Berbasis Platform (PBP) ini, saya memegang teguh prinsip kejujuran akademik. Berikut adalah penjelasan terbuka dan rinci mengenai pemanfaatan kecerdasan buatan selama proses pengerjaan:

- **Alat Bantu yang Digunakan:** Gemini (Google AI).
- **Peran AI dalam Proses Belajar Saya:**
  Karena materi perkuliahan PBP (seperti arsitektur framework Django, struktur file proyek, dan styling CSS modern) merupakan hal yang baru bagi saya di semester ini, saya memanfaatkan Gemini sebagai **teman belajar dan tutor diskusi mandiri (*study companion*)** untuk membantu saya memahami alur pengerjaan tugas dari awal secara bertahap di luar jam kelas.

- **Rincian Bantuan yang Saya Pelajari Bersama Gemini:**
  1. **Memahami Fungsi Setiap File dalam Proyek Django dari Nol:**
     - Karena awalnya saya belum paham struktur bawaan Django, saya bertanya ke Gemini untuk memahami apa fungsi masing-masing file yang ada di proyek, seperti apa fungsi `manage.py`, `settings.py`, `urls.py`, `views.py`, serta apa bedanya folder `templates/` (untuk file HTML) dan folder `static/` (untuk file CSS dan gambar).
     - Saya juga mempelajari file apa saja yang harus diubah saat ingin menghubungkan tampilan HTML (`views.py` dan `urls.py`) dan cara mengatur `STATICFILES_DIRS` di `settings.py` agar CSS dan gambar bisa terbaca saat di-deploy ke PWS.
  2. **Mempelajari dan Menghafal Sintaks CSS yang Baru:**
     - Saya berkonsultasi mengenai bagaimana cara kerja CSS Grid untuk membuat layout Bento (seperti fungsi `repeat(12, 1fr)`, `grid-column: span`, dan `gap`), cara mengatur Flexbox agar elemen berada di tengah secara rapi, serta bagaimana cara menuliskan Media Queries (`@media (max-width: ...px)`) untuk membuat tampilan web responsif di HP.
  3. **Mengatasi Tampilan yang Rusak / Error (*Troubleshooting Layout*):**
     - Saat awal mencoba tampilan di layar HP, teks email saya sempat keluar dari kotak kartu dan layarnya bisa tergeser ke kanan. Saya menanyakan ke Gemini kenapa hal itu bisa terjadi, dan dari penjelasan tersebut saya belajar cara mengatasinya menggunakan properti `white-space: nowrap`, `overflow-x: hidden`, dan merapikan padding.
  4. **Konsultasi Pemilihan Warna Desain:**
     - Saya meminta saran perpaduan kode warna HEX untuk tema *Sage Green* yang lembut agar tampilan portofolio terlihat bersih, modern, dan tetap mudah dibaca.

- **Komitmen Pengerjaan Mandiri:**
  Semua penjelasan alur file, konsep struktur Django, dan saran sintaks CSS dari Gemini selalu saya baca dan pelajari terlebih dahulu agar saya benar-benar mengerti fungsinya. Seluruh penulisan kode HTML semantik, perancangan tata letak Bento Grid, penulisan file CSS, pengisian seluruh isi portofolio, hingga proses pengujian di browser dan *deployment* ke server PWS CS UI saya kerjakan dan pahami secara mandiri.
