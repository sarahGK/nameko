from nameko.runners import ServiceRunner
from nameko.testing.utils import get_container

class ServiceA:
  name = "service_a"

class ServiceB:
  name = "service_b"

runner = ServiceRunner(config={})
runner.add_service(ServiceA)
runner.add_service(ServiceB)

container_a = get_container(runner,ServiceA)

runner.start()

runner.stop()
