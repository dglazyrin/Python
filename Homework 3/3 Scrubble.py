slovar=['AaEeIiOoUuLlNnSsTtRrАаВвЕеИиНнОоРрСсТт0','DdGgДдКкЛлМмПпУу1','BbCcMmPpБбГгЁёЬьЯя2','FfHhVvWwYyЙйЫы3','KkЖжЗзХхЦцЧч4','JjXxШшЭэЮю7','QqZzФфЩщЪъ9']
slovo=str(input("Введите слово - "))
price=int(0)
for i in slovo:
     for j in slovar:
          if i in j:
               price+=int(j[-1])+1
print(price)