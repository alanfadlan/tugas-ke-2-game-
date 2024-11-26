import random

def dapatkan_pilihan_bot():
    choices = ["batu", "kertas", "gunting"]
    return random.choice(choices)

def dapatkan_pilihan_kita():
    choice = input("Masukkan pilihan Anda (batu, kertas, gunting): ").lower()
    while choice not in ["batu", "kertas", "gunting"]:
        print("Pilihan tidak sesuai. Silakan coba lagi.")
        choice = input("Masukkan pilihan Anda (batu, kertas, gunting): ").lower()
    return choice

def determine_winner(pilihan_kita, pilihan_bot):
    if pilihan_kita == pilihan_bot:
        return "Seri!"
    elif (pilihan_kita == "batu" and pilihan_bot == "gunting") or \
         (pilihan_kita == "kertas" and pilihan_bot == "batu") or \
         (pilihan_kita == "gunting" and pilihan_bot == "kertas"):
        return "Anda menang.....!"
    else:
        return "Anda kalah.....!"

def game_mulai():
    print("Selamat datang di permainnan Gunting, Batu, Kertas!")
    
    while True:
        pilihan_kita = dapatkan_pilihan_kita()
        pilihan_bot = dapatkan_pilihan_bot()
        
        print(f"Anda memilih: {pilihan_kita}")
        print(f"bot memilih: {pilihan_bot}")
        
        result = determine_winner(pilihan_kita, pilihan_bot)
        print(result)
        
        play_again = input("Apakah Anda ingin bermain lagi? (ya/tidak): ").lower()
        if play_again != 'ya':
            print("Terima kasih telah bermain!")
            break

if __name__ == "__main__":
    game_mulai()