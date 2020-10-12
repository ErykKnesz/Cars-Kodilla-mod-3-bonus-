models = ['Volkswagen - Golf','Renault - Clio','Volkswagen - Polo',
'Ford - Fiesta','Nissan - Qashqai','Peugeot - 208','VW - Tiguan','Skoda - Octavia',
'Toyota - Yaris','Opel - Corsa','Dacia - Sandero','Renault - Captur','Citroen - C3',
'Peugeot - 3008','Ford - Focus','Fiat - 500','Dacia - Duster','Peugeot - 2008',
'Skoda - Fabia','Fiat - Panda','Opel - Astra','VW - Passat','Mercedes-Benz - A-Class',
'Peugeot - 308','Ford - Kuga']

sales2018 = ['445,754','336,268','299,920','270,738','233,026','230,049','224,788',
'223,352','217,642','217,036','216,306','214,720','210,082','204,197','196,583',
'191,205','182,100','180,204','172,511','168,697','160,275','157,986','156,020',
'155,925','154,125']

sales2017 = ['483,105','327,395','272,061','254,539','247,939','244,615','234,916',
'230,116','199,182','232,738','196,067','212,768','207,299','166,784','214,661',
'189,928','NA','180,868','180,136','187,322','217,813','184,123','NA','NA','NA']

sales2016 = ['492,952','315,115','308,561','300,528','234,340','249,047','180,198',
'230,255','193,969','264,844','170,300','217,105','134,560','NA','214,435',
'183,730','NA','NA','177,301','191,617','253,483','208,575','NA','195,653','NA']

answer1_dict = {}
answer2_dict = {}

cars = {}
for model, qty2018, qty2017, qty2016 in zip(models, sales2018, sales2017, sales2016):
    qty2018 = qty2018.replace('NA' , '0')
    qty2017 = qty2017.replace('NA' , '0')
    qty2016 = qty2016.replace('NA' , '0')
    qty2018 = int(qty2018.replace(',' , ''))
    qty2017 = int(qty2017.replace(',' , ''))
    qty2016 = int(qty2016.replace(',' , ''))
    car = model.split(" - ")
    if not car[0] in cars.keys():
        cars[car[0]] = {car[1] : {"sales" : {"2016" : qty2016, "2017" : qty2017, "2018" : qty2018}}}
    else:
        cars[car[0]][car[1]] = {"sales" : {"2016" : qty2016, "2017" : qty2017, "2018" : qty2018}}
    answer1_dict[model] = qty2017
    #answer2_dict[model] = qty2018 
print(cars)


for brand, a_dict_of_everything in cars.items():
    for sales, a_dict_of_sales in a_dict_of_everything.items():
        for year2018, sales2018 in a_dict_of_sales.items():
            
            answer2_dict[brand] = sales2018

answer1 = max(answer1_dict, key = answer1_dict.get)
print(answer1)

#answer2 =  max(answer2_dict, key = answer2_dict.get)
#answer2.split(" - ")
#print(answer2_dict)
answer3 = [] # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria
answer4 = "" # wskaż nazwę modelu jako string
answer5 = "" # odpowiedź podaj w formacie procentowym jako string. Np. '21%' 
