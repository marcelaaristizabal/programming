import matplotlib.pyplot as plt 
#----------------1--------------#
equipos = ['Atlético Nacional','Santa Fé','Millonarios FC','Deportivo Cali','Deportes Tolima','La Equidad','Junior Club SA.','América de Cali',]
partidosGanados = [10,9,10,8,8,8,8,7]
plt.bar(equipos,partidosGanados, color ='y')
##################
#Título
plt.title('Mejores equipos de futbol en Colombia')
plt.xlabel('Equipos colombianos')
plt.ylabel('Cantidad de partidos ganados en la temporada 2021-I')
plt.savefig('GraficodeBarrasEquipos.png')
##################
plt.show ()

#-----------------2--------------#
paisesmedallasdeOroNatacion= ['Estados Unidos','Reino Unido','Países Bajos','Canadá','Alemania','Francia','Suecia','Polonia']
cantidadDeMedallasOroNatacion= [240,180,172,153,134,117,103,102]
plt.bar(paisesmedallasdeOroNatacion,cantidadDeMedallasOroNatacion, color = 'g')
#########################
#Título
plt.title('Mejores 8 países en el Medallero de Natación en los Juegos Paralímpicos')
plt.xlabel('Naciones')
plt.ylabel('Cantidad de Medallas de Oro ganadas')
plt.savefig('GraficosdeBarrasMedalladOro.png')
#########################
plt.show ()

#------------------3-----------------#
fluctuacionDolar = [1175,1525,1875,2225,2575,2925,3275,3625,3650,4350]
añosTasaDeCambio = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
plt.bar(añosTasaDeCambio,fluctuacionDolar, color = 'c')
##########################
#Título 
plt.title('Fluctuación del dólar en los últimos 10 años')
plt.xlabel('Años')
plt.ylabel (' Fluctuación del dólar US ')
plt.savefig('GraficodeBarrasFluctuacionUS.png')
##########################
plt.show ()

#-----------------4------------------#
cantidadDeReproducionesMensualesSpotify= [32.2 , 12.5 , 45.5 , 54.6 , 37.3 ]
artistasEscuchadosSpotifyMensual= ['Camila Cabello','Blink 182','Bad Bunny','J Balvin','Coldplay']
plt.bar(artistasEscuchadosSpotifyMensual,cantidadDeReproducionesMensualesSpotify, color = 'm' )
#########################
#Título 
plt.title(' Artistas más escuchados mensuales en Spotify ')
plt.xlabel('Artistas más escuchados al mes en Spotify')
plt.ylabel('Cantidad de reproducciones mensuales')
plt.savefig ('GraficosdeBarrasArtistasEscuchados.png')
#########################
plt.show ()

#---------------5--------------------#
cantidadDeMegalopolis = [ 36.6 , 22.5 , 22.15 ,20.9 , 20.25 , 20 , 19.7 , 18.8 ,18.4 , 16.8 ]
megalopolisDelMundo = ['Tokio (Japón)','Seúl(Corea)','Delhi (India)','Bombay (India)','São Paulo (Brasil)','CDX (México)','Nueva York (EE.UU)','Jakarta (Indonesia)','Shangai (China)','Osaka (Japón)']
plt.bar (megalopolisDelMundo, cantidadDeMegalopolis, color = 'r')
########################
#Título
plt.title('Ciudades más pobladas del mundo (Megalópolis)')
plt.xlabel('Megalópolis del Mundo')
plt.ylabel('Cantidad de habitantes (Millones) en las Megalópolis')
plt. savefig ('GraficodeBarrasMegalopolis.png')
#######################
plt.show ()