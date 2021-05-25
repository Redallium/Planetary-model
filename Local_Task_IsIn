#Алгоритм определения нахождения точки внутри или вне замкнутой несамопересекающейся ломаной линии на координатной плоскости
import math
sqrt = math.sqrt
sin = math.sin
cos = math.cos
pi = math.pi
EPS = 10e-100
################################################################
class Point:                       #Создание класса точки в трехмерном евклидовом пространстве
	def __init__(self, x = 0, y = 0, z = 0):
		self.x, self.y, self.z = x, y, z
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y and self.z == other.z
	def print(self):
		print('(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')')
################################################################
class Vector:                      #Создание класса вектора в трехмерном евклидовом пространстве  
	def __init__(self, startpoint = Point(), endpoint = Point()):
		self.x, self.y, self.z = endpoint.x - startpoint.x, endpoint.y - startpoint.y, endpoint.z - startpoint.z
		self.startpoint = startpoint
		self.endpoint = endpoint
	def __pos__(self):
		return self
	def __neg__(self):
		return Vector(self.endpoint, self.startpoint)
	def __eq__(self, other):
		dx = abs(self.x - other.x)
		dy = abs(self.y - other.y)
		dz = abs(self.z - other.z)
		return dx < EPS and dy < EPS and dz < EPS
	def norm(self):
		""" Возвращает норму (длину, магнитуду) вектора """
		return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
	def normalize(self):
		""" Возвращает нормированный на еденицу вектор, отложенной от точки (0, 0, 0), либо нулевой вектор"""
		norm = self.norm()
		if norm > EPS:
			normed = Vector(Point(), Point(self.x / norm, self.y / norm, self.z / norm))
			return normed
		else:
			return self
	def __add__(self, other):
		""" Возвращает вектор, равный сумме векторов и отложенной от точки (0, 0, 0) """
		return Vector(Point(), Point(self.x + other.x, self.y + other.y, self.z + other.z))
	def __sub__(self, other):
		""" Возвращает вектор, равный разности векторов и отложенной от точки (0, 0, 0) """
		return Vector(Point(), Point(self.x - other.x, self.y - other.y, self.z - other.z))
	def print(self):
		#print("Startpoint: ", end = '')
		#self.startpoint.print()
		print('(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')')
################################################################
def ScalarProduct(Vector1, Vector2):
	""" Возвращает скалярное произведение двух векторов """
	return Vector1.x * Vector2.x + Vector1.y * Vector2.y + Vector1.z * Vector2.z
################################################################
def VectorProduct(Vector1, Vector2):
	""" Возвращает вектор - результат векторного произведения двух векторов, отложенный от точки (0, 0, 0) """
	return Vector(Point(), Point(Vector1.y * Vector2.z - Vector2.y * Vector1.z, Vector2.x * Vector1.z - Vector1.x * Vector2.z, Vector1.x * Vector2.y - Vector2.x * Vector1.y))
################################################################
def IntersectionCounterFix(DegenerateSegments, intersection_counter):    #Функция исправляет значение intersection_counter в зависимости от наличия вырожденных случаев
	""" Необходимо исправить эту функцию и сделать так, чтобы любая последовательность 1-2-1 и 1-1 была учтена, даже в случаях, когда конец списка "Разоединяет" эти последовательности,
	то есть необходимо двигаться по списку DegenerateSegments как по замкнутому на концах списку и придумать оптимальный способ распознавать нужные последовательности  """
	#???????????????????????????????????????????????????????????????????
	i = 0   #Счётчик для цикла
	pointnum = len(DegenerateSegments)
	while i != pointnum - 1:
		if(DegenerateSegments[i] == 1):
			if(DegenerateSegments[i + 1] == 1):  #Если две еденицы идут подряд
				if( (VectorProduct(TraserBeam, MaskSegments[i])).normalize() == - (VectorProduct(TraserBeam, MaskSegments[i + 1])).normalize() ):     #Если отнормированные результаты векторных произведений TraserBeam и каждого из двух сегментов противоположны, то пересечение нужно учесть
					intersection_counter += 1
					i += 2
			elif(DegenerateSegments[i + 1] == 2):    #Если за еденицей идёт двойка( => комбинация однозначно 1 - 2 - 1)
				if( (VectorProduct(TraserBeam, MaskSegments[i])).normalize() == - (VectorProduct(TraserBeam, MaskSegments[i + 2])).normalize() ):     #Если отнормированные результаты векторных произведений TraserBeam и двух сегментов(не пересекаемых по отрезку, а по крайней точке) противоположны, то пересечение нужно учесть
					intersection_counter += 1
					i += 3
	return intersection_counter
