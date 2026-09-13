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

---

### Tugas 2: Implementasi Model-View-Template (MVT) pada Django

1. **Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.**

   **Jawaban:**  
   Alur kerja siklus *Request-Response* ketika pengguna membuka halaman baru (*Honors & Awards* di rute `/awards/`):

   - **Permintaan Pengguna (*HTTP GET Request*):**  
     Pengguna mengeklik menu **Honors & Awards** di navbar atau memasukkan URL `http://localhost:8000/awards/` di browser. Browser mengirimkan sebuah *HTTP GET Request* ke server Django.
   - **Pemeriksaan Rute Proyek (`portofolio/urls.py`):**  
     Server Django menerima request dan memeriksa berkas `portofolio/urls.py`. Berkas ini mencocokkan awalan rute dan menggunakan `path("", include("main.urls"))` untuk meneruskan penanganan rute `awards/` ke berkas `urls.py` milik aplikasi `main`.
   - **Pemeriksaan Rute Aplikasi (`main/urls.py`):**  
     Di `main/urls.py`, Django menemukan pola rute `path("awards/", show_awards, name="show_awards")` yang memetakan URL tersebut ke fungsi controller `show_awards` di `views.py`.
   - **Pengambilan Data di View (`main/views.py`):**  
     Fungsi `show_awards(request)` mengeksekusi kueri ORM: `Award.objects.all().order_by("-year", "-created_at")`. View membungkus seluruh data penghargaan tersebut ke dalam *dictionary context* bersama data profil.
   - **Akses Data oleh Model (`main/models.py`):**  
     Model `Award` bertindak sebagai representasi skema tabel di database. Django ORM menerjemahkan pemanggilan model menjadi perintah SQL ke database SQLite (`SELECT * FROM main_award ...`) dan mengembalikan kumpulan data objek (*QuerySet*) ke view.
   - **Rendering Antarmuka di Template (`templates/awards.html`):**  
     View memanggil fungsi `render(request, "awards.html", context)`. Mesin Django Template Language (DTL) membaca template `awards.html`, memproses perulangan `{% for award in award_list %}` untuk menampilkan kartu-kartu penghargaan secara dinamis, atau menampilkan pesan di blok `{% empty %}` jika data belum ada.
   - **Pengiriman Respons ke Browser (*HTTP Response*):**  
     Server Django mengembalikan berkas HTML yang telah lengkap terisi data dinamis beserta kode status `200 OK` ke browser pengguna untuk ditampilkan.

---

