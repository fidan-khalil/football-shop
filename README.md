### Tugas 2 ###

link aplikasi PWS: https://fidan-khalil-footballshop.pbp.cs.ui.ac.id/

Langkah-langkah implementasi:
    1. Membuat sebuah proyek Django baru
        - Membuat direktori baru bernama football-shop dan membuat serta mengaktifkan env pada terminal dengan menjalankan python -m venv env dan env\Scripts\activate

        -  Membuat dan menginstall requirements.txt, lalu membuat proyek Django bernama football_shop

        - Membuat file .env untuk menggunakan database SQLite dan file .env.prod untuk menggunakan database PostgreSQL

        - Memodifikasi file settings.py untuk meng-import environment variables dari file .env, menambahkan host lokal ke list host yang diizinkan untuk mengakses web, menambahkan konfigurasi PRODUCTION, dan mengubah konfigurasi DATABASES

        - Menghubungkan ke github dan pws

    2. Membuat aplikasi dengan nama main pada proyek:
        - Menjalankan perintah python manage.py startapp main

    3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main:
        - Menambahkan aplikasi main pada list aplikasi 

    4. Membuat model pada aplikasi main:
        - Mengisi file models.py dengan membuat class Product dan berisi atribut name bertipe Charfield, price bertipe IntegerField, description bertipe TextField, thumbnail bertipe URLField, category bertipe CharField, dan is_featured bertipe BooleanField

    5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML:
        - Membuat sebuah fungsi bernama show_main dengan parameter request. Lalu membuat context yang berisi NPM, nama, dan kelas yang berguna untuk dikirimkan ke template. Lalu fungsi me-return fungsi render

        - Mengubah main.html menjadi struktur Django, agar dapat menampilkan data yang diambil dari model tanpa menulis manual

    6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py:
        - Membuat file urls.py di dalam direktori main dan mengisinya dengan path ke main.views

        - Menghubungkan urls.py pada direktori main ke urls.py pada direktori proyek football-shop

    7. Melakukan deployment ke PWS:
        - Membuat projek baru pada PWS dan menyimpan username dan password

        - Mengubah isi pada tab environs dengan copy paste isi file .env.prod

        - Menambahkan list host yang diizinkan untuk mengakses web dengan link deployment PWS

        - Menjalankan git remote add pws, git branch -M master, git push pws master pada terminal

        -Mengisi username dan password Git Credential Manager dengan username dan password yang tadi sudah disimpan



Bagan Request:
    request -> urls.py -> views.py -> models.py -> views.py -> template -> response

    browser akan melakukan request dan urls.py memetakan URL ke view tertentu. Lalu views.py akan mengambil data dari models.py dan memproses datanya. Data tersebut akan dikirim ke template dan mengubah berkas html. Barulah response akan muncul pada browser



Peran settings.py:
    1. Menentukan penggunaan SQLite atau PostgreSQL atau yang lain
    2. Menentukan siapa saja host yang diizinkan untuk mengakses web
    3. Mendaftarkan aplikasi yang digunakan pada proyek
    4. Middleware



Cara kerja migrasi database di Django:
    1. Membuat berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data
    2. Setelah menjalankan perintah migrate, perubahan yang terjadi akan diimplementasikan ke basis data



Alasan framework Django dijadikan permulaan pembelajaran pengembangan perangkata lunak:
    1. Framework Django memiliki struktur yang jelas, karena menggunakan pola MVT (Model-View-Template) yang memungkinkan untuk memisah logika model, logika view, dan logika tampilan sejak awal
    2. Django sudah menyediakan perlindungan terhadap serangan umum seperti SQL Injection, XSS, CSRF, dan lain-lain secara otomatis
    3. Django menjadi jembatan ke konsep lanjutan seperti REST API, deployment, dan framework lain.
    4. Django banyak digunakan di industri, seperti Instagram dan Pinterest


### Tugas 3 ###

Alasan mengapa kita membutuhkan data delivery dalam pengimplementasian sebuah platform:
    Karena dalam implementasi sebuah platform, ada kalanya kita membutuhkan data dari stack lain. Oleh karena itu, kita memerlukan data delivery untuk mengirimkan data dari suatu stack ke stack lainnya.

Lebih baik mana antara XML dengan JSON dan mengapa JSON lebih populer dibandingkan XML:
    Menurut saya lebih baik JSON, karena syntax JSON lebih ringkas dan lebih mudah dibaca oleh manusia dibandingkan syntax XML, dan untuk parsing, JSON lebih ringan dan cepat dibandingkan dengan XML.

    Alasan kenapa JSON lebih populer dibandingkan XML adalah:
        1. JSON butuh lebih sedikit karakter, sehingga untuk transfer data lebih ringkas dan lebih cepat
        2. Framework-framework modern lebih mengutamakan JSON dibanding XML
        3. Syntax JSON lebih mudah dibaca oleh manusia dibanding syntax XML

