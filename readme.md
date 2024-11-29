# Panduan Memulai Docker untuk Pemula

Docker adalah platform yang memungkinkan Anda untuk mengotomatisasi penyebaran aplikasi dalam bentuk kontainer yang portabel dan mandiri. Berikut adalah panduan langkah demi langkah untuk memulai dengan Docker.

## Prasyarat

1. **Sistem Operasi yang Didukung**
   - Windows 10 atau yang lebih baru
   - MacOS Mojave 10.14 atau yang lebih baru
   - Linux (distribusi modern seperti Ubuntu, Fedora)

2. **Hak Akses Administrator**
   - Pastikan Anda memiliki hak akses administrator pada komputer Anda.

## Langkah 1: Instalasi Docker

1. **Unduh Docker Desktop**
   - Kunjungi [situs resmi Docker](https://www.docker.com/products/docker-desktop) dan unduh Docker Desktop untuk sistem operasi Anda.

2. **Instal Docker Desktop**
   - Jalankan file instalasi yang telah diunduh.
   - Ikuti instruksi instalasi sesuai petunjuk di layar.
   - Untuk pengguna Windows, pastikan konfigurasi BIOS mendukung virtualisasi dan fitur Hyper-V diaktifkan.
   - Untuk pengguna Mac, Anda mungkin perlu melakukan beberapa langkah tambahan terkait hak akses pengaturan macOS.

3. **Jalankan Docker Desktop**
   - Setelah instalasi selesai, buka Docker Desktop. Anda tahu Docker sudah berjalan jika ikon Docker muncul di area notifikasi (system tray).

## Langkah 2: Memahami Konsep Dasar Docker

1. **Image**
   - Docker image adalah template read-only yang digunakan untuk membuat kontainer. Anggap ini sebagai blueprint untuk kontainer yang akan Anda buat.

2. **Container**
   - Kontainer adalah instance dari image Docker yang dapat berjalan, berisi segala yang dibutuhkan oleh aplikasi Anda.

3. **Docker Hub**
   - Docker Hub adalah repositori online tempat Anda dapat mencari dan menyimpan Docker image.

## Langkah 3: Menggunakan Docker

1. **Menjalankan Docker Container**
   - Buka terminal atau command prompt.
   - Jalankan perintah berikut untuk menjalankan kontainer "Hello World":
     ```bash
     docker run hello-world
     ```
   - Perintah ini akan menarik (download) image `hello-world` dari Docker Hub jika belum ada di komputer Anda dan menjalankannya dalam sebuah kontainer.

2. **Menjalankan Kontainer Lain (Contoh: Nginx)**
   - Jalankan perintah berikut untuk menjalankan server web Nginx:
     ```bash
     docker run --name mynginx -d -p 8080:80 nginx
     ```
   - Buka browser dan akses `http://localhost:8080` untuk melihat halaman default Nginx.

3. **Memahami Perintah Dasar Docker**
   - `docker ps`: Menampilkan daftar kontainer yang sedang berjalan.
   - `docker ps -a`: Menampilkan semua kontainer, termasuk yang telah dihentikan.
   - `docker stop [container_id]`: Menghentikan sebuah kontainer.
   - `docker rm [container_id]`: Menghapus sebuah kontainer.
   - `docker images`: Menampilkan daftar image yang ada di sistem Anda.

4. **Menghentikan dan Menghapus Kontainer**
   - Untuk menghentikan kontainer Nginx:
     ```bash
     docker stop mynginx
     ```
   - Untuk menghapus kontainer Nginx:
     ```bash
     docker rm mynginx
     ```

## Langkah 4: Membuat Dockerfile

1. **Apa itu Dockerfile?**
   - Dockerfile adalah file teks berisi serangkaian instruksi untuk membangun Docker image.

2. **Contoh Dockerfile Sederhana**

   - Buat file baru bernama `Dockerfile` dengan isi berikut:
     ```dockerfile
     # Gunakan image dasar
     FROM alpine:latest

     # Tambahkan informasi pemelihara
     LABEL maintainer="your-email@example.com"

     # Install aplikasi sederhana
     RUN apk add --no-cache python3

     # Set work directory
     WORKDIR /app

     # Salin file yang dibutuhkan
     COPY . /app

     # Tentukan command yang dijalankan ketika kontainer di-start
     CMD ["python3", "your-app.py"]
     ```

3. **Membangun Image dari Dockerfile**
   - Jalankan perintah berikut di direktori yang sama dengan Dockerfile:
     ```bash
     docker build -t my-python-app .
     ```

## Langkah 5: Mengelola Docker dengan Docker Compose

1. **Apa itu Docker Compose?**
   - Docker Compose adalah tool untuk mendefinisikan dan menjalankan aplikasi Docker multi-kontainer.

2. **Memulai Docker Compose**

   - Buat file bernama `docker-compose.yml` dengan isi di bawah ini:
     ```yaml
     version: '3'

     services:
       web:
         image: nginx
         ports:
           - "8080:80"
       database:
         image: mysql
         environment:
           MYSQL_ROOT_PASSWORD: example
     ```

3. **Menjalankan Docker Compose**
   - Jalankan perintah berikut untuk memulai semua layanan yang didefinisikan di `docker-compose.yml`:
     ```bash
     docker-compose up
     ```

4. **Menghentikan dan Menghapus Layanan Compose**
   - Untuk menghentikan layanan:
     ```bash
     docker-compose down
     ```

## Langkah Berikutnya

- Setelah menguasai dasar-dasar Docker, Anda dapat bereksperimen membuat kontainer aplikasi Anda sendiri, menggunakan volume untuk penyimpanan data, dan menjelajahi ekosistem Docker yang lebih luas.


Selamat bereksperimen dan semoga panduan ini bermanfaat!