2. **Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.**

   **Jawaban:**  
   Menyimpan data pada Model Django (`models.py`) memberikan banyak keuntungan dibandingkan mengetik data secara manual (*hard-coded*) di dalam template HTML:

   - **Pemisahan Antara Data dan Tampilan (*Separation of Concerns*):**  
     Pemisahan antara lapisan data (`models.py`), logika pemrosesan (`views.py`), dan tampilan antarmuka (`templates/`) membuat struktur proyek lebih rapi, terorganisir, dan mudah dikelola.
   - **Kemudahan Pemeliharaan (*Maintainability*):**  
     Ketika ingin menambah, mengedit, atau menghapus riwayat penghargaan, kita cukup melakukannya melalui antarmuka **Django Admin** (`/admin/`) tanpa perlu menyentuh atau membongkar kode HTML sama sekali.
   - **Efisiensi Kode (*DRY - Don't Repeat Yourself*):**  
     Struktur tampilan kartu penghargaan cukup ditulis satu kali di template menggunakan looping `{% for %}`. Jika ingin mengubah desain kartu, kita cukup mengubah satu blok kode template tersebut saja dan perubahan otomatis berlaku untuk semua data.
   - **Integritas dan Validasi Data (*Data Integrity*):**  
     Model memastikan setiap data yang masuk sesuai dengan tipe dan aturan yang ditentukan (misalnya batasan panjang karakter di `CharField`, pilihan kategori pada `choices`, dan tanggal otomatis pada `DateTimeField`).
   - **Skalabilitas dan Fleksibilitas Fitur (*Scalability*):**  
     Data yang ada di database dapat dengan mudah diurutkan, difilter per kategori, dicari, maupun diubah ke dalam format JSON/API untuk kebutuhan integrasi aplikasi ke depannya.

---

3. **Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.**

   **Jawaban:**  
   Perbedaan perintah `makemigrations` dan `migrate` di Django:

   | Aspek | `python manage.py makemigrations` | `python manage.py migrate` |
   | :--- | :--- | :--- |
   | **Fungsi Utama** | Mendeteksi perubahan pada `models.py` dan membuat berkas skrip migrasi baru (*migration blueprint*). | Menjalankan instruksi migrasi tersebut untuk memperbarui skema fisik tabel pada database. |
   | **Lokasi Operasi** | Beroperasi pada level kode lokal (menghasilkan file Python di direktori `main/migrations/`). | Beroperasi langsung pada sistem database (`db.sqlite3`). |
   | **Dampak ke Database** | **Belum** mengubah struktur tabel database. | Mengubah, membuat, atau menghapus tabel dan kolom database secara nyata. |
   | **Analogi** | Seperti **Arsitek** yang merancang cetak biru denah ruangan di atas kertas. | Seperti **Tukang Bangunan** yang membangun ruangan fisik sesuai cetak biru tersebut. |

   **Contoh Perubahan Model yang Mengharuskan Kedua Perintah Tersebut:**

   - **Contoh 1 — Pembuatan Model Baru:**  
     1. Menambahkan definisi kelas model `Award` pada `main/models.py`.  
     2. Menjalankan `python manage.py makemigrations main` untuk menghasilkan berkas cetak biru `0002_award.py`.  
     3. Menjalankan `python manage.py migrate` agar Django mengeksekusi berkas tersebut dan membentuk tabel `main_award` di database.  
   - **Contoh 2 — Penambahan Field/Kolom Baru:**  
     1. Menambahkan atribut baru pada model `Award`, misalnya tautan sertifikat: `certificate_url = models.URLField(blank=True, null=True)`.  
     2. Menjalankan `makemigrations` untuk merekam penambahan kolom baru tersebut ke berkas migrasi.  
     3. Menjalankan `migrate` untuk menyisipkan kolom `certificate_url` ke tabel database yang sudah ada.

---

### AI Disclosure (Pernyataan Penggunaan Kecerdasan Buatan)

Dalam pengerjaan Tugas Individu Pemrograman Berbasis Platform (PBP) Semester Gasal 2026/2027, saya menjunjung tinggi integritas dan kejujuran akademik. Berikut adalah penjelasan terbuka mengenai pemanfaatan alat bantu kecerdasan buatan:

- **Alat Bantu yang Digunakan:** Gemini (Google AI).
- **Peran AI dalam Proses Belajar:**
  Sebagai mahasiswi Sistem Informasi, saya memosisikan AI secara etis sebagai **teman belajar dan rekan diskusi konsep (*study companion / peer tutor*)** untuk membantu saya memahami alur framework Django yang baru saya pelajari di semester ini. AI tidak digunakan untuk menyalin kode secara buta tanpa pemahaman.

- **Rincian Bantuan yang Dipelajari Bersama Gemini:**
  1. **Tugas 1 (Web Statis HTML5 & CSS3 Bento Grid):**
     - Berdiskusi mengenai struktur semantik HTML5 (`<header>`, `<main>`, `<section>`, `<article>`, `<footer>`).
     - Mempelajari cara kerja CSS Grid untuk tata letak Bento (`grid-template-columns: repeat(12, 1fr)`, `grid-column: span`) dan Media Queries responsif agar tampilan web rapi di layar ponsel.
     - Konsultasi pemilihan palet warna *Sage Green* dan *Warm Gold* yang elegan.
  2. **Tugas 2 (Implementasi MVT pada Django):**
     - Memahami alur kerja siklus *Model-View-Template* (MVT) pada Django.
     - Mempelajari cara kerja *Django Admin* (`admin.py`) untuk mengelola data secara dinamis dari tampilan web.
     - Merancang skema model `Award` (penggunaan `UUIDField`, `CharField`, `choices`, `DateTimeField`), pendaftaran rute di `urls.py`, serta penggunaan tag DTL `{% for %}` dan `{% empty %}` di template `awards.html`.
     - Menyusun skenario pengujian otomatis (*Unit Testing*) menggunakan `TestCase` untuk memastikan URL berstatus 200 OK, template terpanggil dengan benar, dan data tampil sesuai database.

- **Komitmen Pemahaman Mandiri:**
  Setiap konsep, kode logika, skema basis data, dan konfigurasi yang dirancang bersama Gemini telah saya pelajari secara bertahap, saya jalankan dan uji mandiri di terminal dan browser lokal, serta dipastikan lulus 100% pada `python manage.py test` sebelum diunggah ke GitHub dan server PWS Fasilkom UI.