################################################################
def IsTheSegmentsIntersect(MaskSegment, TraserBeam):           #Функция проверяет, пересекаются ли отрезки на плоскости. в качестве аргументов идет отрезок ломаной контура маски MaskSegment и произвольный луч(TraserBeam), исходящий из проверяемой нами точки
	HelpingVector_1 = Vector(TraserBeam.startpoint, MaskSegment.startpoint)   #Вспомогательный вектор №1. Используется для подсчёта векторного произведения с вектором TraserBeam в целях определения ориентировки отрезка
	HelpingVector_2 = Vector(TraserBeam.startpoint, MaskSegment.endpoint)     #Вспомогательный вектор №2. Используется для подсчёта векторного произведения с вектором TraserBeam в целях определения ориентировки отрезка
	VectorProd_1 = VectorProduct(TraserBeam, HelpingVector_1)     #Вектор, являющийся результатом векторного произведения векторов TraserBeam и HelpingVector_1, отложенный от начала координат
	VectorProd_2 = VectorProduct(TraserBeam, HelpingVector_2)     #Вектор, являющийся результатом векторного произведения векторов TraserBeam и HelpingVector_2, отложенный от начала координат
	VectorProd_1 = VectorProd_1.normalize()       #Нормируем вектора на еденицу
	VectorProd_2 = VectorProd_2.normalize()

	""" VectorProd_1.print()
	VectorProd_2.print()
	print('\n') """

	if((VectorProd_1 == NULLVECTOR and VectorProd_2 != NULLVECTOR) or (VectorProd_1 != NULLVECTOR and VectorProd_2 == NULLVECTOR)):     #Случай, когда TraserBeam и MaskSegment пересекаются по точке startpoint или endpoint отрезка MaskSegment
		return 'ExtremePoint'
	if(VectorProd_1 == NULLVECTOR and VectorProd_2 == NULLVECTOR):     #Случай, когда TraserBeam и MaskSegment пересекаются по отрезку MaskSegment
		return 'Segment'
	if(VectorProd_1 == - VectorProd_2):     #Если вектора противоположно направлены, то один из отрезков удовлетворяет критерию пересечение отрезков и необходимо проверить второй
		HelpingVector_2 = - HelpingVector_1                                      #Вспомогательный вектор №2. Используется для подсчёта векторного произведения с вектором MaskSegment в целях определения ориентировки отрезка
		HelpingVector_1 = Vector(MaskSegment.startpoint, TraserBeam.endpoint)    #Вспомогательный вектор №1. Используется для подсчёта векторного произведения с вектором MaskSegment в целях определения ориентировки отрезка
		VectorProd_1 = VectorProduct(MaskSegment, HelpingVector_1)     #Вектор, являющийся результатом векторного произведения векторов MaskSegment и HelpingVector_1, отложенный от начала координат
		VectorProd_2 = VectorProduct(MaskSegment, HelpingVector_2)     #Вектор, являющийся результатом векторного произведения векторов MaskSegment и HelpingVector_2, отложенный от начала координат
		VectorProd_1 = VectorProd_1.normalize()       #Нормируем вектора на еденицу
		VectorProd_2 = VectorProd_2.normalize()

		""" VectorProd_1.print()
		VectorProd_2.print()
		print('\n') """

		if(VectorProd_1 == - VectorProd_2):
			return 1
		else:
			return 0
	else:
		""" Бывают случаи, когда TraserBeam пересекает MaskSegment по startpoint или по endpoint, причем в таком случае пересекать он будет сразу два отрезка, поэтому для корректности работы необходимо
		учесть пересечение с каким - то одним из отрезков и не учитывать с другим. Важно заметить, что два последовательных вектора MaskSegment могут лежать как по одну сторону от TraserBeam, так и по
		разные стороны. Необходимо учитывать такое касание исключительно в том случае, если эти вектора лежат по разные стороны, иначе пересечение учитывать нельзя.
		(Не решение)В качестве решения этой проблемы предлагаю считать знак косинуса угла между этими двумя последовательными векторами MaskSegment. Если косинус отрицательный, то такое пересечение не учитываем, 
		если же положительный, то учитываем. """
		return 0
