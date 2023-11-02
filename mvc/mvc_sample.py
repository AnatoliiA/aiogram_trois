__author__ = "Chetan"


class Model(object):
    services = {
        "email": {
            "number": 1000,
            "price": 2,
        },
        "sms": {
            "number": 1000,
            "price": 10,
        },
        "voice": {
            "number": 1000,
            "price": 15,
        },
    }


class View(object):
    def __str__(self):
        return f"view object {self.__hash__()}"

    def list_services(self, services):
        print(self.__str__())
        for svc in services:
            print(svc, " ")
        print("+++++++++++++++++++++")

    def list_pricing(self, services):
        print(self.__str__())
        for svc in services:
            print(
                "For",
                Model.services[svc]["number"],
                svc,
                "message you pay $",
                Model.services[svc]["price"],
            )


class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services)

    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)


class Client(object):
    controller = Controller()
    print("Services Provided:")
    controller.get_services()
    print("Pricing for Services:")
    controller.get_pricing()
