from nameko.containers import ServiceContainer

class Service:
  name = "service"

  container = ServiceContainer(Service,config={})

  service_extensions = list(container.extensions)

  container.start()

  container.stop()
