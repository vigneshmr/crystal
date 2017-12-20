import matplotlib.pyplot as plt


def plot_multi_stock_data(data):
    plt.clf()
    plt.plot(data)
    plt.ylabel('time')
    plt.xlabel('stock value')
    plt.title('stocks')
    plt.legend(data.columns)
    plt.grid(True)
    plt.draw()
    plt.get_current_fig_manager().show()


def plot_single_stock_data(data, symbol):
    plt.clf()
    plt.plot(data)
    plt.ylabel('time')
    plt.xlabel('stock value')
    plt.title('stocks')
    plt.legend([symbol])
    plt.grid(True)
    plt.draw()
    plt.get_current_fig_manager().show()
