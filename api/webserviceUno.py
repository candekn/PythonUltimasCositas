import requests
r = requests.get("http://localhost:7001/student") 
print(r.status_code) #estado de la comunicacion. Dependiendo el code se sabe si la comunicacion fue exitosa o no 
#r = requests.post("http://localhost:7001/student", json={"name": "Lautaro", "courses": 3})
#print("Codigo de estado: ", r.status_code)
#print("Contenido de la respuesta: ", r.json())

#tuplaAlumnos = (("Ambar",4),("Lucia",3),("Samuel",7),("Marcos",2))
''' 
for n, c in tuplaAlumnos:
    r = requests.post("http://localhost:7001/student", json={"name": n, "courses": c})
    print("Contenido de la respuesta: ", r.json())
 '''
estudiante = r.json()
print(estudiante["students"][2]["name"]) #te trae el nombre del estudiante de la pos 2
datos = {"courses": 6}
r = requests.put("http://localhost:7001/student/2",json=datos) #Modificamos la cantidad de cursos

r = requests.delete("http://localhost:7001/student/2") #elimina al estudiante con ese id