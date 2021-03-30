import matplotlib.pyplot as plt

with open('data.商业分析实习.csv','r') as f:
    datalist = f.readlines()

city_salary_dict = {}
city_job_num_dict = {}

for data in datalist:
    if '薪资面议' in data:
        continue
    city = data.split(',')[2]
    salary = data.split(',')[3]
    useful_salary = salary.split('/')[0]
    low_salary = useful_salary.split('-')[0]
    high_salary = useful_salary.split('-')[1]
    average_salary = (int(low_salary)+int(high_salary)) / 2

    if city not in city_salary_dict.keys():
        city_salary_dict[city] = []
    city_salary_dict[city].append(average_salary)

for key, value in city_salary_dict.items():
    city_average_salary = sum(value) // len(value)

    city_salary_dict[key] = city_average_salary
    city_job_num_dict[key] = len(value)


plt.bar(city_salary_dict.keys(),city_salary_dict.values())
plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
plt.xlabel('城市')
plt.ylabel('平均薪资')

plt.bar(city_job_num_dict.keys(),city_job_num_dict.values())
plt.xlabel('城市')
plt.ylabel('工作数量')

plt.show()
