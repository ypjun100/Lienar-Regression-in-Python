class Util:
    X, Y = [], []
    LEARNING_RATE = 0

    def __init__(self, LEARNING_RATE):          #Get LEARNING_RATE value
        self.LEARNING_RATE = LEARNING_RATE

    def input_data(self, X, Y):                 #Get X and Y value
        self.X = X
        self.Y = Y

    def Differentiation(self, w, b, max_row):   #Calculate differentiation
        h = self.LEARNING_RATE                  #Difference

        cost = 0
        for j in range(max_row):
            hy = w * self.X[j] + b
            cost = cost + (self.Y[j] - hy) ** 2
        f1 = cost / max_row

        cost = 0
        for j in range(max_row):
            hy = (w + h) * self.X[j] + b
            cost = cost + (self.Y[j] - hy) ** 2
        f2 = cost / max_row

        return (f1 - f2) / h                    #Differentiation formula is f(a+h) - f(a) / h