################################################################
########################## MAIN BLOCK ##########################
################################################################
NULLVECTOR = Vector(Point(), Point())   #Глобальная константа "Нулевой Вектор"
PointToCheck = Point(2, 3, 0)    #Эксперементальное значение для проверяемой точки(Временное)


MaskPoints = []      #Список всех точек ломаной, задающей маску
pointnum = 0       #Актуальное число точек ломаной


try:
	F = open("Test_Mask.txt", "r")
except IOError:
	print("File reading error\n")     	 #Открытие файла для чтения контура маски с исключением на возможную ошибку открытия файла
	exit()


MaskPoints = F.readlines()     #Читаем все строки файла(то есть все точки)
for point in MaskPoints:      #Цикл по всем точкам в файле
	Current = Point()
	point = point[1:-2]      #Удаляем скобки
	SplitedPoint = point.split(', ')    #Разделяем компоненты точки на отдельные подстроки и присваиваем точке Current эти значения
	Current.x = float(SplitedPoint[0])
	Current.y = float(SplitedPoint[1])
	Current.z = float(SplitedPoint[2])
	MaskPoints[pointnum] = Current
	pointnum += 1


MaskSegments = [0 for i in range(pointnum)]    #Список отрезков(векторов) ломаной контура маски
for i in range(pointnum - 1):          #Заполнение списка отрезков(векторов) ломаной контура маски
	MaskSegments[i] = Vector(MaskPoints[i], MaskPoints[i + 1])
MaskSegments[pointnum - 1] = Vector(MaskPoints[-1], MaskPoints[0])    #Замыкание списка векторов вектором, соединяющим последнюю и первую точки


intersection_counter = 0      #Счетчик пересечений луча с отрезками ломаной контура маски
TraserBeam = Vector(PointToCheck, Point(PointToCheck.x + 100, PointToCheck.y, PointToCheck.z))    #Создается фиксированный трассирующий луч(достаточной длины, в данном случае 100), испускаемый из проверяемой точки(в данном случае параллельно оси Ox)


DegenerateSegments = []    #Массив вырожденных отрезков. Отрезки, с которыми TraserBeam пересекаются по точке, в этом массиве записываются 1, а отрезки, с которыми TraserBeam пересекается по самому отрезку записываются 2(Более подробно в функции IsTheSegmentsIntersect)


for segment in MaskSegments:    #Цикл по всем отрезкам ломаной контура маски
	value = IsTheSegmentsIntersect(segment, TraserBeam)   #Результат работы функции IsTheSegmentsIntersect
	if(value == 1):
		intersection_counter += 1
		DegenerateSegments.append(0)
	elif(value == 'ExtremePoint'):
		DegenerateSegments.append(1)
	elif(value == 'Segment'):
		DegenerateSegments.append(2)
	else:
		DegenerateSegments.append(0)

intersection_counter = IntersectionCounterFix(DegenerateSegments, intersection_counter)


print(intersection_counter)
print(DegenerateSegments)
if(intersection_counter % 2 == 1):     #Если число пересечений чётное - точка вне контура, нечётное - внутри
	print("Точка внутри контура")
else:
	print("Точка вне контура")


"""for i in range(len(MaskPoints)):
	MaskPoints[i].print()
print(pointnum)
for i in range(len(MaskSegments)):
	MaskSegments[i].print()"""


#a = Point(1, 1, 1)
#b = Point(2, 2, 2)
#c = Vector(a, b)
#c.normalize().print()
#F.close()
