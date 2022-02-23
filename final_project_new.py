# Gudang Data stock Levi's 501 store
stockGudang =[
    {
        'warna':'hitam',
        'jenis':'original',
        'harga':1600000,
        'qty':13
    },
    {
        'warna':'biru',
        'jenis':'vintage',
        'harga':4999000,
        'qty':23
    },
    {
        'warna':'wash',
        'jenis':'slim tapper',
        'harga':1999000,
        'qty':38

    }
]


while True :
    menuUtama = input('''
    **** Data stock gudang Levi's 501 ****

    1. Report Data Stock
    2. Menambahkan Data Stock
    3. Mengubah Data Stock
    4. Menghapus Data Stock
    5. Exit

    Silahkan pilih main menu (1-5) : ''')
    def judulKolom () :
        print('Data Stock\nKode\t|Warna\t|Jenis\t\t|Harga\t\t|qty')
    def isiKolom (isi1,isi2,isi3,isi4,isi5) :
        isi1 = i
        isi2 = stockGudang[i]['warna']
        isi3 = stockGudang[i]['jenis']
        isi4 = stockGudang[i]['harga']
        isi5 = stockGudang[i]['qty']
        print('{}\t|{}\t|{}\t|{}\t|{}\t'.format(isi1,isi2,isi3,isi4,isi5))


    while True :
        if (menuUtama == '1'):
            readData = input('''
                *** Report Data Stock Gudang Levi's 501 ***
                1. Report seluruh data
                2. Report Data Tertentu
                3. kembali ke Menu Utama
                Silahkan pilih sub Menu read data (1-3) : ''')

            if (readData == '1'):
                judulKolom ()
                for i in range(len(stockGudang)):
                    isiKolom (i,i,i,i,i)
            elif (readData == '2'):
                kodeRead = int(input('masukan kode : '))
                kodeReadif = len(stockGudang)
                if(kodeRead < kodeReadif):
                    print('Report data stock\n')
                    judulKolom()
                    i = kodeRead
                    isiKolom(i,i,i,i,i)

                elif(kodeReadif > kodeReadif):
                    print('***Tidak ada Data***')
                    break

            elif (readData == '3') :
                break
            else :
                print('masukan sesuai sub menu (1-3) !!')



        elif(menuUtama == '2'):
            menambahData = input('''
            *** Menambah data stock Gudang Levi's 501 ***

            1. Tambah data stock
            2. Kembali ke Menu Utama 
            masukan pilihan (1-2) : ''')

            if (menambahData == '1'):

                warnaInput = input('input warna : ')
                jenisInput = input('input jenis : ')
                hargaInput = int(input('input harga : '))
                qtyInput = int(input('input quantity : '))
                stockGudang.append({
                    'warna':warnaInput,
                    'jenis':jenisInput,
                    'harga':hargaInput,
                    'qty':qtyInput
                })

                print('\nReport Tambahan data stock\n')
                judulKolom()
                kodeTambah = (len(stockGudang) - 1)
                i = kodeTambah
                isiKolom(i,i,i,i,i)

                while True:    
                    saveInput = input('Jika mau disave masukan Y/N : ').upper()
                    if (saveInput == 'Y'):
                        break
                    elif (saveInput == 'N'):
                        del stockGudang[kodeTambah]
                        break
                    else :
                        print('masukan (Y/N) !!')
                
            elif (menambahData == '2'):
                break
            else :
                print('Silahkan Pilih Sub Menu Create Data (1-2) !!')

        elif(menuUtama == '3' ):
            mengUbah = input('''
            *** Mengubah Data Stock Gudang Levi's 501 ***

            1. Ubah data stock
            2. Kembali ke Menu Utama 
            masukan pilihan (1-2) : ''')

            if (mengUbah == '1') :
                kodeUbah = int(input('masukan kode : '))
                kodeStock = len(stockGudang)
                if (kodeUbah < kodeStock ):
                    judulKolom()
                    i = kodeUbah
                    isiKolom(i,i,i,i,i)                    
                    while True :
                        ubahYorN = input('Tekan Y jika anda ingin mengubah data, N jika cancel ubah Y/N : ').upper()
                        
                        if (ubahYorN == 'Y'):
                            kolomStockGudang = str(input('masukan kolom/keterangan yg ingin di edit : '))
                            dataBaru = input('masukan data {} yang baru : '.format(kolomStockGudang))
                            saveData = input('apakah data akan di ubah Y/N : ').upper()
                            if (saveData == 'Y') :
                                stockGudang[i][kolomStockGudang] = dataBaru
                                print('Data berhasil Diubah!!')
                                break
                            elif (saveData == 'N'):
                                break
                            else :
                                print('masukan (Y/N) !!')

                        elif(ubahYorN == 'N'):
                            break
                    
                        else :
                            print('Masukan (Y/N) !!')
                        
                elif (kodeUbah > kodeStock ):
                    print('Data tidak ada')
                    break

            elif(mengUbah == '2') :
                break
            else :
                print('Silahkan Pilih Sub Menu Mengubah Data (1-2) !!')

        elif (menuUtama == '4') :
            mengHapus = input('''
            *** Menghapus Data Stock Gudang Levi's 501 ***

            1. Hapus Data Stock
            2. Kembali ke Menu Utama
            Masukan pilihan (1-2) : ''')
            if(mengHapus == '1') :
                kodeHapus = int(input('Masukan Kode yg ingin di hapus : '))
                kodeStock = int(len(stockGudang))
                if (kodeHapus < kodeStock) :
                    judulKolom()
                    i = kodeHapus
                    isiKolom(i,i,i,i,i)
                    
                    while True :
                        pilihanHapus = input('apakah data Stock akan dihapus Y/N : ').upper()

                        if (pilihanHapus == 'Y') :
                            del stockGudang[kodeHapus]
                            print('Data berhasil dihapus !!')
                            break

                        elif (pilihanHapus == 'N') :
                            break
                        else :
                            print('masukan Y/N !')
                elif(kodeHapus > kodeStock) :
                    print('Kode Tidak Terdaftar !!')
                    break
            elif (mengHapus == '2') :
                break
            else :
                print('Silahkan Pilih Sub Menu Menghapus Data (1-2) !!')
                


        elif (menuUtama == '5') :
            print('Thank you and Goodbye !!')
            break
            

        else :
            print('*******Pilihan yang anda masukan Salah*******')
            break



        