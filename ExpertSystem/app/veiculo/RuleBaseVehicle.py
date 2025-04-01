from ExpertSystem.api.esBooleanRuleBase import BooleanRuleBase
from ExpertSystem.api.esRuleVariable import RuleVariable
from ExpertSystem.api.esCondition import Condition
from ExpertSystem.api.esRule import Rule
from ExpertSystem.api.esClause import Clause

class RuleBaseVehicle:
    def __init__(self, nome, goals_list):
        self.br = BooleanRuleBase(nome)
        self.goals_list = goals_list

    def get_goal_list(self):
        return self.goals_list

    def create(self):
        veiculo = RuleVariable(self.br, "veiculo")
        tipo = RuleVariable(self.br, "tipoDeVeiculo")

        tamanho = RuleVariable(self.br, "tamanho")
        tamanho.set_labels("pequeno medio grande")
        tamanho.set_prompt_text("Qual é o tamanho do veículo?")

        numeroDeRodas = RuleVariable(self.br, "numeroDeRodas")
        numeroDeRodas.set_labels("2 3 4")
        numeroDeRodas.set_prompt_text("Quantas rodas o veículo possui?")

        numeroDePortas = RuleVariable(self.br, "numeroDePortas")
        numeroDePortas.set_labels("2 3 4")
        numeroDePortas.set_prompt_text("Quantas portas o veículo possui?")

        motor = RuleVariable(self.br, "motor")
        motor.set_labels("sim nao")
        motor.set_prompt_text("O veículo possui motor?")

        c_equals = Condition("=")
        c_less = Condition("<")

        Rule(self.br, "Regra 01", [Clause(numeroDeRodas, c_less, "4")],
             Clause(tipo, c_equals, "velocipede"))

        Rule(self.br, "Regra 02", [Clause(numeroDeRodas, c_equals, "4"),
                                   Clause(motor, c_equals, "sim")],
             Clause(tipo, c_equals, "automotivo"))

        Rule(self.br, "Regra 03", [Clause(tipo, c_equals, "velocipede"),
                                   Clause(numeroDeRodas, c_equals, "2"),
                                   Clause(motor, c_equals, "nao")],
             Clause(veiculo, c_equals, "bicicleta"))

        Rule(self.br, "Regra 04", [Clause(tipo, c_equals, "velocipede"),
                                   Clause(numeroDeRodas, c_equals, "3"),
                                   Clause(motor, c_equals, "nao")],
             Clause(veiculo, c_equals, "triciclo"))

        Rule(self.br, "Regra 05", [Clause(tipo, c_equals, "velocipede"),
                                   Clause(numeroDeRodas, c_equals, "2"),
                                   Clause(motor, c_equals, "sim")],
             Clause(veiculo, c_equals, "motocicleta"))

        Rule(self.br, "Regra 06", [Clause(tipo, c_equals, "automotivo"),
                                   Clause(tamanho, c_equals, "medio"),
                                   Clause(numeroDePortas, c_equals, "2")],
             Clause(veiculo, c_equals, "carroEsporte"))

        Rule(self.br, "Regra 07", [Clause(tipo, c_equals, "automotivo"),
                                   Clause(tamanho, c_equals, "medio"),
                                   Clause(numeroDePortas, c_equals, "4")],
             Clause(veiculo, c_equals, "sedan"))

        Rule(self.br, "Regra 08", [Clause(tipo, c_equals, "automotivo"),
                                   Clause(tamanho, c_equals, "medio"),
                                   Clause(numeroDePortas, c_equals, "3")],
             Clause(veiculo, c_equals, "minivan"))

        Rule(self.br, "Regra 09", [Clause(tipo, c_equals, "automotivo"),
                                   Clause(tamanho, c_equals, "grande"),
                                   Clause(numeroDePortas, c_equals, "4")],
             Clause(veiculo, c_equals, "veiculoEsporteUtilitario"))

        return self.br  # Fim do método create()

    def demo_fc(self, LOG):
        self.demo_fc1(LOG)

    def demo_fc1(self, LOG):
        LOG.append("--- Executando consulta 1 ---")
        self.br.set_variable_value("numeroDeRodas", "2")
        self.br.set_variable_value("motor", "nao")
        self.br.forward_chain()
        self.br.display_variables(LOG)

    def demo_fc2(self, LOG):
        LOG.append("--- Executando consulta 2 ---")
        self.br.set_variable_value("numeroDeRodas", "3")
        self.br.set_variable_value("motor", "nao")
        self.br.forward_chain()
        self.br.display_variables(LOG)

    def demo_fc3(self, LOG):
        LOG.append("--- Executando consulta 3 ---")
        self.br.set_variable_value("numeroDeRodas", "2")
        self.br.set_variable_value("motor", "sim")
        self.br.forward_chain()
        self.br.display_variables(LOG)

    def demo_fc4(self, LOG):
        LOG.append("--- Executando consulta 4 ---")
        self.br.set_variable_value("numeroDeRodas", "4")
        self.br.set_variable_value("motor", "sim")
        self.br.set_variable_value("tamanho", "medio")
        self.br.set_variable_value("numeroDePortas", "2")
        self.br.forward_chain()
        self.br.display_variables(LOG)

    def demo_fc5(self, LOG):
        LOG.append("--- Executando consulta 5 ---")
        self.br.set_variable_value("numeroDeRodas", "4")
        self.br.set_variable_value("motor", "sim")
        self.br.set_variable_value("tamanho", "medio")
        self.br.set_variable_value("numeroDePortas", "4")
        self.br.forward_chain()
        self.br.display_variables(LOG)

    def demo_fc6(self, LOG):
        LOG.append("--- Executando consulta 6 ---")
        self.br.set_variable_value("numeroDeRodas", "4")
        self.br.set_variable_value("motor", "sim")
        self.br.set_variable_value("tamanho", "grande")
        self.br.set_variable_value("numeroDePortas", "4")
        self.br.forward_chain()
        self.br.display_variables(LOG)
    def demo_bc(self, LOG):
        LOG.append("--- Executando consulta backward-chain ---")
        self.br.set_variable_value("veiculo", None)
        self.br.set_variable_value("tipoDeVeiculo", None)
        self.br.set_variable_value("tamanho", None)
        self.br.set_variable_value("numeroDeRodas", None)
        self.br.set_variable_value("numeroDePortas", None)
        self.br.set_variable_value("motor", None)
        self.br.display_variables(LOG)
   
