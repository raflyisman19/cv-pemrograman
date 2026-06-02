<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CV Rafly Isman - Network Engineer</title>

  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" />

  <!-- Bootstrap Icons -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet" />

  <style>
    /* Identitas Mahasiswa
       Nama: Rafly Isman
       NIM: 250401010489
       Kelas: IF210
       Mata Kuliah: Pemrograman Web I
    */

    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: #f4f7fb;
      color: #333;
      scroll-behavior: smooth;
    }

    .navbar {
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }

    .hero {
      min-height: 100vh;
      background: linear-gradient(135deg, #0d6efd, #0b2447);
      color: white;
      display: flex;
      align-items: center;
      padding-top: 80px;
    }

    .profile-img {
      width: 240px;
      height: 240px;
      object-fit: cover;
      border-radius: 50%;
      border: 6px solid white;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    }

    .section-title {
      font-weight: 700;
      color: #0d6efd;
      margin-bottom: 25px;
      position: relative;
    }

    .section-title::after {
      content: '';
      width: 70px;
      height: 4px;
      background: #0d6efd;
      display: block;
      margin-top: 8px;
      border-radius: 10px;
    }

    .card-custom {
      border: none;
      border-radius: 18px;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
      transition: 0.3s;
    }

    .card-custom:hover {
      transform: translateY(-6px);
    }

    .skill-badge {
      margin: 5px;
      padding: 10px 14px;
      border-radius: 30px;
      font-size: 14px;
    }

    .project-img {
      height: 190px;
      object-fit: cover;
      border-radius: 15px;
    }

    footer {
      background: #0b2447;
      color: white;
      padding: 25px 0;
    }

    .dark-mode {
      background: #121212;
      color: #f1f1f1;
    }

    .dark-mode .card,
    .dark-mode .table {
      background: #1f1f1f;
      color: #f1f1f1;
    }
  </style>
</head>
<body>

  <!-- Navbar -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
    <div class="container">
      <a class="navbar-brand fw-bold" href="#home">M Rafly Isman</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item"><a class="nav-link" href="#about">Tentang</a></li>
          <li class="nav-item"><a class="nav-link" href="#skills">Keahlian</a></li>
          <li class="nav-item"><a class="nav-link" href="#education">Pendidikan</a></li>
          <li class="nav-item"><a class="nav-link" href="#projects">Project</a></li>
          <li class="nav-item"><a class="nav-link" href="#contact">Kontak</a></li>
        </ul>
        <button class="btn btn-light btn-sm ms-lg-3" onclick="toggleDarkMode()">
          <i class="bi bi-moon-stars"></i> Mode
        </button>
      </div>
    </div>
  </nav>

  <!-- Home Section -->
  <section id="home" class="hero">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-md-7">
          <h1 class="display-4 fw-bold"> Muhammad <span class="text-warning">Rafly Isman</span></h1>
          <h3 class="mb-3">Network Engineer</h3>
          <p class="lead">
            Saya adalah mahasiswa Informatika yang memiliki minat besar pada bidang jaringan komputer,
            infrastruktur IT, dan keamanan jaringan.
          </p>
          <a href="#contact" class="btn btn-warning btn-lg mt-3">Hubungi Saya</a>
          <a href="#projects" class="btn btn-outline-light btn-lg mt-3 ms-2">Lihat Project</a>
        </div>
        <div class="col-md-5 text-center mt-4 mt-md-0">
          <img src="c:\All Foto\1739112419_9873b0ff9177a4017fb9.jpg" alt="Foto Profil" class="profile-img" />
          <p class="mt-3"><small>Explore My Portfolio</small></p>
        </div>
      </div>
    </div>
  </section>

  <!-- About Section -->
  <section id="about" class="py-5">
    <div class="container">
      <h2 class="section-title">Tentang Saya</h2>
      <div class="card card-custom p-4">
        <p>
          Nama saya <strong> Muhammad Rafly Isman</strong>. Saya sedang menempuh pendidikan di bidang
          <b>Informatika</b> dan memiliki ketertarikan pada dunia <mark>Network Engineering</mark>.
          Saya suka mempelajari cara kerja jaringan komputer, konfigurasi perangkat jaringan,
          serta proses troubleshooting ketika terjadi gangguan koneksi.
        </p>
        <p>
          Dalam proses belajar, saya mulai memahami beberapa konsep seperti <em>TCP/IP</em>,
          <u>subnetting</u>, routing, switching, VLAN, dan penggunaan tools seperti Cisco Packet Tracer,
          MikroTik Winbox, serta Wireshark. Saya memiliki semangat belajar yang tinggi dan ingin terus
          mengembangkan kemampuan agar siap bekerja di bidang IT Support, NOC, maupun Junior Network Engineer.
        </p>
      </div>
    </div>
  </section>

  <!-- Skills Section -->
  <section id="skills" class="py-5 bg-light">
    <div class="container">
      <h2 class="section-title">Keahlian</h2>
      <div class="card card-custom p-4">
        <h5>Hard Skills</h5>
        <ul>
          <li>Konfigurasi IP Address dan Subnetting</li>
          <li>Routing dan Switching Dasar</li>
          <li>Simulasi jaringan menggunakan Cisco Packet Tracer</li>
          <li>Troubleshooting jaringan komputer</li>
        </ul>

        <h5 class="mt-4">Soft Skills</h5>
        <ol>
          <li>Mampu bekerja sama dalam tim</li>
          <li>Memiliki kemampuan problem solving</li>
          <li>Disiplin dan bertanggung jawab</li>
          <li>Mudah beradaptasi dengan teknologi baru</li>
        </ol>

        <div class="mt-3">
          <span class="badge bg-primary skill-badge">MikroTik</span>
          <span class="badge bg-success skill-badge">< HTML ></HTml></span>
          <span class="badge bg-warning text-dark skill-badge">C++</span>
          <span class="badge bg-info text-dark skill-badge">IT Support</span>
          <span class="badge bg-danger skill-badge">Networking</span>
          <span class="badge bg-dark skill-badge">Linux</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Education Section -->
  <section id="education" class="py-5">
    <div class="container">
      <h2 class="section-title">Pendidikan & Pengalaman</h2>
      <div class="row g-4">
        <div class="col-md-6">
          <div class="card card-custom p-4 h-100">
            <h4>Pendidikan</h4>
            <table class="table table-striped table-bordered mt-3">
              <thead class="table-primary">
                <tr>
                  <th>Tahun</th>
                  <th>Institusi</th>
                  <th>Jurusan</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>2025 - Sekarang</td>
                  <td>Universitas Siber Asia</td>
                  <td>Informatika</td>
                </tr>
                <tr>
                  <td>2023-2025</td>
                  <td>SMK TRIMULIA JAKARTA</td>
                  <td>TEKNIK KOMPUTER DAN JARINGAN</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="col-md-6">
          <div class="card card-custom p-4 h-100">
            <h4>Pengalaman / Pelatihan</h4>
            <table class="table table-hover table-bordered mt-3">
              <thead class="table-primary">
                <tr>
                  <th>Kegiatan</th>
                  <th>Keterangan</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Belajar Jaringan Komputer</td>
                  <td>Mempelajari dasar TCP/IP, subnetting, dan topologi jaringan.</td>
                </tr>
                <tr>
                  <td>Simulasi Cisco Packet Tracer</td>
                  <td>Membuat jaringan sederhana antar komputer, switch, dan router.</td>
                </tr>
                <tr>
                  <td>Belajar Web Dasar</td>
                  <td>Membuat website menggunakan HTML, C++.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Projects Section -->
  <section id="projects" class="py-5 bg-light">
    <div class="container">
      <h2 class="section-title">Project Saya</h2>
      <div class="row g-4">
        <div class="col-md-4">
          <div class="card card-custom p-3 h-100">
            <img src="c:\isman coding\assets\IMG-20260501-WA0019.jpg" class="project-img" alt="Project Jaringan" />
            <div class="card-body">
              <h5>Simulasi Jaringan Kantor</h5>
              <p>Memastikan Jaringan pada router, switch, dan beberapa komputer.</p>
            </div>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card card-custom p-3 h-100">
            <img src="c:\isman coding\assets\IMG-20260423-WA0025.jpg" class="project-img" alt="Project Website" />
            <div class="card-body">
              <h5>IT Support</h5>
              <p>Memastikan dan mengecek keluhan dari client agar kendala bisa diselesaikan baik secara langsung atau secara remote. </p>
            </div>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card card-custom p-3 h-100">
            <img src="c:\isman coding\assets\IMG-20260501-WA0026.jpg" class="project-img" alt="Project IT" />
            <div class="card-body">
              <h5>Monitoring Jaringan</h5>
              <p>Memantau jaringan selama 24/7 secara realtime.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Link Section -->
  <section class="py-5">
    <div class="container">
      <h2 class="section-title">Link Penting</h2>
      <div class="card card-custom p-4">
        <p>Berikut beberapa link yang berkaitan dengan pembelajaran dan portofolio saya:</p>
        <a href="https://www.tiktok.com/@raflyisman19?is_from_webapp=1&sender_device=pc" target="_blank" class="btn btn-outline-primary m-1">Tiktok</a>
        <a href="https://www.instagram.com/rflyisman?igsh=MXBpd2dhdW5ycWFjOA==" target="_blank" class="btn btn-outline-dark m-1">instagram</a>
        <a href="https://www.linkedin.com/in/muhammad-rafly-isman-630b97362/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app&lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BekPWd5EAQy2CigMqlBOnmg%3D%3D" target="_blank" class="btn btn-outline-info m-1">LinkedIn</a>
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="py-5 bg-light">
    <div class="container">
      <h2 class="section-title">Kontak</h2>
      <div class="row">
        <div class="col-md-6">
          <div class="card card-custom p-4 h-100">
            <h4>Informasi Kontak</h4>
            <p><i class="bi bi-envelope"></i> Email: raflyisman19@gmail.com</p>
            <p><i class="bi bi-telephone"></i> Telepon: 087849453748</p>
            <p><i class="bi bi-geo-alt"></i> Lokasi: Indonesia</p>
          </div>
        </div>

        <div class="col-md-6 mt-4 mt-md-0">
          <div class="card card-custom p-4 h-100">
            <h4>Kirim Pesan</h4>
            <form onsubmit="kirimPesan(event)">
              <div class="mb-3">
                <label class="form-label">Nama</label>
                <input type="text" class="form-control" id="nama" required />
              </div>
              <div class="mb-3">
                <label class="form-label">Pesan</label>
                <textarea class="form-control" id="pesan" rows="3" required></textarea>
              </div>
              <button type="submit" class="btn btn-primary">Kirim</button>
            </form>
            <p id="hasilPesan" class="mt-3 fw-bold text-success"></p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="text-center">
    <p class="mb-0">&copy; Rafly Isman, Dibuat untuk tugas UTS Pemrograman Web I.</p>
  </footer>

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

  <script>
    // Fungsi untuk dark mode
    function toggleDarkMode() {
      document.body.classList.toggle('dark-mode');
    }

    // Fungsi sederhana untuk menampilkan pesan dari form
    function kirimPesan(event) {
      event.preventDefault();
      const nama = document.getElementById('nama').value;
      const pesan = document.getElementById('pesan').value;
      document.getElementById('hasilPesan').innerHTML =
        'Terima kasih, ' + nama + '! Pesan kamu sudah diterima: "' + pesan + '"';
      event.target.reset();
    }
  </script>
</body>
</html>
