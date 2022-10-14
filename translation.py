class Translation(object):
    START_TEXT = """<b>𝙎𝘾𝙍𝘼𝙋 𝙈𝘼𝙉 di buat untuk Membantu anda Untuk Mengambil APP ID dan API Hash dengan Mudah dan AMAN!
━━━━━━━━━━━━━━━━━━━━━━━━
Silahkan Masukkan Nomor Telepon Telegram Anda Dengan Format Kode Negara.
Contoh : +628xxxxxxx</b>
"""
    AFTER_RECVD_CODE_TEXT = """<b>No HP Diterima!
Silahkan kirimkan kode yang anda terima dari Telegram!</b>

Kode ini hanya digunakan untuk tujuan mendapatkan ID APP dari my.telegram.org
Jika anda tidak mempercayai dev bot ini, ngambil manual aja.
"""
    BEFORE_SUCC_LOGIN = "<code>Kode Diterima. Scarpping Web Page. . .</code>"
    ERRED_PAGE = """Hadeh Error. Coba dengan Cara Manual

Cara Ambil APP ID dan API HASH Secara Manual:
1. Buka my.telegram.org/auth
2. Loginkan akun telegram kalian
3. klik menu API Development
4. isi data seperti dibawah ini :
• App Title : tgbot
• Short Name : tgbot
• URL : (kosongin)
• Platform : desktop
5. Selesai

Bila Berhasil Ambil Manual Silahkan Coba Lagi di Bot ini"""
    CANCELLED_MESG = "<b>Bye! Silahkan /start kembali untuk mengulang</b>"
    IN_VALID_CODE_PVDED = "<b>Kode OTP yang anda Masukan SALAH</b>"
    IN_VALID_PHNO_PVDED = "<b>No HP yang anda masukan SALAH, Silahkan Masukkan Nomor Telepon Telegram Anda Dengan Format Kode Negara.\nContoh: +628xxxxxxx</b>"
