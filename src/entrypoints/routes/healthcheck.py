#  Usar un health check bien diseñado es una solución muy robusta y aceptada como estándar
# para monitorear la salud de tu aplicación en lugar de depender de try-except en el bloque
# principal (uvicorn.run). Esto es particularmente útil cuando estás en un entorno de
# producción gestionado por herramientas como Kubernetes, Docker, o un Load Balancer.
