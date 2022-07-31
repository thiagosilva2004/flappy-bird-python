import pygame
import os
import random


class Cano:
    DISTANCIA_CANOS = 200
    VELOCIDADE = 5
    IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imagens', 'pipe.png')))

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.posicao_topo = 0
        self.posicao_base = 0
        self.CANO_TOPO = pygame.transform.flip(self.IMAGEM_CANO, False, True)
        self.CANO_BASE = self.IMAGEM_CANO
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.posicao_topo = self.altura - self.CANO_TOPO.get_height()
        self.posicao_base = self.altura + self.DISTANCIA_CANOS

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.posicao_topo))
        tela.blit(self.CANO_BASE, (self.x, self.posicao_base))

    def colidir(self, passaro):
        passaro_mascara = passaro.pegar_mascara()
        topo_mascara = pygame.mask.from_surface(self.CANO_TOPO)
        base_mascara = pygame.mask.from_surface(self.CANO_BASE)

        distancia_topo = (self.x - passaro.x, round(self.posicao_topo) - round(passaro.y))
        distancia_base = (self.x - passaro.x, round(self.posicao_base) - round(passaro.y))

        base_ponto = passaro_mascara.overlap(topo_mascara, distancia_topo)
        topo_ponto = passaro_mascara.overlap(base_mascara, distancia_base)

        if base_ponto or topo_ponto:
            return True
        else:
            return False
