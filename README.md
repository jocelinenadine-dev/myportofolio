# Proyek Portofolio Web - Pemrograman Berbasis Platform (CSGE602022)

- **Nama:** Joceline Nadine Immanuella  
- **NPM:** 2506656835  
- **Kelas:** PBP A  
- **Program Studi:** S1 Sistem Informasi, Fakultas Ilmu Komputer, Universitas Indonesia  
- **Link Deployment PWS:** [http://joceline-nadine-myportofolio.pws.cs.ui.ac.id](http://joceline-nadine-myportofolio.pws.cs.ui.ac.id)  
- **Link Repository GitHub:** [https://github.com/jocelinenadine-dev/myportofolio](https://github.com/jocelinenadine-dev/myportofolio)

---

## Panduan Instalasi, Menjalankan Proyek, dan Pengujian (Setup, Run & Test)

### 1. Prasyarat Sistem
- **Python:** Versi 3.10 atau lebih baru (Disarankan Python 3.13)
- **Git:** Terpasang pada sistem
- **Virtual Environment (`venv`):** Modul bawaan Python

### 2. Langkah Instalasi & Setup Lokal

1. **Clone repositori proyek dari GitHub:**
   ```bash
   git clone https://github.com/jocelinenadine-dev/myportofolio.git
   cd myportofolio
   ```

2. **Buat dan aktifkan lingkungan virtual (*virtual environment*):**
   - **macOS / Linux:**
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```
   - **Windows:**
     ```cmd
     python -m venv env
     env\Scripts\activate
     ```

3. **Install dependensi proyek:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan migrasi database:**
   ```bash
   python manage.py migrate
   ```

### 3. Menjalankan Server Pengembangan (*Development Server*)

Jalankan perintah berikut pada terminal:
```bash
python manage.py runserver
```
Buka browser dan akses URL berikut:
- **Halaman Utama (Profile):** [http://localhost:8000/](http://localhost:8000/)
- **Halaman Experience:** [http://localhost:8000/experience/](http://localhost:8000/experience/)
- **Halaman Honors & Awards:** [http://localhost:8000/awards/](http://localhost:8000/awards/)
- **Endpoint API JSON Experience:** [http://localhost:8000/api/experience/](http://localhost:8000/api/experience/)
- **Endpoint API JSON Awards:** [http://localhost:8000/api/awards/](http://localhost:8000/api/awards/)

### 4. Menjalankan Automated Unit Tests

Proyek ini dilengkapi dengan 31 automated unit tests untuk memverifikasi keandalan model, view, routing URL, validasi form, CRUD, search filtering, dan serialisasi data JSON/XML.

Jalankan pengujian otomatis dengan perintah:
```bash
python manage.py test
```
*Output yang diharapkan: `Ran 31 tests in ...s — OK (Found 31 test(s), 0 errors, 0 failures)`.*

---

## Ringkasan Progres Mingguan (*Weekly Progress Tracker*)

| Minggu / Tugas | Fokus Utama & Capaian Fitur | Status |
| :--- | :--- | :--- |
| **Tugas 1 (Minggu 1)** | • Pembuatan Web Statis Portofolio Pribadi berbasis Semantic HTML5 (`<header>`, `<main>`, `<section>`, `<article>`, `<footer>`).<br>• Perancangan layout responsif *Sage Green Bento Grid* menggunakan CSS3 Grid & Flexbox.<br>• Optimasi mobile media queries (`max-width: 960px` dan `max-width: 600px`). | Selesai (100%) |
| **Tugas 2 (Minggu 2)** | • Inisialisasi arsitektur Model-View-Template (MVT) pada Django.<br>• Pembuatan model database `Experience` dan `Award` dengan skema `UUIDField`, `CharField`, `choices`, dan `DateTimeField`.<br>• Konfigurasi *Django Admin* (`admin.py`) untuk pengelolaan data dinamis.<br>• Pendaftaran rute URL modular dan pembuatan data migration untuk inisialisasi deployment PWS. | Selesai (100%) |
| **Tugas 3 (Minggu 3)** | • Penerapan **Template Inheritance** dengan kerangka utama [`templates/base.html`](templates/base.html) dan pembersihan duplikasi template.<br>• Pembuatan Django `ModelForm` ([`main/forms.py`](main/forms.py)) untuk `ExperienceForm` dan `AwardForm` dengan validasi server-side otomatis.<br>• Implementasi **Full CRUD (Create, Read, Update, Delete)** pada bagian Experience dan Awards.<br>• Pembuatan antarmuka modal konfirmasi hapus menggunakan HTML5 Popover API dengan backdrop blur.<br>• Fitur pencarian instan dinamis (*search bar*) dengan parameter kueri `?title=...`.<br>• Implementasi **Data Delivery** (API JSON dan XML) serta deserialisasi data internal.<br>• Penyusunan **31 automated unit tests** (100% lolos). | Selesai (100%) |

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

### Tugas 3: Form & Data Delivery pada Django

1. **Jelaskan mengapa kita menggunakan `ModelForm` pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan `{% csrf_token %}` pada form tersebut!**

   **Jawaban:**  
   - **Alasan Menggunakan `ModelForm` alih-alih Form HTML Manual:**
     1. **Pemetaan Otomatis dari Model ke Form (*Automatic Field Mapping*):**  
        `ModelForm` secara otomatis membaca definisi kolom dan tipe data pada `models.py` (seperti `CharField`, `TextField`, `choices`) dan langsung menerjemahkannya ke elemen form input HTML yang sesuai (`<input type="text">`, `<textarea>`, `<select>`). Kita tidak perlu menulis tag input satu per satu secara manual.
     2. **Validasi Data Otomatis & Keamanan Tipe Data (*Built-in Validation*):**  
        `ModelForm` menangani validasi data secara otomatis di sisi server (memeriksa apakah field wajib sudah terisi, memeriksa batas `max_length`, serta memastikan format input valid) melalui fungsi `form.is_valid()`. Jika ada input yang keliru, Django otomatis mengembalikan pesan error ke template tanpa perlu kita menulis logika pengecekan manual yang rumit.
     3. **Kemudahan Penyimpanan dan Pembaruan Data (*Instance Binding & Clean CRUD*):**  
        Untuk menyimpan data baru, kita cukup memanggil `form.save()`. Sedangkan untuk memperbarui (*update*) data yang sudah ada, kita cukup menyertakan objek data lama melalui argumen `instance=objek_terpilih`. Form akan langsung terisi (*pre-filled*) dengan data lama dan pembaruan akan langsung tersimpan ke database tanpa perlu menulis kueri SQL `UPDATE` manual.
     4. **Prinsip DRY (*Don't Repeat Yourself*):**  
        Menghindari duplikasi kode antara skema database dan form tampilan. Jika sewaktu-waktu ada perubahan field pada model, form akan otomatis menyesuaikan diri secara konsisten.

   - **Kewajiban Menambahkan `{% csrf_token %}`:**
     - Tag `{% csrf_token %}` adalah lapisan keamanan wajib di Django untuk mencegah serangan **Cross-Site Request Forgery (CSRF)**.
     - Serangan CSRF adalah jenis eksploitasi di mana situs web berbahaya pihak ketiga memanfaatkan sesi login / kredensial pengguna yang masih aktif di browser untuk mengirimkan permintaan palsu (seperti *HTTP POST request* untuk menambah, mengedit, atau menghapus data) ke server kita tanpa disadari oleh pengguna.
     - Tag `{% csrf_token %}` menghasilkan sebuah token keamanan acak yang unik, aman secara kriptografis, dan terikat dengan sesi pengguna saat ini. Token ini disisipkan sebagai input tersembunyi (*hidden input field*) pada form.
     - Saat form dikirimkan, middleware Django (`CsrfViewMiddleware`) memvalidasi keaslian token tersebut. Jika permintaan POST tidak memiliki token yang cocok, Django akan langsung memblokir request dengan respons `403 Forbidden`, sehingga melindungi data dari manipulasi pihak luar.

---

2. **Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?**

   **Jawaban:**  
   JSON (*JavaScript Object Notation*) menjadi format standar utama dalam pengembangan aplikasi web modern dibandingkan XML karena beberapa alasan utama:
   - **Struktur Ringkas dan Ukuran Data Lebih Kecil (*Lightweight & Efficient*):**  
     JSON menggunakan format pasangan kunci-nilai (*key-value*) dengan tanda kurung kurawal `{}` dan kurung siku `[]`, sedangkan XML membutuhkan tag pembuka dan penutup yang panjang (`<experience><title>...</title></experience>`). Format JSON yang ringkas membuat ukuran berkas (*payload size*) jauh lebih kecil sehingga menghemat kuota data dan mempercepat transmisi jaringan, terutama untuk pengguna ponsel pintar.
   - **Dukungan Alami (*Native Support*) pada JavaScript dan Frontend Modern:**  
     JSON diturunkan langsung dari sintaksis objek JavaScript. Di sisi browser dan framework frontend modern (seperti React, Vue, Flutter, maupun JavaScript murni), data JSON dapat langsung diubah menjadi objek JavaScript secara instan menggunakan fungsi bawaan `JSON.parse()`. Sebaliknya, XML memerlukan *XML DOM Parser* khusus yang lebih berat dan rumit untuk diekstraksi.
   - **Kecepatan Pemrosesan (*Faster Parsing Performance*):**  
     Karena strukturnya yang sederhana, proses serialisasi dan deserialisasi data JSON oleh mesin browser atau server berjalan jauh lebih cepat dibandingkan penguraian pohon XML (*XML DOM tree*).
   - **Keterbacaan yang Tinggi (*Human-Readable*):**  
     Bagi pengembang (*developer*), struktur JSON sangat bersih, intuitif, dan mudah dibaca secara visual. Di hampir semua bahasa pemrograman modern (Python `dict`, Java, Go, Dart), JSON langsung dipetakan ke struktur data bawaan seperti Dictionary, Map, atau List.
   - **Standar Utama Arsitektur RESTful API & Microservices:**  
     Ekosistem teknologi web saat ini telah mengadopsi JSON sebagai standar *de facto* untuk komunikasi antar-layanan (API) karena kemudahan integrasi dan fleksibilitasnya.

---

3. **Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?**

   **Jawaban:**  
   - **Alur Kerja Fungsi View Mengembalikan Data JSON:**
     1. **Penerimaan Permintaan (*HTTP GET Request*):**  
        Klien (browser, antarmuka JavaScript, atau aplikasi lain) mengirimkan permintaan GET ke endpoint API, misalnya `/api/experience/` atau `/api/awards/` (bisa disertai kueri pencarian `?title=...`).
     2. **Pengambilan Data dari Database via ORM (*QuerySet Retrieval*):**  
        Fungsi controller di `views.py` (seperti `get_experiences_json`) mengeksekusi kueri ORM Django: `Experience.objects.all().order_by("-started_at")` (atau menerapkan filter kueri jika ada parameter pencarian). Langkah ini menghasilkan sekumpulan objek Python bernama *QuerySet*.
     3. **Proses Serialisasi (*Data Serialization*):**  
        View memanggil fungsi serialisasi Django: `serializers.serialize("json", experiences)`. Modul ini mengiterasi setiap objek model, membaca seluruh field dan nilainya, lalu menerjemahkannya ke dalam bentuk string berformat JSON terstandarisasi.
     4. **Pembungkusan Respons HTTP (*HTTP Response Delivery*):**  
        String JSON tersebut dibungkus ke dalam objek `HttpResponse(experiences_json, content_type="application/json")` dengan kode status `200 OK`. Header `content-type: application/json` memberitahukan browser/klien bahwa data yang dikirimkan adalah payload JSON mentah.

   - **Mengapa Perlu Melakukan Proses Serialization?**
     - Objek model Django (*QuerySet* dan instance class Python) adalah objek internal yang tersimpan dalam memori Python runtime dan tidak dapat dikirimkan langsung melalui protokol jaringan HTTP.
     - Protokol HTTP hanya dapat mentransmisikan data dalam bentuk teks terstruktur atau representasi byte.
     - **Serialisasi adalah jembatan penerjemah** yang mengubah objek Python yang kompleks menjadi format string JSON yang terstandarisasi universal, sehingga data database dapat dipahami, diuraikan (*parsed*), dan digunakan kembali oleh platform atau aplikasi apapun di sisi klien.

---

### Langkah-Langkah Implementasi Checklist Tugas 3

Berikut adalah rincian tahapan implementasi yang telah saya lakukan untuk memenuhi seluruh checklist tugas:

1. **Refactoring Template Utama Menggunakan Template Inheritance (`base.html`):**
   - Membuat berkas [`templates/base.html`](templates/base.html) sebagai kerangka induk (*root template*) yang memuat deklarasi HTML5, meta viewport, font Google (Plus Jakarta Sans & Space Grotesk), pemanggilan stylesheet `/static/css/style.css`, navbar interaktif, penampung notifikasi *flash messages*, blok konten dinamis `{% block content %}`, dan footer.
   - Merefaktor seluruh template (`index.html`, `experience.html`, `awards.html`, `experience_form.html`, `award_form.html`) agar menggunakan sintaksis `{% extends "base.html" %}` sehingga tidak ada duplikasi kode boilerplate HTML.

2. **Membuat `ModelForm` Baru di `main/forms.py`:**
   - Mendefinisikan kelas `ExperienceForm(ModelForm)` pada [`main/forms.py`](main/forms.py) untuk merepresentasikan model `Experience`.
   - Memilih 4 field yang bervariasi: `title` (`TextInput`), `category` (`Select` dropdown dengan opsi kategori organisasi/duta/kepanitiaan), `description` (`Textarea`), dan `thumbnail` (`TextInput` URL). Field `id` dan `started_at` diabaikan karena ditangani otomatis oleh database.
   - Memasangkan widget custom dengan class styling (`form-input`, `form-select`, `form-textarea`) serta label bahasa Indonesia yang jelas.

3. **Membuat Fungsi Controller (Views) CRUD & Serialisasi Data:**
   - **Create:** Mengimplementasikan fungsi `create_experience` di [`main/views.py`](main/views.py) yang menerima *HTTP POST request*, memvalidasi data form melalui `form.is_valid()`, menyimpan data via `form.save()`, menyisipkan notifikasi sukses via `messages.success()`, dan melakukan `redirect` ke halaman daftar pengalaman.
   - **Update (Edit):** Mengimplementasikan fungsi `edit_experience` dengan mengambil objek data berdasarkan ID menggunakan `get_object_or_404(Experience, pk=experience_id)` dan menghubungkannya ke form melalui `ExperienceForm(request.POST or None, instance=experience)`.
   - **Delete:** Mengimplementasikan fungsi `delete_experience` yang menghapus entitas data secara aman hanya jika request berjenis *HTTP POST* dengan proteksi `{% csrf_token %}`.
   - **JSON & XML Data Delivery:** Mengimplementasikan fungsi `get_experiences_json` dan `get_experiences_xml` yang mengambil *QuerySet* `Experience.objects.all().order_by("-started_at")`, menerapkan filter pencarian jika parameter kueri `?title=...` dikirimkan, lalu mengembalikan data yang diserialisasi melalui `HttpResponse` dengan *content-type* yang sesuai.
   - **Deserialisasi & Display:** Mengimplementasikan fungsi `show_experience` yang memanggil `get_experiences_json`, melakukan deserialisasi data JSON menggunakan `serializers.deserialize("json", ...)`, dan menyalurkan objek data ke template `experience.html`.

4. **Membuat Antarmuka Pengguna (UI/UX) dan Modal Konfirmasi:**
   - Membuat halaman [`templates/experience_form.html`](templates/experience_form.html) yang *reusable* untuk mode tambah dan edit data dengan indikator judul dinamis (`is_edit`).
   - Membuat komponen modal konfirmasi hapus [`templates/components/experience_delete_modal.html`](templates/components/experience_delete_modal.html) berbasis **HTML5 Popover API** (`popover="auto"`) dan efek CSS *backdrop blur* sehingga data tidak terhapus tanpa konfirmasi sadar dari pengguna.
   - Menambahkan bilah pencarian dinamis (*search bar*) pada halaman `experience.html` dan `awards.html` untuk memfilter tampilan kartu secara instan.

5. **Penyusunan 31 Automated Unit Tests:**
   - Menyusun 31 skenario pengujian komprehensif pada [`main/tests.py`](main/tests.py) yang mencakup validasi form, alur CRUD lengkap, penanganan form invalid, filter search query, dan serialisasi API.
   - Menjalankan perintah `python manage.py test` dan memastikan seluruh 31 test lolos (100% OK).

---

## AI Disclosure & Catatan Penggunaan AI

Dalam pengerjaan Tugas 3 ini, saya memanfaatkan generative AI (Gemini) sebagai sarana diskusi untuk memperdalam konsep arsitektur Django, mekanisme keamanan form, serta perancangan skenario automated unit testing.

- **Tools:** Gemini (Google AI)
- **Model:** Gemini 2.5 Pro / Flash
- **Tautan Percakapan:** [Tautan Chat Log Gemini - Tugas 3 PBP](https://gemini.google.com/share/d/1sY624wqiyiVDcBsovaGRB5HkTiyqBnwo?usp=sharing)

---

### 1. Catatan Evaluasi & Penyesuaian Mandiri

Seluruh saran dan luaran dari AI telah saya telaah dan sesuaikan secara manual agar selaras dengan arsitektur proyek:

1. **Form Styling & Layout:**  
   Saran awal AI umumnya menggunakan rendering standar `{{ form.as_p }}`. Saya merancang *custom widgets* pada `forms.py` dengan kelas CSS terpisah (`form-input`, `form-select`, `form-textarea`) dan menyusun struktur grid form sendiri agar serasi dengan antarmuka *Sage Green Bento Grid*.
2. **Pembersihan Karakter Emoji:**  
   Menghapus seluruh karakter emoji pada kode dan template untuk menjaga estetika antarmuka yang bersih dan profesional.
3. **Penyelarasan Model Portofolio:**  
   Menyesuaikan seluruh logika CRUD agar merefleksikan model riil portofolio saya (`Experience` dan `Award`), bukan sekadar model generik tutorial.
4. **Keamanan Penghapusan Data & Modal Popover:**  
   Menambahkan lapisan konfirmasi hapus interaktif menggunakan HTML5 Popover API dengan efek *backdrop blur* serta memastikan penghapusan data hanya berjalan melalui metode HTTP POST.

---

### 2. Rangkuman Log Diskusi dan Prompt Percakapan

Berikut adalah transkrip pertanyaan/prompt yang saya ajukan selama berdiskusi dengan Gemini beserta ringkasan konsep yang diterapkan pada proyek:

#### 1. Konsep ModelForm dan Proteksi CSRF
- **Prompt:**  
  *"Halo Gemini, di Tugas 3 ini kita diminta bikin form pakai `ModelForm`. Boleh tolong jelasin secara konsep kenapa di Django kita harus pakai `ModelForm` dibanding bikin tag `<form>` dan `<input>` HTML manual di file template? Terus fungsi tag `{% csrf_token %}` yang wajib ada di dalam form itu secara teknis buat apa ya?"*
- **Poin Diskusi & Penerapan:**  
  ModelForm menyederhanakan pemetaan skema database ke input form dan menyediakan validasi data otomatis di sisi server. Tag `{% csrf_token %}` menghasilkan token kriptografis unik untuk melindungi server dari serangan Cross-Site Request Forgery. Konsep ini saya terapkan pada `ExperienceForm` dan `AwardForm` di `main/forms.py`.

---

#### 2. Mekanisme Update Form (*Instance Binding*)
- **Prompt:**  
  *"Gemini, di checklist tugas ada fitur Update/Edit data menggunakan form. Apa kita harus bikin file template HTML baru yang khusus buat edit, atau bisa pakai template form tambah data yang sudah ada? Terus gimana caranya supaya saat form edit dibuka, kotak inputnya udah otomatis terisi data lama yang mau diubah?"*
- **Poin Diskusi & Penerapan:**  
  Memahami teknik *instance binding* (`form = ExperienceForm(..., instance=experience)`) yang otomatis mengisi form dengan data lama dan mengeksekusi operasi update saat disimpan. Saya menyatukan antarmuka form tambah dan ubah dalam satu template `experience_form.html` menggunakan penanda `is_edit`.

---

#### 3. Keamanan Delete Data & Modal Konfirmasi
- **Prompt:**  
  *"Untuk fitur hapus data, gimana cara bikin yang aman dan tampilannya bagus? Aku gamau langsung kehapus begitu tombol diklik, maunya ada pop-up konfirmasi dulu tanpa emoji dan tanpa perlu library JavaScript luar."*
- **Poin Diskusi & Penerapan:**  
  Memastikan penghapusan data tidak menggunakan GET request dan membangun modal popover HTML5 murni (`popover="auto"`) dengan backdrop blur agar proses penghapusan aman dan intuitif.

---

#### 4. Serialisasi JSON/XML & Dynamic Search Filter
- **Prompt:**  
  *"Kenapa di aplikasi modern sekarang orang lebih milih format data JSON dibanding XML? Terus di view Django, gimana alur serialisasi dari QuerySet database sampai jadi response JSON, dan gimana cara nambahin filter pencarian judul (`?title=...`)?"*
- **Poin Diskusi & Penerapan:**  
  Memahami keunggulan efisiensi payload dan kemudahan parsing JSON di JavaScript dibandingkan XML. Mengimplementasikan fungsi `get_experiences_json` dan `get_experiences_xml` dengan dukungan filter kueri `?title=...`.

---

#### 5. Penyusunan 31 Automated Unit Tests
- **Prompt:**  
  *"Bantu aku merancang skenario automated unit tests menyeluruh di `main/tests.py`. Aku mau mastiin semua form (valid dan invalid), fitur edit, fitur delete, search bar, dan API JSON/XML semuanya dites dan lulus 100% saat dijalankan."*
- **Poin Diskusi & Penerapan:**  
  Menyusun skenario pengujian komprehensif di `main/tests.py` untuk menguji form validation, operasi CRUD, respon status HTTP, keamanan delete, serta endpoint API (31/31 tests OK).

