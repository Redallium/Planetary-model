#Программа для рассчета распределения толщины покрытия на сферической детали, наклонённой к горизонтали под углом при покрытии с использованием планетарной модели
import math
sqrt = math.sqrt
sin = math.sin
cos = math.cos
pi = math.pi

#inf = 2e308   #В python такое число работает как бесконечно большое(Будет использовано в будущем для объединения с плоским случаем)

H = 535        #Высота планет относительно испарителя
R = 200        #Радиус кривизны покрываемой детали
sec_rad = 100  #Радиус сечения сферической детали(Половина диаметра детали)
d = 195        #Расстояние от главной оси камеры до центра планеты
L = 200        #Расстояние от главной оси камеры до испарителя
phi = pi / 7   #Угол поворота детали относительно горизонтали в положительном направлении
N = 11         #Число контрольных точек на одном из радиусов планеты
w1 = pi / 21   #Угловая скрость вращения главной оси камеры(рад/c)
w2 = pi / 3    #Угловая скрость вращения оси планеты(рад/c)
T = 84 	       #Время работы машины (w1 * T  = 2*pi*k & w2 * T = 2*pi*m, где k и m - натуральные числа)
alpha = 1      #Степень косинуса угла вылета из испарителя(Параметр, описывающий диаграмму направленности испарителя)

Thickness = []  #Список толщин слоя на контрольных точках

try:
	F = open("Graph_Spherical_Surf_With_Angle_Planetary.txt", "w")
except IOError:
	print("File reading error\n")      #Открытие файла для записи распределения толщины по радиусу с исключением на возможную ошибку открытия файла
	exit()

N_dt = 1000    #Число дискретезации процесса(Число исследуемых моментов времени)
TimeMoments = [t / N_dt for t in  range(0, N_dt * T, T)]    #Список всех исследуемых моментов времени

s = R - sqrt(R * R - sec_rad * sec_rad)	  #Длина стрелки прогиба покрываемой детали

for n in range(N):                        #Цикл по всем контрольным точкам
	Thickness.append(0)                   #Заполнение нулями списка толщин

	r = sec_rad * (n / (N - 1))           #Радиус вращения n-ой контрольной точки вокруг оси детали
	z0 = (R - s) - sqrt(R * R - r * r)    #z - овая координата контрольной точки в системе координат с центром в центре планеты(Расстояние от прообраза контрольной точки на плоскости сечения детали до самой контрольной точки)
	p = sqrt(R * R - r * r) * sin(phi)    #Константа, необходимая при подсчете косинуса угла(Не несёт особого смысла). Считается в этом блоке в целях экономии памяти.
	q = sqrt(R * R - r * r) * cos(phi)    #Константа, необходимая при подсчете косинуса угла(Не несёт особого смысла). Считается в этом блоке в целях экономии памяти.

	for t in TimeMoments:                 #Цикл по всем моментам времени
		dx = d + z0 * sin(phi) + r * cos(w2 * t) * cos(phi) - L * cos(w1 * t)        #Разница x - овых координат n - ой контрольной точки и испарителя
		dz = H + z0 * cos(phi) - r * cos(w2 * t) * sin(phi)                          #Разница z - овых координат n - ой контрольной точки и испарителя.
		R_l_cos_fall_angle = (L * r * (cos(w2 * t) * cos(w1 * t) * cos(phi) + sin(w2 * t) * sin(w1 * t))
		- r * d * cos(w2 * t) * cos(phi) + H * r * cos(w2 * t) * sin(phi) + p * dx + q * dz - r * r)  #Косинус угла между радиус-вектором контрольной точки из центра кривизны детали и вектором потока из испарителя, умноженный на R, на l и на -1

		"""Считается знак косинуса угла между радиус-вектором, проведённым из центра кривизны детали в контрольную точку, и вектором, соединяющим испаритель и контрольную точку
		Если этот косинус отрицательный, то угол тупой, то есть точка не заслонена от испарителя, если же положительный,то угол острый и испаритель в данном конкретном положении заслонён от контрольной точки
		То есть в такой момент увеличение толщины учитывать нельзя"""

		if R_l_cos_fall_angle > 0:    #Критерий на знак косинуса
			dy = r * sin(w2 * t) - L * sin(w1 * t)   #Разница y - овых координат n - ой контрольной точки и испарителя
			l = sqrt(dx * dx + dy * dy + dz * dz)    #Формула для расстояния между испарителем и контрольной точкой n
			dh = (((dz / l) ** alpha) * (R_l_cos_fall_angle / (R * l))) / (l * l)    #Формула для наростающей толщины (пропорциональна косинусу угла вылета из испарителя и косинусу угла падения на деталь и обратно пропорцилнальна квадрату расстояния от испарителя до контрольной точки)
			Thickness[n] += dh    #Наростание толщины

max_thickness = max(Thickness)
for n in range(N):     #Нормируем толщины и переводим их в относительные величины
	Thickness[n] = Thickness[n] / max_thickness
	F.write(str(round(sec_rad * (n / (N - 1)), 3)) + ' ' + str(Thickness[n]) + '\n')    #Запись в файл радиуса вращения n - ой контрольной точки и толщина покрытия на этой точке
print("Толщина покрытия равномерна с максимальным отклонением", 100 - min(Thickness) / max(Thickness) * 100, '%')
F.close()
print("Successful\n")
