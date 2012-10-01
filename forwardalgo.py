#!/usr/bin/python -B

class ForwardAlgo:
    """
       Implement the forward algorithm.
    """
    def __init__(self):
        self.__state = []
        #P(obeservations|state)
        self.__o_hot = [0.2,0.4,0.4]
        self.__o_cold = [0.5,0.4,0.1]
        #P(state|state),as order of hot ,cold
        self.__from_start = [0.8,0.2]
	self.__from_hot = [0.7,0.3]
        self.__from_cold = [0.4,0.6]
        self.__to_end = [0.5,0.5]

    def compute(self, observations):
        """
           To compute the probability of given sequence of observations.
        """
        #initialize,for each sub-array hot->0,cold->1 
        self.__state = [[1,1] for i in xrange(len(observations))]
        #compute each cell(state)
        for i in range(len(observations)):
            #change char to int
            o_num = ord(observations[i]) - 48
            if i == 0:
                #for hot
                self.__state[i][0] = self.__from_start[0] * self.__o_hot[o_num-1]
                #for cold
                self.__state[i][1] = self.__from_start[1] * self.__o_cold[o_num-1]
            else:  
                #for hot
                self.__state[i][0] = self.__state[i-1][0] * self.__from_hot[0] * self.__o_hot[o_num-1] + \
                                     self.__state[i-1][1] * self.__from_cold[0] * self.__o_hot[o_num-1]
                #for cold
                self.__state[i][1] = self.__state[i-1][0] * self.__from_hot[1] * self.__o_cold[o_num-1] + \
                                     self.__state[i-1][1] * self.__from_cold[1] * self.__o_cold[o_num-1]
        #for end
        result = self.__state[i][0] * self.__to_end[0] + self.__state[i][1] * self.__to_end[1]

        return result
               

if __name__ == "__main__":
    algo = ForwardAlgo()
    observation1 = "312312312"
    prob1 = algo.compute(observation1)
    print(observation1 + "'s probability is:")
    print(prob1)
    observation2 = "311233112"
    prob2 = algo.compute(observation2)
    print(observation2 + "'s probability is:")
    print(prob2)
    if prob1 > prob2:
         print("The probability of " + observation1 + " is bigger.")
    else:
         print("The probability of " + observation2 + " is bigger.")
