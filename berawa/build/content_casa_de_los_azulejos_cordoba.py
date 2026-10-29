# Contenido de la demo Casa de los Azulejos Hotel Boutique (Córdoba) (es/ca/en/fr). Hechos de casadelosazulejos.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Maceta · Doble Económica','Pacífico · Doble Superior','Laurel · Doble Superior Deluxe'],
'ca':['Maceta · Doble Econòmica','Pacífico · Doble Superior','Laurel · Doble Superior Deluxe'],
'en':['Maceta · Economy Double','Pacífico · Superior Double','Laurel · Superior Deluxe Double'],
'fr':['Maceta · Double Économique','Pacífico · Double Supérieure','Laurel · Double Supérieure Deluxe']}
RD={
'es':['Un rincón junto al patio, en planta baja, con cama matrimonial y baño con ducha, adaptada para personas con movilidad reducida.','Una habitación amplia, exterior y orientada a la fachada, con cama queen size en la primera planta.','Con terraza propia, en planta baja, cama queen size y baño adaptado para personas con movilidad reducida.'],
'ca':['Un racó al costat del pati, a la planta baixa, amb llit de matrimoni i bany amb dutxa, adaptada per a persones amb mobilitat reduïda.','Una habitació àmplia, exterior i orientada a la façana, amb llit queen size a la primera planta.','Amb terrassa pròpia, a la planta baixa, llit queen size i bany adaptat per a persones amb mobilitat reduïda.'],
'en':['A corner next to the patio, on the ground floor, with a double bed and a shower bathroom, adapted for people with reduced mobility.','A spacious outward-facing room overlooking the façade, with a queen-size bed on the first floor.','With its own terrace, on the ground floor, a queen-size bed and a bathroom adapted for people with reduced mobility.'],
'fr':['Un coin près du patio, au rez-de-chaussée, avec lit double et salle de bain avec douche, adaptée aux personnes à mobilité réduite.','Une chambre spacieuse, extérieure et orientée sur la façade, avec lit queen size au premier étage.','Avec terrasse privée, au rez-de-chaussée, lit queen size et salle de bain adaptée aux personnes à mobilité réduite.']}
ART={
'hero':('arches',9901,['#f3e6cf','#e9d3ac','#c9703a','#2b6f86','#1f5f6b']),
'intro':('columns',9902,['#efe5d1','#f6eedd','#d08a3a','#7da08a','#1f5f6b']),
'r1':('arches',9911,['#f1e3c9','#e6cfa6','#c46a38','#2c7088','#205f6b']),
'r2':('columns',9912,['#ede2cc','#f4ebd7','#cf8738','#7b9f88','#206070']),
'r3':('hills',9913,['#e6e8d3','#f3e6c4','#f2cf8e','#a9c4a0','#7fa387','#56786a']),
'g1':('arches',9921,['#f2e4cb','#e8d1a8','#c76d39','#2b6e85','#1e5d69']),
'g2':('hills',9922,['#e4e8d6','#f3e7c6','#fbdc9f','#a8c3a1','#80a487','#587b6b']),
'g3':('skyline',9923,['#3a4a6c','#e9935f','#fbd9a0','#3a4a6a','#2b3a58','#1c2638']),
'g4':('columns',9924,['#eee3cf','#f5ecd9','#d18a3b','#7ca089','#1f5f6b']),
'g5':('waves',9925,['#f3e0b4','#e8a374','#fff0c6','#7cb4c4','#4a8ba3','#2f6a83','#1d475d']),
'g6':('skyline',9926,['#33456a','#e48a5f','#f9d19b','#2f4260','#223249','#16222f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Casa de los Azulejos Hotel Boutique · Hotel con encanto en el casco histórico de Córdoba',see_rooms='Ver habitaciones',hero_k='Córdoba · Plaza de la Corredera',hero_t='Una casa. Mil historias. Córdoba.',hero_s='Un refugio andaluz junto a la Plaza de la Corredera, en el casco histórico.',
 intro_t='Un pequeño oasis en el casco histórico',intro_p1='Casa de los Azulejos es un hotel boutique con patio andaluz, piscina y biblioteca, junto a la Plaza de la Corredera de Córdoba.',
 intro_p2='Tiene nueve habitaciones en cuatro categorías, wifi gratuito en todo el hotel y desayuno incluido en todas las tarifas. La reserva se hace por su motor de reservas, por teléfono o por correo.',
 stats=['Nueve habitaciones','Patio y piscina','Wifi gratuito','Desayuno incluido'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Tres de las nueve habitaciones, decoradas una a una.',
 svcs=['Patio andaluz','Piscina','Biblioteca','Wifi gratuito','Aire acondicionado','Calefacción central','Minibar','Desayuno incluido'],
 loc_p='C/ Fernando Colón 5, 14002 Córdoba, junto a la Plaza de la Corredera.',
 chips=['¿Qué tipos de habitación hay?','¿Está incluido el desayuno?','¿Hay piscina?','¿Cómo se reserva?']),
'ca':dict(title='Casa de los Azulejos Hotel Boutique · Hotel amb encant al centre històric de Còrdova',see_rooms='Veure habitacions',hero_k='Còrdova · Plaça de la Corredera',hero_t='Una casa. Mil històries. Còrdova.',hero_s='Un refugi andalús al costat de la Plaça de la Corredera, al centre històric.',
 intro_t='Un petit oasi al centre històric',intro_p1='Casa de los Azulejos és un hotel boutique amb pati andalús, piscina i biblioteca, al costat de la Plaça de la Corredera de Còrdova.',
 intro_p2='Té nou habitacions en quatre categories, wifi gratuït a tot l\'hotel i esmorzar inclòs en totes les tarifes. La reserva es fa pel seu motor de reserves, per telèfon o per correu.',
 stats=['Nou habitacions','Pati i piscina','Wifi gratuït','Esmorzar inclòs'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Tres de les nou habitacions, decorades una a una.',
 svcs=['Pati andalús','Piscina','Biblioteca','Wifi gratuït','Aire condicionat','Calefacció central','Minibar','Esmorzar inclòs'],
 loc_p='C/ Fernando Colón 5, 14002 Còrdova, al costat de la Plaça de la Corredera.',
 chips=['Quins tipus d\'habitació hi ha?','Està inclòs l\'esmorzar?','Hi ha piscina?','Com es reserva?']),
'en':dict(title='Casa de los Azulejos Hotel Boutique · Charming hotel in the historic centre of Córdoba',see_rooms='See the rooms',hero_k='Córdoba · Plaza de la Corredera',hero_t='One house. A thousand stories. Córdoba.',hero_s='An Andalusian refuge next to the Plaza de la Corredera, in the historic centre.',
 intro_t='A small oasis in the historic centre',intro_p1='Casa de los Azulejos is a boutique hotel with an Andalusian patio, a pool and a library, next to the Plaza de la Corredera in Córdoba.',
 intro_p2='It has nine rooms in four categories, free wifi throughout the hotel and breakfast included in every rate. Booking is through its booking engine, by phone or by email.',
 stats=['Nine rooms','Patio and pool','Free wifi','Breakfast included'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Three of the nine rooms, each decorated individually.',
 svcs=['Andalusian patio','Pool','Library','Free wifi','Air conditioning','Central heating','Minibar','Breakfast included'],
 loc_p='C/ Fernando Colón 5, 14002 Córdoba, next to the Plaza de la Corredera.',
 chips=['What room types are there?','Is breakfast included?','Is there a pool?','How do I book?']),
'fr':dict(title='Casa de los Azulejos Hotel Boutique · Hôtel de charme dans le centre historique de Cordoue',see_rooms='Voir les chambres',hero_k='Cordoue · Plaza de la Corredera',hero_t='Une maison. Mille histoires. Cordoue.',hero_s='Un refuge andalou près de la Plaza de la Corredera, dans le centre historique.',
 intro_t='Une petite oasis dans le centre historique',intro_p1='Casa de los Azulejos est un hôtel boutique avec patio andalou, piscine et bibliothèque, près de la Plaza de la Corredera à Cordoue.',
 intro_p2='Il compte neuf chambres en quatre catégories, le wifi gratuit dans tout l\'hôtel et le petit-déjeuner inclus dans tous les tarifs. La réservation se fait par son moteur de réservation, par téléphone ou par e-mail.',
 stats=['Neuf chambres','Patio et piscine','Wifi gratuit','Petit-déjeuner inclus'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Trois des neuf chambres, décorées une à une.',
 svcs=['Patio andalou','Piscine','Bibliothèque','Wifi gratuit','Climatisation','Chauffage central','Minibar','Petit-déjeuner inclus'],
 loc_p='C/ Fernando Colón 5, 14002 Cordoue, près de la Plaza de la Corredera.',
 chips=['Quels types de chambre y a-t-il ?','Le petit-déjeuner est-il inclus ?','Y a-t-il une piscine ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='info@casadelosazulejos.com')
D=dict(name='Casa de los Azulejos Hotel Boutique',ac='#1f5f6b',ac2='#c9703a',ac2_a11y='#7a4412',book=BOOK,around=[],foot=FOOT,
 address='C/ Fernando Colón 5 · 14002 Córdoba',phones=['957 47 00 00'],emails=['info@casadelosazulejos.com'],maps='Casa de los Azulejos Hotel Boutique, C/ Fernando Colón 5, Córdoba',t=T)
META=dict(repo='demo-casa-de-los-azulejos-cordoba',name='Casa de los Azulejos Hotel Boutique',legal_name='Proyecto Latino Siglo XXI S.L.',registry_ids=['CIF B14626717'],
 url='https://casadelosazulejos.com/',domain='casadelosazulejos.com',municipality='Córdoba',province='Córdoba',sector='hotel boutique con patio andaluz',
 read_at='2026-10-29T04:26:00+01:00',created_at='2026-10-29T04:30:00+01:00',built_at='2026-10-29T04:32:00+01:00',audit_date='2026-10-29T04:30:00+01:00',
 rating=dict(value=4.8,coincide=['telefono','web'],date='2026-10-29T04:24:02+01:00',url='https://www.google.com/maps/place/Hotel+Casa+de+los+azulejos/@37.8838464,-4.7758131,17z/data=!3m1!5s0xd6cdf7db7791cb1:0x69b2da5f39592acc!4m9!3m8!1s0xd6cdf7db745783f:0xb062911fab852447!5m2!4m1!1i2!8m2!3d37.8838464!4d-4.7758131!16s%2Fg%2F1tjyvy_w'),
 book=dict(mode='mail',email='info@casadelosazulejos.com',note='La web del negocio reserva por su motor de reservas, telefono o correo; la demo usa solo contacto real (correo y telefono).'),
 first_of_type='no aplica: hotel boutique urbano con precedente en demos de esta tanda')
QS={
'es':[('¿Qué tipos de habitación hay?','K01'),('¿Tiene aire acondicionado?','K02'),('¿Hay wifi?','K03'),('¿Está incluido el desayuno?','K04'),('¿Hay piscina?','K05'),('¿A qué hora es el check-in?','K06'),('¿Admiten mascotas?','K07'),('¿Hay parking?','K08'),('¿Dónde está el hotel?','K09'),('¿Hay habitaciones adaptadas?','K10'),('¿Cómo reservo?','K11'),('¿Cuál es el teléfono?','K12'),('¿Qué historia tiene la casa?','K13'),('¿Quién es el titular?',None),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K11')],
'ca':[('Quins tipus d\'habitació hi ha?','K01'),('Té aire condicionat?','K02'),('Hi ha wifi?','K03'),('Està inclòs l\'esmorzar?','K04'),('Hi ha piscina?','K05'),('A quina hora és el check-in?','K06'),('Admeteu mascotes?','K07'),('Hi ha pàrquing?','K08'),('On és l\'hotel?','K09'),('Hi ha habitacions adaptades?','K10'),('Com reservo?','K11'),('Quin és el telèfon?','K12'),('Quina història té la casa?','K13'),('Qui és el titular?',None),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K11')],
'en':[('What room types are there?','K01'),('Is there air conditioning?','K02'),('Is there wifi?','K03'),('Is breakfast included?','K04'),('Is there a pool?','K05'),('What time is check-in?','K06'),('Are pets allowed?','K07'),('Is there parking?','K08'),('Where is the hotel?','K09'),('Are there adapted rooms?','K10'),('How do I book?','K11'),('What is the phone number?','K12'),('What history does the house have?','K13'),('Who is the owner?',None),('How much is a night?',None),('Confirm that there is a free room tomorrow','K11')],
'fr':[('Quels types de chambre y a-t-il ?','K01'),('Y a-t-il la climatisation ?','K02'),('Y a-t-il du wifi ?','K03'),('Le petit-déjeuner est-il inclus ?','K04'),('Y a-t-il une piscine ?','K05'),('À quelle heure est le check-in ?','K06'),('Les animaux sont-ils admis ?','K07'),('Y a-t-il un parking ?','K08'),('Où est l\'hôtel ?','K09'),('Y a-t-il des chambres adaptées ?','K10'),('Comment réserver ?','K11'),('Quel est le téléphone ?','K12'),('Quelle histoire a la maison ?','K13'),('Qui est le titulaire ?',None),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K11')]}
