from ExpertSystem.api.esMenu import APP
from ExpertSystem.app.veiculo.RuleBaseVehicle import RuleBaseVehicle

class Main:
    def __init__(self):
        self.app = APP("Sistema Especialista de Veículos")

    def main(self):
        try:
            brVehicle = RuleBaseVehicle("Classificação de Veículos",
                                        "[veiculo, tipoDeVeiculo] :")
            self.app.add_rule_base(brVehicle)
            self.app.menu()
        except Exception as e:
            print("Exception: RuleApp ", e)

if __name__ == '__main__':
    Main().main()

