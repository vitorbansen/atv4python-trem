class Trem:
    MAX_POSICAO = 50
    MAX_MOVIMENTOS_CONSECUTIVOS = 20

    def __init__(self):
        self.posicao = 0
        self.movimentos_consecutivos = 0
        self.ultimo_comando = None
        self.total_movimentos = 0

    def mover(self, comando: str):
        if comando not in ["ESQUERDA", "DIREITA"]:
            raise ValueError(f"Comando inválido: {comando}")

        if self.total_movimentos >= Trem.MAX_POSICAO:
            print("Limite de posições atingido.")
            return
        
        if self.ultimo_comando == comando:
            self.movimentos_consecutivos += 1
        else:
            self.movimentos_consecutivos = 1
            self.ultimo_comando = comando
        
        if self.movimentos_consecutivos > Trem.MAX_MOVIMENTOS_CONSECUTIVOS:
            print("Limite de movimentos consecutivos atingido.")
            return

        if comando == "DIREITA":
            self.posicao += 1
        elif comando == "ESQUERDA":
            self.posicao -= 1
        
        self.total_movimentos += 1

    def executar_comandos(self, comandos: list):
        for comando in comandos:
            self.mover(comando)
            if self.total_movimentos >= Trem.MAX_POSICAO:
                break
    
    def obter_posicao(self):
        return self.posicao

    def verificar_restrições(self):
        if self.total_movimentos > Trem.MAX_POSICAO:
            return "Violação do limite de posições."
        if self.movimentos_consecutivos > Trem.MAX_MOVIMENTOS_CONSECUTIVOS:
            return "Violação do limite de movimentos consecutivos."
        return "Restrições respeitadas."

# Exemplo de uso
if __name__ == '__main__':
    trem = Trem()
    comandos = ["DIREITA", "DIREITA", "ESQUERDA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "DIREITA"]
    trem.executar_comandos(comandos)
    print(f"Posição final: {trem.obter_posicao()}")