Fungsi method is_valid():
    Untuk mengecek apakah data yang dikirim valid (form tidak kosong, tipe field sesuai, dan sesuai dengan aturan-aturan lainnya) atau tidak

Mengapa kita membutuhkan csrf_token saat membuat form di Django dan apa yang terjadi ketika tidak menambahkan csrf_token:
    csrf_token dibutuhkan untuk memastikan request HTTP dibuat oleh halaman dari web sendiri, bukan dari web jahat yang memaksa browser pengguna request ke web kita. Jika csrf_token tidak ditambahkan tetapi middleware aktif, request akan ditolak (403). Sedangkan jika csrf_token dan middleware dinonaktifkan, penyerang dapat membuat request seakan-akan korban yang sedang login. Hal ini dapat dimanfaatkan oleh penyerang dengan cara penyerang membuat halaman yang memuat form HTML yang membuat request ke server web. Ketika korban mengunjungi halaman yang dibuat oleh penyerang, server akan melihat request sebagai request yang sah dan dapat mengakses web dengan akun korban.

langkah-langkah implementasi:
    1. Menambahkan 4 fungsi views baru:
        XML dan JSON:
            - Membuat sebuah variabel untuk menyimpan hasil query dari seluruh data yang ada pada Product

            - Ubah objek model menjadi format XML atau JSON

            - Lalu fungsi me-return berupa HttpResponse
        
        XML by id dan JSON by id:
            - Membuat sebuah variabel untuk menyimpan hasil query dari data dengan id tertentu

            - Ubah objek model menjadi format XML atau JSON

            - Jika product ditemukan, fungsi akan me-return berupa HttpResponse, sedangkan jika tidak ditemukan, fungsi akan me-return status 404

    2. Routing URL untuk masing-masing views:
        - Import fungsi-fungsi yang dibuat pada urls.py

        - Membuat path URL ke dalam list urlpatterns untuk mengakses fungsi-fungsi yang sudah di-import
    
    3. Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form dan tombol "Detail" pada setiap data objek model:
        - Membuat file forms.py pada direktori main untuk membuat struktur form yang dapat menerima data product baru.

        - Menambahkan fungsi pada file views.py untuk membuat product baru dan menampilkan detail dari product

        - Import fungsi-fungsi yang dibuat pada views.py ke urls.py dan mebambahkan path URL ke list urlpatterns

        - Pada file main.html, menambahkan button "Add" yang akan redirect ke halaman form. Lalu menampilkan semua product yang ada pada product_list yang masing-masing terhubung ke halaman detail dari product

    4. Membuat halaman form:
        Membuat file HTML baru untuk halaman form input

    5. Membuat halaman detail product:
        Membuat file HTML baru untuk halaman detail dari product

Akses keempat URL pada postman: https://drive.google.com/drive/folders/1-Vb6tE-PDQb6DARx55CB8C2QZ9W8lu8R?usp=sharing


### Tugas 4 ###

Apa itu Django AuthenticationForm? dan kelebihan kekurangannya:
    Django AuthenticationForm adalah form bawaan Django untuk login user. Berguna untuk memvalidasi username dan password, user ada di database, dan akun user aktif.

    Kelebihan:
        1. Tidak perlu membuat form login manual
        2. Mudah untuk di-custom
        3. Sudah menyediakan validasi keamanan

    kekurangan:
        1. Terbatas untuk username dan password, tidak bisa login menggunakan email atau OTP
        2. Tidak menyediakan UI, sehingga membutuhkan template sendiri

Perbedaan Autentikasi dan Otorisasi:
    - Autentikasi = proses memverifikasi identitas user
    - Otorisasi = proses menentukan hak akses user setelah autentikasi

    Autentikasi di Django menggunakan fungsi authenticate, login, dan logout

    Otorisasi di Django menggunakan @login_required

Kelebihan dan kekurangan session dan cookies:
    Cookies
    Kelebihan:
        1. Tidak membebani server karena data disimpan di client
        2. Mudah diakses melalui JavaScript
    
    Kekurangan:
        1. Kapasitasnya terbatas
        2. Rawan untuk dimanipulasi user

    Session
    Kelebihan:
        1. Kapasitas lebih besar daripada cookies
        2. Data lebih aman karena data tidak disimpan di client

    Kekurangan:
        1. Membebani server
        2. Memerlukan manajemen session

Apakah cookies aman secara default? dan bagaimana Django menangani hal tersebut?
    Cookies tidak aman secara default, Django menangani hal ini dengan cara menyediakan:
        1. SESSION_COOKIE_SECURE = True -> cookie hanya dikirim melalui HTTPS
        2. SESSION_COOKIE_HTTPONLY = True -> cookie tidak bisa diakses JavaScript
        3. SESSION_COOKIE_SAMESITE = 'Lax' / 'Strict' -> mencegah CSRF lintas website
        4. {% csrf_token %}

