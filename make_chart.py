from matplotlib import pyplot as plt
import chroller as chrol


def makeGraph(numbers, countries):    
    print("numbers = " + str(numbers))
    print("countries = " + str(countries))

    data = numbers
    labels = countries

    plt.xticks(range(len(data)), labels)
    plt.xlabel('국가', fontsize=4)
    plt.ylabel('확진자 수', fontsize=4)
    plt.title(f'국가별 확진자 수[{chrol.kr}]')
    # plt.bar(range(len(data)), data) 

    plt.bar(range(len(data)), data, color='royalblue', alpha=0.7)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)


    plt.show()
    
    # number_infected = numbers
    # ax = pyplot.subplot()
    # size = list(range(len(countries)))
    # print(size)
    # ax.set_xticks(size)
    # ax.set_xticklabels(countries)
    # pyplot.bar(range(len(number_infected)),number_infected)
    plt.savefig(f"graph[{chrol.kr}].png", bbox_inches='tight')
    plt.close()