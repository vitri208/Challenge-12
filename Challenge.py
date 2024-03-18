import random
import string
import os

i = 0
data_dict = []
while True:
  print('*'*15, '-INPUT DATA MAPEL-' , '*'*15)

  data_01 = ('Mata pelajaran', 'Guru', 'Hari', 'Jam', 'Ruangan')
  data = dict.fromkeys(data_01)

  data['Mata pelajaran'] = input('Mapel : ')
  data['Guru'] = input('Guru : ')
  data['Hari'] = input('Hari : ')
  data['Jam'] = input('Jam : ')
  data['Ruangan'] = input('Ruangan : ')

  lanjut = input("Lanjut (Y/T)? ").lower()
  Id = ''.join(random.choice(string.ascii_uppercase) for i in range(3))
  i += 1
  data_dict.append({
    'Id': Id,
    'data': data,
  })

  if lanjut == 'y':
    print("-" * 50)
    os.system('cls')
    continue

  if lanjut == 't':
    print("*" * 70)
    print(f'{"ID":<10} {"Mata Pelajaran":<20} {"Guru":<13} {"Hari":<5} {"Jam":<5} {"Ruangan":<10}')
    print("*" * 70)
    for key, value in enumerate(data_dict, start=1):
      print(f"MPL.{value['Id']:<6} {value['data']['Mata pelajaran']:<20} {value['data']['Guru']:<13} {value['data']['Hari']:<6} {value['data']['Jam']:<6} {value['data']['Ruangan']:<10}")
    break

  else:
    print("Tidak Valid")
    break