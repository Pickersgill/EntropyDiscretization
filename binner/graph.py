import matplotlib.pyplot as plt

class Graph:

    series1 = []

    def __init__(self):
        print("New graph created")
        
    def add_to_series(self, item):
        self.series1.append(item)

    def show(self):
        print("Rendering graph...")
        fig, axis = plt.subplots(2)

        s1 = self.series1
        x_range = range(1, len(s1) + 1)

        norm_s1 = [x / i for i, x in enumerate(s1, start=1)]

        axis[0].plot(x_range, s1)
        axis[0].set_xlabel("Iteration Number (+1 bin per iter.)")
        axis[0].set_ylabel("Total Entropy")

        axis[1].plot(x_range, norm_s1)
        axis[1].set_xlabel("Iteration Number (+1 bin per iter.)")
        axis[1].set_ylabel("Normalized Total Entropy")
        plt.show()
        
