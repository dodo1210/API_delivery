class Validacao:
	def weight_most_zero(self,weight):
		if weight<=0:
			return []
		return weight

	def min_max(self,height,width):
		print(height,width)
		if height < 5 or height> 200 or width<6 or width>140:
			return 0
		if height>=5 and height<10:
			return 1
		if (width>=6 and width<=13) or (width>=125 and width<=140) or (height>=140 and height<=200):
			return 2


