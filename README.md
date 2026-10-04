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

5. **(Opsional) Membuat Akun Superuser & Setup Peran Editor:**
   ```bash
   python manage.py createsuperuser
   ```
   *Masuk ke `http://localhost:8000/admin/`, buat Group baru bernama `Editor`, lalu tambahkan pengguna tertentu ke dalam grup tersebut untuk menguji hak akses peran Editor.*

### 3. Menjalankan Server Pengembangan (*Development Server*)

Jalankan perintah berikut pada terminal:
```bash
python manage.py runserver
```
Buka browser dan akses URL berikut:
- **Halaman Utama (Profile):** [http://localhost:8000/](http://localhost:8000/)
- **Halaman Registrasi:** [http://localhost:8000/register/](http://localhost:8000/register/)
- **Halaman Login:** [http://localhost:8000/login/](http://localhost:8000/login/)
- **Halaman Experience:** [http://localhost:8000/experience/](http://localhost:8000/experience/)
- **Halaman Honors & Awards:** [http://localhost:8000/awards/](http://localhost:8000/awards/)
- **Endpoint API JSON Experience:** [http://localhost:8000/api/experience/](http://localhost:8000/api/experience/)
- **Endpoint API JSON Awards:** [http://localhost:8000/api/awards/](http://localhost:8000/api/awards/)

### 4. Menjalankan Automated Unit Tests

Proyek ini dilengkapi dengan **50 automated unit tests** untuk memverifikasi keandalan model, view, routing URL, validasi form, CRUD, otorisasi 4 peran pengguna (Pengunjung, Pengguna Biasa, Editor, Superuser), manajemen cookie `last_login`, fitur Star, dan serialisasi data API.

Jalankan pengujian otomatis dengan perintah:
```bash
python manage.py test
```
*Output yang diharapkan: `Ran 50 tests in ...s — OK (Found 50 test(s), 0 errors, 0 failures)`.*

---

## Ringkasan Progres Mingguan (*Weekly Progress Tracker*)

| Minggu / Tugas | Fokus Utama & Capaian Fitur | Status |
| :--- | :--- | :--- |
| **Tugas 1 (Minggu 1)** | • Pembuatan Web Statis Portofolio Pribadi berbasis Semantic HTML5 (`<header>`, `<main>`, `<section>`, `<article>`, `<footer>`).<br>• Perancangan layout responsif *Sage Green Bento Grid* menggunakan CSS3 Grid & Flexbox.<br>• Optimasi mobile media queries (`max-width: 960px` dan `max-width: 600px`). | Selesai (100%) |
| **Tugas 2 (Minggu 2)** | • Inisialisasi arsitektur Model-View-Template (MVT) pada Django.<br>• Pembuatan model database `Experience` dan `Award` dengan skema `UUIDField`, `CharField`, `choices`, dan `DateTimeField`.<br>• Konfigurasi *Django Admin* (`admin.py`) untuk pengelolaan data dinamis.<br>• Pendaftaran rute URL modular dan pembuatan data migration untuk inisialisasi deployment PWS. | Selesai (100%) |
| **Tugas 3 (Minggu 3)** | • Penerapan **Template Inheritance** dengan kerangka utama [`templates/base.html`](templates/base.html) dan pembersihan duplikasi template.<br>• Pembuatan Django `ModelForm` ([`main/forms.py`](main/forms.py)) untuk `ExperienceForm` dan `AwardForm` dengan validasi server-side otomatis.<br>• Implementasi **Full CRUD (Create, Read, Update, Delete)** pada bagian Experience dan Awards.<br>• Pembuatan antarmuka modal konfirmasi hapus menggunakan HTML5 Popover API dengan backdrop blur.<br>• Fitur pencarian instan dinamis (*search bar*) dengan parameter kueri `?title=...`.<br>• Implementasi **Data Delivery** (API JSON dan XML) serta deserialisasi data internal.<br>• Penyusunan **31 automated unit tests** (100% lolos). | Selesai (100%) |
| **Tugas 4 (Minggu 4)** | • Implementasi sistem autentikasi bawaan Django: **Register** (`UserCreationForm`), **Login** (`AuthenticationForm`), dan **Logout**.<br>• Pembaruan antarmuka Navbar dengan status autentikasi dinamis (`{% if user.is_authenticated %}`).<br>• Manajemen **Session & Cookie**: penerbitan cookie `last_login` saat login dan penghapusan saat logout, serta penampilannya pada profil utama.<br>• Penerapan **Otorisasi 4 Peran Pengguna**: Pengunjung (Guest), Pengguna Biasa, Editor (Django Group `Editor`), dan Superuser (Admin).<br>• Proteksi server-side: `@login_required` dan pembatasan `PermissionDenied` (HTTP 403 Forbidden).<br>• Fitur interaktif **Star (★)** berbasis relasi `ManyToManyField(User)` pada model `Experience`.<br>• Penyusunan **50 automated unit tests** komprehensif (100% lolos). | Selesai (100%) |

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
        View memanggil fungsi serialisasi Django: `serializers.serialize("json", experiences, use_natural_foreign_keys=True)`. Modul ini mengiterasi setiap objek model, membaca seluruh field dan nilainya, lalu menerjemahkannya ke dalam bentuk string berformat JSON terstandarisasi.
     4. **Pembungkusan Respons HTTP (*HTTP Response Delivery*):**  
        String JSON tersebut dibungkus ke dalam objek `HttpResponse(experiences_json, content_type="application/json")` dengan kode status `200 OK`. Header `content-type: application/json` memberitahukan browser/klien bahwa data yang dikirimkan adalah payload JSON mentah.

   - **Mengapa Perlu Melakukan Proses Serialization?**
     - Objek model Django (*QuerySet* dan instance class Python) adalah objek internal yang tersimpan dalam memori Python runtime dan tidak dapat dikirimkan langsung melalui protokol jaringan HTTP.
     - Protokol HTTP hanya dapat mentransmisikan data dalam bentuk teks terstruktur atau representasi byte.
     - **Serialisasi adalah jembatan penerjemah** yang mengubah objek Python yang kompleks menjadi format string JSON yang terstandarisasi universal, sehingga data database dapat dipahami, diuraikan (*parsed*), dan digunakan kembali oleh platform atau aplikasi apapun di sisi klien.

---

### Tugas 4: Autentikasi, Session, Cookie, dan Hak Akses Pengguna

*(Catatan: Pertanyaan reflektif untuk Tugas 4 ditiadakan sesuai instruksi tim pengajar PBP).*

#### 1. Pembagian Hak Akses 4 Peran
- **Pengunjung (Guest / Unauthenticated):** Hanya dapat melihat halaman portofolio. Jika mencoba aksi tambah, edit, hapus, atau star, pengguna akan otomatis dialihkan ke halaman login (`/login/?next=...`).
- **Pengguna Biasa (Logged-in User):** Dapat melihat portofolio dan memberikan atau membatalkan Star pada kartu pengalaman. Aksi mutasi seperti tambah, edit, atau hapus diblokir dengan respons `HTTP 403 Forbidden`.
- **Editor (Anggota Grup `Editor`):** Dapat melihat portofolio, memberi Star, dan mengedit data Experience serta Award. Aksi tambah dan hapus tetap diblokir dengan `HTTP 403 Forbidden`.
- **Superuser (Admin / Pemilik Portofolio):** Memiliki hak akses penuh untuk seluruh operasi CRUD (tambah, lihat, edit, hapus) serta fitur Star.

---

#### 2. Panduan Menguji Peran Editor di Django Admin
1. Buat akun superuser melalui terminal jika belum ada:
   ```bash
   python manage.py createsuperuser
   ```
2. Buka antarmuka Django Admin di [http://localhost:8000/admin/](http://localhost:8000/admin/) dan login menggunakan akun superuser.
3. Masuk ke menu **Groups** $\rightarrow$ klik **Add Group**.
4. Beri nama grup persis: **`Editor`** $\rightarrow$ klik **Save**.
5. Buka menu **Users** $\rightarrow$ pilih akun pengguna yang ingin dijadikan editor $\rightarrow$ centang grup **`Editor`** pada bagian *Groups* $\rightarrow$ klik **Save**.
6. Akun tersebut kini memiliki hak akses Editor (tombol Edit akan muncul pada kartu, namun tombol Tambah dan Hapus tetap disembunyikan/diblokir).

---

#### 3. Rincian Fitur yang Diterapkan
- **Sistem Autentikasi:** Implementasi form register (`UserCreationForm`), login (`AuthenticationForm`), dan logout (`logout`). Navbar otomatis mendeteksi status pengguna via `{% if user.is_authenticated %}`.
- **Session & Cookie `last_login`:** Cookie dibuat saat proses login berhasil, ditampilkan pada kartu profil di halaman utama (`show_main`), dan dihapus saat pengguna logout.
- **Proteksi Server-Side:** Memanfaatkan `@login_required` dan `PermissionDenied` pada `views.py` agar pembatasan hak akses tidak bisa ditembus langsung melalui URL.
- **Fitur Interaktif Star:** Menambahkan relasi `starred_by = models.ManyToManyField(User, ...)` pada model `Experience` dan view `toggle_star` dengan metode POST berproteksi token CSRF.
- **Automated Unit Tests:** Menyusun 50 unit test di `main/tests.py` untuk menguji form, CRUD, cookie, fitur star, dan otorisasi 4 peran pengguna (50/50 test lulus OK).

---

## AI Disclosure & Catatan Penggunaan AI

Dalam pengerjaan tugas portofolio ini, saya berdiskusi dengan Google Gemini untuk memperdalam pemahaman mengenai konsep otorisasi Django, keamanan otentikasi, dan perancangan skenario unit testing.

- **Tools:** Gemini (Google AI)
- **Model:** Gemini 2.5 Pro / Flash
- **Tautan Percakapan Publik:** [https://gemini.google.com/share/d/1_Fuz4e5kjXMxK0enMutm6VqO_xx5NWeN?usp=sharing](https://gemini.google.com/share/d/1_Fuz4e5kjXMxK0enMutm6VqO_xx5NWeN?usp=sharing)

### Catatan Evaluasi & Penyesuaian Mandiri:
1. **Penerapan Otorisasi 4 Peran:** Menyusun logika hak akses di backend menggunakan helper `is_editor_user` dan `PermissionDenied` agar respons status HTTP 403 Forbidden tertangani secara standar bawaan Django.
2. **Penyesuaian Tampilan Bento Grid:** Merancang styling form mandiri pada `forms.py` agar serasi dengan antarmuka Bento Grid portofolio.
3. **Pembersihan Emoji:** Menghapus seluruh karakter emoji pada kode, template, dan antarmuka agar tampilan web bersih dan profesional.
4. **Penyelarasan Model Portofolio:** Menyesuaikan seluruh operasi CRUD dan relasi `ManyToManyField` dengan model riil portofolio saya (`Experience` dan `Award`).
5. **Keamanan Hapus Data:** Menambahkan modal konfirmasi popover HTML5 murni dan memastikan penghapusan hanya berjalan melalui metode HTTP POST demi integritas data.

### Tugas 5: Web Interactivity with JavaScript

**1. Jelaskan apa itu *debouncing* dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!**

**Jawaban:**  
*Debouncing* adalah teknik *programming* untuk menunda (*delay*) eksekusi sebuah fungsi sampai pengguna benar-benar berhenti melakukan aksi (misalnya berhenti mengetik) selama rentang waktu tertentu. 

Pada fitur pencarian menggunakan AJAX, fungsi ini sangat krusial karena:
- **Mencegah Beban Server (*Server Overload*):** Tanpa *debouncing*, setiap huruf yang diketik oleh *user* akan langsung menembakkan satu *request* ke server. Jika *user* mengetik kata "Django", browser akan mengirim 6 *request* beruntun dalam hitungan milidetik. *Debouncing* memastikan *request* hanya dikirim (misalnya setelah jeda 300ms) saat *user* sudah selesai merangkai kata.
- **Menghindari *Race Condition*:** Karena AJAX bersifat *asynchronous*, respon dari *request* pertama bisa saja tiba lebih lambat dari *request* terakhir, yang berisiko membuat hasil pencarian di layar jadi melompat-lompat dan tidak sinkron dengan kata kunci terakhir.

**2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?**

**Jawaban:**  
Secara bawaan, fungsi `fetch()` di JavaScript berjalan secara asinkron (*asynchronous*) dan langsung mengembalikan objek *Promise* (janji bahwa data akan datang), bukan mengembalikan datanya langsung. Fungsi dari sintaks `await` adalah untuk memerintahkan JavaScript agar menunda eksekusi baris kode di bawahnya sampai proses *fetch* tersebut benar-benar selesai (di-*resolve*) dan datanya utuh terkirim dari server.

Jika kita **tidak menggunakan `await`**:
Variabel penampung tidak akan berisi JSON atau respon dari server, melainkan hanya status *Promise* yang menggantung (*pending*). Akibatnya, baris kode selanjutnya yang mencoba memanipulasi DOM atau membaca data tersebut akan langsung dieksekusi duluan, menyebabkan pesan *error* (seperti `undefined`) karena objek yang ingin dibaca secara harfiah belum tersedia di memori.

**3. Jelaskan apa itu serangan XSS (*Cross-Site Scripting*) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui *template* Django!**

**Jawaban:**  
XSS (*Cross-Site Scripting*) adalah celah keamanan di mana penyerang dapat menyuntikkan skrip berbahaya (biasanya JavaScript seperti `<script>` atau `onerror`) ke input data. Ketika data itu ditampilkan di layar pengguna lain, skrip tersebut akan ikut tereksekusi oleh browser dan berpotensi mencuri data krusial seperti *session cookies*.

**Mengapa manipulasi DOM lewat JS lebih rentan?**
- Ketika menggunakan **Template Django** (`{{ variable }}`), mesin DTL memiliki fitur *Autoescaping* bawaan. Ia otomatis mengubah karakter berbahaya seperti `<` dan `>` menjadi entitas aman (`&lt;` dan `&gt;`) sebelum HTML dikirim ke klien, sehingga skrip tidak akan bisa jalan.
- Namun, ketika menggunakan **AJAX**, kita merender datanya secara manual di sisi klien (JS) menggunakan properti seperti `innerHTML` atau `insertAdjacentHTML()`. Browser akan memproses teks yang masuk secara mentah. Jika kita lupa membersihkan datanya secara manual di sisi klien (dengan fungsi kustom `escapeHtml`) dan di sisi server (dengan `strip_tags`), skrip berbahaya itu akan langsung tereksekusi tanpa halangan.

---

### AI Disclosure (Pernyataan Penggunaan Kecerdasan Buatan)

Dalam pengerjaan Tugas Individu 5 PBP, saya memosisikan AI sebagai *study companion* untuk membantu memperkuat pemahaman logika saya mengenai *asynchronous JavaScript* dan manipulasi DOM, dengan rincian:

- **Alat Bantu:** Gemini (Google AI)
- **Tautan Log Diskusi:** [https://gemini.google.com/share/d/1NgaZ8VFpxsq6rwDAz5Osu8xTmGl9vhV5?usp=sharing](https://gemini.google.com/share/d/1NgaZ8VFpxsq6rwDAz5Osu8xTmGl9vhV5?usp=sharing)
- **Rincian Bantuan yang Dipelajari:**
  1. Mempelajari konsep serialisasi JSON di Django dan mengapa *QuerySet* tidak bisa dikirim langsung ke sisi *frontend* JavaScript.
  2. Berdiskusi mendalam tentang cara kerja teknik optimasi *Debouncing* pada fitur *search bar* dinamis.
  3. Membedah logika di balik kewajiban penggunaan sintaks `await` pada `fetch()` API.
  4. Konsultasi mengenai celah kerentanan injeksi XSS pada *client-side rendering* dibandingkan dengan DTL (*Django Template Language*).
  
Saya mengonfirmasi bahwa seluruh kode AJAX, penataan Modal, pengaturan notifikasi *Toast*, serta sanitasi keamanan data (*strip_tags*), murni diimplementasikan, diuji otomatis dengan *unit testing*, dan dikelola secara bertahap melalui sistem kontrol versi Git oleh saya sendiri.
