import matplotlib.pyplot as plt


def plot_multi_stock_data(data):
    plt.plot(data)
    plt.ylabel('time')
    plt.xlabel('stock value')
    plt.title('stocks')
    plt.legend(data.columns)
    plt.draw()
    plt.grid(True)
    plt.show()


def plot_single_stock_data(data, symbol):
    plt.plot(data)
    plt.ylabel('time')
    plt.xlabel('stock value')
    plt.title('stocks')
    plt.legend([symbol])
    plt.draw()
    plt.grid(True)
    plt.show()
