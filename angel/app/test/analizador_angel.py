from app.analizador_angel import Anapu

puertos = Anapu()
puertos_disponibles = puertos.listar_puertos_activos()
for p in puertos_disponibles:
    print(p)