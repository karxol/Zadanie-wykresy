import plotly.graph_objects as go

#Ćwiczenia 
# X = [0,1,2,3]
# Y = [0,1,0,1]

# data = go.Scatter(x=X, y=Y)
# layout = {
# 	'title': 'Zigzag with plotly'
# }
# fig = go.Figure(data, layout)
# fig.show()


salaries = [
	("Mark", 1000),
	("John", 1500),
	("Daniel", 2300),
	("Greg", 5000)
]

names = list(map(lambda tup:tup[0], salaries))
salary_values = list(map(lambda tup:tup[1], salaries))

#wkres liniowy
data_1=go.Scatter(x=names, y=salary_values)
layout_1={
    "title": "Wynagrodzenie nieszczęśników"
}
fig_1 = go.Figure(data_1, layout_1)
fig_1.show()

#wykres słupkowy - rozwiązanie zadania
data_1a=go.Bar(x=names, y=salary_values)
layout_1a={
    "title": "Wynagrodzenie czterech nieszczęśników"
}
fig_1a = go.Figure(data_1a, layout_1a)
fig_1a.show()
