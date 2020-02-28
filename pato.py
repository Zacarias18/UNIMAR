class Entrenar:
   def __init__(self):

     self.tipo = tipo
     self.tiempo = tiempo
     self.ejercicios = ejercicios
      
   def TipoEntenamiento (self, tipo):
	   print ('1. Entrenamiento simple')
	   print ('2. Entrenamiento medio')
	   print ('3. Entrenamiento fuerte')
	   while True:
		   TipoEntenamiento()
		   
		   opcTipo = input('Especifique el tipo de entrenamiento')
		   if opcTipo == '1':
			   print('ENTRENAMIENTO SIMPLE')
		   elif opcTipo == '2':
			   print('ENTRENAMIENTO MEDIO')
		   elif opcTipo == '3':
			   print ('ENTRENAMIENTO FUERTE')
		   else:
			   print('Debe especificar el tipo para entrenar')
   def TiempoEntrenamiento (self, tiempo):
	   tiempo = int(input('Ingrese horas de entrenamiento: '))
	   if tiempo > 3 :		   
		   print('El tiempo maximo de entrenamiento son 3 horas')
	   else:
		   print('Aun no alcanza el maximo de horas de entrenamiento')
   def CantidadEjercicios (self, ejercicios):
	   if ejercicios = 20:
		   print('Es la cantidad perfecta para entrenar')
	   else:
		   if ejercicios < 20:
		       print('Hay que exigirse para tener una vida sana')
		   else:
			   print('No hay que exigirse demasiado')
