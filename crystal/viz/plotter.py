import matplotlib.pyplot as plt


def plot_stock_data(data):
    plt.plot(data)
    plt.ylabel('time')
    plt.xlabel('stock value')
    plt.title('stocks')
    plt.legend(data.columns)
    plt.draw()
    plt.grid(True)
    plt.show()
