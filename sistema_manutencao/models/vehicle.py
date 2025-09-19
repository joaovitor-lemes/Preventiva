from datetime import datetime, timedelta
from typing import Optional

class Vehicle:
    def __init__(self, 
                 # Parâmetros obrigatórios
                 frota: str,
                 modelo: str,
                 data: datetime,                 
                 tipo_manutencao: str,
                 descricao: str,
                 

                # Parâmetros opcionais (tem valor padrão, vem com sinal de "=")
                 km_ultima_manutencao: int = 0,
                 horimetro_ultima_manutencao: int = 0,
                 intervalo_manutencao_km: int = 25000,
                 intervalo_manutencao_horimetro: int = 600,                            
                 
                 categoria: Optional[str] = None,
                 odometro: int = 0,
                 horimetro: int = 0,
                 ultimo_abastecimento: Optional[datetime] = None,
                 media_km: float = None,
                 media_l: float = None,
                 volume: float = None,
                 status: bool = True,
                 ultima_manutencao: Optional[datetime] = None):
        
        if tipo_manutencao not in ["odometro", "horimetro"]:
            raise ValueError("Tipo de manutenção inválido")
        


        self.frota = frota
        self.data = data
        self.descricao = descricao
        self.modelo = modelo
        self.categoria = categoria
        self.intervalo_manutencao_km = intervalo_manutencao_km
        self.intervalo_manutencao_horimetro = intervalo_manutencao_horimetro        
        self.km_ultima_manutencao = km_ultima_manutencao
        self.horimetro_ultima_manutencao = horimetro_ultima_manutencao
        self.odometro = odometro
        self.horimetro = horimetro
        self.tipo_manutencao = tipo_manutencao        
        self.ultimo_abastecimento = ultimo_abastecimento
        self.media_km = media_km
        self.media_l = media_l
        self.volume = volume  # Valor padrão 0.0
        self.status = status
        self.ultima_manutencao = ultima_manutencao
        
    
    
    def needs_maintenance(self):

        if self.tipo_manutencao == "odometro":
            if self.odometro - self.km_ultima_manutencao >= self.intervalo_manutencao_km:
                return True
            else:
                return False
            
        elif self.tipo_manutencao == "horimetro":
            if self.horimetro - self.horimetro_ultima_manutencao >= self.intervalo_manutencao_horimetro:
                return True
            else:
                return False
        
        
    def remaining_maintenance(self):

        if self.tipo_manutencao == "odometro":
            return self.intervalo_manutencao_km - (self.odometro - self.km_ultima_manutencao)
        elif self.tipo_manutencao == "horimetro":
            return self.intervalo_manutencao_horimetro - (self.horimetro - self.horimetro_ultima_manutencao)



    def needs_alert(self):

        if self.tipo_manutencao == "odometro":
            if self.odometro - self.km_ultima_manutencao >= 24000:
                return True
            else:
                return False
            
        elif self.tipo_manutencao == "horimetro":
            if self.horimetro - self.horimetro_ultima_manutencao >= 550:
                return True
            else:
                return False
        

    def update_odometro(self, new_value: int):

        if new_value < 0:
            raise ValueError("Odômetro não pode ser negativo")
        
        if self.odometro is not None and new_value < self.odometro:
            raise ValueError(f"Novo odômetro ({new_value}) não pode ser menor que o atual ({self.odometro})")
        
        # Atualizar valor
        self.odometro = new_value
        print(f"Veículo {self.frota}: odômetro atualizado para {new_value} km")


    def update_horimetro(self, new_value: int):

        if new_value < 0:
            raise ValueError("Horímetro não pode ser negativo")
        
        if self.horimetro is not None and new_value < self.horimetro:
            raise ValueError(f"Novo horímetro ({new_value}) não pode ser menor que o atual ({self.horimetro})")
        
        # Atualizar valor
        self.horimetro = new_value
        print(f"Veículo {self.frota}: horímetro atualizado para {new_value} horas")   



    def realizar_manutencao(self, data_manutencao: Optional[datetime] = None): 

        """ Realiza a manutenção do veículo """

        if data_manutencao is None:
            data_manutencao = datetime.now()

        if self.tipo_manutencao == "odometro":

            self.km_ultima_manutencao = self.odometro or 0
            

        elif self.tipo_manutencao == "horimetro":

            self.horimetro_ultima_manutencao = self.horimetro or 0
            
        
        self.ultima_manutencao = data_manutencao


        print(f"Veículo {self.frota}: manutenção realizada em {data_manutencao}")
        print(f"Veículo {self.frota} realizou a manutenção com {self.km_ultima_manutencao} km")
        print(f"Veículo {self.frota} realizou a manutenção com {self.horimetro_ultima_manutencao} horas")



        
        


    def data_proxima_manutencao(self):

        """ Retorna a data da próxima manutenção """

        if self.ultima_manutencao is None:
            return "Não existem dados da última manutenção"

        
        hoje = datetime.now()
        dias_desde_ultima_manutencao = (hoje - self.ultima_manutencao).days

        if dias_desde_ultima_manutencao <= 0:
            return "A manutenção ja foi realizada"

        if self.tipo_manutencao == "odometro":
            return self._calcular_data_odometro(dias_desde_ultima_manutencao) # Criei um método auxiliar para calcular a data da próxima manutenção
        
        elif self.tipo_manutencao == "horimetro":
            return self._calcular_data_horimetro(dias_desde_ultima_manutencao) # Criei um método auxiliar para calcular a data da próxima manutenção


        """ CRIAÇÃO DOS MÉTODOS AUXILIARES """


    def _calcular_data_odometro(self, dias_desde_ultima_manutencao: int):

        # Quantos km desde a última manutenção
        km_atual = self.odometro or 0
        km_rodado = km_atual - self.km_ultima_manutencao 

        if km_rodado <= 0:
            return "Diferença de km é negativa ou igual a 0"

            # Cálculo da média
        km_por_dia = km_rodado / dias_desde_ultima_manutencao


        if km_por_dia <= 0:
            return "Média de km é negativa ou igual a 0"
            
        km_proxima_manutencao = self.km_ultima_manutencao + self.intervalo_manutencao_km
        km_restantes = km_proxima_manutencao - km_atual

        if km_restantes <= 0:
            return datetime.now()
            
            # Cálculo de quantos dias para atingir os km necessários
        dias_restantes = km_restantes / km_por_dia

        data_prevista = datetime.now() + timedelta(days = int(dias_restantes))

        return data_prevista   
     
        
    def _calcular_data_horimetro(self, dias_desde_ultima_manutencao: int):

        # Quantas horas desde a última manutenção
        horimetro_atual = self.horimetro or 0
        horimetro_rodado = horimetro_atual - self.horimetro_ultima_manutencao


        if horimetro_rodado <=0:
            return "Diferença de horimetro é negativa ou igual a 0"
            
        horas_por_dia = horimetro_rodado / dias_desde_ultima_manutencao

        if horas_por_dia <= 0:
            return "Média de horas é negativa ou igual a 0"

        horas_proxima_manutencao = self.horimetro_ultima_manutencao + self.intervalo_manutencao_horimetro
        horas_restantes = horas_proxima_manutencao - horimetro_atual

        if horas_restantes <= 0:
            return datetime.now()

        dias_restantes = horas_restantes / horas_por_dia
        data_prevista = datetime.now() + timedelta(days = int(dias_restantes))

        return data_prevista

            






    def is_valid() -> bool:

        """ Verifica se o veículo é válido """
        pass

    
    def __lt__(self, other):

        """ Permite ordendar veículos (por data, frota, urgencia) """

        pass



    def to_dict(self) -> dict:

        """ Retorna o veículo como um dicionário """

        pass


    def update_from_dict(self, data: dict):

        """ Atualiza vários campos de uma vez (útil ao importar excel) """

        pass


    def get_maintenance_status(self) -> str:
        """ Retorna: OK, ALERTA, URGENTE, ATRASADO """


        if self.needs_maintenance():
            return "URGENTE"
        
        elif self.needs_alert():
            return "ALERTA"
        
        else:
            return "Dentro do prazo"




        

    def get_days_since_last_maintenance(self) -> Optional[int]:

        """ Retorna o número de dias desde a última manutenção """

        pass









# ✅ VERSÃO CORRIGIDA:
bs2001 = Vehicle(
    frota="BS2001", 
    descricao="Compactador", 
    data=datetime(2025, 9, 19),
    modelo="Mercedes-Benz",
    categoria="VW", 
    odometro=90000, 
    horimetro=752, 
    km_ultima_manutencao=59000, 
    horimetro_ultima_manutencao=598,  
    tipo_manutencao="horimetro", 
    ultima_manutencao=datetime(2025, 5, 10)
)

# Testar
resultado = bs2001.data_proxima_manutencao()
print(resultado)