Langkah-langkah implementasi checklist:
    1. Membuat fungsi dan form registrasi:
        - Import UserCreationForm pada views.py
        - Membuat fungsi register() pada views.py
        - Membuat halaman untuk register (register.html)
        - Memetakan fungsi register pada urls.py

    2. Membuat fungsi dan form login:
        - Import AuthenticationForm, authenticate, login pada views.py
        - Membuat fungsi login_user() pada views.py
        - Membuat halaman untuk login (login.html)
        - Memetakan fungsi login pada urls.py

    3. Membuat fungsi logout:
        - Import logout pada views.py
        - Membuat fungsi logout_user() pada views.py
        - Menambahkan button logout pada main.html
        - Memetakan fungsi logout pada urls.py

    4. Merestriksi akses halaman main dan product details:
        - Import login_required pada views.py
        - Menambahkan @login_required sebelum show_main dan show_product  

    5. Menghubungkan model Product dengan User:
        - Pada models.py, import User
        - Pada models.py di dalam class, tambahkan user = models.ForeignKey
        - Pada views.py, modifikasi method create_product() dan show_main(), sehingga dapat melakukan filter berdasarkan user
        - Pada main.html, tambahkan button filter
        - Pada product_details.html, tambahkan nama user  

    6. Membuat 2 akun pengguna dengan masing-masing 3 dummy data:
        Melakukan registrasi 2 kali untuk membuat 2 akun yang berbeda, lalu masing-masingnya menambahkan 3 dummy data


### Tugas 5 ###

Urutan prioritas pengambilan CSS selector:
    1. Inline style
    2. ID selector
    3. Class, Attribute selector, dan Pseudo class
    4. Tag selector
    5. Urutan muncul

Mengapa responsive design penting? berikan contoh aplikasi yang sudah dan belum menerapkan responsive design:
    Penting karena responsive design membuat tampilan web menyesuaikan ukuran layar perangkat. Sehingga user dapat mengakses web dengan user experience yang baik.

    Contoh aplikasi yang sudah responsive:
        - Instagram Web
        - Tokopedia

    Contoh aplikasi yang belum responsive:
        - siasisten.cs.ui.ac.id

Perbedaan margin, border, dan padding:
    padding: area kosong di sekitar konten di dalam border
    border: garis pembatas antara padding dan margin
    margin: area kosong di luar border

    cara implementasinya:
        margin: 10px;
        border: 1px;
        padding: 10px;

Konsep flex box dan grid layout:
    flex box:
        - Digunakan untuk layout 1 dimensi (horizontal atau vertikal)
        - Elemen otomatis menyesuaikan ruang kosong
        - Biasa digunakan untuk navbar dan alignment

    grid layout:
        - Digunakan untuk layout 2 dimensi (baris dan kolom)
        - Biasa digunakan untuk menampilkan sebuah list (contoh: produk pada e-commerce)

Langkah-langkah implementasi checklist:
    Implementasi fungsi untuk menghapus product:
        1. Pada views.py di folder main tambahkan method delete_product yang menerima parameter request dan id. Lalu cari product tersebut berdasarkan id nya dan product tersebut di-delete product.delete(). Setelah itu, method tersebut me-return HttpResponseRedirect ke main

        2. Lalu pada file urls.py, import fungsi delete_product yang sudah dibuat pada views.py dan membuat path-nya

        3. Setelah itu, pada file card_product.html tambahkan button delete 

    Implementasi fungsi untuk mengedit product:
        1. Pada views.py di folder main tambahkan method edit_product yang menerima parameter request dan id. Lalu cari product tersebut berdasarkan id-nya dan meminta user untuk isi form untuk merubah data dari product tersebut. Setelah itu, method tersebut me-return redirect ke main

        2. Lalu pada file urls.py, import fungsi edit_product yang sudah dibuat pada views.py dan membuat path-nya

        3. Setelah itu, membuat halaman html untuk edit product

        4. Lalu pada file card_product.html tambahkan button edit product yang terhubung ke halaman edit product

    Kustomisasi desain:
        1. Tambahkan tailwind ke base.html menggunakan <script src="https://cdn.tailwindcss.com">
        2. Kustomisasi halaman login, register, tambah product, edit product, dan detail product dengan ketentuan jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar. Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card

    Buat 2 button untuk mengedit dan menghapus product untuk setiap card_product:
        pada file card_product, tambahkan button edit yang terhubung ke halaman edit_product. Lalu tambahkan button delete yang berguna untuk menghapus product tersebut.

    Buat navbar:
        1. Buat file baru navbar.html
        2. Buat ul (Unordered List) yang di dalamnya terdapat beberapa li (List Item) yang masing-masing terhubung ke fungsinya sendiri
            - <li>Home</li> terhubung ke halaman utama
            - <li>Create Product</li> terhubung ke halaman create_product